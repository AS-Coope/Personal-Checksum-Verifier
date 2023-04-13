import hashlib
import os

# Ryan Cooper
# v0.1 - First Implementation (CLI)

# This function receives the File Path and the Provided Checksum (for example on the website)
def checksumVerifier(filePath, provCheck):
    filePathNew = open(filePath, 'r')
    hasher = hashlib.new('sha256')
    hasher.update(filePathNew.encode())
    hdigest = hasher.hexdigest()

    if (hdigest == provCheck):
        print("Success, the checksums match")
    else:
        print("Unfortunately, the checksums did not match")
    
    pass

# Entry point of the program
def main():

    # User Interface (CLI version for the user)
    print("Welcome to your Personal Checksum Verifier")
    print("Type and enter the number beside the option you would like to do: ")
    print("1. Verify Checksum [SHA256]")
    choice = int(input("Choice: "))

    if (choice == 1):
        fp = input("Enter the path of the file: ")
        provCheck = input("Enter the checksum provided at the place where the file was downloaded")

        checksumVerifier(fp, provCheck)
    else:
        print("Invalid input")
    

