dic = {}

try:
    print(dic['error'])

except Exception as err:
    print('Mensagem: ', err)


class OptionInvalidError(Exception):
    def __init__(self, option):
        self.option = option

    def __str__(self): # -> retorna uma string que descreve o objeto
        if self.option is not None:
            return f'InvalidOptionError: Option {self.option} does not exist'
        return f'InvalidOptionError: Option is absent'

# 6.16 min