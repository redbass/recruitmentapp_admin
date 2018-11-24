from io import StringIO
from unittest import TestCase

from lib.picklist import csv_to_json_values


class TestPicklist(TestCase):

    def setUp(self):
        self.csv = """
        key_1, value_1
        key_2,    value_2     
        
        key_3, value_3
           key_4,    value_4   
        """  # noqa:  W391

    def test_convert_csv_to_json_key_value(self):
        expected_result = [
            {'key': "key_1", "value": "value_1"},
            {'key': "key_2", "value": "value_2"},
            {'key': "key_3", "value": "value_3"},
            {'key': "key_4", "value": "value_4"}
        ]

        csv_file = StringIO(self.csv)
        result = csv_to_json_values(csv_file)

        self.assertEquals(expected_result, list(result))
