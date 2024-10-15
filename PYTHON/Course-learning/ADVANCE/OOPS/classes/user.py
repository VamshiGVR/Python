#file name should be in lower case
#class name should PASCAL
class User:
    
    #CONSTRUCTOR: is executed, when ever we create the object sfrom this class
    #Here the word self refers to current instance of class, is used to access variables belong to class
    def __init__(self, email, name, password, job_Title):
        self.email = email
        self.name = name
        self.password = password
        self.job_Title = job_Title

    
    def change_password(self, new_password):
        self.password = new_password
    

    def get_user(self):
        print(f"User {self.name} is working as {self.job_Title}, and email is {self.email} & pswd: {self.password}")


