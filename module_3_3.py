def print_params(a=1, b='Строка', c=True):
    print(a, b, c)
print_params(b = 25)
print_params(c = [1,2,3])
values_list = [3, "string", 2.2]
values_dict = {'a': 6, 'b': 'nice', 'c': False}
print_params(**values_dict)
print_params(*values_list)
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
