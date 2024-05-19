from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base


# 'mysql+pymysql://<user>:<user_password>@<host>:<port>/<db_name>'

engine = create_engine(
    url='mysql+pymysql://root:kAkA$84kA097@localhost:3306/alchemy_summary'
)

Base = declarative_base()
