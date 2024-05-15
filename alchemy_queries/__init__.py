from sqlalchemy import create_engine

from sqlalchemy.orm import declarative_base


engine = create_engine(
    url='mysql+pymysql://root:kAkA$84kA097@localhost:3306/test_system'
)


Base = declarative_base()
