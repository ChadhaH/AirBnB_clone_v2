#!/usr/bin/python3
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker


class DBStorage:
    """
        Represents a database storage engine.
    """
    __engine = None
    __session = None

    user = getenv("HBNB_MYSQL_USER")
    pwd = getenv("HBNB_MYSQL_PWD")
    db = getenv("HBNB_MYSQL_DB")
    host = getenv("HBNB_MYSQL_HOST")
    env = getenv("HBNB_ENV")

    self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                  .format(user, pwd, host, db),
                                  pool_pre_ping=True)
    if env == "test":
        Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
            Return dictionnary of objects
        """
        dict = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for i in query:
                key = "{}.{}".format(type(i).__name__, i.id)
                dic[key] = i
        else:
            lis = [State, City, User, Place, Review, Amenity]
            for j in lis:
                query = self.__session.query(j)
                for i in query:
                    key = "{}.{}".format(type(i).__name__, i.id)
                    dict[key] = i
        return (dict)

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        sess = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess)
        self.__session = Session()

    def close(self):
        self.__session.close()
