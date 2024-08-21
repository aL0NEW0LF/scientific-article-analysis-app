FROM python:3.12-slim

WORKDIR /code

COPY ./app ./app

RUN pip install langchain==0.2.1 fastapi langserve uvicorn langchain-community==0.2.1 chromadb ollama
RUN pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cpu
RUN pip3 install transformers tqdm numpy scikit-learn scipy nltk sentencepiece
RUN pip3 install --no-deps sentence-transformers sse_starlette
RUN pip install -U "huggingface_hub[cli]"
RUN huggingface-cli download dunzhang/stella_en_1.5B_v5

CMD exec uvicorn app.server:app --host 0.0.0.0 --port 8000