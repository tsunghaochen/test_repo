from zenml import step
from zenml.logger import get_logger
from apps.uc_pipeline.uc import my_use_case
import mlflow

logger = get_logger(__name__)

@step(enable_cache=False, experiment_tracker="mlflow_experiment_tracker")
def uc_pipe(graph: str, use_case: str) -> str:
    output = my_use_case(graph, use_case)
    mlflow.log_param("graph_str", graph)
    return output