import unittest
import os

from varianter_cit import Cit
from varianter_cit.Parser import Parser


class Basic(unittest.TestCase):

    def test_interface(self):

        abs_path = os.path.abspath(__file__)
        dir_name = os.path.dirname(os.path.dirname(abs_path))
        input_file = os.path.join(dir_name, "data_file_example.txt")

        with open(input_file) as input_file:
            parameters, constraints = Parser.parse(input_file)
        t_value = 2
        input_data = [parameter.get_size() for parameter in parameters]
        program = Cit.Cit(input_data, t_value, constraints)
        result = program.compute()
        self.assertIsNotNone(result)
