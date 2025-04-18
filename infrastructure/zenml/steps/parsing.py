import sys
import os
from zenml import step
from zenml.logger import get_logger
from apps.parsing_pipeline.parser  import my_parser

logger = get_logger(__name__)

@step
def parsing_pipe(parsing_doc: str) -> str:
    parsed_data = my_parser(parsing_doc)
    return parsed_data