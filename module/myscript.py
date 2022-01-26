# 標準ライブラリ、サードパーティのライブラリ、自分たちのライブラリ、ローカルのライブラリ
# ↑それぞれ1行ずつ空けて羅列するとわかりやすい

# import sys, mymodule # 複数羅列せず1行ずつimportすること
import sys
sys.path.append("D:/vscode/kamesan-git/python-basic/function")
import docstring

# import mymodule
import mymodule as mm ### 非推奨!!! 自分で作った個別モジュールにasは使わない。わかりにくい ###
# mymodule.myfunc()
# print(mymodule.myvariable)

###
# 特定の関数やグローバル変数だけインポート
###
# from mymodule import myfunc, myvariable, anotherfunc
# from mymodule import * ### 非推奨!!! _始まりの関数や変数は呼べない###
mm.myfunc()
print(mm.myvariable)
mm.anotherfunc()
# mm._non_public_func() _始まりは外から使わない

print(sys.path)

print(docstring.multiply(3, 4))
