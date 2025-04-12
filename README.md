# HSA13_hw27_Serverless_calculations


Follow these steps to deploy your AWS Lambda image converter function:
1. Create the AWS Lambda Layer with Pillow

Run the following script to create a zip file containing the Pillow library:

```
chmod +x create_pillow_layer.sh
./create_pillow_layer.sh
```
Upload the generated pillow_layer.zip to AWS Lambda Layers via the AWS Console, and note the ARN (Amazon Resource Name).
2. Prepare the Lambda Function Zip

Create a ZIP file containing your Lambda function (lambda_function.py):

zip lambda_function.zip lambda_function.py

3. Terraform Initialization and Deployment

Initialize and deploy your AWS resources using Terraform:
```
terraform init
terraform apply
```
Terraform will prompt you to confirm the actions—type yes and hit Enter to proceed.
4. Test the Setup

To test your setup:

    Upload a JPEG image file to your source S3 bucket.

    AWS Lambda will automatically trigger and convert the image into BMP, GIF, and PNG formats.

    Converted files will appear in your specified output S3 bucket.
![изображение](https://github.com/user-attachments/assets/ae4d2724-a0dc-40e9-b8dc-09210a2e412e)

