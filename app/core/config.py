import os 

class Settings:

    DATABASE_URL:str = os.getenv("DATABASE_URL","mysql+pymysql://root:root@localhost:3306/ContactManagerDB")

    SECRET_KEY: str = os.getenv("SECRET_KEY","change-me-in-production")

    ALGORITHM: str =os.getenv("ALGORITHM","HS256")

    ACCESS_TOKEN_EXPIRE_MINUTES:int = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES",500)

settings = Settings()