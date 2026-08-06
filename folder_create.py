import os 

folder_name ="mydownloads"

os.mkdir(folder_name)

folder_path =os.path.abspath(folder_name)

print("folder create successfully")
print("folder path  : ",folder_path)

