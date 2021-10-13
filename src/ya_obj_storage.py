import os

import boto3

from src.file import filename_from_path


class UploadFileToYaObjCloud:
    endpoint_url = 'https://storage.yandexcloud.net'
    region_name = "ru-central1"
    bucket = os.environ["YA_OBJ_STORAGE_BUCKET"]
    aws_access_key_id = os.environ["YA_OBJ_STORAGE_AWS_ACCESS_KEY_ID"]
    aws_secret_access_key = os.environ["YA_OBJ_STORAGE_AWS_SECRET_ACCESS_KEY"]

    def __call__(self, path: str) -> str:
        filename = filename_from_path(path)

        session = boto3.session.Session()
        s3 = session.client(
            service_name='s3',
            endpoint_url=self.endpoint_url,
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key,
            region_name=self.region_name,
        )

        res = s3.upload_file(path, self.bucket,filename )
        assert res is None

        return f"{self.endpoint_url}/{self.bucket}/{filename}"


if __name__ == '__main__':
    print(UploadFileToYaObjCloud()("../data/opus/v vendetta.opus"))
