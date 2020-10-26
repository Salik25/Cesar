import logging

logging.basicConfig(format = u'%(levelname)-8s [%(asctime)s] %(message)s', level = logging.DEBUG, filename = u'mylog.log')
# Сообщение отладочное
# logging.debug( u'This is a debug message' )
# # Сообщение информационное
# logging.info( u'This is an info message' )
# # Сообщение предупреждение
# logging.warning( u'This is a warning' )
# # Сообщение ошибки
# logging.error( u'This is an error message' )
# # Сообщение критическое
# logging.critical( u'FATAL!!!' )

def in_ASCII(string): #функия представления символов в числовой код таблицы ASCII
    a = []
    for i in string:
        a.append(ord(i))
    logging.info(u'Создан массив и заполнен числами символов строки')
    return a


def encryption(list, step): #функция дообавление шага к нужным символам
    new_list = []
    for i in list:
        if i in AZ:
            i += step
            if i > 90: #проверка
                i = (i % 90) + 65
            logging.debug(u'Прошла проверка на латинский заглавный алфавит')
        elif i in az:
            i += step
            if i > 122: #проверка
                i = (i % 122) + 97
            logging.debug(u'Прошла проверка на латинский строчной алфавит')
        elif i in AZ_Rus:
            i += step
            if i > 1071: #проверка
                i = (i % 1071) + 1040
            logging.debug(u'Прошла проверка на русский заглавный алфавит')
        elif i in az_Rus:
            i += step
            if i > 1103: #проверка
                i = (i % 1103) + 1072
            logging.debug(u'Прошла проверка на русский строчной алфавит')
        new_list.append(i)
    logging.info(u'Создан и заполнен массив числами символа+шаг')
    return new_list


def decryption(new_list): #функция перевода числовых значений таблицы ASCII в символы
    a = str()
    for i in new_list:
        a += chr(i)
    logging.info(u'Создана и заполнена строка с закодированным текстом')
    return a


AZ = set(i for i in range(65, 91))
az = set(i for i in range(97, 123))
AZ_Rus = set(i for i in range(1040, 1072))
az_Rus = set(i for i in range(1072, 1104))

decr = open('source.txt', 'r')
encr = open('encryption.txt', 'w')
step = 'g'
while type(step) != int():
    try: # проверка ошибок на ввод шага
        step = int(input()) # вводим шаг кодировки
        for line in decr:
            encr.write(decryption(encryption(in_ASCII(line), step))) # вывод в файл закодированного текста
        decr.close()
        encr.close()
        print("Перевод выполнен")
        logging.info(u'Программа выполнена успешно')
        break
    except ValueError:
        print('Это не число.')
        logging.error(u'Введенный шаг не является числом')