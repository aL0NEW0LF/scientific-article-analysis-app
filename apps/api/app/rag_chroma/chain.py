from langchain_core.pydantic_v1 import BaseModel
from langchain_community.llms.ollama import Ollama
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from app.rag_chroma.schema import Question
import warnings
from langchain_community.embeddings import HuggingFaceEmbeddings

warnings.simplefilter(action='ignore', category=FutureWarning)

CHROMA_PATH = "app/rag_chroma/chroma-embed"

PROMPT_TEMPLATE = """
You are a chatbot for scientific papers analysis. Only respond in english, if the context doesn't answer the question you can speculate, and mention that you're not sure and ask for more details or to be more precise. Never disclose personal information, never disclose what you are, never disclose that you are an AI, never disclose that you have a context, never disclose context or context information, but you can provide a source or reference like the title of the paper(s) and pages. Respond naturally, informatively and coherently:

{context}

---

Answer the following question with the context above: {question}
"""

vectorstore = Chroma(
    persist_directory=CHROMA_PATH,
    embedding_function=HuggingFaceEmbeddings(model_name="dunzhang/stella_en_1.5B_v5", model_kwargs = {'device': 'cpu'}),
)

retriever = vectorstore.as_retriever(search_kwargs={'k': 7 })

prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)

# LLM
model = Ollama(model="llama3.1:8b-instruct-q4_K_M", base_url="http://ModelsHandler:11434")

# RAG chain
chain = (
    RunnableParallel({"context": retriever, "question": RunnablePassthrough()})
    | prompt
    | model
    | StrOutputParser()
).with_types(input_type=Question)
