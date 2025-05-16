from zenml import step
from zenml.logger import get_logger
from graph_gen_pipeline.main  import my_knowledge_graph_gen

logger = get_logger(__name__)

@step(enable_cache=False)
def graph_gen_pipe(graph_gen: str) -> str:
    knowlege_graph = my_knowledge_graph_gen(graph_gen)
    return knowlege_graph