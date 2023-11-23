import os
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

STORE = os.getenv('HBNB_TYPE_STORAGE')

if STORE == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
