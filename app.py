# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 02:16:38 2019

@author: haythem jaidane
"""
# import the modules that we need to this app
from tkinter import *
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math
import sympy
#set the functions of the software
def plot():
    try:
        min1=float(f1.get())
        max1=float(f2.get())
        u=f.get()
        if max1>min1:
            if len(u)>0 and not u.isspace():
                if u[0]!='/' and u[0]!='*':
                    x=np.linspace(min1,max1,int((max1-min1)*10000))
                    i=0
                    r=[] # "ln" ,"()" , e**() ,sin(), cos(),tan(),**(),log(),sqrt()
                    rr=[[np.zeros(int((max1-min1)*10000)),np.zeros(int((max1-min1)*10000))]]
                    mul=["+"] # "*"-->1  "+"-->2  "-"-->4  "/"-->6
                    mul1=[]
                    gold=0
                    mulable=[(True,0)]
                    iii=0
                    ii=0
                    ss=np.zeros(int((max1-min1)*10000))
                    while iii!=len(u)-1:
                        if u[iii]=="(":
                            gold=gold+1
                        elif u[iii]==")":
                            gold=gold-1
                        if gold==0:
                            if u[iii]=="+" or u[iii]=="-" or u[iii]=="/" or (u[iii]=="*" and u[iii+1]!="*" and u[iii-1]!="*"):
                                mul.append(u[iii])
                        iii=iii+1
                    jh=[]
                    while i<=len(u)-1:
                        tf=i
                        k=u[i]
                        if len(r)!=0 and len(mul1)!=len(r):
                            mul2=['+']
                            ff=i
                            m=0
                            while True:
                                if u[ff]==")":
                                    if m==0:
                                        break
                                    else:
                                        m=m-1
                                elif u[ff]=='(':
                                    m=m+1
                                if (u[ff]=="+" or u[ff]=="-" or u[ff]=="/" or (u[ff]=="*" and u[ff-1]!="*" and u[ff+1]!="*") and m==0):
                                    mul2.append(u[ff])
                                ff=ff+1
                            mul1.append(mul2)
                            rr.append([np.zeros(int((max1-min1)*10000)),np.zeros(int((max1-min1)*10000))])
                            mulable.append((True,0))
                            jh.append(0)
                        if k==' ':
                            i=i+1
                        elif k=="x":
                            if mulable[len(r)][0]==True:
                                rr[len(r)][0]=x
                            else:
                                rr[len(r)][1]=x
                            i=i+1
                        elif k=='(':
                            r.append(2)
                            i=i+1
                        elif k==')':
                            if mul1[len(r)-1][-1]=="+":
                                rr[len(r)-1][1]=rr[len(r)-1][1]+rr[len(r)][0]
                            elif mul1[len(r)-1][-1]=="-":
                                rr[len(r)-1][1]=rr[len(r)-1][1]-rr[len(r)][0]
                            elif mul1[len(r)-1][-1]=="*": 
                                rr[len(r)][0]=rr[len(r)][0]*rr[len(r)][1]
                                if mulable[len(r)][1]=="+":
                                    print("zeb")
                                    rr[len(r)-1][1]=rr[len(r)-1][1]+rr[len(r)][0]
                                elif mulable[len(r)][1]=="-":
                                   rr[len(r)-1][1]=rr[len(r)-1][1]-rr[len(r)][0]
                                print("rr 1: ",rr[len(r)-1][1])
                            elif mul1[len(r)-1][-1]=="/":
                                rr[len(r)][0]=rr[len(r)][0]/rr[len(r)][1]
                                if mulable[len(r)][1]=="+":
                                    rr[len(r)-1][1]=rr[len(r)-1][1]+rr[len(r)][0]
                                elif mulable[len(r)][1]=="-":
                                    rr[len(r)-1][1]=rr[len(r)-1][1]-rr[len(r)][0]
                            bgt=r[-1]
                            r.pop(-1)
                            if bgt==1:
                                if mulable[len(r)][0]==True:
                                    rr[len(r)][0]=np.log(rr[len(r)][1])
                                    rr[len(r)][1]=np.zeros(int((max1-min1)*10000))
                                else:
                                    rr[len(r)][1]=np.log(rr[len(r)][1])
                            elif bgt==2:
                                if mulable[len(r)][0]==True:
                                    rr[len(r)][0]=rr[len(r)][1]
                                else:
                                    pass
                            elif bgt==3:
                                if mulable[len(r)][0]==True:
                                    rr[len(r)][0]=np.exp(rr[len(r)][1])
                                    rr[len(r)][1]=0
                                else:
                                    rr[len(r)][1]=np.exp(rr[len(r)][1])
                        
                            elif bgt==4:
                                if mulable[len(r)][0]==True:
                                    rr[len(r)][0]=np.sin(rr[len(r)][1] * (np.pi / 180))
                                    rr[len(r)][1]=0
                                else:
                                    rr[len(r)][1]=np.sin(rr[len(r)][1] * (np.pi / 180))
                                
                            elif bgt==5:
                                if mulable[len(r)][0]==True:
                                    rr[len(r)][0]=np.cos(rr[len(r)][1]* (np.pi / 180))
                                    rr[len(r)][1]=0
                                else:
                                    rr[len(r)][1]=np.cos(rr[len(r)][1] * (np.pi / 180))
                                    
                            elif bgt==6:
                                if mulable[len(r)][0]==True:
                                    rr[len(r)][0]=np.tan(rr[len(r)][1] * (np.pi / 180))
                                    rr[len(r)][1]=0
                                else:
                                    rr[len(r)][1]=np.tan(rr[len(r)][1] * (np.pi / 180))
                             
                            elif bgt==7:
                                g=[]
                                for hj in rr[len(r)][1]:
                                    if hj>=0:
                                        hj=math.factorial(int(hj))
                                        g.append(hj)
                                    else:
                                        g.append(np.nan)
                                if mulable[len(r)][0]==True:
                                    rr[len(r)][0]=np.array(g)
                                    rr[len(r)][1]=0
                                else:
                                    rr[len(r)][1]=np.array(g)
                            
                            elif bgt==8:
                                if mulable[len(r)][0]==True:
                                    rr[len(r)][0]=np.power(rr[len(r)][0],rr[len(r)][1]) 
                                    rr[len(r)][1]=0
                                else:
                                    rr[len(r)][1]=np.power(rr[len(r)][0],rr[len(r)][1])
                            
                            elif bgt==9:
                                if mulable[len(r)][0]==True:
                                    rr[len(r)][0]=np.log10(rr[len(r)][1])
                                    rr[len(r)][1]=0
                                else:
                                    rr[len(r)][1]=np.log10(rr[len(r)][1])
                                
                            elif bgt==10:
                                if mulable[len(r)][0]==True:
                                    rr[len(r)][0]=np.sqrt(rr[len(r)][1])
                                    rr[len(r)][1]=0
                                else:
                                    rr[len(r)][1]=np.sqrt(rr[len(r)][1])
                                
                            mulable.pop(-1)
                            rr.pop(-1)
                            mul1.pop(-1)
                            jh.pop(-1)
                            i=i+1
                        elif k.lower()=="s":
                            if len(u)-1-i>=4:
                                if u[i].lower()=="s" and u[i+1].lower()=="i" and u[i+2].lower()=="n" and u[i+3]=="(":
                                    r.append(4)
                                    i=i+4
                            if len(u)-1-i>=5:
                                if u[i].lower()=="s" and u[i+1].lower()=="q" and u[i+2].lower()=="r" and u[i+3].lower()=="t" and u[i+4]=="(":
                                    r.append(10)
                                    i=i+5 
                        elif k.lower()=="c":
                            if u[i].lower()=="c" and u[i+1].lower()=="o" and u[i+2].lower()=="s" and u[i+3]=="(":
                                r.append(5)
                                i=i+4
                        elif k.lower()=="t":
                            if u[i].lower()=="t" and u[i+1].lower()=="a" and u[i+2].lower()=="n" and u[i+3]=="(":
                                r.append(6)
                                i=i+4
                        elif k.lower()=="f":
                            if u[i].lower()=="f" and u[i+1].lower()=="a" and u[i+2].lower()=="c" and u[i+3].lower()=="t" and u[i+4]=='(':
                                r.append(7)
                                i=i+5
                        elif k=='*' and u[i+1]=="*":
                            if k=="*" and u[i+1]=="*" and u[i+2]=='(':
                                r.append(8)
                                i=i+3
                        elif k.lower()=="l":
                            if len(u)-1-i>=3:
                                if u[i].lower()=="l" and u[i+1].lower()=="n" and u[i+2]=="(":
                                    r.append(1)
                                    i=i+3
                                if u[i].lower()=="l" and u[i+1].lower()=="o" and u[i+2].lower()=="g" and u[i+3]=="(":
                                    r.append(9)
                                    i=i+4
                        elif k.lower()=="e":
                            if len(u)-1-i>=4:
                               if u[i].lower()=="e" and u[i+1]=="*" and u[i+2]=="*"and u[i+3]=="(":
                                   r.append(3)
                                   i=i+4
                            else:
                                if mulable[len(r)][0]==True:
                                    rr[len(r)][0]=(math.e)*(np.ones(int((max1-min1)*10000)))
                                else:
                                    rr[len(r)][1]=(math.e)*(np.ones(int((max1-min1)*10000)))
                                i=i+1
                        elif k=="+" or k=="-" or (k=="*" and u[i+1]!="*") or k=="/":
                            if len(r)==0:
                                if k=="-" or k=="+":
                                    if mul[ii]=="+":
                                        ss=ss+rr[0][0]
                                        rr[0][0]=np.zeros(int((max1-min1)*10000))
                                    elif mul[ii]=="-":
                                        ss=ss-rr[0][0]
                                        rr[0][0]=np.zeros(int((max1-min1)*10000))
                                    else:
                                        if mul[ii]=="*":
                                            rr[0][0]=rr[0][0]*rr[0][1]
                                        elif mul[ii]=="/":
                                            rr[0][0]=rr[0][0]/rr[0][1]
                                        if mulable[0][1]=="+":
                                            ss=ss+rr[0][0]
                                        elif mulable[0][1]=="-":
                                            ss=ss-rr[0][0]
                                    rr[0][0]=np.zeros(int((max1-min1)*10000))
                                    rr[0][1]=np.zeros(int((max1-min1)*10000))
                                    mulable[0]=(True,0)
                        
                                
                                else:
                                    if mul[ii]=="+" or mul[ii]=="-":
                                        mulable[0]=(False,mul[ii])
                                    elif mul[ii]=="*":
                                        rr[0][0]=rr[0][0]*rr[0][1]
                                        rr[0][1]=np.zeros(int((max1-min1)*10000))
                                    elif mul[ii]=="/":
                                        rr[0][0]=rr[0][0]/rr[0][1]
                                        s1=rr[0][1]=np.zeros(int((max1-min1)*10000))
                                ii=ii+1
                            else:
                                if k=="-" or k=="+":
                                    if mul1[len(r)-1][jh[len(r)-1]]=="+":
                                        rr[len(r)-1][1]=rr[len(r)-1][1]+rr[len(r)][0]
                                        rr[len(r)][0]=np.zeros(int((max1-min1)*10000))
                                    elif mul1[len(r)-1][jh[len(r)-1]]=="-":
                                        rr[len(r)-1][1]=rr[len(r)-1][1]-rr[len(r)][0]
                                        rr[len(r)][0]=np.zeros(int((max1-min1)*10000))
                                    else:
                                        if mul1[len(r)-1][jh[len(r)-1]]=="*":
                                            rr[len(r)][0]=rr[len(r)][0]*rr[len(r)][1]
                                        elif mul1[len(r)-1][jh[len(r)-1]]=="/":
                                            rr[len(r)][0]=rr[len(r)][0]/rr[len(r)][1]
                                        if mulable[len(r)][1]=="+":
                                            rr[len(r)-1][1]=rr[len(r)-1][1]+rr[len(r)][0]
                                        elif mulable[len(r)][1]=="-":
                                            rr[len(r)-1][1]=rr[len(r)-1][1]+rr[len(r)][0]
                                        rr[len(r)][0]=np.zeros(int((max1-min1)*10000))
                                        rr[len(r)][1]=np.zeros(int((max1-min1)*10000))
                                        mulable[len(r)]=(True,0)
                        
                            
                                else:
                                    if mul1[len(r)-1][jh[len(r)-1]]=="+" or mul1[len(r)-1][jh[len(r)-1]]=="-":
                                        mulable[len(r)]=(False,mul1[len(r)-1][jh[len(r)-1]])
                                    elif mul1[len(r)-1][jh[len(r)-1]]=="*":
                                        rr[len(r)][0]=rr[len(r)][1]*rr[len(r)][0]
                                        rr[len(r)][1]=np.zeros(int((max1-min1)*10000))
                                    elif mul1[len(r)-1][jh[len(r)-1]]=="/":
                                        rr[len(r)][0]=rr[len(r)][1]/rr[len(r)][0]
                                        rr[len(r)][1]=np.zeros(int((max1-min1)*10000))
                                jh[len(r)-1]=jh[len(r)-1]+1
                            i=i+1
                        elif k.isdigit() or k=='.':
                            ro=""
                            while u[i].isdigit() or u[i]=='.':
                                ro=ro+u[i]
                                if i<len(u)-1:
                                    i=i+1
                                else:
                                    i=i+1
                                    break
                            if mulable[len(r)][0]==True:
                                rr[len(r)][0]=float(ro)*np.ones(int((max1-min1)*10000))
                            else:
                                rr[len(r)][1]=float(ro)*np.ones(int((max1-min1)*10000))
                        if tf==i:
                            messagebox.showerror("error","invalid function")
                            return 0    
                    if len(r)!=0:
                        messagebox.showerror("error","invalid function")
                        return 0
                    if mul[-1]=="+":
                        ss=ss+rr[0][0]
                    elif mul[-1]=="-":
                        ss=ss-rr[0][0]
                    elif mul[-1]=="*":
                        rr[0][0]=rr[0][0]*rr[0][1]
                        if mulable[0][1]=="+":
                            ss=ss+rr[0][0]
                        elif mulable[0][1]=="-":
                            ss=ss-rr[0][0]
                    elif mul[-1]=="/":
                        rr[0][0]=rr[0][0]/rr[0][1]
                        if mulable[0][1]=="+":
                            ss=ss+rr[0][0]
                        elif mulable[0][1]=="-":
                            ss=ss-rr[0][0]
                    l=Toplevel()
                    l.config(bg="white")
                    l.geometry("600x400")
                    l.iconbitmap("icon.ico")
                    figure = Figure(figsize=(5, 4), dpi=100)
                    plot = figure.add_subplot(1, 1, 1)
                    if min(ss)<=0 and max(ss)>=0:
                        plot.plot(x,np.zeros(x.shape),color="black",linestyle="--")
                    if min1<=0 and max1>=0:
                        plot.plot(np.zeros(ss.shape),ss,color="black",linestyle="--")
                    plot.plot(x,ss)
                    canvas = FigureCanvasTkAgg(figure,l)
                    canvas.get_tk_widget().pack()
                    l.resizable(width=False,height=False)
            else:
                messagebox.showerror("error","enter your function please")
        else:
            messagebox.showerror("error","max value is smaller than min value") 
    except:
        messagebox.showerror("error","enter a true max or min value")
def stady():
    u=f.get()
    x=sympy.symbols('x')
    if len(u)>0 and not u.isspace() and u[0]!="*" and u[0]!="/" and u[-1]!="*" and u[-1]!="-" and u[-1]!="/" and u[-1]!="+":
        mul=["+"]
        mul1=[]
        gold=0
        mulable=[(True,0)]
        ii=0
        iii=0
        while iii!=len(u)-1:
            if u[iii]=="(":
                gold=gold+1
            elif u[iii]==")":
                gold=gold-1
            if gold==0:
                if u[iii]=="+" or u[iii]=="-" or u[iii]=="/" or (u[iii]=="*" and u[iii+1]!="*" and u[iii-1]!="*"):
                    mul.append(u[iii])
            iii=iii+1
        i=0
        r=[] # x**() , () , sin() , sqrt() , cos() ,tan() ,fact(),**(),ln(),log(),e**()
        ss=0
        rr=[[0,0]]
        jh=[]
        while i<=len(u)-1 :
            s=i
            k=u[i]
            if len(r)!=0 and len(r)!=len(mul1):
                pl=0
                mul12=["+"]
                tyty=i
                for o in u[i:]:
                    if o==")":
                       if pl==0:
                           break
                       else:
                           pl=pl-1
                    if o=='(':
                        pl=pl+1
                    if ((o=="+" or o=="-" or o=="/" )or (o=="*" and u[tyty-1]!="*" and u[tyty+1]!="*" )) and pl==0:
                        mul12.append(o)
                    tyty=tyty+1
                mul1.append(mul12)
                jh.append(0)
            if k==" ":
                i=i+1
            elif k.lower()=="x": 
                if len(u)-1-i>=4 :
                    if u[i].lower()=="x" and u[i+1]=="*" and u[i+2]=="*" and u[i+3]=="(":
                        r.append(1)
                        rr.append([0,0])
                        mulable.append((True,0))
                        i=i+4
                    else:
                        if len(r)==0:
                            if mulable[0][0]==True:
                                rr[0][0]=x
                            else:
                                rr[0][1]=x
                        else:
                            if mulable[len(r)][0]==True:
                                rr[len(r)][0]=x
                            else:
                                rr[len(r)][1]=x
                        i=i+1
                else:
                    if len(r)==0:
                        if mulable[0][0]==True:
                            rr[0][0]=x
                        else:
                            rr[0][1]=x
                    else:
                        if mulable[len(r)][0]==True:
                            rr[len(r)][0]=x
                        else:
                            rr[len(r)][1]=x
                    i=i+1
                    
            elif k=="(":
                r.append(2)
                rr.append([0,0])
                mulable.append((True,0))
                i=i+1
               
            elif k==")":
                if mul1[-1][-1]=="+":
                    rr[len(r)-1][1]=rr[len(r)-1][1]+rr[len(r)][0]
                elif mul1[-1][-1]=="-":
                    rr[len(r)-1][1]=rr[len(r)-1][1]-rr[len(r)][0]
                elif mul1[-1][-1]=="*":
                    rr[len(r)][0]=rr[len(r)][0]*rr[len(r)][1]
                    if mulable[len(r)][1]=="+":
                        rr[len(r)-1][1]=rr[len(r)-1][1]+rr[len(r)][0]
                    elif mulable[len(r)][1]=="-":
                        rr[len(r)-1][1]=rr[len(r)-1][1]-rr[len(r)][0]
                elif mul1[-1][-1]=="/":
                    rr[len(r)][0]=rr[len(r)][0]/rr[len(r)][1]
                    if mulable[len(r)][1]=="+":
                        rr[len(r)-1][1]=rr[len(r)-1][1]+rr[len(r)][0]
                    elif mulable[len(r)][1]=="-":
                        rr[len(r)-1][1]=rr[len(r)-1][1]-rr[len(r)][0]
                g=r[-1]
                if g==1:
                    if mulable[len(r)-1][0]==True:
                        rr[len(r)-1][0]=x**(rr[len(r)-1][1])
                        print(rr[len(r)-1][0])
                        rr[len(r)-1][1]=0
                    else:
                        rr[len(r)-1][1]=x**(rr[len(r)-1][1])
                    print(ss,rr)
                elif g==2:
                    if mulable[len(r)-1][0]==True:
                        rr[len(r)-1][0]=rr[len(r)-1][1]
                        rr[len(r)-1][1]=0
                    else:
                        pass
                elif g==3:
                    if mulable[len(r)-1][0]==True:
                        rr[len(r)-1][0]=sympy.sin(rr[len(r)-1][1])
                        rr[len(r)-1][1]=0
                    else:
                        rr[len(r)-1][1]=sympy.sin(rr[len(r)-1][1])
                elif g==4:
                    if mulable[len(r)-1][0]==True:
                        rr[len(r)-1][0]=rr[len(r)-1][1]**(0.5)
                        rr[len(r)-1][1]=0
                    else:
                        rr[len(r)-1][1]=rr[len(r)-1][1]**(0.5)
                elif g==5:
                    if mulable[len(r)-1][0]==True:
                        rr[len(r)-1][0]=sympy.cos(rr[len(r)-1][1])
                        rr[len(r)-1][1]=0
                    else:
                        rr[len(r)-1][1]=sympy.cos(rr[len(r)-1][1])
                elif g==6:
                    if mulable[len(r)-1][0]==True:
                        rr[len(r)-1][0]=sympy.tan(rr[len(r)-1][1])
                        rr[len(r)-1][1]=0
                    else:
                        rr[len(r)-1][1]=sympy.tan(rr[len(r)-1][1])
                elif g==7:
                    if mulable[len(r)-1][0]==True:
                        rr[len(r)-1][0]=sympy.factorial(rr[len(r)-1][1])
                        rr[len(r)-1][1]=0
                    else:
                        rr[len(r)-1][1]=sympy.factorial(rr[len(r)-1][1])
                elif g==8:
                    if mulable[len(r)-1][0]==True:
                        rr[len(r)-1][0]=rr[len(r)-1][0]**(rr[len(r)-1][1])
                        rr[len(r)-1][1]=0
                    else:
                        rr[len(r)-1][1]=rr**(rr[len(r)-1][1])
                elif g==9:
                    if mulable[len(r)-1][0]==True:
                        rr[len(r)-1][0]=sympy.log(rr[len(r)-1][1],sympy.exp(1))
                        rr[len(r)-1][1]=0
                    else:
                        rr[len(r)-1][1]=sympy.log(rr[len(r)-1][1],sympy.exp(1))
                elif g==10:
                    if mulable[len(r)-1][0]==True:
                        rr[len(r)-1][0]=sympy.log(rr[len(r)-1][1],10)
                        rr[len(r)-1][1]=0
                    else:
                        rr[len(r)-1][1]=sympy.log(rr[len(r)-1][1],10)
                elif g==11:
                    if mulable[len(r)-1][0]==True:
                        rr[len(r)-1][0]=sympy.exp(rr[len(r)-1][1])
                        rr[len(r)-1][1]=0
                    else:
                        rr[len(r)-1][1]=sympy.exp(rr[len(r)-1][1])
                mulable.pop(-1)
                r.pop(-1)
                rr.pop(-1)
                jh.pop(-1)
                mul1.pop(-1)
                i=i+1
            elif k.isdigit():
                ro=""
                while u[i].isdigit() or u[i]=='.':
                    ro=ro+u[i]
                    if i<len(u)-1:
                        i=i+1
                    else:
                        i=i+1
                        break
                if mulable[len(r)][0]==True:
                    rr[len(r)][0]=float(ro)
                else:
                    rr[len(r)][1]=float(ro)
            
            elif k=="+" or k=="-" or k=="/" or (k=="*" and u[i+1]!="*" and u[i-1]!="*"):# "*"-->1  "+"-->2  "-"-->4  "/"-->6
                if len(r)==0:
                    if k=="-" or k=="+":
                        if mul[ii]=="+":
                            ss=ss+rr[0][0]
                            rr[0][0]=0
                        elif mul[ii]=="-":
                            ss=ss-rr[0][0]
                            rr[0][0]=0
                        else:
                            if mul[ii]=="*":
                                rr[0][0]=rr[0][0]*rr[0][1]
                            elif mul[ii]=="/":
                                rr[0][0]=rr[0][0]/rr[0][1]
                            if mulable[0][1]=="+":
                                ss=ss+rr[0][0]
                            elif mulable[0][1]=="-":
                                ss=ss-rr[0][0]
                            rr[0][0]=0
                            rr[0][1]=0
                            mulable[0]=(True,0)
                        
                            
                    else:
                        if mul[ii]=="+" or mul[ii]=="-":
                            mulable[0]=(False,mul[ii])
                        elif mul[ii]=="*":
                            rr[0][0]=rr[0][0]*rr[0][1]
                            rr[0][1]=0
                        elif mul[ii]=="/":
                            rr[0][0]=rr[0][0]/rr[0][1]
                            rr[0][1]=0
                    ii=ii+1
                else:

                    if k=="-" or k=="+":
                        if mul1[-1][jh[-1]]=="+":
                            rr[len(r)-1][1]=rr[len(r)-1][1]+rr[len(r)][0]
                            rr[len(r)][0]=0
                        elif mul1[-1][jh[-1]]=="-":
                            [len(r)-1][1]=[len(r)-1][1]-[len(r)][0]
                            rr[len(r)][0]=0
                        else:
                            if mul1[-1][jh[-1]]=="*":
                                rr[len(r)][0]=rr[len(r)][0]*rr[len(r)][1]
                            elif mul1[-1][jh[-1]]=="/":
                                rr[len(r)][0]=rr[len(r)][0]/rr[len(r)][1]
                            if mulable[len(r)][1]=="+":
                                rr[len(r)-1][1]=rr[len(r)-1][1]+rr[len(r)][0]
                            elif mulable[len(r)][1]=="-":
                                rr[len(r)-1][1]=rr[len(r)-1][1]-rr[len(r)][0]
                            rr[len(r)][0]=0
                            rr[len(r)][1]=0
                            mulable[len(r)]=(True,0)
                        
                            
                    else:
                        if mul1[-1][jh[-1]]=="+" or mul1[-1][jh[-1]]=="-":
                            mulable[len(r)]=(False,mul1[-1][jh[-1]])
                        elif mul1[-1][jh[-1]]=="*":
                            rr[len(r)][0]=rr[len(r)][0]*rr[len(r)][1]
                            rr[len(r)][1]=0
                        elif mul1[-1][jh[-1]]=="/":
                            rr[len(r)][0]=rr[len(r)][0]/rr[len(r)][1]
                            rr[len(r)][1]=0
                    jh[-1]=jh[-1]+1
                i=i+1
                
                    
            elif k.lower()=="s":
                if len(u)-1-i>=4:
                    if u[i].lower()=="s" and u[i+1].lower()=="i" and u[i+2].lower()=="n" and u[i+3]=="(":
                        r.append(3)
                        rr.append([0,0])
                        mulable.append((True,0))
                        i=i+4
                    if len(u)-1-i>=5:
                        if u[i].lower()=="s" and u[i+1].lower()=="q" and u[i+2].lower()=="r" and u[i+3].lower()=="t" and u[i+4]=="(":
                            r.append(4)
                            rr.append([0,0])
                            mulable.append((True,0))
                            i=i+5 
            elif k.lower()=="c":
                if u[i].lower()=="c" and u[i+1].lower()=="o" and u[i+2].lower()=="s" and u[i+3]=="(":
                    r.append(5)
                    rr.append([0,0])
                    mulable.append((True,0))
                    i=i+4
            elif k.lower()=="t":
                if u[i].lower()=="t" and u[i+1].lower()=="a" and u[i+2].lower()=="n" and u[i+3]=="(":
                    r.append(6)
                    rr.append([0,0])
                    mulable.append((True,0))
                    i=i+4
            elif k.lower()=="f":
                if u[i].lower()=="f" and u[i+1].lower()=="a" and u[i+2].lower()=="c" and u[i+3].lower()=="t" and u[i+4]=='(':
                    r.append(7)
                    rr.append([0,0])
                    mulable.append((True,0))
                    i=i+5
            elif k=='*' and u[i+1]=="*":
                if k=="*" and u[i+1]=="*" and u[i+2]=='(':
                    r.append(8)
                    rr.append([0,0])
                    mulable.append((True,0))
                    i=i+3
            elif k.lower()=="l":
                if len(u)-1-i>=3:
                    if u[i].lower()=="l" and u[i+1].lower()=="n" and u[i+2]=="(":
                        r.append(9)
                        rr.append([0,0])
                        mulable.append((True,0))
                        i=i+3
                    if u[i].lower()=="l" and u[i+1].lower()=="o" and u[i+2].lower()=="g" and u[i+3]=="(":
                        r.append(10)
                        rr.append([0,0])
                        mulable.append((True,0))
                        i=i+4
            elif k.lower()=="e":
                if len(u)-1-i>=4:
                    if u[i].lower()=="e" and u[i+1]=="*" and u[i+2]=="*"and u[i+3]=="(":
                        r.append(11)
                        rr.append([0,0])
                        mulable.append((True,0))
                        i=i+4
                    else:
                        if mulable[len(r)][0]==True:
                            rr[len(r)][0]=sympy.exp(1)
                        else:
                            rr[len(r)][1]=sympy.exp(1)
                        i=i+1
                else:
                    if mulable[len(r)][0]==True:
                        rr[len(r)][0]=sympy.exp(1)
                    else:
                        rr[len(r)][1]=sympy.exp(1)
                    i=i+1
            if s==i:
                messagebox.showerror("error","invalid function")
                return 0 
        if len(r)!=0:
            messagebox.showerror("error","invalid function")
            return 0
        if mul[-1]=="+":
            ss=ss+rr[0][0]
        elif mul[-1]=="-":
            ss=ss-rr[0][0]
        elif mul[-1]=="*":
            rr[0][0]=rr[0][0]*rr[0][1]
            if mulable[0][1]=="+":
                ss=ss+rr[0][0]
            elif mulable[0][1]=="-":
                ss=ss-rr[0][0]
        elif mul[-1]=="/":
            rr[0][0]=rr[0][0]/rr[0][1]
            if mulable[0][1]=="+":
                ss=ss+rr[0][0]
            elif mulable[0][1]=="-":
                ss=ss-rr[0][0]
        try:
            kk=sympy.integrate(ss)
        except:
            kk=ss*x
        messagebox.showinfo("   ","function :"+str(ss)+"\n"+"deriveé :"+str(sympy.diff(ss))+"\n"+"Intergral :"+str(kk))
    else:
        messagebox.showerror("error","enter your function please")
#open a new Tk() window
w=Tk()
#settings of the window
w.title("function study")
w.config(bg="blue")
w.geometry("700x700")
w.resizable(width=False,height=False)
w.iconbitmap("icon.ico")
#design of the software
Label(w,text="",bg="blue",bd=5).pack()
Label(w,text="Function study",bg="blue",fg="white",font=("Helvetica", "30")).pack()
Label(w,text="",bg="blue",bd=50).pack()
r=Frame(w,bg="blue")
Label(r,text="enter your function :",bg="blue",fg="white",font=("Helvetica", "25")).pack(side=LEFT)
f=Entry(r,bg="white",fg="blue",font=("Helvetica", "25"))
f.pack()
r.pack()
Label(w,text="",bg="blue",bd=5).pack()
r1=Frame(w,bg="blue")
Label(r1,text="min Value:",bg="blue",fg="white",font=("Helvetica", "25")).pack(side=LEFT)
f1=Entry(r1,bg="white",fg="blue",font=("Helvetica", "25"))
f1.pack(side=LEFT)
r2=Frame(w,bg="blue")
Label(r2,text="max Value:",bg="blue",fg="white",font=("Helvetica", "25")).pack(side=LEFT)
f2=Entry(r2,bg="white",fg="blue",font=("Helvetica", "25"))
f2.pack(side=LEFT)
r1.pack()
r2.pack()
Label(w,text="",bg="blue",bd=35).pack()
r3=Frame(w,bg="blue")
Button(r3,text="Plot the function",bg="blue",fg="white",font=("Helvetica", "25"),command=plot).pack(side=LEFT)
Button(r3,text="stady the function",bg="blue",fg="white",font=("Helvetica", "25"),command=stady).pack(side=LEFT)
r3.pack()
w.mainloop()