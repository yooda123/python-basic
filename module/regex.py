import re

# Regular Expression(正規表現)

email = "myemail@gmail.com"
print("@" in email)

matched = re.search("@\w+\.", email)
if matched:
  print(matched)
  print("Matched")
else:
  print("Not found!")

# []
print(re.search('[abc]', "apple"))
print(re.search('[a-c]', "aaa"))
print(re.search('[0-9]', "fgsafd4f"))

# ^ 最初の文字
print(re.search('^[0-9]', "test0"))
print(re.search('^[0-9]', "0test0"))

# {n} n回リピート
print(re.search('^[0-9]{4}', "2021/3/31"))
print(re.search('^[0-9]{4}', "21/3/31"))

# {n, m} 最低n回、最高m回リピート
print(re.search('^[0-9]{2,4}', "21/3/31"))
print(re.search('^[0-9]{2,4}', "2021/3/31"))

# $ 最後の文字
print(re.search('[0-9]{2}$', "2021/3/31"))
print(re.search('[0-9]{2}$', "2021/3/1"))

# * 左のパターンを0回以上リピート
print(re.search('a*b', "aaaaab"))
print(re.search('a*b', "ab"))
print(re.search('a*b', "b"))

# + 左のパターンを1回以上リピート
print(re.search('a+b', "aaaaab"))
print(re.search('a+b', "ab"))
print(re.search('a+b', "b"))

# ? 左のパターンを0回か1回リピート
print(re.search('ab?', "aaaaab"))
print(re.search('ab?', "ab"))
print(re.search('ab?', "a"))

# | or
print(re.search('abc|012', "abc"))
print(re.search('abc|012', "012"))
print(re.search('abc|012', "ab2"))

# () グループ
print(re.search('te(s|x)t', "test"))
print(re.search('te(s|x)t', "text"))
print(re.search('te(s|x)t', "texst"))

# . 任意の1文字
print(re.search('h.t', "h1t"))
print(re.search('h.t', "ht"))
print(re.search('h.t', "h.t"))

# \ エスケープ
print(re.search('h\.t', "h1t"))
print(re.search('h\.t', "h.t"))

# \w [a-zA-Z0-9_]　全てのアルファベット、数字およびアンダースコア
print(re.search('h\wt', "hit"))
print(re.search('h\wt', "h0t"))
print(re.search('h\wt', "hZt"))
print(re.search('h\wt', "h_t"))
print(re.search('h\wt', "hZZt"))
print(re.search('h\wt', "h.t"))


#challenge1
while True:
  birth = input("生年月日を入力してください: ")
  matched = re.search('^(19|20)[0-9]{2}/([1-9]|1[0-2])/([1-9]|[12][0-9]|3[01])$', birth)
  if matched:
    print("正しいフォーマットです")
    break
  else:
    print("正しくないフォーマットです")


#challenge2
while True:
  mail = input("メールアドレスを入力してください: ")
  matched = re.search('^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,3}$', mail)
  if matched:
    print("正しいフォーマットです")
    break
  else:
    print("正しくないフォーマットです")
