import os
import json
import sys
import tarfile
import zipfile
import gzip
import bz2
import lzma
import fnmatch

def get_base_path():
    """실행 파일의 경로를 반환합니다."""
    if getattr(sys, 'frozen', False):  # PyInstaller로 패키징된 경우
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(__file__)

def load_input_file(input_file_name):
    base_path = get_base_path()  # 실행 파일의 경로를 기반으로 파일 경로 설정
    input_file_path = os.path.join(base_path, input_file_name)
    with open(input_file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def normalize_name(name):
    """공백을 제거하고 소문자로 변환하여 파일명 및 폴더명을 표준화합니다."""
    return name.replace(" ", "").lower()

def match_pattern(pattern, name):
    """패턴에 '*'가 포함된 경우 fnmatch를 사용하여 like 검색을 수행하고, 포함되지 않은 경우 정확히 일치하는지 확인."""
    normalized_pattern = normalize_name(pattern)
    normalized_name = normalize_name(name)

    # 패턴에 '*'가 포함된 경우 like 검색 수행
    if '*' in pattern:
        return fnmatch.fnmatch(normalized_name, normalized_pattern)
    else:
        return normalized_name == normalized_pattern

def extract_files_from_archive(archive_path):
    """압축 파일 내의 파일 목록을 반환합니다."""
    files_in_archive = []

    if tarfile.is_tarfile(archive_path):  # .tar, .tar.gz, .tar.bz2, .tar.xz 등 지원
        with tarfile.open(archive_path, 'r:*') as tar:
            files_in_archive = [normalize_name(member.name) for member in tar.getmembers() if member.isfile()]

    elif zipfile.is_zipfile(archive_path):  # .zip 파일 지원
        with zipfile.ZipFile(archive_path, 'r') as zipf:
            files_in_archive = [normalize_name(file) for file in zipf.namelist()]

    # 단일 파일 압축 형식 지원: .gz, .bz2, .xz 등
    elif archive_path.endswith('.gz'):  # GZIP 압축 파일 처리
        with gzip.open(archive_path, 'rb') as f:
            files_in_archive.append(normalize_name(os.path.basename(archive_path).replace('.gz', '')))

    elif archive_path.endswith('.bz2'):  # BZIP2 압축 파일 처리
        with bz2.open(archive_path, 'rb') as f:
            files_in_archive.append(normalize_name(os.path.basename(archive_path).replace('.bz2', '')))

    elif archive_path.endswith('.xz'):  # LZMA/XZ 압축 파일 처리
        with lzma.open(archive_path, 'rb') as f:
            files_in_archive.append(normalize_name(os.path.basename(archive_path).replace('.xz', '')))

    return files_in_archive

def validate_file_extensions(files, allowed_extensions, folder_path):
    errors = []
    allowed_extensions = [ext.lower() for ext in allowed_extensions]  # 확장자를 소문자로 변환
    for file in files:
        file_extension = file.split(".")[-1].lower()  # 파일 확장자를 소문자로 변환
        if file_extension not in allowed_extensions:
            errors.append(f"오류: {folder_path} 폴더에 허용되지 않는 파일 '{file}' 확장자가 존재합니다.")
        elif os.path.getsize(os.path.join(folder_path, file)) == 0:
            errors.append(f"오류: {folder_path} 폴더에 0바이트 파일 '{file}'이 존재합니다.")
    return errors

def validate_directory_structure(current_path, file_tree, errors):
    """폴더 및 파일 구조를 검증합니다."""
    if not os.path.exists(current_path):
        errors.append(f"오류: '{current_path}' 폴더가 존재하지 않습니다.")
        return

    try:
        directory_content = os.listdir(current_path)
    except FileNotFoundError:
        errors.append(f"오류: '{current_path}' 경로가 존재하지 않습니다.")
        return

    # 폴더 및 파일 구조 검증
    for item in directory_content:
        item_path = os.path.join(current_path, item)
        if os.path.isdir(item_path):  # 폴더일 경우
            folder_matched = False
            if isinstance(file_tree, dict):  # 현재 노드가 폴더일 경우만 딕셔너리임
                for expected_folder in file_tree.keys():
                    if match_pattern(expected_folder, item):  # * 패턴을 허용하는 like 검색 적용
                        folder_matched = True
                        validate_directory_structure(item_path, file_tree[expected_folder], errors)
                        break
            if not folder_matched:
                errors.append(f"오류: '{current_path}'에 정의되지 않은 폴더 '{item}'이(가) 존재합니다.")
        else:  # 파일일 경우
            file_extension = item.split(".")[-1].lower()
            if file_extension in ['tar', 'zip', 'gz', 'bz2', 'xz']:  # 다양한 압축 파일 지원
                files_in_archive = extract_files_from_archive(item_path)
                if isinstance(file_tree, list):
                    # 압축 파일의 내부 파일이 부모 폴더의 규칙을 따르도록 처리
                    errors.extend(validate_file_extensions(files_in_archive, file_tree, current_path))
            elif isinstance(file_tree, list):  # 현재 노드가 파일 확장자 리스트일 경우
                errors.extend(validate_file_extensions([item], file_tree, current_path))
            else:
                errors.append(f"오류: '{current_path}'에 정의되지 않은 파일 '{item}'이(가) 존재합니다.")

def validate_missing_directories(current_path, file_tree, errors):
    """fileTree에 정의된 폴더가 실제로 존재하는지 확인."""
    if isinstance(file_tree, dict):
        for folder_name, sub_tree in file_tree.items():
            folder_matched = False
            directory_content = os.listdir(current_path)
            for item in directory_content:
                if match_pattern(folder_name, item):  # 정의된 폴더와 실제 폴더를 매칭
                    folder_matched = True
                    validate_missing_directories(os.path.join(current_path, item), sub_tree, errors)
                    break
            if not folder_matched:
                errors.append(f"오류: '{os.path.join(current_path, folder_name)}' 폴더가 누락되었습니다.")

def write_output_file(errors):
    base_path = get_base_path()  # 실행 파일 경로 가져오기
    output_file_path = os.path.join(base_path, 'output.txt')  # 실행 파일 경로에 output.txt 저장
    with open(output_file_path, 'w', encoding='utf-8') as f:
        if not errors:
            f.write('모든 점검이 통과되었습니다. 디렉터리 구조가 파일 트리 구조와 일치합니다.\n')
        else:
            for error in errors:
                f.write(f"{error}\n")

# 기존 validate_file_tree_structure에서 결과 저장 부분 수정
def validate_file_tree_structure(input_file):
    data = load_input_file(input_file)
    target_directory = data['targetDirectoryPath']
    file_tree = data['fileTree']
    errors = []

    # 파일 트리와 실제 폴더 구조 비교 시작
    validate_directory_structure(target_directory, file_tree, errors)
    validate_missing_directories(target_directory, file_tree, errors)

    # 결과 출력
    write_output_file(errors)  # 수정된 함수 호출

if __name__ == '__main__':
    validate_file_tree_structure('input.txt')
