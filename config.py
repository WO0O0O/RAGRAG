import os

class Settings:
    """
    Application configuration settings.
    Loads configurations from environment variables.
    """
    # Static X-API-Key used to authenticate clients.
    # Default provided for local development.
    API_KEY: str = os.getenv("FINSPAM_API_KEY", "dev-api-key-12345")

settings = Settings()
