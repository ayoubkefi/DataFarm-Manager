from pydantic_settings import BaseSettings 
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    database_url : str 
    api_host : str = "0.0.0.0"
    api_port : int = 8000
    debug : bool = True
    
    class config : 
        env_file = "/home/ayoub/Projects/SOP-Manager/.env"

settings = Settings()