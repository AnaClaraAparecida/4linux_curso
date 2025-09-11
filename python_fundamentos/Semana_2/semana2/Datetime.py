import time

antes = time.process_time()
depois = time.process_time()
dif = depois - antes
print(dif)

import datetime

# datetime.datetime.now() -> retorna o ano, dia, mes, hora, minuto e milesimo

t1 = datetime.datetime.now()
time.sleep(10)
t2 = datetime.datetime.now()
