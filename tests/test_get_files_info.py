import unittest
from functions.get_files_info import get_files_info


class TestGetFiles_Info(unittest.TestCase):
        
    def test_get_files_info_calculator(self):
        required = [
            "main.py",
            "tests.py",
            "pkg",
            "file_size=",
            "is_dir="
        ]
        
        output = get_files_info("calculator", ".")
        
        for token in required:
            self.assertIn(token, output, msg=f"Missing token: {token}")
        
    def test_get_files_info_calculator_pkg(self):
        required = [
            "calculator.py",
            "render.py",
            "file_size=",
            "is_dir="
        ]
        
        output = get_files_info("calculator", "pkg")
        
        for token in required:
            self.assertIn(token, output, msg=f"Missing token: {token}")
        
    def test_get_files_info_calculator_bin(self):
        required = "Error: Cannot list \"/bin\" as it is outside the permitted working directory"
        
        output = get_files_info("calculator", "/bin")
        self.assertIn(required, output, msg=f"Missing token: {required}")
        
    def test_get_files_info_calculator_outside(self):
        required = "Error: Cannot list \"../\" as it is outside the permitted working directory"
        
        output = get_files_info("calculator", "../")
        self.assertIn(required, output, msg=f"Missing token: {required}")

if __name__ == "__main__":
    unittest.main()