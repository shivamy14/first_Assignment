from minio import Minio
from io import BytesIO
from minio.error import S3Error
import uuid

client = Minio(
    "minio:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
    secure=False
)

BUCKET = "images"


def upload(filename: str, data: bytes, content_type: str) -> str:
    try:
        if not client.bucket_exists(BUCKET):
            client.make_bucket(BUCKET)
    except S3Error:
        pass  # bucket already exists

    object_name = f"{uuid.uuid4()}_{filename}"

    client.put_object(
        bucket_name=BUCKET,
        object_name=object_name,
        data=BytesIO(data),
        length=len(data),
        content_type=content_type
    )

    return f"http://localhost:9000/{BUCKET}/{object_name}"
