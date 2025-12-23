
import asyncio
import time
import sys
from funct import n, main, send_mail, summa
from classes import MyClass
import data

print(sys.builtin_module_names)
print('Это исполняемый модуль')

if __name__ == '__main__':
    print('Код ниже не выполнится, если этот файл будет импортируемым модулем в другой исполняемый файл')

    print(dir())

    start_time = time.time()
    asyncio.run(main())

    print(f'Время выполнения программы: {time.time() - start_time} с')

    print(summa(2, 5))

    a = MyClass()

    print(data.lst)