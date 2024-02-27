# компоненты библиотеки для описания структуры таблицы
from sqlalchemy import Column, String, Integer, Float, Boolean, ForeignKey
# импортируем модуль для связки таблиц
from sqlalchemy.orm import relationship, backref

# импортируем модель Категория для связки моделей
from models.category import Category
from data_base.dbcore import Base


class Products(Base):
    """
    Класс для создания таблицы "Товар",
    основан на декларативном стиле SQLAlchemy
    """
    # название таблицы
    __tablename__ = 'products'

    # поля таблицы
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    title = Column(String)
    price = Column(Float)
    quantity = Column(Integer)
    is_active = Column(Boolean)
    category_id = Column(Integer, ForeignKey('category.id'))
    # для каскадного удаления данных из таблицы
    category = relationship(
        Category,
        backref=backref('products',
                        uselist=True,
                        cascade='delete,all'))

    def __repr__(self):
        """
        Метод возвращает формальное строковое представление указанного объекта
        """
        return f"{self.name} {self.title} {self.price}"
