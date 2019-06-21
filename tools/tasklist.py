"""@tasklist.py
    @par DESCRIPTION :
        - tasklist() -> Returns generator object 
        - find_process uses tasklist to iterate
    @par AUTHOR:
        -- 3van --
"""
from subprocess import check_output

def tasklist():
    """ tasklist() :: -generator- obj """
    for task in (line.split() for line in check_output("tasklist").splitlines()[3:]):
        yield task[0].decode('utf-8')
              
def find_process(process):
    """ find_process :: iterates through tasklist() to find"""
    for task in tasklist():
        if process.lower() == task.lower():
            return True
    return False
   
if __name__ == '__main__':
    if find_process('notepad.exe'):
        print('Process found!')
    else:
        print('Process is not running!')
