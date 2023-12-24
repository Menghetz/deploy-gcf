import main
import unittest
import json
from unittest.mock import Mock


class TestCalculations(unittest.TestCase):
    def test_print_hello_world(self):
        data = {}
        req = Mock(get_json=Mock(return_value=data), args=data)

        # Call tested function
        assert main.hello_world(req) == "Hello world!"

    def test_print_name(self):
        name = "Bob"
        data = {"name": name}
        req = Mock(get_json=Mock(return_value=data), args=data)

        # Call tested function
        assert main.hello_world(req) == f"Hello {name}!"


if __name__ == '__main__':
    unittest.main()