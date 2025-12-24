import os 
import sys 
from src.ML_project.exception import CustomException
from src.ML_project.logger import logging
import pandas as pd 
import pymysql
from dotenv import load_dotenv

load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv("db")

def read_sql_data():
    logging.info("Reading SQL database Started")

    try:
      mydb=pymysql.connect(
         host=host,
         user=user,
         password=password,
         db=db
        )
      logging.info("connection established",mydb)
      df=pd.read_sql_query('Select * from students',mydb)
      print(df.head())

      return df 

    except Exception as ex :
        raise CustomException(ex)
