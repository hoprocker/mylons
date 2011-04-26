from datetime import datetime

from sqlalchemy import create_engine  ##,MetaData,Table
from sqlalchemy.schema import Column  ##,ForeignKey
from sqlalchemy.types import String  ##,Integer,DateTime,PickleType, etc
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

"""
conf.logins contains the following:
DB_HOST = ""
DB_USER = ""
DB_PASS = ""
DB_NAME = ""
DB_DEFAULTS_FILE = ""
"""
from conf.logins import *

MAIN_DB = "%s://%s:%s@%s/%s?charset=utf8" % (DB_PROTO, DB_USER, DB_PASS, DB_HOST, DB_NAME)

TOKEN_LENGTH = 16
POOL_TIMEOUT = 1800 ## timeout in seconds that mysql connections are valid
USERLIST_TYPES = {
        'normal': 0,
        'suppression': 1,
}

db_engine = create_engine(MAIN_DB, pool_recycle=POOL_TIMEOUT, echo_pool=True)

# SQLAlchemy session manager.
Session = scoped_session(sessionmaker())

## declarative definitions
Base = declarative_base(bind=user_engine)

class CommonColumnsMixin(object):
    id = Column('id', Integer, primary_key=True, autoincrement=True, unique=True)
    ctime = Column('ctime', DateTime, default=datetime.now())
    atime = Column('atime', DateTime)
    mtime = Column('mtime', DateTime)

"""
class SampleTable(Base,CommonColumnsMixin):
    __tablename__ = 'sample'

    sample_col = Column('sample_col', String(512), unique=True, nullable=False)
    def __unicode__(self):
        return "%s" % (str(self.id),)
    def __str__(self):
        return self.__unicode__()
"""

## if importing existing tables
"""
meta = MetaData(prosper_engine)

class SampleORMTable(object):
    pass
"""

def init_model():
    """
    table setup and definition

    optionally import table definitions, and create any declarative-style tables; this
    is called from the setup method in main.py
    """

    ## if importing existing tables
    """
    ## overly-complicated method of assoc obj<-->tbl def args b/c we want to 
    ## decouple table creation, in case we need to modify args/kwargs
    tbl_maps = []
    tbl_maps.append((SampleORMTable, ('sample_table_name', meta,
                                Column('id',
                                        Integer,
                                        primary_key=True,
                                        unique=True,
                                        index=True))))
    for obj, tbl_def in tbl_maps:
        kwargs = {"autoload":True, "autoload_with":db_engine}
        mapper(obj, Table(*tbl_def, **kwargs))
    """

    ## now declarative table creation
    Base.metadata.create_all()
