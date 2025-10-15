import pymysql

class MySqlConn:
    def_init_(self, 
       user = 'root', 
       password = '4linux',
       host = 'localhost',     
       database = 'teste'    
):
    
    self.conn = None
    self.user = user
    self.password = password
    self.host = host
    self.database = database


def criarConexao(self):
    try:
        self.conn = pymysql.connect(
            user = self.user, 
            password = self.password, 
            host = self.host,
            database = self.database)
        
    except Exception as err:
        print(f'Nao foi possivel conectar com o Banco de dados - {err}')

if __name__ == '__main__':
    mysql = MySqlConn()