# import sys
import os

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

ignore_dirs = {'.git', '.github', 'scripts', '.idea'}
ignore_files = {'README.md', '.gitignore'}

dir = "./"
project_folder = os.listdir(dir)


# for item in project_folder:
#     if os.path.isdir(item):
#         folders = os.listdir(item)
#         for file in folders:
#             dict_files[item]=file

# print("dict:", dict_files)

def iterate_project_dirs(root):
    dict_files = {}
    for item in os.listdir(root):  # Listar o conteúdo do diretório raiz
        item_path = os.path.join(root, item)  # Obter o caminho completo do item
        if os.path.isdir(item_path):  # Verificar se o item é um diretório
            dict_files[item] = os.listdir(item_path)  # Armazenar a lista de arquivos/pastas do diretório
    print("interno: ", dict_files)
    return dict_files


iterate = iterate_project_dirs(project_folder)


