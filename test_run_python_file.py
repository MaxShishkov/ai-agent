from functions.run_python_file import run_python_file

def main():
    # 1) "calculator/main.py"
    output = run_python_file("calculator", "main.py")
    print("\n")
    print("Result for calculator/main.py:")
    print(output)
    
    # 2) "calculator/main.py + expression"
    output = run_python_file("calculator", "main.py", ["3 + 5"])
    print("\n")
    print("Result for calculator/main.py + expression:")
    print(output)

    # 3) "calculator/tests.py"
    output = run_python_file("calculator", "tests.py")
    print("\n")
    print("Result for calculator/tests.py")
    print(output)
    
    # 4) "../main.py"
    output = run_python_file("calculator", "../main.py")
    print("\n")
    print("Result for ../main.py")
    print(output)
    
    # 5) "nonexistent.py"
    output = run_python_file("calculator", "nonexistent.py")
    print("\n")
    print("Result for nonexistent.py")
    print(output)
    
    # 6) "lorem.txt"
    output = run_python_file("calculator", "lorem.txt")
    print("\n")
    print("Result for lorem.txt")
    print(output)
    
if __name__ == "__main__":
    main()