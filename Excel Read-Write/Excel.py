"""@Excel.py
*******************************************************************************
@par DESCRIPTION:

        - Excel Basic operations Class:
        Basic Excel App control through COM Server based on Pywin32 lib
    
    == Author: '3van' ==

@NOTE:
    Created on Python v3.7  

*******************************************************************************
"""

import win32com.client
import psutil, sys, time, os

class Excel(object):

    def __init__(self, filepath, *args, **kwargs):

        try:
            self.debug = True if 'debug' in args else False
            if self.debug: breakpoint()
            
            # - Kill current Excel running workbooks
            if self.__isExcelRunning__():
                os.system('taskkill /F /IM excel.exe')

            self.ExcelApp = win32com.client.Dispatch("Excel.Application")

            # - Open Excel Workbook 
            self.file_path = filepath
            self.ExcelWorkbook = self.ExcelApp.Workbooks.Open(
                self.file_path, UpdateLinks = 0 
            )
            if not isinstance(self.ExcelWorkbook, object):
                raise RuntimeError(
                    'Not able to Open Excel Workbook'
                )

        except Exception as error:
            print(
                'Not possible to Dispatch Excel App',
                type(error).__doc__, type(error).__name__, error
            )
            sys.exit(0)

    def __isExcelRunning__(self):
        try:
            for p in psutil.process_iter():
               if 'EXCEL.EXE' in p.name():
                   return True
            return False
        except Exception as error:
            print(
                type(error).__doc__, type(error).__name__, error
            )
            return False

    def write(self, sheet, row, column, value):

        try:   

            if (row + column)<2:
                raise ValueError(
                    'Row/Column value must be higher than 0.'
                )
            if self.debug: breakpoint()
            self.ExcelWorkbook.Worksheets( str(sheet) ).Cells(
                int(row), int(column)
            ).Value = str(value)

        except Exception as error:
            print(
                'Not possible to write on Excel workbook',
                type(error).__doc__, type(error).__name__, error
            )

    def read(self, sheet, row, column):

        try:
            if ( int(row) + int(column) )<2:
                raise ValueError(
                    'Row/Column value must be higher than 0.'
                )

            if self.debug: breakpoint()
            cell_data = self.ExcelWorkbook.Worksheets( str(sheet) ).Cells(
                int(row), int(column)
            ).Value

            return cell_data
        except Exception as error:
            print(
                'Not possible to read Excel workbook',
                type(error).__doc__, type(error).__name__, error
            )

    def close(self):
        try:
            self.ExcelWorkbook.Save()
            self.ExcelApp.Application.Quit()
        except Exception as error:
            print(
                'Not possible to write on Excel workbook',
                type(error).__doc__, type(error).__name__, error
            )


if __name__ == '__main__':

    # Open Workbook
    path = os.getcwd() + '\\Test.xlsx'
    Workbook = Excel(filepath=path)

    # Write Excel Workbook | Cell 1-1
    Workbook.write(         
        sheet='Sheet1',
        row=1,
        column=1,
        value='Hello World!'
    )

    # Read Excel Workbook | Cell 1-1
    before = Workbook.read(   
        sheet='Sheet1',
        row=1,
        column=1
    )
    # Write Excel Workbook | Cell 1-1
    Workbook.write(         
        sheet='Sheet1',
        row=1,
        column=1,
        value='This is a Test!'
    )

    # Read Excel Workbook | Cell 1-1
    after = Workbook.read(   
        sheet='Sheet1',
        row=1,
        column=1
    )

    # Save changes and close Workbook
    Workbook.close()

    
    print(
        'Before:', before,
        '\nAfter: ', after
    )

    
