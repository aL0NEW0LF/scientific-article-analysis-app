FROM ollama/ollama:latest

WORKDIR /model

COPY ./run_ollama.sh /model/run_ollama.sh

RUN chmod +x run_ollama.sh
RUN /model/run_ollama.sh