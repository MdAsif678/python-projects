# Master Password: Password123


import json
import hashlib

class PasswordManager:
    def __init__(self):
        self.entries = {}
        self.master_hash = hashlib.sha256("Password123".encode()).hexdigest()

    def check_master_password(self,attempt):
        attempt_hash = hashlib.sha256(attempt.encode()).hexdigest()
        if(attempt_hash == self.master_hash):
            return True
        else:
            return False


    def _encrypt(self,text):
        
        encrypted = ""
        for chars in text:
            if chars == " ":
                encrypted += chars
            elif chars.islower():
                encrypted += chr((ord(chars)-97+3)%26+97)
            elif chars.isupper():
                encrypted += chr((ord(chars)-65+3)%26+65)
            else:
                encrypted += chars
        
        return encrypted

    def _decrypt(self,text):
        
        decrypted = ""
        for chars in text:
            if chars == " ":
                decrypted += chars
            elif chars.islower():
                decrypted += chr((ord(chars)-97-3)%26+97)
            elif chars.isupper():
                decrypted += chr((ord(chars)-65-3)%26+65)
            else:
                decrypted += chars
        
        return decrypted    

    def add_entry(self,site,username,password):
        password = self._encrypt(password)
        self.entries[site] = {"Username": username,"Password":password}
        return True

    def view_entry(self,site):
        if site not in self.entries:
            print("No site username and passwords stored\n")
            return
        
        entry = self.entries[site]

        password = self._decrypt(entry["Password"])

        print(f"\nSite: {site}")
        print(f"Username: {entry['Username']}")
        print(f"Password: {password}\n")

    def delete_entry(self,site):
        if site not in self.entries:
            print("No data available for this site\n")
            return
        
        popped = self.entries.pop(site)
        return popped
    
    def view_site(self):
        if len(self.entries) == 0:
            print("No saved data available\n")
            return
        
        lst = []
        for sites in self.entries:
            lst.append(sites)
        print(f"Available sites: "+",".join(lst))
        return True

    def save_to_file(self,filename):
        if len(self.entries) == 0:
            print("No data available to save\n")
            return
        
        if filename:
            with open(filename,"w") as f:
                json.dump(self.entries, f, indent=4)
        

    def load_from_file(self,filename):
        try:
            with open(filename,"r") as f:
                self.entries = json.load(f)
        except FileNotFoundError:
            print("No such file exist\n")        

pm = PasswordManager()

# pm.add_entry("Gmail","MdAsif678","Thisismypassword")
# pm.add_entry("Github","MdAsif6667","ThisagainisMyPassword")


# pm.delete_entry("Gmail")
# pm.add_entry("Gmail","MdAsif678","ThisisGonnaBemyNextPassword")

# print(pm.entries)
# pm.view_site()

# pm.save_to_file("passwords.json")
# print(pm.entries)
# pm.view_entry("Gmail")
# pm.view_entry("Github")


pas = input("Enter the master password: ")
if pm.check_master_password(pas) == True:
    print("Welcome to PAssword Manager")
    while True:
        
        print("What would you like to do")
        print("1. Add Entry \n2. Delete Entry \n3. View Entry \n4. View the sites \n5. save to a File \n6. Load from a file \n7. Exit")
        try:
            choice = int(input("Enter a choice: "))
        
            if choice == 1:
                site = input("Enter the name of the site/app: ")
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                status = pm.add_entry(site,username,password) 
                if status:
                    print("Entry added successfully")
            
            elif choice == 2:
                site = input("Enter the name of the site: ")
                status = pm.delete_entry(site)
                if status:
                    print("Entry deleted successfully")
            
            elif choice == 3:
                site = input("Enter the name of the site: ")
                pm.view_entry(site)
            
            elif choice == 4:
                pm.view_site()
            
            elif choice == 5:
                filename = input("Enter the name of the file you want to save in: ")
                pm.save_to_file(filename)
            
            elif choice == 6:
                filename = input("Enter the name of the file you want to load from(with extension): ")
                pm.load_from_file(filename)
            
            elif choice == 7:
                break

            else:
                print("Not a valid Choice!")

        except ValueError:
            print("Thats Not a valid CHOICE")
            continue
else:
    print("Incorrect password! ACESS DENIED")
