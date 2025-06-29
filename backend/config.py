from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    DATABASE_HOST: str = "localhost"
    DATABASE_NAME: str = "todos"
    DATABASE_USER: str = "postgres"
    DATABASE_PASSWORD: str = ""
    DATABASE_PORT: int = 5432
    app_name: str = "Full Stack To Do App"

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "extra": "ignore"
    }

@lru_cache()
def get_settings():
    return Settings()




# from pydantic_settings import BaseSettings
# import os

# class Settings(BaseSettings):
#     DATABASE_HOST: str = "localhost"
#     DATABASE_NAME: str = "todos"
#     DATABASE_USER: str = "postgres"
#     DATABASE_PASSWORD: str = ""
#     DATABASE_PORT: int = 5432
#     app_name: str = "Full Stack To Do App"

# # debugging function:
#     # def __init__(self, **kwargs):
#     #     super().__init__(**kwargs)
#     #     print("Current working directory:", os.getcwd())
#     #     print("Environment variables available:", os.environ)

#     model_config = {
#         "env_file": ".env",
#         "env_file_encoding": "utf-8",
#         "extra": "ignore"
#     }