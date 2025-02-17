#напишите игру крестики-нолики на поле 3х3 с использованием функций и циклов 
#программа должна выводить поле в виде:
#   0 1 2
# 0 - - -
# 1 - - -
# 2 - - -
#программа должна спрашивать у пользователя ход, записывать его на поле и отрисовывать его
#программа должна проверять выигрышные комбинации и завершать игру
#программа должна проверять ничью и завершать игру

def print_field(field):
    print('  0 1 2')
    for i in range(3):
        print(i, end=' ')
        for j in range(3):
            print(field[i][j], end=' ') #выводим поле на экран в виде таблицы 3х3 с координатами строк и столбцов
        print()

def check_win(field):
    for i in range(3):
        if field[i][0] == field[i][1] == field[i][2] and field[i][0] != '-': #проверяем выигрышные комбинации по горизонтали и вертикали
            return field[i][0] #возвращаем символ выигравшего игрока
        if field[0][i] == field[1][i] == field[2][i] and field[0][i] != '-': #проверяем выигрышные комбинации по диагонали
            return field[0][i] #возвращаем символ выигравшего игрока
    if field[0][0] == field[1][1] == field[2][2] and field[0][0] != '-': #проверяем выигрышные комбинации по диагонали
        return field[0][0] #возвращаем символ выигравшего игрока
    if field[0][2] == field[1][1] == field[2][0] and field[0][2] != '-': #проверяем выигрышные комбинации по диагонали
        return field[0][2]
    return None

def check_draw(field):
    for i in range(3):
        for j in range(3):
            if field[i][j] == '-': #проверяем есть ли на поле пустые клетки
                return False
    return True

def main():
    field = [['-' for _ in range(3)] for _ in range(3)] #создаем поле 3х3
    player = 'X' #первый ходит игрок X
    while True:
        print_field(field)
        x, y = map(int, input(f'Введите координаты {player} (x y): ').split()) #просим ввести координаты для хода
        if field[x][y] == '-': #проверяем пустая ли клетка
            field[x][y] = player #записываем ход на поле
            win = check_win(field) #проверяем выигрыш
            if win is not None:
                print_field(field)
                print(f'Выиграл {win}!')
                break
            if check_draw(field): #проверяем ничью
                print_field(field)
                print('Ничья!')
                break
            player = 'O' if player == 'X' else 'X' #меняем игрока
        else:
            print('Ячейка не пуста!')

if __name__ == '__main__':
    main()
