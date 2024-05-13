"""
Этот файл создан для того, чтобы вся папка воспринималась, как модуль.
Тут в основном мы определили создание движка для подключения к
базе данных и так же создание базового класса моделей
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

engine = create_engine('mysql+pymysql://root:root@localhost:3306/test_alchemy')
# engine = create_engine('mysql://root:kAkA$84kA097@localhost:3306/test_alchemy')
# engine = create_engine('sqlite:///локальный/путь/к/базе/данных/тестовая_база.db')
# engine = create_engine('sqlite:///:memory:')
Base = declarative_base()
