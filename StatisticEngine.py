def main():
    while True:
        print_everything(GetNumber())


def GetNumber():
    print("Введите числа в любом порядке, разделяя через пробел. Когда закончите ввод чисел нажмите ENTER.")
    while True:
        list = input("Введите числа: ").split()
        if str_list_to_number(list):
            return str_list_to_number(list)
        else:
            print("В ряду присутсвуют посторонние символы.")

def Ask():
    print("Теперь выберите что хотите сделать:")
    print("1 - ранжировать")
    print("2 - найти среднее арифметическое")
    print("3 - найти моду(при наличии)")
    print("4 - найти размах чисел")
    print("5 - найти медиану")
    print("6 - выйти в ввод числа")
    success = False
    mode = 0
    while not success:
        mode = str_to_int(input("Введите номер режима: "))
        if mode == 6:
            return False
        elif 1 <= mode <= 5:
            success = True
        else:
            print("Неккоректный режим.")
    return mode

def print_everything(list):
    print(f'Список в ранжированном порядке: {make_another(rank(list))}')
    print(f'Среднее арифметическое: {arithmetic_mean(list)}')
    print(f'Мода: {fashion(list)}')
    print(f'Размах: {scope(list)}')
    print(f'Медиана: {median(list)}')

def massiver(n):
    m = []
    for i in range(len(n)):
        m += n[i]
    return m

def str_list_to_number(listik):
    response = []
    for element in listik:
        if not str_to_int(element):
            return False
    for element in listik:
        response.append(int(element))
    return response

def str_to_int(number):
    if not (number == '0' or number == '1' or number == '2' or number == '3' or number == '4' or number == '5' or number == '6' or number == '7' or number == '8' or number == '9'):
        return False
    else:
        return int(number)

def rank(listik):
    return sorted(listik)

def arithmetic_mean(listik):
    return round(make(sum(listik) / len(listik)), 2)

def fashion(listik):
    a = 0
    m = 0
    for element in listik:
        fte = 0
        for inside in listik:
            if element == inside:
                fte += 1
        if fte > m:
            m = fte
            a = element
    if m == 1: return 'отсутствует'
    else: return a

def scope(listik):
    listik = rank(listik)
    return listik[len(listik)-1] - listik[0]

def median(listik):
    listik = rank(listik)
    if len(listik) % 2 == 0:
        return round(make((listik[(len(listik)) // 2] + (len(listik)+1) // 2)/2), 2)
    else:
        return round(make(listik[(len(listik)-1) // 2]), 2)

def make_another(s):
    a = ''
    for el in s:
        a += (str(el)+' ')
    return a

def make(n):
    if n - int(n) == 0: return int(n)
    else: return n

main()