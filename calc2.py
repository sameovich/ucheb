print("Программа калькулятор, что ее выключить введите 0")
while True:
    s = input("Знак (+,-,*,/,**):")
    if s == '0': break
    if s in('+','-','*','/','**'):
        x = float(input("x = "))
        y = float(input("y = "))
        if s == '+':
            print("\tРезультат = ",x+y)
        elif s == '-':
            print("\tРезультат = ",x-y)
        elif s == '*':
            print("\tРезультат = ",x*y)
        elif s == '**':
            print("\tРезультат = ",x**y)
        elif s == '/':
            if y != 0:
                print("\tРезультат = ",x/y)
            else:
                print("\tНеверно")
    else:
        print("\tНеверный введен знак")