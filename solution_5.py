try:
    s = 0
    with open('input_5.txt', 'r', encoding='utf-8') as f:
                s = f.readlines()
                print(s)
                p = (int(s[0]) / int(s[1])) + int(s[2])
                with open('output_5.txt', 'w') as r:
                    print(p)
                    r.write(str(p))
except ValueError:
        print('ошибка в значении')
except ZeroDivisionError:
        print('Ошибка деления на ноль')
