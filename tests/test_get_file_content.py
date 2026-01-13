import unittest
from functions.get_file_content import get_file_content


class TestGetFiles_Content(unittest.TestCase):
        
    def test_get_files_content_lorem(self):
        required = "wait, this isn't lorem ipsum"
        
        output = get_file_content("tests", "lorem.txt")
        
        for token in required:
            self.assertIn(token, output, msg=f"Missing token: {token}")
        
    def test_get_files_contents_outside_permitted(self):
        required = "Error: Cannot read \"/bin/cat\" as it is outside the permitted working directory"
        
        output = get_file_content("calculator", "/bin/cat")
        self.assertIn(required, output, msg=f"Missing token: {required}")
        
    def test_get_files_info_file_doesnt_exist(self):
        required = "Error: File not found or is not a regular file: \"tests/does_not_exist.py\""
        
        output = get_file_content("calculator", "tests/does_not_exist.py")
        self.assertIn(required, output, msg=f"Missing token: {required}")

if __name__ == "__main__":
    unittest.main()