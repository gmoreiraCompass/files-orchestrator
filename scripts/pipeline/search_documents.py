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


# for item in project_folder:
#     if os.path.isdir(item):
#         folders = os.listdir(item)
#         for file in folders:
#             dict_files[item]=file

# print("dict:", dict_files)

def iterate_project_dirs(root):
    if isinstance(root, list):
        # Se root é uma lista, iterar sobre cada caminho na lista
        dict_files = {}
        for directory in root:
            if os.path.isdir(directory):
                dict_files.update(iterate_project_dirs(directory))
        return dict_files

    # Se root é um único diretório
    dict_files = {}
    for item in os.listdir(root):  # Listar o conteúdo do diretório raiz
        item_path = os.path.join(root, item)  # Obter o caminho completo do item
        if os.path.isdir(item_path):  # Verificar se o item é um diretório
            dict_files[item_path] = os.listdir(item_path)  # Armazenar a lista de arquivos/pastas do diretório
    print("intern: ", dict_files)
    return dict_files


root = "./"
result = iterate_project_dirs(root)
print(result)
