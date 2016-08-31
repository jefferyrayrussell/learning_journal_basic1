from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text
    UnicodeText,
    Unicode,
    Date
)

from .meta import Base


class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    title = Column(UnicodeText)
    # date = Column(UnicodeText)
    creation_date = Column(UnicodeText)
    body = Column(UnicodeText)


Index('my_index', MyModel.id, unique=True, mysql_length=255)

# Index('my_index', MyModel.name, unique=True, mysql_length=255)
# what to do with date sorting?