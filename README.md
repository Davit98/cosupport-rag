# cosupport-rag


### Setup

1. Create .env file at the root and add your credentials (OPENAI_API_KEY, PINECONE_API_KEY, and PINECONE_INDEX_NAME)
2. Run ```poetry install``` to install project's dependencies. To install optional groups, e.g. 'dev', you need to
   run ```poetry install --with dev```


### Run dashboard

```bash
export PYTHONPATH=.
streamlit run src/dashboard.py --server.port 8502  --server.address 0.0.0.0 --theme.backgroundColor "#FFFFFF" --theme.secondaryBackgroundColor "#EDF7FF" --theme.textColor "#000000"
```

### Running Tests

```shell
pytest -s -vv tests
```