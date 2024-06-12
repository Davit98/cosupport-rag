FROM python:3.10.9

WORKDIR /app

COPY poetry.lock poetry.lock
COPY pyproject.toml pyproject.toml

RUN pip install --upgrade pip && \
    pip install "poetry==1.5.1" && \
    poetry config installer.max-workers 10 && \
    poetry config virtualenvs.create false && \
    poetry install

COPY . .

ENV PYTHONPATH .

EXPOSE 8502
ENTRYPOINT streamlit run src/dashboard.py --server.port 8502  --server.address 0.0.0.0