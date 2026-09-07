import unittest
from models.base_model import BaseModel

class TestBsseModel(unittest.TestCase):
    def test_init(self):
        model = BaseModel()
        self.assrtIsNotDone(model.created_at)
        self.assrtIsNotDone(model.updated_at)
        def test_save(self):
            model = BaseModel()
            old_updated_at = model.updated_at
            model.save()
            self.assertNotEqual(model.updated_at, old_updated_at)