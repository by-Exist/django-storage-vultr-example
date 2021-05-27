# Django-Storage[Vultr]

- Django에서 Vultr Storage를 사용하는 예제

## Requirements

- django
- django-storages
- boto3

## 중요 파일

- backend/config/storages.py
- backend/config/vultr_settings.py

## 설명

- storages.py 파일과 vultr_settings.py 참조

## 테스트

### Vultr 설정

- vultr에서 object storage를 생성
- 해당 object의 overview 확인
  - Location => "AWS_S3_REGION_NAME" (object의 hostname dot(.)으로 구분된 가장 앞부분)
  - Access Key => "AWS_ACCESS_KEY_ID"
  - Secret Key => "AWS_SECRET_ACCESS_KEY"
- 버킷 생성
  - static 용 버킷
  - media 용 버킷

### Django 설정

- 해당 레포지토리 clone
- Django의 Admin User 생성
- storages.py의 bucket_name을 자신의 bucket_name으로 수정
- python manage.py migrate

### Static Storage

- python manage.py collectstatic
- yes 입력
- vultr의 object에 접속
- 자신의 static 버킷에 파일이 저장되었는지 확인

### Media Storage

- python manage.py runserver
- 어드민 페이지 접속 - http://127.0.0.1/admin
- Login -> post -> 임의의 게시물 생성
- vultr의 object에 접속
- 자신의 media 버킷에 파일이 저장되었는지 확인
