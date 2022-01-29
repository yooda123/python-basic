# join
text = " ".join(["Hi", "My", "name", "is", "John"])
print(text)

# sprit
print("Hi My name is John".split())
print("Hi/My/name/is/John".split("/"))

filename = "sample.py"
print(filename.split(".")[0]) # ファイル名の前半
print(filename.split(".")[-1]) # 拡張子
