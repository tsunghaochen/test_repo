from zenml import step
from zenml.logger import get_logger
from uc_pipeline.main import my_use_case
# import os
# import urllib3
import mlflow

# # monkey patch to avoid SSL errors
# os.environ["CURL_CA_BUNDLE"] = ""
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

logger = get_logger(__name__)

@step(enable_cache=False, experiment_tracker="mlflow_experiment_tracker")
def uc_pipe(graph: str, use_case: str) -> str:
    output = my_use_case(graph, use_case)
    mlflow.log_param("graph_str", graph)
    return output