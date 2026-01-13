from functions.write_file import write_file

def main():
    # 1) "lorem.txt"
    output = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print("Result for lorem.txt:")
    print(output)

    
    # 2) "pkg/morelorem.txt"
    output = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    
    print("\n")
    print("Result for calculator/pkg/morelorem.txt:")
    print(output)
    
    # 3) "/tmp/temp.txt":"
    output = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print("\n")
    print("Result for /tmp/temp.txt:")
    print(output)


if __name__ == "__main__":
    main()