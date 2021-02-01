# -*- coding: utf-8 -*-

import sys


if len(sys.argv) != 2:

    print("")
    print("This script is a class test launcher. You should provide the name of the class to test such as in this example :")
    print("$ python tests.py CLASSNAME")
    print("")

else:

    CLASSNAME = sys.argv[1]

    exec(f"import lib.{CLASSNAME} as classModule")
    exec(f"Class = classModule.{CLASSNAME}")

    from config import *
    Class.test(CONFIG)