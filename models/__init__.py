"""Models package and the single storage object used by the application."""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
