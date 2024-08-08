import warnings
from langchain_huggingface import HuggingFaceEmbeddings

warnings.simplefilter(action='ignore', category=FutureWarning)

def get_embedding_function():
    # embeddings = OllamaEmbeddings(model="mxbai-embed-large:335m")
    embeddings = HuggingFaceEmbeddings(model_name="dunzhang/stella_en_1.5B_v5", model_kwargs = {'device': 'cuda'})
    return embeddings