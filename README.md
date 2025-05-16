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

- run pipeline locally (with python orchestrator)
```bash
zenml stack set default-s3-mlflow
zenml integration install mlflow s3
```

- run pipeline remotely (wiht Airflow)
```bash
zenml stack set airflow-dockerhub-s3
zenml integration install mlflow s3 airflow
zenml init # this step is necessary to let zenml know where is the root repo.
```

**Note**: Without doing `zenml init`, zenml will not know the exact root repo location and will miss source codes in artifacts

4. set python path at root repo
```bash
export PYTHONPATH="$(pwd)"
```
5. run the code
```bash
python infrastructure/zenml/run.py
```