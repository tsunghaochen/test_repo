from zenml import step
from zenml.logger import get_logger
from parsing_pipeline.main  import my_parser

logger = get_logger(__name__)

@step(enable_cache=False)
def parsing_pipe(parsing_doc: str) -> str:
    parsed_data = my_parser(parsing_doc)
    return parsed_data