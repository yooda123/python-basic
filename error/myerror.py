# 例外（Exception）を自作

# ・Exceptionクラスを継承する（BaseExceptionは継承を意図して作られていないので注意）
# ・〇〇Errorという名前にするとわかりやすい（もしその例外がエラーなら）
# ・自作例外はなるべく別ファイルにまとめておく（exceptions.py, errors.py)

class MyError(Exception):
    def __str__(self):
        return "my error occurred."


if __name__ == '__main__':
    response = input("y/n: ")

    # try:

    if response != 'y' and response != 'n':
        raise MyError

    # except MyError as e:
    #     print(e)  # e.__str__()
