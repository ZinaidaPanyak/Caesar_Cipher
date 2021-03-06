## Назначение программы
 Данная программа предназначена для быстрого шифрования и дешифрования текста с помощью шифра Цезаря. Этот метод шифрования заключается в замене одного символа другим, находящимся на некотором расстоянии левее или правее него в алфавите, причем это значение этого расстояния остаётся постоянным.
## Запуск программы
  1. Для того, чтобы запустить программу, необходимо наличие какого-либо браузера. 
  2. Нужно установить на компьютер любой редактор кода для языка Python (подойдут Visual Studio Code, Jupyter Notebook, PyCharm и другие)
  3. Пройти по ссылке https://github.com/ZinaidaPanyak/Caesar_Cipher и открыть файл Caesar.py (должно появиться окно с кодом)
  4. Скопировать код и вставить в окно среды разработки, выбранной во втором пункте 
  5. Нажать на значок в виде зеленого треугольника в правом верхнем углу (кнопка «run»)
  6. После этого внизу должно появиться диалоговое окно с сообщением: «Введите значение сдвига (целое число)». Программа готова к работе.
 
 *Примечание:* в случае, если такого сообщения не появилось, попробуйте нажать на значок с названием программы в левом верхнем углу экрана (Caesar.py) и в открывшемся списке нажать «Run ‘Caesar’» или зажать клавиши Ctrl +Shift +F10.
## Выполнение основных функций
 Программа:
-	принимает от пользователя целое число, обозначающее значение сдвига
-	принимает на ввод текст (строка из букв русского алфавита, пробелов, символов)
-	преобразует введенный текст: каждую букву заменяет на другую, с порядковым номером, который считается так: к порядковому номеру исходной буквы прибавляется и вычитается значение сдвига и заменяет на соответствующие новые значения. Таким образом, на выходе имеется две строки: одна с шифрованием, другая с дешифрованием.
## Завершение программы
Программа завершается сразу после вывода на экран результата своей работы. Для повторного использования её следует вновь запустить.
