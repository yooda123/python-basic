
# try:
#     f = open("fileio/pep8_introduction.txt")
#     # print(f)
#     for line in f:
#         print(line, end="")  # default: end="\n
# finally:
#     f.close()

with open("fileio/pep8_introduction.txt") as f:
    for line in f:
        print(line, end="")
