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



# Diretório raiz do projeto
project_root = Path()

# Listas de pastas e arquivos a serem ignorados
ignore_dirs = {'.git', '.github', 'scripts'}
ignore_files = {'README.md'}

# Função para iterar sobre as pastas do projeto
def iterate_project_dirs(root):
  project_structure = {}
  for dirpath, dirnames, filenames in os.walk(root):
      # Remover pastas a serem ignoradas da lista de pastas
      dirnames[:] = [d for d in dirnames if d not in ignore_dirs]

      # Iterar sobre os arquivos no diretório atual
      for filename in filenames:
          # Pular arquivos que devem ser ignorados
          if filename in ignore_files:
              continue
          # Caminho completo do arquivo
          file_path = os.path.join(dirpath, filename)
          print(file_path)  # Aqui você pode substituir pela lógica desejada
          project_structure[relative_path] = filenames
  return project_structure

# Chamar a função de iteração
iterate_project_dirs(project_root)