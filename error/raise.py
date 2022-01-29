# どちらでもOK。上のほうでも裏でインスタンス化する
# raise ValueError
# raise ValueError()


try:
    # TODO あとで削除
    raise ValueError()
except ValueError:
    print("Do something")
    raise
