from venv import create
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os 
import cloudinary
import cloudinary.uploader
import cloudinary.api

cloudinary.config( 
  cloud_name = "", 
  api_key = "", 
  api_secret = "",
)




#SQLALCHEMY_DABASE_URL = "postgresql://postgres:1234!@localhost/SolomonJuliusDatabase"

# DATABASE_URL = \
#     'postgresql://{username}:{password}@{host}:{port}/{database}'.format(
#         username='postgres',
#         password='1111',
#         host='localhost',
#         port='5432',
#         database='solomon',)

if 'RDS_DB_NAME' in os.environ:
    DATABASE_URL = \
        'postgresql://{username}:{password}@{host}:{port}/{database}'.format(
            username=os.environ['RDS_USERNAME'],
            password=os.environ['RDS_PASSWORD'],
            host=os.environ['RDS_HOSTNAME'],
            port=os.environ['RDS_PORT'],
            database=os.environ['RDS_DB_NAME'],
        )
else:
    DATABASE_URL = \
    'postgresql://{username}:{password}@{host}:{port}/{database}'.format(
        username='postgres',
        password='postgres',
        host='aa1u5ij2gyw8uw2.clucxh6clt9r.us-east-1.rds.amazonaws.com',
        port='5432',
        database='ebdb',)

engine  = create_engine(
    DATABASE_URL,)


#engine  = create_engine(
#    SQLALCHEMY_DABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


