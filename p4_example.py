from flask import Flask, request, redirect, render_template

import json
import boto3
import uuid

AWSKEY = ''
AWSSECRET = ''
PUBLIC_BUCKET = 'garfsters-web-public'
DYNAMOTABLE = 'Images'
STORAGE_URL = 'https://s3.amazonaws.com/' + PUBLIC_BUCKET + '/'

def get_public_bucket():
    s3client = boto3.resource(service_name='s3',
                          region_name='us-east-1',
                          aws_access_key_id=AWSKEY,
                          aws_secret_access_key=AWSSECRET
                          )

    bucket = s3client.Bucket(PUBLIC_BUCKET)
    return bucket

def get_dynamo_table():
    dynamo = boto3.resource(service_name='dynamodb',
                            region_name='us-east-1',
                            aws_access_key_id=AWSKEY,
                            aws_secret_access_key=AWSSECRET)
    table = dynamo.Table(DYNAMOTABLE)
    return table

def uploadfile():
    bucket = get_public_bucket()
    table = get_dynamo_table()

    file = request.files["file"]
    caption = request.form.get("caption")
    filename = file.filename
    file_id = str(uuid.uuid4())
    # you can get other form elements like this: x = request.form.get('x')

    #content type = ct
    # the code is just informing us of the file type being a png.
    ct = 'image/jpeg' # it can also be ct = '' we're just assuming it's a jpeg at first
    if filename.endswith('.png'):
        ct = 'image/png'

    bucket.upload_fileobj(file, filename, ExtraArgs={'ContentType': ct}) # informing us it's a .png

    table.put_item(Item={
        'uuid':file_id,
        'caption': caption,
        'filename': filename
        })
    return { 'results': 'OK' }

def listfiles():
    table = get_dynamo_table()
    items = table.scan()['Items']

    output = []
    for item in items:
        d = {'filename': item['filename'],'caption': item['caption']}
        output.append(d)

    return {'url':STORAGE_URL, 'items': output}





