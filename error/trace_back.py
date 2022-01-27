import traceback


def split_bill(price):
    num = input("割り勘する人数を入力してください: ")
    try:
        each = price / int(num)
    except ZeroDivisionError:
        print("0以外の数字を入力してください")
    else:
        print(f"1人{each}円です")


def check(bill):
    total_bill = sum(bill.values())
    split_bill(total_bill)


if __name__ == '__main__':
    bill = {'burger': 500, 'pasta': 1400, 'fries': 300, 'egg': 200}

    try:
        check(bill)
    except ValueError:
        traceback.print_exc()
        print("エラーが出ました。やり直してください")
        print("プログラムは問題なく実行されました")
