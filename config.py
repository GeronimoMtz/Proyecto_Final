class BasicConfig:
    USER_DB = 'postgres'
    PASS_DB = 'admin'
    URL_DB = 'localhost'
    NAME_DB = 'dbfinal'
    FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'
    SQLALCHEMY_DATABASE_URI = FULL_URL_DB
    DEBUG = True
    SECRET_KEY = "secretKey"
    BCRYPT_LOG_ROUNDS = 13