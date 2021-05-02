from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str
    run_cron_job: bool
    oanda_url: str
    oanda_token: str
    oanda_account: str
    units: int

    class Config:
        env_file = ".env"


settings = Settings()