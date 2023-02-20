#!/usr/bin/python3
""" Storage """
from models.engine.file_storage import FileStorage
from .base_model import BaseModel

storage = FileStorage()
storage.reload()
