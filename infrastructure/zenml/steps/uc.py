import urllib3
from zenml import step
from zenml.logger import get_logger
from apps.uc_pipeline.uc import my_use_case
import mlflow

from urllib3.util.ssl_ import create_urllib3_context

# Monkey-patch urllib3 to disable SSL verification
def disable_ssl_verification():
    """Disable SSL verification globally for urllib3."""
    def patched_create_urllib3_context(*args, **kwargs):
        context = create_urllib3_context(*args, **kwargs)
        context.check_hostname = False
        context.verify_mode = False
        return context

    urllib3.connection.create_urllib3_context = patched_create_urllib3_context

disable_ssl_verification()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

logger = get_logger(__name__)

@step(enable_cache=False, experiment_tracker="mlflow_experiment_tracker")
def uc_pipe(graph: str, use_case: str) -> str:
    output = my_use_case(graph, use_case)
    mlflow.log_param("graph_str", graph)
    return output