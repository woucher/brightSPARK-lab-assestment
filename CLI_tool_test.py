import unittest
import os
from CLI_tool import main as CLI_tool_main
example_1 = """\
records:
- name: Zelma Ivatt 
  details: In division 1 from 2018-01-02 performing Offensive Duties 
- name: Terza Lowton 
  details: In division 1 from 2017-09-15 performing Defensive Duties 
- name: Zedekiah Miller 
  details: In division 3 from 2018-04-09 performing Offensive Duties 
  """
example_2 = """\
records:
- details: In division 1 from 2018-01-02 performing Offensive Duties
  name: Zelma Ivatt
- details: In division 1 from 2017-09-15 performing Defensive Duties
  name: Terza Lowton
- details: In division 3 from 2018-04-09 performing Offensive Duties
  name: Zedekiah Miller 
  """
all_examples = [example_1] + [example_2]
all_examples_no_space = [example_1.replace(" ", "")] + [example_2.replace(" ", "")]

local_file_str = 'E:\Desktop\\brightSPARK lab job app\given_test_file.csv'
class testMethods(unittest.TestCase):
    def test_os_path_given(self):
        file_path = os.path.abspath(os.getcwd()) +"\given_test_file.csv"
        self.assertEqual(type(file_path),str)
    def test_CLI_tool_is_called(self):
        file_path = os.path.abspath(os.getcwd()) +"\given_test_file.csv"
        self.assertIsNotNone(CLI_tool_main(file_path,3))
    def test_CLI_tool_output(self):
        file_path = os.path.abspath(os.getcwd()) +"\given_test_file.csv"
        our_result = CLI_tool_main(file_path,3)
        self.assertIn(our_result,all_examples)
    def test_CLI_tool_output_nospace(self):
        file_path = os.path.abspath(os.getcwd()) +"\given_test_file.csv"
        our_result = CLI_tool_main(file_path,3)
        our_result = our_result.replace(" ", "")
        self.assertIn(our_result,all_examples_no_space)
if __name__ == '__main__':
    unittest.main()