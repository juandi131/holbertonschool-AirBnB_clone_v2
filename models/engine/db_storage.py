#!/usr/bin/python3
from os import environ
from sqlalchemy import create_engine, text
from models.base_model import BaseModel, Base
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage():
    """Placeholder"""
    __engine = None
    __session = None

    def __init__(self):
        """instantiation"""
        user = environ.get('HBNB_MYSQL_USER')
        pw = environ.get('HBNB_MYSQL_PWD')
        ht = environ.get('HBNB_MYSQL_HOST')
        db = environ.get('HBNB_MYSQL_DB')
        self.__engine = create_engine(f'mysql+mysqldb://{user}:{pw}@{ht}/{db}',
                                      pool_pre_ping=True)
        if environ.get("HBNB_ENV") == "test":
            Base.metadata.drop(self.__engine)

    def all(self, cls=None):
        """Returns a dict of the specified cls"""
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'State': State, 'City': City, 'User': User,
            'Place': Place, 'Amenity': Amenity, 'Review':
                Review
            }

        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

        ret = {}

        if cls:
            if type(cls) is not str:
                cls = cls.__name__
            for obj in self.__session.query(classes[cls]):
                ret[str(cls) + '.' + obj.id] = obj
        else:
            for k in classes.keys():
                for obj in self.__session.query(classes[k]):
                    ret[str(k) + '.' + obj.id] = obj
        return ret

    def new(self, obj):
        """add a new object to the data base"""
        self.__session.add(obj)

    def save(self):
        """commit all change"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete an object if not null"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """reload all the objets"""
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        Base.metadata.create_all(self.__engine)

        ses = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(ses)

    def close(self):
        """Closes the session"""
        self.__session.close()
