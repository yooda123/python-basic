# importのStyle
# correct
import math
import sys
import os
# wrong
# import sys,import os

# correct
from subprocess import Popen, PIPE

# 順番
# 1.Standard library (time, sys)
# 2.Third Party (numpy, pandas)
# 3.Our Library
# 4.Local library
# それぞれ1行空ける

# absolute import
import mypkg.sibling
from mypkg import sbling
from mypdg.sibling import example


# 変数定義
# correct
x = 1
y = 1
# wrong
xxxxx = 1
yyyyy = 1

x = 1  # 無駄なスペース

# 関数の引数の「=」にはスペース不要
# correct


def complex(real, imag=0.0):
    return magic(r=real, i=imag)

# wrong


def complex(real, imag=0.0):
    return magic(r=real, i=imag)


# operatorの周りにスペース1個, operatorにpriorityがある場合はスペースをなくす
# correct
x = x + 1
x += 1
x = x*2 - 1
a = x*x + y*y
c = (a+1) * (a-1)

# wrong
x = x+1
x += 1
x = x * 2 - 1
a = x * x + y * y
c = (a + 1) * (a - 1)

# カンマの後ろにはスペースを入れる
range(1, 11)
a = [1, 2, 3, 4]
b = (1, 2, 3, 4)

# カンマの後ろに閉じ括弧がくる場合はスペース不要
foo = (0,)

# correct
FILES = [
    'setup.cfg',
    'tox.ini',
    'tox2.ini',
    'tox3.ini',  # 　カンマ付ける（バージョン管理で差分が出ないように）
]

# wrong
FILES = ['setup.cfg', 'tox.ini', ]

# 行の折り返し
# correct (引数の先頭を合わせる)
foo = long_function_nmame(
    var_one, var_two,
    var_three, var_four)

# wrong
foo = long_function_nmame(var_one, var_two,
                          var_three, var_four)

# correct (引数は2インデントで。処理の始まりと区別しやすい)


def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# wrong


def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)


# '\'で区切って改行する
print("このように表示する文章が長かったりする場合は\
バックスラッシュで区切ると改行できます")

# correct
a = 1000000000000000000000000000 \
    + 1000000000000000000000 \
    + 1000000000000000000000 \
    + 10000000 \
    + 10000000000

# wrong
a = 1000000000000000000000000000 +\
    1000000000000000000000 +\
    1000000000000000000000 +\
    10000000 +\
    10000000000

# 関数間は2行空ける


def func():
    """
    """
    pass


def func2():
    pass


class MyClass:
    def __init__(self) -> None:
        pass

    def method(self):
        pass


# コメント
# ・コメントは常に最新に。コメントとコードの中身が異なるなら、コメントはないほうがまし
# ・なるべく英語で書く。絶対に日本語がわからない人が読まないなら日本語でもOK
# ・書くときは文書で書くのが望ましい
# ・# のあとに半角スペースを入れる
# ・インラインコメントはコードの後に半角スペースを2つ入れて#を書く
a = 1  # コメントコメント（インラインコメント）
# ・Docstringは基本的に全てのmodule、function、class、methodにつける（non publicな外からアクセスしない関数には不要）
# ・そのコードが「なにをしているか」より「何故そう書いたか」の方が有益


# 命名規則（naming convention)
# 変数名や関数名：snake_case 例）balance, image_height
# クラス名： CamelCase 例）Person、MyClass
# モジュールやパッケージ名：なるべく短いlower caseで必要であればsnake_case 例）time, numpy

# アンダースコア
# _xxx: internal use only(non public)
# xxx_: Pythonで既に使われている単語を使いたいとき
# __xxx: クラスの属性として使うことで名前修飾できる
# __xxx__: magic methodと呼ばれるもので、pythonが特別に設定しているもの、開発者が定義できない（overrideはありうる）
# _: 最近実行した戻り値や、iteration時に使わない変数

for _ in range(10):
    print('hello')

# l, I, 0 一文字の変数は1や0に見間違えるので使わない
# correct
letter = "hello"
length = len(letter)

# wrong
l = len(letter)

# Constants(定数)は大文字のsnakecaseを使う
PI = 3.14
PI = 3  # 変更はできることに注意


# Return


def foo(x):
    if x >= 0:
        return math.sqrt(x)
        # if returnだけにしない。elseも書く
    else:
        return None


# オブジェクトタイプの確認はisinstance()を使う
# correct
if isinstance(obj, int)
# wrong
if type(obj) is type(1)


# Booleanに比較演算子を使わない
# correct
if bool_var:
    pass
    # wrong
if bool_var == True:
    pass


# type hint
def greeting(name: str) -> str:
    return "Hello " + name
# 一つでもhintをつけたら全てに付ける
# pythonは動的型付けなので、typeのチェックをしてくれるわけではない
# typeにとらわれすぎない
# type hintを強制したり、命名規約に入れるべきではない


# import os, sys
x = 1
y = 2

# PythonのLinter
# ・Stylistic Lint,　Logical Lintの2種類ある
# ・Stylistic Lintの代表は、pycodestyle(元pep8)
# ・Logical Lintの代表は、pyflakes
# ・pycodestyleとpyflakesのラッパーライブラリ： flake8
# ・flake8より厳しいのが、pylint
