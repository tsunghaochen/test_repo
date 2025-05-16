import os
from zenml import pipeline, step
from zenml.logger import get_logger
from zenml.config import DockerSettings
from zenml.integrations.airflow.flavors.airflow_orchestrator_flavor import AirflowOrchestratorSettings
from steps import (
    parsing_pipe,
    graph_gen_pipe,
    uc_pipe,
    evaluation_pipe
)

logger = get_logger(__name__)

#
## Test with AXA CA certificates
#
docker_settings = DockerSettings(
    parent_image="docker.io/tsunghaochen/zenml:automodeling_pipeline-orchestrator-intermediate-build-axa",
    environment={
        "REQUESTS_CA_BUNDLE": "/etc/ssl/certs/ca-certificates.crt",
        "SSL_CERT_FILE": "/etc/ssl/certs/ca-certificates.crt",
    }
)

airflow_settings = AirflowOrchestratorSettings(
    dag_output_dir="/Users/z460xj/Documents/airflow_localtest/airflow_docker/dags",  # Change the output path of dag.zip
    # custom_dag_generator="dag_generator_custom", # Don't need this after having axa certs
)

@step(enable_cache=False)
def debug_step():
    print(f"ZENML_STORE_VERIFY_SSL: {os.environ.get('ZENML_STORE_VERIFY_SSL')}")

@pipeline(settings={"docker": docker_settings, "orchestrator": airflow_settings})
def automodeling_pipeline(
    parsing_doc: str,
    uc: str = "Athuring Tool",
    validation: str = "LLM_AAJ",
):
    """
    Start of the automodeling pipeline, call each step function
    """
    debug_step()
    parsed_data = parsing_pipe(parsing_doc)
    knowlege_graph = graph_gen_pipe(parsed_data)
    output = uc_pipe(knowlege_graph, uc)
    score = evaluation_pipe(output, validation)

if __name__ == "__main__":
    automodeling_pipeline(parsing_doc="Axa_Contract2.pdf")
    # can create other pipelines and cascade them by having the output of 
    # first pipeline to be the the input of second pipeline