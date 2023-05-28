import sys
try:
    try:
        try:
            input()
        except KeyboardInterrupt as kb_int:
            print('Keyboard interrupted')
            raise ExceptionGroup('Multiple things went wrong', 
                                    [SystemError(1), OSError(1)])
    except* SystemError:
        print('One of the things that went wrong was a System err')
except* OSError:
    print('One of the things that went wrong was an OS err')