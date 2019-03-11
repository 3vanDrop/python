from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext, messagebox
import os
__version__ = '2.2'
class GUI:

    def __init__(self):
        self.window = Tk()
        self.window.title('SW v'+__version__)
        self.window.geometry('500x300')
        title_lbl = Label(self.window, text="SW v"+__version__)
        title_lbl.grid(column=4, row=4)

        self.test_suites = Combobox(self.window)        
        self.test_suites['values']= (self.get_test_suites())
        self.test_suites.current(1)
        self.test_suites.grid(column=4, row=25)
        
        update_btn = Button(self.window, text="Update test cases", command=self.update_test_cases)
        update_btn.grid(column=10, row=25)

        run_btn = Button(self.window, text="Run selected", command=self.run_selection)
        run_btn.grid(column=10, row=35)

        self.listbox = Listbox(self.window, selectmode=EXTENDED)
        self.listbox.grid(column=4, row=30)
        self.window.mainloop()
    
    def get_test_suites(self):
        test_suites = (
            next(i for _, i, _ in os.walk(os.getcwd()+'\\Testcases'))
        )
        return test_suites

    def update_test_cases(self):
        self.listbox.delete(0, END)
        for test_script in self.get_files(): 
            self.listbox.insert(END, test_script)

    def get_files(self):
        return [
            i for _,_,i in os.walk(os.getcwd()+"\\Testcases\\"+self.test_suites.get())
        ][0]
    
    def run_selection(self):
        test_suite = self.test_suites.get()
        test_cases = self.listbox.selection_get().replace('.py', '').split()

        print('py launcher.py -r {0} -t {1}'.format(
            test_suite, ','.join(test_cases)
        ))

launch = GUI()