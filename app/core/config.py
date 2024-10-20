from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Shortify"
    API_V1_STR: str = "/api/v1"
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///./test.db"
    # 短链接前缀，本服务的域名+短链接跳转接口
    SHORT_URL_PREFIX: str = "http://127.0.0.1:9002/t"


settings = Settings()  # type: ignore
