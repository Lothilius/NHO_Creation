__author__ = 'Lothilius'

from sqlalchemy.orm import sessionmaker
from sqlalchemy import BigInteger, Column, Date, DateTime, Enum, Float, Index, Integer, Numeric, SmallInteger, String, Text, VARBINARY, text
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timedelta
from sqlalchemy import desc
from sqlalchemy import update
from sqlalchemy import connectors as conn
from sqlalchemy.orm.exc import MultipleResultsFound
from os import system
from authentication import mysql_engine_test



Base = declarative_base()

db = mysql_engine_test()

Session = sessionmaker()
Session.configure(bind=db)

session = Session()



class Profiles(Base):
    __tablename__ = u'Profiles'

    key_id = Column(Integer, primary_key=True)
    id = Column(String(18), nullable=True)
    name = Column(String(63), nullable=True)

class Title_Profile_Mapping(Base):
    __tablename__ = u'Title_Profile_Mapping'

    key_id = Column(Integer, primary_key=True)
    profile_id = Column(Integer, nullable=True)
    title = Column(String(100), nullable=True)

    def __init__(self, key_id, profile_id, title):
        self.key_id = key_id
        self.profile_id = profile_id
        self.title = title
