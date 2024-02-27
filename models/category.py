# компоненты библиотеки для описания структуры таблицы
from sqlalchemy import Column, String, Integer, Boolean

from data_base.dbcore import Base


class Category(Base):
    """
    Класс-модель для описания таблицы "Категория товара",
    основан на декларативном стиле SQLAlchemy
    """
    # название таблицы
    __tablename__ = 'category'

    # поля таблицы
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    is_active = Column(Boolean)

    def __repr__(self):
        """
        Метод возвращает формальное строковое представление указанного объекта
        """
        return self.name
