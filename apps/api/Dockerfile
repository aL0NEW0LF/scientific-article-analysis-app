FROM python:3.11-slim

WORKDIR /code

COPY ./app ./app

RUN pip install -U langchain fastapi langserve uvicorn langchain-community chromadb ollama langchain-ollama langchain-huggingface langchain-chroma
RUN pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cpu
RUN pip3 install transformers tqdm numpy scikit-learn scipy nltk sentencepiece
RUN pip3 install --no-deps sentence-transformers huggingface-cli sse_starlette
RUN pip install -U "huggingface_hub[cli]"
RUN huggingface-cli download dunzhang/stella_en_1.5B_v5

CMD exec uvicorn app.server:app --host 0.0.0.0 --port 8000