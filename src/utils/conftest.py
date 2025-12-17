import os

class Configuration:
    URL = os.getenv("BASE_URL", "http://127.0.0.1:9000/")

    ADMIN_BODY = {
        "username": os.getenv("ADMIN_USERNAME", "admin_user"),
        "password": os.getenv("ADMIN_PASSWORD", "password123")
    }

    USER_BODY = {
        "username": os.getenv("USER_USERNAME", "Jessica_Jimenez"),
        "password": os.getenv("USER_PASSWORD", "password123")
    }
