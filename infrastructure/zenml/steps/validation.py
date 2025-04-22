from zenml import step
from zenml.logger import get_logger
from apps.validation_pipeline.validation import my_validation

logger = get_logger(__name__)

@step(enable_cache=False)
def validation_pipe(output: str, validation: str) -> float:
    score = my_validation(output, validation)
    return score