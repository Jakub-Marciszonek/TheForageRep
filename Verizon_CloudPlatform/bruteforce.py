'''
Forage AIG Cybersecurity Program
Bruteforce starter template
'''

from zipfile import ZipFile

# Use a method to attempt to extract the zip file with a given password
# def attempt_extract(zf_handle, password):
#     
#
#
def main():
    counter = 0
    print("[+] Beginning bruteforce ")
    with ZipFile("Verizon_CloudPlatform\enc.zip") as zf:
        with open("Verizon_CloudPlatform\rockyou.txt", "rb") as f:
            for i in f:
                password = i.strip()
                try:
                    zf.extractall(pwd=password)
                    print(f"Password number: {counter}\n\
Password: {password}")
                    return
                except RuntimeError:
                    counter += 1
                    #Incorrect password will raise it
                except Exception as e:
                    print(f"Error: {e}")
        print("Password not found in the list")
            # Write your logic here...
            # Iterate through password entries in rockyou.txt

            # Attempt to extract the zip file using each password

            # Handle correct password extract versus incorrect password attempt)
if __name__ == "__main__":
    main()