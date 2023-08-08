import os
from minio import Minio
from minio.error import S3Error

client = Minio(endpoint="minioapi.shomamamama.com",
    access_key="biighunter",
    secret_key="11236939.Smh",
    secure=True)

def upload_folder():
    try:
        bucket_name = "taco-files"
        folder_path = "/root/HoHoHoo/Taco/mySite"
        
        if not client.bucket_exists(bucket_name):
            return f"{bucket_name} bucket does not exist :("
        else:
            try:
                for root, _, files in os.walk(folder_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        object_name = os.path.relpath(file_path, folder_path)
                        with open(file_path, "rb") as file_data:
                            file_size = os.path.getsize(file_path)
                            if file_size == 0:
                                print(f"Skipping empty file: {object_name}")
                                continue
                            client.put_object(bucket_name, object_name, file_data, length=file_size)
                return f"Folder {folder_path} successfully uploaded to {bucket_name}"
            except FileNotFoundError:
                return "Folder not found."
    except Exception as e:
        return f"Error: {e}"
    
upload_folder()