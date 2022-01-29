# # for文でループ回す
# with open("fileio/pep8_introduction.txt") as f:
#     for line in f:
#         print(line, end="")

# # .read()でファイルの内容すべてを1つのStringとして返す（メモリ消費大！！！）
# with open("fileio/pep8_introduction.txt") as f:
#     print(f.read())

# .readline()で一行ずつ取得しtれStringで返す
# with open("fileio/pep8_introduction.txt") as f:
#     # print(f.readline())
#     line = f.readline()
#     while line:
#         print(line, end="")
#         line = f.readline()

# .readlines()で全ての行をリストで返す
with open("fileio/pep8_introduction.txt") as f:
    lines = f.readlines()
    print(lines)
