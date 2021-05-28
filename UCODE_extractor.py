def ucode(img):
    file = open(img)
    lastname = (file.name).split("-")

    print(lastname[-1].split(".")[0])


# smiling-face.jpg was the name of the selfie
ucode("smiling-face.jpg")


# import logging
# import boto3
# from botocore.exceptions import ClientError


# def upload_file(file_name, bucket, object_name=None):
#
#     # If S3 object_name was not specified, use file_name
#     if object_name is None:
#         object_name = file_name
#
#     # Upload the file
#     s3_client = boto3.client('s3')
#     try:
#         response = s3_client.upload_file(file_name, bucket, object_name)
#     except ClientError as e:
#         logging.error(e)
#         return False
#     return True
#
#
# s3 = boto3.client('s3')
# with open("smiling_face.jpg", encoding="utf8") as f:
#     s3.upload_fileobj(f, "kwikpic_selfies", "OBJECT_NAME")
