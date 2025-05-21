# S3 Auto-Delete Untagged Lambda

This Lambda function automatically deletes any file uploaded to an S3 bucket **if it does not have tags** or **does not include the tag `Name`**.

## 🔧 How It Works

1. Triggered by `s3:ObjectCreated:*` event.
2. Checks the tags of the uploaded object.
3. Deletes the object if:
   - It has **no tags**, or
   - It **does not include a `Name` tag**

## ✅ Example Event Trigger

Make sure this is connected to an S3 Event Notification:
- Event type: `s3:ObjectCreated:*`
- Prefix/Suffix (optional)
- Lambda destination: This function

## 📦 Deployment Instructions

### Option 1: Zip Upload
```bash
zip function.zip lambda_function.py
aws lambda update-function-code --function-name s3-auto-delete-untagged --zip-file fileb://function.zip
