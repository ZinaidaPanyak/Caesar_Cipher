try:
    a = int(input('Введите значения сдвига (целое число) '))
except ValueError:
        try:
            a = int(input('Не верные данные. Введите целое число '))
        except ValueError:
            print('Были введены некорректные данные. Шифровка производится со сдвигом 1')
            a = 1

text = input('Введите текст ')
letters = ['а', 'б', 'в', 'г', 'д', 'е', 'ё' ,'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х',
           'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
b_letters = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У',
             'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']

def Cipher(text, move=a):
    stroka = ' '
    for b in text:
        if b in letters:
            num = letters.index(b)
            k = num + move
            if k > 32:
              z = k - 33
              stroka += letters[z]
            elif k <= 32:
              stroka += letters[k]
        elif b in b_letters:
            num = b_letters.index(b)
            k = num + move
            if k > 32:
                z = k - 33
                stroka += b_letters[z]      
        else:
            stroka += b
    return stroka


print('Шифровка: ', Cipher(text))


def DeCipher(text, move=a):
    stroka = ' '
    for b in text:
        if b in letters:
            num = letters.index(b)
            stroka += letters[num - move]
        elif b in b_letters:  
            num = b_letters.index(b)
            stroka += b_letters[num - move]    
        else:
            stroka += b
    return stroka

print('Расшифровка: ', DeCipher(text))

