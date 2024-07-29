#!/usr/bin/env python
# coding: utf-8

# In[1]:


import warnings
warnings.filterwarnings("ignore")
import numpy as np 
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import datetime

from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import tkinter.font as font
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
from win32api import GetSystemMetrics
import sqlite3 as sq
import datetime
from datetime import date, timedelta
from tkinter.scrolledtext import ScrolledText
from itertools import combinations 
from collections import Counter

import pickle
from sklearn import model_selection, preprocessing, pipeline, utils,decomposition


# In[2]:


t1=datetime.datetime.now()
w1="yellow2"
w2='blue2'
w3="lawn green"
w4="green2"
w5="orange"
sig="Times New Roman Bold"


# In[3]:


def read_model():
    filename = 'Best_Model.sav'
    loaded_best = pickle.load(open(filename, 'rb'))
    return loaded_best


# In[4]:


def ReadDB():
    drs=os.listdir()
    if "Encoded_Data.csv" in drs:
        HDB=pd.read_csv("Encoded_Data.csv")
    else:
        HDB=pd.read_csv("Complete_Data.csv")
    HDB=HDB.drop('Unnamed: 0',axis=1)
    return HDB


# In[5]:


def DataNorm(incd): 
    prepproc = preprocessing.MinMaxScaler() 
    incnr=prepproc.fit_transform(incd) 
    return incnr 


# In[6]:


def SalaryApp():
    salwdg=Tk()
    salwdg.resizable(False, False)
    #salwdg.wm_attributes('-alpha', 0.9)
    salwdg.title("Employee Salary Predictor")
    salwdg.configure(bg=w2)
    stylesalwdg = Style() 
    stylesalwdg.configure('W.TButton', font = (sig, 15, 'bold'), foreground = w2,borderwidth = '3') 
    salwdg.geometry(str(GetSystemMetrics(0)-400)+'x'+str(GetSystemMetrics(1)-200))
    
 
    #########################################################
    reslbl2=Label(salwdg, text="Employee Statistics",font=(sig,25))
    reslbl2.place(x=651,y=122)
    reslbl2.configure(foreground=w1,background=w2)
    ########################################################
    canvas2 = Canvas(width=600, height=250, bg=w2) 
    canvas2.place(x=480,y=172) 
    #################################################################

    #################################################################
    usbs=Label(salwdg, text="Base Salary",font=(sig,20))
    usbs.place(x=500,y=200)
    usbs.configure(foreground=w4,background=w2)
    usbsdis=Label(salwdg, text="{}".format("____________"),font=(sig,20))
    usbsdis.place(x=780,y=200)
    usbsdis.configure(foreground=w5,background=w2)

    uslp=Label(salwdg, text="Longevity Pay",font=(sig,20))
    uslp.place(x=500,y=250)
    uslp.configure(foreground=w4,background=w2)
    uslpdis=Label(salwdg, text="{}".format("____________"),font=(sig,20))
    uslpdis.place(x=780,y=250)
    uslpdis.configure(foreground=w5,background=w2)

    upop=Label(salwdg, text="Overtime Pay",font=(sig,20))
    upop.place(x=500,y=300)
    upop.configure(foreground=w4,background=w2)
    upopdis=Label(salwdg, text="{}".format("____________"),font=(sig,20))
    upopdis.place(x=780,y=300)
    upopdis.configure(foreground=w5,background=w2)

    usdp=Label(salwdg, text="Department",font=(sig,20))
    usdp.place(x=500,y=350)
    usdp.configure(foreground=w4,background=w2)
    usdpdis=Label(salwdg, text="{}".format("____________"),font=(sig,17))
    usdpdis.place(x=780,y=350)
    usdpdis.configure(foreground=w5,background=w2)
    ########################## Upto This ############################
    
    
    
    lbl_0=Label(salwdg, text="Employee Salary Predictor",font=(sig,28))
    lbl_0.place(x=381,y=5)
    lbl_0.configure(foreground=w3,background=w2)

    ddt=pd.read_csv("DeptData.csv")
    div=pd.read_csv("DivData.csv")
    gap=100
    dnm=tuple(ddt['Department Name'].tolist())
    entr_dnm=Label(salwdg, text="Department",font=(sig,20))
    entr_dnm.place(x=20,y=gap+80)
    entr_dnm.configure(foreground=w1,background=w2)
    entr_dnmc = Combobox(salwdg,width=22)
    entr_dnmc['values']= dnm
    entr_dnmc.place(x=290,y=gap+82,height=28)
    
    dv=tuple(div['Division'].tolist())
    entr_dv=Label(salwdg, text="Division",font=(sig,20))
    entr_dv.place(x=20,y=gap+130)
    entr_dv.configure(foreground=w1,background=w2)
    entr_dvc = Combobox(salwdg,width=22)
    entr_dvc['values']= dv
    entr_dvc.place(x=290,y=gap+132,height=28)
    
    entr_bsl=Label(salwdg, text="Base Salary",font=(sig,20))
    entr_bsl.place(x=20,y=gap+180)
    entr_bsl.configure(foreground=w1,background=w2)
    entr_bsle = Entry(salwdg,width=25)
    entr_bsle.place(x=290,y=gap+182,height=28)
    
    entr_lgp=Label(salwdg, text="Longevity Pay",font=(sig,20))
    entr_lgp.place(x=20,y=gap+230)
    entr_lgp.configure(foreground=w1,background=w2)
    entr_lgpe = Entry(salwdg,width=25)
    entr_lgpe.place(x=290,y=gap+232,height=28)
    
    
    entr_ovp=Label(salwdg, text="Overtime Pay",font=(sig,20))
    entr_ovp.place(x=20,y=gap+280)
    entr_ovp.configure(foreground=w1,background=w2)
    entr_ovpe = Entry(salwdg,width=25)
    entr_ovpe.place(x=290,y=gap+282,height=28)
       
    
    def result():
        #hdb=ReadDB()
        dptn=entr_dnmc.get()
        dvn=entr_dvc.get()
        bs=entr_bsle.get()
        lp=entr_lgpe.get()
        op=entr_ovpe.get()
        #messagebox.showinfo("Info","Department: {}\nBase Salary: {}".format(dptn,bs))
        bs=float(bs)
        lp=float(lp)
        op=float(op)
        bpov=bs+op
        bpl=bs+lp
        ttls=bs+op+lp
        avp=ttls
        ddt=pd.read_csv("DeptData.csv")
        div=pd.read_csv("DivData.csv")
        ddten=ddt['Dept'].tolist()
        diven=div['Div'].tolist()
        tsdpt, tsdiv=0,0
        tsdpt=float(ddt[ddt['Department Name']==dptn]['Dept'].tolist()[0])
        tsdiv=float(div[div['Division']==dvn]['Div'].tolist()[0])
        
        usbsdis.configure(text="{}".format(bs))
        uslpdis.configure(text="{}".format(lp))
        upopdis.configure(text="{}".format(op))
        usdpdis.configure(text="{}".format(dptn))
        
        testdata=[tsdpt,tsdiv,bs,lp,bpov,bpl,ttls,avp]
        testdatanrm=DataNorm([testdata])
        model=read_model()
        result=model.predict(testdatanrm)
        resultprb=model.predict_proba([testdata])
        if result[0]=="High Income":
            messagebox.showinfo("Prediction Result","\nYou Belong to {} Group\n-----Salary Possibilities-----\nIncome Lowerbound: 80000\nIncome Upperbound: No Bound".format("High Income"))
        if result[0]=="Medium High Income":
            messagebox.showinfo("Prediction Result","\nYou Belong to {} Group\n-----Salary Possibilities-----\nIncome Lowerbound: 50000\nIncome Upperbound: 79999".format("Medium High Income"))
        if result[0]=="Average Income":
            messagebox.showinfo("Prediction Result","\nYou Belong to {} Group\n-----Salary Possibilities-----\nIncome Lowerbound: 30000\nIncome Upperbound: 49999".format("Average Income"))
        if result[0]=="Low Income":
            messagebox.showinfo("Prediction Result","\nYou Belong to {} Group\n-----Salary Possibilities-----\nIncome Lowerbound: No Bound\nIncome Upperbound: 29999".format("Low Income"))
        
        
        ################ This ############
        
    res_btn = Button(salwdg, text="Result", command=result, style = 'W.TButton')
    res_btn.place(x=80,y=500)
    
    def clear():
        entr_dnmc.delete(0,END)
        entr_dvc.delete(0,END)
        entr_bsle.delete(0,END)
        entr_lgpe.delete(0,END)
        entr_ovpe.delete(0,END)
            
    buttncln = Button(salwdg, text="Clear", command=clear, style = 'W.TButton')
    buttncln.place(x=220,y=500)
    
    def quit():
        salwdg.destroy()
    
    buttnqt = Button(salwdg, text="Quit", command=quit, style = 'W.TButton')
    buttnqt.place(x=150,y=560)

    
    def rfrs():
        usbsdis.configure(text="____________")
        uslpdis.configure(text="____________")
        upopdis.configure(text="____________")
        usdpdis.configure(text="____________")
    
    buttnfr = Button(salwdg, text="Refresh", command=rfrs, style = 'W.TButton')
    buttnfr.place(x=750,y=500)
    
    salwdg.mainloop()
SalaryApp()


# In[ ]:




