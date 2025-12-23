print('Это модуль функций')

n = 2

def summa(x, y):
    
    n = 3 

    return (x + y) * n

async def send_mail(num):
    print('Улетело сообщение {}'.format(num))
    time.sleep(1)
    print('Сообщение {} доставлено'.format(num))


async def main():
    tasks = [send_mail(i) for i in range(10)]
    #print(tasks)
    #await asyncio.gather(*tasks)
