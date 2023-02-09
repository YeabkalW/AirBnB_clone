#!/usr/bin/python3
"""create a unique FileStorage Instance for our application"""

from engine.file_storage import FileStorage

storage = FileStorage()

storage.reload()
