import unittest
from functions.run_python_file import run_python_file


class TestRunPythonFile(unittest.TestCase):
        
    def test_run_python_file_calculator_main(self):
        required = [
            "STDOUT: Calculator App",
            "Usage: python main.py \"<expression>\"",
            "Example: python main.py \"3 + 5\"",
        ]
        
        output = run_python_file("calculator", "main.py")
        
        for token in required:
            self.assertIn(token, output, msg=f"Missing token: {token}")
        
    def test_run_python_file_calculator_expression(self):
        required = [
            "STDOUT:",
            "\"expression\": \"3 + 5\"",
            "\"result\": 8"
        ]
        
        output = run_python_file("calculator", "main.py", ["3 + 5"])
        
        for token in required:
            self.assertIn(token, output, msg=f"Missing token: {token}")
            
    def test_run_python_file_outside_permitted(self):
        required = "Error: Cannot execute \"../main.py\" as it is outside the permitted working directory"
        
        output = run_python_file("calculator", "../main.py")
        self.assertIn(required, output, msg=f"Missing token: {required}")
        
    def test_run_python_file_lorem_txt(self):
        required = "Error: \"lorem.txt\" is not a Python file"
        
        output = run_python_file("tests", "lorem.txt")
        self.assertIn(required, output, msg=f"Missing token: {required}")
        
    def test_run_python_file_doesnt_exist(self):
        required = "Error: \"nonexistent.py\" does not exist or is not a regular file"
        
        output = run_python_file("tests", "nonexistent.py")
        self.assertIn(required, output, msg=f"Missing token: {required}")
        

if __name__ == "__main__":
    unittest.main()