import hashlib
import os

def calculate_hash(filename):
    sha256 = hashlib.sha256()

    with open(filename, 'rb') as file:
        while chunk := file.read(4096):
            sha256.update(chunk)

    return sha256.hexdigest()

def main():
    print("=== File Integrity Checker ===")
    print()
    print("1. Create file baseline")
    print("2. Check file integrity")
    print()

    choice = input("Choose an option: ")

    filename = input("Enter the file path: ")

    if not os.path.isfile(filename):
        print("File not found")
        return

    file_hash = calculate_hash(filename)

    if choice == "1":
        with open("baseline.txt", "w") as file:
            file.write(file_hash)

        print()
        print("Baseline hash saved.")
        print(file_hash)

    elif choice == "2":
        if not os.path.isfile("baseline.txt"):
            print("No baseline found. Create one first.")
            return

        with open("baseline.txt", "r") as file:
            original_hash = file.read().strip()

        print()
        print("Original Hash:")
        print(original_hash)
        print()
        print("Current Hash:")
        print(file_hash)
        print()

        if file_hash == original_hash:
            print("File integrity check passed.")
            print("The file has not been modified.")
        else:
            print("WARNING: File integrity check failed.")
            print("The file may have been modified.")

    else:
        print("Invalid option.")

if __name__ == "__main__":
    main()