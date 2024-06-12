from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

PACKAGE_ROOT = Path(__file__).resolve().parent
ENV_FILE_PATH = PACKAGE_ROOT.parent / ".env"
CSV_DATA_PATH = PACKAGE_ROOT.parent / "data/rag_data.csv"


class EnvironmentVariables(BaseSettings):
    model_config = SettingsConfigDict(env_file=ENV_FILE_PATH, env_file_encoding='utf-8', extra='ignore')

    openai_api_key: str

    pinecone_api_key: str
    pinecone_index_name: str


environment_vars = EnvironmentVariables()
