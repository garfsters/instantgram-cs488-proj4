Created a simple “Image Uploader” system similar to https://imgur.com/ using DynamoDB and S3.

Web Page - Has the following fields:
- Displayed Images (128px)
- Caption (below image)
- File Upload
- Button

Web Service:
- Uploads image (with or without caption)
  - Saves id (uuid), caption, image name, etc., to DynamoDB
  - Saves image data to S3
- Lists Images
  - List method is from the database (not S3)
