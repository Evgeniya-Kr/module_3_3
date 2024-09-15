print('Задача 1: Функция с параметрами по умолчанию:')
def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)


print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])


print('___________________________')
print('Задача 2: Распаковка параметров:')

def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)


values_list = [7, 'True', False ]
values_dict = {'a': 10, 'b': 'строка', 'c': 35.79}
print_params(*values_list,)
print_params(**values_dict)


print('___________________________')
print('Задача 3: Распаковка + отдельные параметры:')
def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)


values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)