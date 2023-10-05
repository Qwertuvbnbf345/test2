import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String
import faker
import random

engine = create_engine("postgresql+psycopg2://postgres:1234@localhost/home.test.work")

Base = declarative_base()
Session = sessionmaker(bind=engine)
s = Session()

fake = faker.Faker("ru_RU")


class Mates(Base):
    __tablename__ = "OK test 4"
    name = Column(String, nullable=False, )
    age = Column(Integer, nullable=False)
    id = Column(Integer, nullable=False, primary_key=True)


Base.metadata.create_all(engine)

# s.query(Mates).filter(Mates.id >= 2000).delete()
s.query(Mates).filter(Mates.id % 2 == 0).update({"name": "Jackie Chan"})
s.commit()
#  for b in a:
#      return True
#  return False
#

# res = check("Леша")
# if res:
#    print("ДА")
# else:
#    print("НЕТ")
