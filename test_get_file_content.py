from functions.get_file_content import get_file_content
from config import MAX_CHARS

def main():
    # 1) "lorem.txt"
    output = get_file_content("calculator", "lorem.txt")
    print("Result for lorem.txt:")
    print(len(output))
    print(output[MAX_CHARS:])
    
    # 2) "calculator/main.py"
    output = get_file_content("calculator", "main.py")
    
    print("\n")
    print("Result for calculator/main.py:")
    print(output)
    
    # 3) "calculator/pkg/calculator.py:"
    output = get_file_content("calculator", "pkg/calculator.py")
    print("\n")
    print("Result for calculator/pkg/calculator.py:")
    print(output)

    # 4) "bin/cat":
    output =  get_file_content("calculator", "/bin/cat")
    print("\n")
    print("Result for bin/cat:")
    print(output)
    
    # 5) "pkg/does_not_exist.py":
    output =  get_file_content("calculator", "pkg/does_not_exist.py")
    print("\n")
    print("Result for pkg/does_not_exist:")
    print(output)

if __name__ == "__main__":
    main()