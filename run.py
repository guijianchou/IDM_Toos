#/etc/bin/env python
#-*- coding: UTF-8 -*-

__auther__='guijianchou'

'run.py'

import cleanfile 
import copyfile


def __run_func1():
    try:
        cleanfile.clean_file2()
    except TypeError,e:
        print 'Exception:',e
    finally:
        pass

def __run_func2():
    try:
        copyfile.copy_file2()
    except TypeError,e:
        print 'Exception:',e
    finally:
        pass

if __name__=='__main__':
    __run_func1()
    __run_func2()
    print"All Job DONE !"