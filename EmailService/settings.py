from pydantic import (BaseSettings)


class Settings(BaseSettings):
    Email: str
    Email_Password: str
    
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
