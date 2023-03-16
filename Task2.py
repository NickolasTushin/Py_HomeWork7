"""
Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. 
Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.
*Пример:*

**Ввод:** `print_operation_table(lambda x, y: x * y) ` 
**Вывод:**
1 2 3 4 5 6

2 4 6 8 10 12 
3 6 9 12 15 18 
4 8 12 16 20 24
5 10 15 20 25 30
6 12 18 24 30 36
"""

oper = lambda x, y: [x, y]
def print_operation_table(oper, num_rows=6, num_columns=6):
    list_row = []
    list_col = []
    print_row = ""
    res = None
    for i in range(num_rows):
        for k in range(num_columns):
            res = (i + 1) * (k + 1)
            list_row.append(res)
        list_col.append(list_row)
        list_row = []
    print(f"Элемент найден = {list_col[oper[0] - 1][oper[1] - 1]}")
    return
list_row = []
list_col = []
print_row = ""
num_rows = int(input("Введите количество строк: "))
num_columns = int(input("Введите количество столбцов: "))
print("Таблица: ")
for i in range(num_rows):
    for k in range(num_columns):
        res = (i + 1) * (k + 1)
        print_row = print_row + " " + str(res)
    print(print_row)
    print_row = ""
row = int(input("Введите номер строки: "))
col = int(input("Введите номер столбца: "))

print_operation_table(oper(row, col))
