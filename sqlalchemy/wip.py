from sqlalchemy import create_engine #create_engine é uma fábrica de conexoes

engine = create_engine(
    'postgresql+psycopg://app_user:app_password@localhost:7000/app_db'
)

con = engine.connect()