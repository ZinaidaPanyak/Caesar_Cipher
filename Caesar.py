import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("MyLogFile.log")
file_handler.setLevel(logging.DEBUG)
logger_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(logger_formatter)
logger.addHandler(file_handler)

logger.info("__________Новое__________")
try:
    a = int(input('Введите значение сдвига (целое число) '))
except ValueError:  # Если появляется ошибка, даем возможность повторного ввода
    try:
        a = int(input('Неверные данные. Введите целое число '))
    except ValueError:
        print('Были введены некорректные данные. Шифровка производится со сдвигом 1')
        logger.warning("Введены некорректные данные")
        a = 1
logger.info("Значение сдвига %s " % (a))
text = input('Введите текст ')
letters = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
           'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
b_letters = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У',
             'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
logger.info("Введен текст: %s " % (text))


def Cipher(text, move=a):
    logger.info("_______Шифрование_______")
    stroka = ' '  # Создаем пустую строку, которая будет заполняться
    for b in text:
        if b in letters:
            num = letters.index(b)  # Определяем номер буквы
            logger.info("Номер буквы %s = %s " % (b, num))
            d = move - (move // 33) * 33
            k = num + d
            logger.info("Новый порядковый номер = %s " % (k))
            if k > 32:  # Учитываем, что при номере новой буквы, превышающем 32, нужно перейти к началу алфавита
                kn = k - 33
                stroka += letters[kn]  # Добавляем новую букву с учетом сдвига
                logger.info("Заменяем на %s " % (letters[kn]))
            elif k <= 32:
                stroka += letters[k]
                logger.info("Заменяем на %s " % (letters[k]))
        elif b in b_letters:  # Всё то же самое, но для заглавных букв
            num = b_letters.index(b)
            logger.info("Номер буквы %s = %s " % (b, num))
            d = move - (move // 33) * 33
            k = num + d
            logger.info("Новый порядковый номер = %s " % (k))
            if k > 32:
                kn = k - 33
                stroka += b_letters[kn]
                logger.info("Заменяем на %s " % (letters[kn]))
            elif k <= 32:
                stroka += b_letters[k]
                logger.info("Заменяем на %s " % (letters[k]))
        else:  # Если введена не буква, то ничего не меняется
            stroka += b
    return stroka


def DeCipher(text, move=a):
    logger.info("______Дешифрование______")
    stroka = ' '  # Создаем пустую строку, которая будет заполняться
    for b in text:
        if b in letters:
            num = letters.index(b)  # Определяем номер буквы
            d = move - (move // 33) * 33
            k = num - d
            logger.info("Новый порядковый номер = %s " % (k))
            stroka += letters[k]
            logger.info("Заменяем на %s " % (letters[k]))
        elif b in b_letters:  # Все то же самое для заглавных букв
            num = b_letters.index(b)
            d = move - (move // 33) * 33
            k = num - d
            logger.info("Новый порядковый номер = %s " % (k))
            stroka += b_letters[k]
            logger.info("Заменяем на %s " % (letters[k]))
        else:
            stroka += b  # Если введена не буква, то ничего не меняется
    return stroka


print('Шифровка: ', Cipher(text))
print('Расшифровка: ', DeCipher(text))

