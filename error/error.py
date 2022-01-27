def split_bill(price):
    num = input("何人で割り勘しますか？")
    try:
        each = price / int(num)
    except ZeroDivisionError as e:
        print("0で割ることはできません。正しい値を入力してください")
        each = price
        print(e)
    except Exception as e1:
        print('koko---------------------------------')
        print("error!!" + str(e1))
        each = price

    print(f"1人{each}円です")


if __name__ == '__main__':
    split_bill(10000)
