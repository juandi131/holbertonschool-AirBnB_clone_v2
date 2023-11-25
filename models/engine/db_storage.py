#!/usr/bin/python3
""" db storage """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base, BaseModel
import os
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review

USER = os.getenv('HBNB_MYSQL_USER')
PASS = os.getenv('HBNB_MYSQL_PWD')
HOST = os.getenv('HBNB_MYSQL_HOST')
DATA = os.getenv('HBNB_MYSQL_DB')
ENV = os.getenv('HBNB_ENV')


class DBStorage:
    """ db storage """
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(
            f"mysql+mysqldb://{USER}:{PASS}@{HOST}/{DATA}", pool_pre_ping=True)
        if ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ returns a dict """
        classes = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
                   'State': State, 'City': City, 'Amenity': Amenity,
                   'Review': Review}

        dic = {}
        if cls is not None:
            class_name = classes[cls].__name__
            for obj in self.__session.query(classes[cls]).all():
                dic[f"{class_name}.{obj.id}"] = obj
        else:
            for class_name, class_instance in classes.items():
                for obj in self.__session.query(class_instance).all():
                    dic[f"{class_name}.{obj.id}"] = obj
        return dic

    def new(self, obj):
        """ add object to the current database """
        self.__session.add(obj)
        self.save()

    def reload(self):
        """ creates all tables """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def save(self):
        """ commit all changes """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database """
        if obj is not None:
            self.__session.delete(obj)
            self.save()

    def close(self):
        """ close the session """
        self.__session.remove()
