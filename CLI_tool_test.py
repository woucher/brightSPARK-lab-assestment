import unittest
import CLI_tool

class testMethods(unittest.TestCase):

    def test_CLI_tool(self):

        local_file_str = 'E:\Desktop\\brightSPARK lab job app\given_test_file.csv'
        self.assertNotEqual(CLI_tool(local_file_str), None)

    def test_x(self):
        self.assertEqual(None,None)

if __name__ == '__main__':
    unittest.main()