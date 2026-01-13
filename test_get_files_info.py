from functions.get_files_info import get_files_info

def main():
    # 1) "."
    output = get_files_info("calculator", ".")
    print("Result for current directory:")
    for line in output.splitlines():
        print(f"  {line}")

    # 2) "pkg"
    output = get_files_info("calculator", "pkg")
    print("Result for 'pkg' directory:")
    for line in output.splitlines():
        print(f"  {line}")

    # 3) "/bin"
    output = get_files_info("calculator", "/bin")
    print("Result for '/bin' directory:")
    for line in output.splitlines():
        print(f"  {line}")

    # 4) "../"
    output = get_files_info("calculator", "../")
    print("Result for '../' directory:")
    for line in output.splitlines():
        print(f"  {line}")

if __name__ == "__main__":
    main()