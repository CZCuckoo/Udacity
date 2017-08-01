import os

def rename_files():
    file_list = os.listdir(r"C:\Users\Clint\Desktop\Programming projects\Udacity\prank")
    #print(file_list)
    saved_path = os.getcwd()
    print("Current working directory is "+saved_path)
    os.chdir(r"C:\Users\Clint\Desktop\Programming projects\Udacity\prank")
    for file_name in file_list:
        print("Old name - "+file_name)
        print("New name - "+file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))

rename_files()
