# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pickle 
def libdetails():
    name=input('Enter the borrower name:')
    rollno=int(input('Enter the borrower roll number:'))
    bookname=input('Enter the book name:')
    bookno=int(input('Enter the book number:'))
    author=input('Enter the author name:')
    duration=input('Enter the number of days:')
    det={'NAME':name,'ROLL NUM':rollno,'BOOK':bookname,'BOOK ID NO':bookno,'AUTHOR':author,'DURA':duration}
    lib=open('library.dat','ab')
    pickle.dump(det,lib)
    lib.close()
    
def readdetails():
    lib=open('library.dat','rb')
    while True:
        try:
            det=pickle.load(lib)
            print('NAME',det['NAME'])
            print('ROLL NUM',det['ROLL NUM'])
            print('BOOK',det['BOOK'])
            print('BOOK ID NO',det['BOOK ID NO'])
            print('AUTHOR',det['AUTHOR'])
            print('DURA',det['DURA'])
        except EOFError:
            break
        lib.close()
        
def searchname(n):
    lib=open('library.dat','rb')
    pole=False
    while True:
        try:
            det=pickle.load(lib)
            if det['NAME']==n:
                print('NAME',det['NAME'])
                print('ROLL NUM',det['ROLL NUM'])
                print('BOOK',det['BOOK'])
                print('BOOK ID NO',det['BOOK ID NO'])
                print('AUTHOR',det['AUTHOR'])
                print('DURA',det['DURA'])
                pole==True
        except EOFError:
                break
        if pole==False:
            print("THERE ARE NO DETAILS")
        lib.close()
    
def searchrollnum(r):
    lib=open('library.dat','rb')
    bat=False
    while True:
        try:
            det=pickle.load(lib)
            if det["ROLL NUM"]==r:
                print('NAME',det['NAME'])
                print('ROLL NUM',det['ROLL NUM'])
                print('BOOK',det['BOOK'])
                print('BOOK ID NO',det['BOOK ID NO'])
                print('AUTHOR',det['AUTHOR'])
                print('DURA',det['DURA'])
                bat==True
        except EOFError:
                break
        if bat==False:
            print('THERE ARE NO DETAILS')
        lib.close()
        
def deletedetails():
    lib=open('library.dat','rb')
    detailst=[]
    while True:
        try:
            det=pickle.load(lib)
            detailst.append(det)
        except EOFError:
            break
        lib.close()
        lib=open('library.dat','wb')
        for x in detailst:
            if x['ROLL NUM']==r:
                continue
            pickle.dump(x,lib)
        lib.close()
        
while True:
    print('ENTER 1 TO INSERT DETAILS')
    print('ENTER 2 TO SHOW DETAILS')
    print('ENTER 3 TO SEARCH DETAILS VIA NAME')
    print('ENTER 4 TO SEARCH DETAILS VIA ROLL NUMBER')
    print('ENTER 5 TO EXIT')
    choice=int(input('ENTER THE CHOICE YOU WANT'))
    if choice==1:
        libdetails()
    elif choice==2:
        readdetails()
    elif choice==3:
        n=(input('ENTER THE NAME YOU WANT TO SEARCH'))
        searchname(n)
    elif choice==4:
        r=int(input('ENTER THE ROLL NUM YOU WANT TO SEARCH'))
        searchrollnum(r)
    elif choice==5:
        break
    
            