# mode='a' (append): ファイルの最後尾に内容を追加7
# -----
# with open("fileio/writing_file.txt", mode='a') as f:
#     f.write("mode=a appends text.")


# mode='r+': 読み書きどちらも可能。ポインタ位置に注意
# -----
# with open("fileio/writing_file.txt", mode='r+') as f:
#     f.write("All you can write and read with r+ mode!!.")  # 先頭
#     print(f.read())  # 上記最後のポインタから開始なので何も出力しない
#     f.write("This is a pen.")  # 先頭
#     print(f.read())  # 上記最後のポインタから開始なので何も出力しない


# mode = 'w+': 読み書きどちらも可能 Truncateされることに注意
with open("fileio/writing_file.txt", mode='w+') as f:
    # 'w' -> trancatedされる（上書きされる）
    print(f.read())  # 上記最後のポインタから開始
    f.write("You can write and read with w+ mode!!")
    f.seek(0)
    print(f.read())
