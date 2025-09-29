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

# raise -> ele chama a o erro, sendo um aforma de ativar certo erro ex:

# raise KeyError('102920')
# ^ ->  file "<stdin>", line 1, in <module>
# KeyError: '102920'

def raise_for_invalid_option(dic, option=None):
    if option not in dic.keys():
        raise OptionInvalidError(option)

dic = {'1': '1', '2': '2'}

try:
    op = input('')
    raise_for_invalid_option(dic, op)
except OptionInvalidError as err:
    print(err)

else:
    print(dic[op])