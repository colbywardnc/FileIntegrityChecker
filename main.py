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

    filename = input("Enter the file path: ")

    if not os.path.isfile(filename):
        print("File not found")
        return

    file_hash = calculate_hash(filename)

    print()
    print("File: ", filename)
    print("SHA-256 Hash:")
    print(file_hash)
    print()
    print("Keep this hash to compare against the file later.")

if __name__ == "__main__":
    main()