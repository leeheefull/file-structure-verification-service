# 01_변환정보 디렉토리 및 파일 생성
mkdir -p "target_directory/01_변환정보"
touch "target_directory/01_변환정보/file1.xlxs"

# 02_수치도화 디렉토리 및 파일 생성
mkdir -p "target_directory/02_수치도화/01_수정도화모델"
touch "target_directory/02_수치도화/01_수정도화모델/file1.dwg"
touch "target_directory/02_수치도화/01_수정도화모델/file2.dxf"

mkdir -p "target_directory/02_수치도화/02_수정도엽"
touch "target_directory/02_수치도화/02_수정도엽/file1.dwg"
touch "target_directory/02_수치도화/02_수정도엽/file2.dxf"

mkdir -p "target_directory/02_수치도화/03_완성도엽"
touch "target_directory/02_수치도화/03_완성도엽/file1.dwg"
touch "target_directory/02_수치도화/03_완성도엽/file2.dxf"

# 03_지리조사 디렉토리 및 파일 생성
mkdir -p "target_directory/03_지리조사/01_모델색인도"

mkdir -p "target_directory/03_지리조사/02_조사사항기록도면/01_공개제한용"
touch "target_directory/03_지리조사/02_조사사항기록도면/01_공개제한용/file1.dwg"
touch "target_directory/03_지리조사/02_조사사항기록도면/01_공개제한용/file2.dxf"

mkdir -p "target_directory/03_지리조사/02_조사사항기록도면/02_공개용"
touch "target_directory/03_지리조사/02_조사사항기록도면/02_공개용/file1.dwg"

mkdir -p "target_directory/03_지리조사/03_지리조사시획득(사용한 자료)"
touch "target_directory/03_지리조사/03_지리조사시획득(사용한 자료)/file1.dwg"

# 04_편집파일 디렉토리 및 파일 생성
mkdir -p "target_directory/04_편집파일/01_수치지형도 1.0/01_구조화편집(통합)/01_공개제한용"
touch "target_directory/04_편집파일/01_수치지형도 1.0/01_구조화편집(통합)/01_공개제한용/file1.gpkg"
touch "target_directory/04_편집파일/01_수치지형도 1.0/01_구조화편집(통합)/01_공개제한용/file2.shp"

mkdir -p "target_directory/04_편집파일/01_수치지형도 1.0/01_구조화편집(통합)/02_공개용"
touch "target_directory/04_편집파일/01_수치지형도 1.0/01_구조화편집(통합)/02_공개용/file1.gpkg"
touch "target_directory/04_편집파일/01_수치지형도 1.0/01_구조화편집(통합)/02_공개용/file2.shp"

mkdir -p "target_directory/04_편집파일/02_수치지형도 2.0/02_구조화편집(도엽)/01_공개제한용"
touch "target_directory/04_편집파일/02_수치지형도 2.0/02_구조화편집(도엽)/01_공개제한용/file1.gpkg"
touch "target_directory/04_편집파일/02_수치지형도 2.0/02_구조화편집(도엽)/01_공개제한용/file2.shp"

mkdir -p "target_directory/04_편집파일/02_수치지형도 2.0/02_구조화편집(도엽)/02_공개용"
touch "target_directory/04_편집파일/02_수치지형도 2.0/02_구조화편집(도엽)/02_공개용/file1.gpkg"
touch "target_directory/04_편집파일/02_수치지형도 2.0/02_구조화편집(도엽)/02_공개용/file2.shp"

# 05_메타데이터 및 관리 파일 디렉토리 생성
mkdir -p "target_directory/05_메타데이터 및 관리 파일/01_메타데이터"
mkdir -p "target_directory/05_메타데이터 및 관리 파일/02_기판표준"
mkdir -p "target_directory/05_메타데이터 및 관리 파일/03_보안바운더리"

# 06_품질검사보고서 디렉토리 및 파일 생성
mkdir -p "target_directory/06_품질검사보고서/01_기본측량성과 검증결과표"
mkdir -p "target_directory/06_품질검사보고서/02_자체검사 err 파일"
touch "target_directory/06_품질검사보고서/02_자체검사 err 파일/file1.err"

# 07_용역결과보고서 디렉토리 및 파일 생성
mkdir -p "target_directory/07_용역결과보고서"
touch "target_directory/07_용역결과보고서/file1.dwg"
touch "target_directory/07_용역결과보고서/file2.dxf"

# 08_기타성과 디렉토리 및 파일 생성
mkdir -p "target_directory/08_기타성과"
touch "target_directory/08_기타성과/file1.dwg"
touch "target_directory/08_기타성과/file2.dxf"

echo "디렉토리 및 파일 생성이 완료되었습니다."
