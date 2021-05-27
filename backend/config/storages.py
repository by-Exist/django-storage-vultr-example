from storages.backends.s3boto3 import S3Boto3Storage


# 해당 이름의 버킷이 Vultr Object에 생성되어 있어야 함


class StaticStorage(S3Boto3Storage):
    bucket_name = "your-static-bucket-name"


class MediaStorage(S3Boto3Storage):
    bucket_name = "your-media-bucket-name"
