                            # import os

# permite que você manipule arquivos, diretórios e até processos de forma simples

# MANIPULAÇAO DE DIRETORIOS E ARQUIVOS==>

# os.getcwd():
# -> Retorna o diretório atual de trabalho.
# os.chdir(path):
# -> Altera o diretório de trabalho para o caminho especificado.
# os.listdir(path):
# -> Lista os arquivos e pastas dentro de um diretório.
# os.mkdir(path):
# -> Cria um novo diretório.
# os.makedirs(path):
# -> Cria diretórios recursivamente (inclusive subpastas).
# os.remove(path):
# -> Remove um arquivo.
# os.rmdir(path):
# -> Remove um diretório vazio.
# os.rename(src, dst):
# -> Renomeia arquivos ou diretórios.

# INFORMAÇOES DO SISTEMA
# os.name:
# -> Retorna o nome do sistema operacional ('posix', 'nt', etc.).
# os.uname():
# -> Retorna informações detalhadas sobre o sistema (em Unix).
# os.environ:
# -> Acessa variáveis de ambiente como um dicionário.

# EXECUÇAO DE COMANDOS E PROCESSOS
# os.system(command):
# -> Executa comandos do sistema diretamente.
# os.startfile(path):
# -> Abre um arquivo com o programa padrão (Windows).
# os.popen(command):
# -> Executa comandos e retorna um objeto de leitura/escrita.

# PERMISSOES E METADADOS
# os.stat(path):
# -> Retorna informações sobre o arquivo (tamanho, data de modificação, etc.).
# os.chmod(path, mode):
# -> Altera permissões de arquivos.