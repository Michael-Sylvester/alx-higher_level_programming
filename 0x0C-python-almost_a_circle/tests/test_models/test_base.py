import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_to_json_string_empty(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_single_dict(self):
        input_list = [{"key": "value"}]
        self.assertEqual(Base.to_json_string(input_list), '[{"key": "value"}]')

    def test_to_json_string_multiple_dicts(self):
        input_list = [{"key1": "value1"}, {"key2": "value2"}]
        self.assertEqual(Base.to_json_string(input_list),
                         '[{"key1": "value1"}, {"key2": "value2"}]')

    def test_to_json_string_nested_dicts(self):
        input_list = [{"key1": {"nested_key": "nested_value"}}]
        self.assertEqual(Base.to_json_string(input_list),
                         '[{"key1": {"nested_key": "nested_value"}}]')

    def test_save_to_file_empty_list(self):
        Base.save_to_file([])
        with open("Base.json", 'r') as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_single_object(self):
        class TestClass(Base):
            pass
        obj = TestClass()
        Base.save_to_file([obj])
        with open("TestClass.json", 'r') as file:
            self.assertEqual(file.read(), "[{\"id\": 1}]")

    def test_save_to_file_multiple_objects(self):
        class TestClass(Base):
            pass
        obj1 = TestClass()
        obj2 = TestClass()
        Base.save_to_file([obj1, obj2])
        with open("TestClass.json", 'r') as file:
            self.assertEqual(file.read(), "[{\"id\": 1}, {\"id\": 2}]")

    def test_from_json_string_empty_string(self):
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_single_dict(self):
        input_string = '[{"key": "value"}]'
        self.assertEqual(Base.from_json_string(input_string), [{"key": "value"}])

    def test_from_json_string_multiple_dicts(self):
        input_string = '[{"key1": "value1"}, {"key2": "value2"}]'
        self.assertEqual(Base.from_json_string(input_string),
                         [{"key1": "value1"}, {"key2": "value2"}])

    def test_create_rectangle(self):
        class Rectangle(Base):
            def __init__(self, width, height, x=0, y=0, id=None):
                super().__init__(id)
                self.width = width
                self.height = height
                self.x = x
                self.y = y

            def to_dictionary(self):
                return {
                    'id': self.id,
                    'width': self.width,
                    'height': self.height,
                    'x': self.x,
                    'y': self.y
                }
        rect = Rectangle.create(width=10, height=5, x=1, y=2)
        self.assertEqual(rect.to_dictionary(), {'id': 1, 'width': 10, 'height': 5, 'x': 1, 'y': 2})


if __name__ == '__main__':
    unittest.main()
