def row(n):#строим строку
    arr = []
    for i in range(0, n):
        arr += [0]
    return arr
def col(m, n):#строим столбец
    mat = []
    for i in range(0, m):
        mat += [row(n)]
    return mat
def printMat(mat):#выводим матрицу-игровое поле
    for line in mat:
        print(line)
mat = col(10, 10)
ignore = []
total = 0
def checkInt(msg):# проверяем входные данные(число ли было введено?)
    for i in range(0, 10):
        msg = msg.replace(str(i), "")
    return len(msg) == 0
def inputXY():#функция для ввода хода игрока
    while True:
        x = input("X: ")
        y = input("Y: ")
        if not checkInt(x):
            print("Неверный X")
            continue
        elif not checkInt(y):
            print("Неверный Y")
            continue
        else:
            x = int(x)
            y = int(y)
            if x < 1 or x > 10:
                print("X вне диапазона")
                continue
            if y < 1 or y > 10:
                print("Y вне диапазона")
                continue
            if mat[x - 1][y - 1]:
                print("Точка занята")
                continue
            else:
                mat[x - 1][y - 1] = 1
            break
    return (x - 1, y - 1)
def inRange(x, y):#проверка допустимости по диапазону значений x и y
    if x < 0:
        return 0
    if y < 0:
        return 0
    if x > 9:
        return 0
    if y > 9:
        return 0
    return 1
def border(x, y):#
    dots = []
    if inRange(x - 1, y - 1):
        dots += [(x - 1, y - 1)]
    if inRange(x - 1, y):
        dots += [(x - 1, y)]
    if inRange(x - 1, y + 1):
        dots += [(x - 1, y + 1)]
    if inRange(x, y + 1):
        dots += [(x, y + 1)]
    if inRange(x, y - 1):
        dots += [(x, y - 1)]
    if inRange(x + 1, y):
        dots += [(x + 1, y)]
    if inRange(x + 1, y + 1):
        dots += [(x + 1, y + 1)]
    if inRange(x + 1, y - 1):
        dots += [(x + 1, y - 1)]
    return dots
def contain(item, arr):
    for elem in arr:
        if elem[0] == item[0] and elem[1] == item[1]:
            return 1
    return 0
def check(x, y):
    global ignore
    global total
    global mat#добавляем списки из других функций
    ignore += [(x, y)]
    if mat[x][y]:
        total += 1
        for dot in border(x, y):
            if contain((dot[0], dot[1]), ignore):
                continue
            else:
                check(dot[0], dot[1])
    else:
        return total
while True:
    print("Поле клондайк:")
    printMat(mat)
    print("Введите координату:")
    (x, y) = inputXY()
    mat[x][y] =1
    total = 0
    ignore = []
    check(x, y)
    if total > 2:
        printMat(mat)
        print("Вы проиграли")
        break
    else:
        continue
