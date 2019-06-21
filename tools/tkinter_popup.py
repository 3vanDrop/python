"""@tkinter_popup.py

@par Description:
  popup window for ERROR, WARNING, INFO or ASK
   - Based on Tkinter lib
   
@author 3van
"""
from tkinter import messagebox, Tk

class Popup:
    _prefix = 'PREFIX TEXT - '
    root = Tk().withdraw()

    @classmethod
    def error(cls, title, description, **kwargs):
        _error = 'ERROR - '
        prompt = messagebox.showerror(title=cls._prefix + _error + title,
                                        message=description)
        return prompt
                            
    @classmethod
    def warning(cls, title, description, **kwargs):
        _warning = 'WARNING - '
        prompt = messagebox.showwarning(title=cls._prefix + _warning + title,
                                        message=description)
        return prompt
    
    @classmethod
    def info(cls, title, description, **kwargs):
        _info = 'INFO - '
        prompt = messagebox.showinfo(title=cls._prefix + _info + title,
                                        message=description)
        return prompt
        
    @classmethod
    def ask(cls, title, description, **kwargs):
        _options = {'yes' : True, 'no': False}
        prompt = messagebox.askquestion(cls._prefix + title,
                                          description, icon='warning')
        return _options[prompt]

if __name__ == '__main__':

    popup.error(
        title='TEST ERROR',
        description='This is a test!'
    )

    popup.warning(
        title='TEST WARNING',
        description='This is a test!'
    )

    popup.info(
        title='TEST INFO',
        description='This is a test!'
    )

    if popup.ask(title='TEST ASK',  description='Yes or Not?'):
        print('You selected YES!')
    else:
        print('You selected NO!')         
            
  
