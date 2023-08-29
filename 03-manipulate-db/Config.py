class Config:
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = (
        "postgresql+psycopg2://local_admin_h:admin123@localhost/rms"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
