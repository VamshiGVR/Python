import os

#Defining a function
def check_python(command):
    print(os.system(command))
def check_ver(command):
    print(os.system(command))

#Calling the function
check_python("python --version")
check_ver("ver")

#defining a function for multiple usages
def run_command(command):
    print (os.system(command))

run_command("python --version")
run_command("ver")