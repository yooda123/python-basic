# import myfirstpackage.module1
# import myfirstpackage.module2

# myfirstpackage.module1.myfunc()
# myfirstpackage.module2.myfunc()

#######################################################
# from myfirstpackage import module1
# from myfirstpackage import module2

# module1.myfunc()
# module2.myfunc()

#######################################################

###
# NG!!!! どっちのmyfuncかわからない
###
# from myfirstpackage.module1 import myfunc
# from myfirstpackage.subdir.module2 import myfunc

# myfunc()

########################################################
###
# myfirstpackage直下の__init__.py にmodule2のimportを記述すると、myfirstpackage.myfunc()で実行できる
# from myfirstpackage.subdir.module2 import *
###

# import myfirstpackage
# import myfirstpackage.module1

# myfirstpackage.myfunc()
# myfirstpackage.myfunc2()
# myfirstpackage.module1.myfunc()

########################################################

from myfirstpackage.subdir import *
myfunc2()