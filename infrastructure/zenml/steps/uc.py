from zenml import step
from zenml.logger import get_logger
from apps.uc_pipeline.uc import my_use_case

logger = get_logger(__name__)

@step
def uc_pipe(graph: str, use_case: str) -> str:
    output = my_use_case(graph, use_case)
    return output