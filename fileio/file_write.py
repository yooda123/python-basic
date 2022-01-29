with open("fileio/writing_file.txt", mode='w') as f:
    # 'w' -> trancatedされる（上書きされる）
    f.write("You can write contents here.\nuse 'backslash' to break the row.")
    f.write("new write() doesn't bread row.")

    print("You can add a new row using 'file' parameter", file=f)
    print("new print() method breaks the row for you!!", file=f)

    # print(f.read()) # read はできない
