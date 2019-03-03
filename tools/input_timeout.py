"""@input_timeout.py

    @par DESCRIPTION :
        - input_timeout works exactly like input Python built-in
          function, but if a timeout is reached, it takes default
          parameter

    @par USAGE:
        - input_timeout(
            str PROMPT, int SECONDS, bool DEFAULT_VAL
        )

    @par AUTHOR:
        -- 3van --
"""


import sys, select, threading, time

class timer:
    @classmethod
    def input(cls, prompt, timeout=5, default=False):
        print(__name__, prompt)
        threading._start_new_thread( cls.countdown, (timeout, default) )
        i, o, e = select.select( [sys.stdin], [], [], timeout )
        if (i):
          return True
        else:
          return False

    @classmethod
    def countdown(cls, timeout, default):
        for i in reversed(range(1,timeout+1)):
            print(i, end=' ', flush=True)
            time.sleep(1)


print(timer.input('Press ENTER if True', 5, False))
