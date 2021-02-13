# Main Python Code for Stock Analysis and Predictions: 2TheMoon (2TM)
#
# Created by: Barrett Launius - Started 2/11/2021
# This is the main code
#

from tkinter import *
import tkinter as tk
from tkinter.ttk import *
import math
import os

version = "version beta"
print(version)
print('---------------------------')

# CREATE WINDOW
root = tk.Tk()
sizechg = 0.8
height = int((root.winfo_screenheight()) * sizechg)
width = int((root.winfo_screenwidth()) * sizechg)
#maxsize = (str(width)) + 'x' + (str(height))
#root.geometry(maxsize)
root.title("2TheMoon (" + version + ")")
root.anchor(NW)

# A0:A8 (inputs labels)
x = 0  # x is column number
y = 0  # y is row number
lbltime = Label(root, text=':Time:').grid(row=y, column=x, sticky=W)
lbl_blank = Label(root, text='           ').grid(row=y+1, column=x)
lbl_ticker = Label(root, text='Stock Symbol:').grid(row=y+2, column=x, sticky=E)
lbl_sharesowned = Label(root, text='Shares Owned:').grid(row=y+3, column=x, sticky=E)
lbl_entryprice = Label(root, text='Entry Price:').grid(row=y+4, column=x, sticky=E)
lbl_fill = Label(root, text='          ').grid(row=y,column=2)
lbl_fill2 = Label(root, text = '         ').grid(row=y, column=4)

# B0:B8 (inputs)
x = 1   # x is column
y = 2   # y is row #reference is ticker
ticker_in = StringVar()
i_txtticker = Entry(root, width=10, textvariable=ticker_in).grid(row=y, column=x)
sharesowned_in = StringVar()
i_txtsharesowned = Entry(root, width=10, textvariable=sharesowned_in).grid(row=y + 1, column=x)
entryprice_in = StringVar()
i_txtentryprice = Entry(root, width=10, textvariable=entryprice_in).grid(row=y + 2, column=x)

# D0:D8 (outputs labels)
x = 5
y = 0
lbl_currentprice = Label(root, text='Mark:').grid(row=y, column=x, sticky=E)
lbl_amountinvested = Label(root, text='Amount Invested:').grid(row=y+1, column=x, sticky=E)
lbl_currentvalue = Label(root, text='Current Value:').grid(row=y+2, column=x, sticky=E)
lbl_profitlossD = Label(root, text='Profit/Loss ($):').grid(row=y+3, column=x, sticky=E)
lbl_profitlossP = Label(root, text='Profit/Loss (%):').grid(row=y+4, column=x, sticky=E)

# E0:E8 (outputs)
x=6
y=0
# Current Price
#code to get price online

lbl_currentpriceO = Label(root, text='').grid(row=y, column=x, sticky=W)
lbl_amountinvestedO = Label(root, text='').grid(row=y+1, column=x, sticky=W)
lbl_currentvalueO = Label(root, text='').grid(row=y+2, column=x, sticky=W)
lbl_profitlossDO = Label(root, text='').grid(row=y+3, column=x, sticky=W)
lbl_profitlossPO = Label(root, text='').grid(row=y+4, column=x, sticky=W)






# This is the main button (GO)
def analyzeClick():
    cost = 0.00
    currentvalue = 0.00
    profitlossD= 0.00
    profitlossP= 0.00

    # Get Inputs
    ticker = str(ticker_in.get())
    if ticker.isnumeric() or ticker == '':
        ticker='error'
        ticker_in.set(ticker)
        return None
    else:
        ticker=ticker.upper()
        ticker_in.set(ticker)
    print("ticker = "+str(ticker))

    sharesowned = str(sharesowned_in.get())
    if sharesowned.isnumeric() is False:
        sharesowned='error'
        return None
    else:
        sharesowned = int(sharesowned)
    sharesowned_in.set(sharesowned)
    print('sharesowned = '+str(sharesowned))
    entryprice = str(entryprice_in.get())
    #if "." in entryprice or entryprice.isnumeric():
    if entryprice.isdigit() or entryprice.isnumeric():
        entryprice = float(entryprice)
        entryprice_in.set("${:,.2f}".format(entryprice))
    else:
        entryprice = 'error'
        entryprice_in.set(entryprice)
        return None
    print('entryprice = '+ str(entryprice))


    y=0
    x=6
    print('--Begin Calculations--')
    # CURRENT PRICE
    currentprice = 14.50 #currentprice will be the variable of the current stock price (api)
    lbl_currentpriceO = Label(root, text=str("${:,.2f}".format(currentprice))).grid(row=y, column=x, sticky=W)
    print('currentprice = '+str("${:,.2f}".format(currentprice)))

    # COST
    cost = float(sharesowned*entryprice)
    lbl_amountinvestedO = Label(root, text=str("${:,.2f}".format(cost))).grid(row=y+1, column=x, sticky=W)
    print('cost = '+"${:,.2f}".format(cost))

    # CURRENT VALUE
    currentvalue = currentprice*sharesowned
    lbl_currentvalueO = Label(root, text=str("${:,.2f}".format(currentprice*sharesowned))).grid(row=y+2, column = x, sticky=W)
    print('currentvalue = '+str("${:,.2f}".format(currentvalue)))

    # PROFIT/LOSS ($)
    profitlossD = currentvalue-cost
    lbl_profitlossDO=Label(root, text=str("${:,.2f}".format(profitlossD))).grid(row=y+3, column = x, sticky=W)
    print('profitloss $ = '+str("${:,.2f}".format(profitlossD)))

    # PROFIT/LOSS (%)



# Button command
btn_calculate = Button(root, text='Analyze', command=analyzeClick).grid(row=3, column=3)








root.mainloop()
# I don't know what code would go beyond win.mainloop()
