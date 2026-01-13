import unittest
from functions.write_file import write_file


class TestWriteFile(unittest.TestCase):
        
    def test_write_file_content_lorem(self):
        required = "Successfully wrote to \"lorem.txt\""
        
        output = write_file("tests", "lorem.txt", "wait, this isn't lorem ipsum")
        
        self.assertIn(required, output, msg=f"Missing token: {required}")
        
    def test_write_file_outside_permitted(self):
        required = "Error: Cannot write to \"/tmp/temp.txt\" as it is outside the permitted working directory"
        
        output = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
        self.assertIn(required, output, msg=f"Missing token: {required}")
        

if __name__ == "__main__":
    unittest.main()