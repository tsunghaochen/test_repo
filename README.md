# test_repo
Create mock repo strcutrue and apply `zenml` codes accordingly

# QuickStart

1. install dependencies with `poetry`
```bash
poetry install 
```
2. login with `zenml`
```bash
zenml login https://zenml.axa-rev-preprod-mpl-int.merlot.eu-central-1.aws.openpaas.axa-cloud.com --no-verify-ssl
```
3. choose the correct `zenml stack` and installed necessary dependencies with `zenml`
```bash
zenml stack set default-s3-mlflow
zenml integration install mlflow s3
```
4. set python path at root repo
```bash
export PYTHONPATH="$(pwd)"
```
5. run the code
```bash
python infrastructure/zenml/run.py
```