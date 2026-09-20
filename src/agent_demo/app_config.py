from pydantic_settings import BaseSettings, SettingsConfigDict


class AppConfig(BaseSettings):
    llm_base_url:str
    llm_api_key:str
    llm_model:str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


app_config = AppConfig()