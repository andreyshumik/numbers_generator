def schitalka():
    sum = 0
    while True:
        try:
            number = input('Введите число: ')
            if number != "":
                sum += float(number)
            else:
                exit()
            
            if sum%1 == 0:
                print(int(sum))
            else:
                print(sum)
            5
        except (ValueError):
            print('Ввод только чисел!!!')

if __name__ == "__main__":    
    schitalka()