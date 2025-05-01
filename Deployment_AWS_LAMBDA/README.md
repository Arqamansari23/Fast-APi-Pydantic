# FastAPI App on AWS Lambda

This repository is a demo for hosting a FastAPI application on AWS Lambda using Mangum.

## Project Structure

``` sh
. ├── .gitignore 
  ├── main.py 
  ├── README.md 
  └── requirements.txt
```

## Requirements

- Python 3.9+
- AWS Account

2. Create a virtual environment and activate it:

    ```sh
    Conda create -p lambda
    conda activate lambda  # On Linux/Mac use `source .venv/bin/activate`
    ```

3. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

## Running Locally

You can run the FastAPI application locally using Uvicorn, but will need to install uvicorn:

```sh
pip install uvicorn
uvicorn main:app --reload
```

## Deploying to AWS Lambda

Zip your FastAPI application and upload the zip to an AWS Lambda Function.

Zip on Windows:

``` powershell
Compress-Archive .\lambda\Lib\site-packages\* -DestinationPath aws_lambda.zip
Compress-Archive .\main.py -Update -DestinationPath aws_lambda.zip
```


## Now Add this .zip file into AWS Lamda Function to deploy your code 