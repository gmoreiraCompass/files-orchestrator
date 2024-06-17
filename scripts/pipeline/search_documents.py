# import sys
import os
from pathlib import Path

# from aws_config import Config

# # bucket_name=sys.argv[1]
# # aws_key=sys.argv[2]
# # aws_access_key=sys.argv[3]
# # aws_access_secret=sys.argv[4]
# # local_path=sys.argv[5]

# # Config(aws_access_key,aws_access_secret)
# # clientS3 = Config.clientS3()

# project = Path()

# portals = project / 'portais'
# home = portals / 'home'

# print(project)
# print(portals)
# print(home)

# for file in portals.iterdir():
#   if file.is_file():
#     print("Is file", file)


project_root = Path()

ignore_dirs = {'.git', '.github', 'scripts'}
ignore_files = {'README.md'}

dir = "./"
files = os.listdir(dir)
dict_files = {}

for item in files:
    if os.path.isdir(item):
        print('is folder')
        dict_files[item]='folder'

    
print("dict:", dict_files)
 
print(files)
# def iterate_project_dirs(root):
#     for dirpath, dirnames, filenames in os.walk(root):
#     project_structure = {}
#         dirnames[:] = [d for d in dirnames if d not in ignore_dirs]

#         for filename in filenames:
#             if filename in ignore_files:
#                 continue
#             file_path = os.path.join(dirpath, filename)
#             print(file_path)
#             project_structure[file_path] = filenames
#     print(project_structure)
#     return project_structure

# iterate_project_dirs(project_root)
