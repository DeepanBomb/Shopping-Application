import tkinter as tk
from tkinter import *
import tkinter.font
import mysql.connector as mc
import mysql.connector

from tkinter import ttk
from tkinter import messagebox
import random
import time
from datetime import date

# fonts

headingFont= ("Manrope", 50)
backFont= ("Manrope", 18)
typeFont= ( "Manrope", 35)
itemFont= ( "Manrope ", 24)
buttonFont= ("Manrope",15)
priceFont= ("Manrope", 24)
aboutFont= ('Manrope ',15)

# Global

valuesoftheListe=()
valuesoftheListb=()
valuesoftheLists=()
valuesoftheListE=[]
valuesoftheListB=[]
valuesoftheListS=[]
valuesoftheList =()
shopping1=[]
shopping2=[]
shopping3=[]
c11=[]
b11=[]
a11=[]

def mainprog():

    def checkouts():

        valuesoftheList2 = valuesoftheListB+valuesoftheListE+valuesoftheListS
        valuesoftheList1 = c11 + b11 + a11
        if len(valuesoftheList1) == 0:
            mvaluesoftheList = valuesoftheList2
        else:
            mvaluesoftheList= valuesoftheList1

        file1=open("dedented_textoutput.txt","w+")

        a=[]
        b=[]
        c=[]
        L=str(mvaluesoftheList)
        y=L.split("--")
        for i  in range(len(mvaluesoftheList)):
            r=mvaluesoftheList[i]
            t=r.split("--")
            b.append(t[1])
            c.append(t[2]) 
            a.append(t[0])
            i=i+1
        print(a)
        print(b)
        print(c)


        a3=[]
        b3=[]
        c3=[]

        for i  in range(len(valuesoftheListE)):
            r=valuesoftheListE[i]
            t=r.split("--")
            b3.append([t[0],t[1]])

            
        print(a3)
        print(b3)
        print(c3)


        a1=[]
        b1=[]
        c1=[]
        a2=[]
        b2=[]
        c2=[]

        for j  in range(len(valuesoftheListB)):
            r=valuesoftheListB[j]
            t=r.split("--")
            b1.append([t[0],t[1]])

            
        print(a1)
        print(b1)
        print(c1)
        for k  in range(len(valuesoftheListS)):
            r=valuesoftheListS[k]
            t=r.split("--")
            b2.append([t[0],t[1]])

            
        print(a2)
        print(b2)
        print(c2)

        dd=[]

        conn = mc.connect(host = 'localhost', user = 'root', password = 'iamthebomb@123', database = 'deep')
        mycursor = conn.cursor()
        mycursor.execute("SELECT * FROM electronics")
        myresult = mycursor.fetchall()
        g=[]
        
        conn1 = mc.connect(host = 'localhost', user = 'root', password = 'iamthebomb@123', database = 'deep')  
        mycursor1 = conn1.cursor()
        mycursor1.execute("SELECT * FROM books")
        myresult1 = mycursor1.fetchall()
        g1=[]
        
        conn2 = mc.connect(host = 'localhost', user = 'root', password = 'iamthebomb@123', database = 'deep')
        mycursor2 = conn2.cursor()
        mycursor2.execute("SELECT * FROM sports")
        myresult2 = mycursor2.fetchall()
        g2=[]

        for x in myresult:
            g.append(list(x))
        print(g)
        for k in myresult1:
            g1.append(list(k))
        print(g1)
        for j in myresult2:
            g2.append(list(j))
        print(g2)
    
        a4=[]
        a1=[]
        a2=[]
        i=0
        for i in range(len(g)):
                a4.append([g[i][0],g[i][1]])
                a1.append([g1[i][0],g1[i][1]])
                a2.append([g2[i][0],g2[i][1]])
                i=i+1
        print(a4)
        print(a1)
        print(a2)
        electronics=[]
        sports=[]
        books=[]
        for i in range(len(a)):
            dd.append([a[i],b[i]])

            print(dd)

        try:
            kk=0   
            for ij in b3:
                        print("TRUE")
                        print(ij)
                        print(ij[kk][0])
                                                  
                        hi=int(a4[elecitem.index(ij[0])][1])                 
                        pe=int(b3[kk][1])
                        print("hi",hi)
                        print("pe",pe)
                        newquan=hi-pe
                        print("newquan",newquan)
                        print("ij of dd",dd[kk][0])
                        dditem=b3[kk][0]
                          

                        print("Inserting quantity into electronics table")
                        try:
                            connection = mysql.connector.connect(host='localhost',
                                                                    database='deep',
                                                                    user='root',
                                                                    password='iamthebomb@123')
                            cursor = connection.cursor()
                            sql_insert_quantity_query = """update electronics set Stock=%s where item=%s;"""
                            # Convert data into tuple format
                            insert_quantity_tuple = (newquan,dditem)
                            result = cursor.execute(sql_insert_quantity_query, insert_quantity_tuple)
                            connection.commit()
                            print("Order Details inserted successfully into electronics table", result)

                        except mysql.connector.Error as error:
                            print("Failed inserting data into MySQL table {}".format(error))

                        finally:
                            if connection.is_connected():
                                cursor.close()
                                connection.close()
                                print("MySQL connection is closed")
                        kk=kk+1

        except:
            print("no list")
        try:
            kk1=0
            for ij in b1:
                        print("TRUE")
                        print(ij)
                        print(ij[kk1][0])
                                                  
                        hi=int(a1[bookitem.index(ij[0])][1])         
                        pe=int(b1[kk1][1])
                        print("hi",hi)
                        print("pe",pe)
                        newquan=hi-pe
                        print("newquan",newquan)
                        print("ij of dd",dd[kk1][0])
                        dditem=b1[kk1][0]
                          

                        print("Inserting quantity into electronics table")
                        try:
                            connection = mysql.connector.connect(host='localhost',
                                                                    database='deep',
                                                                    user='root',
                                                                    password='iamthebomb@123')
                            cursor = connection.cursor()
                            sql_insert_quantity_query = """update books set Stock=%s where item=%s;"""
                            # Convert data into tuple format
                            insert_quantity_tuple = (newquan,dditem)
                            result = cursor.execute(sql_insert_quantity_query, insert_quantity_tuple)
                            connection.commit()
                            print("Order Details inserted successfully into books table", result)

                        except mysql.connector.Error as error:
                            print("Failed inserting data into MySQL table {}".format(error))

                        finally:
                            if connection.is_connected():
                                cursor.close()
                                connection.close()
                                print("MySQL connection is closed")
                        kk1=kk1+1
        except:
            print("no list")
        try:
            kk2=0
            for ij in b2:
        
                hi=int(a2[sportitem.index(ij[0])][1]) 
                pe=int(b2[kk2][1])
                print(hi)
                print(pe)
                newquan=hi-pe
                dditem=b2[kk2][0]
                  

                print("Inserting quantity into sports table")
                try:
                    connection = mysql.connector.connect(host='localhost',
                                                            database='deep',
                                                            user='root',
                                                            password='iamthebomb@123')
                    cursor = connection.cursor()
                    sql_insert_quantity_query = """update sports set Stock=%s where item=%s;"""
                    # Convert data into tuple format
                    insert_quantity_tuple = (newquan,dditem)
                    result = cursor.execute(sql_insert_quantity_query, insert_quantity_tuple)
                    connection.commit()
                    print("Order Details inserted successfully into sports table", result)
                

                except mysql.connector.Error as error:
                    print("Failed inserting data into MySQL table {}".format(error))

                finally:
                    if connection.is_connected():
                        cursor.close()
                        connection.close()
                        print("MySQL connection is closed")
                kk2=kk2+1
        except:
            print("the list is not CREATED")
       
        
        global intprice 
        intprice=[]
        for pr in c :
            intprice.append(int(pr))
        sumt= sum(intprice)
        intsum= int(sumt)
        global intqty 
        intqty=[]
        for qr in b :
            intqty.append(int(qr))
        print(intprice)
        print(intqty)   
        
        global res_list
        res_list = []
        for i in range(0, len(intprice)):
            res_list.append(intprice[i])
        print(res_list)

        global x_final
        x_final = int()
        for k in range(0,len(intprice)):
            x_final=x_final + res_list[k]       
    
        for t in a:
            file1.write("".join(str(s) for s in t) + '\n')
        file1.close()
        
        file2=open(r"dedented_quantity.txt","w+")
        for s in b:
            file2.write("".join(str(l) for l in s) + '\n')
        file2.close()
        
        file3=open(r"dedented_price.txt","w+")
        for q in c:
            file3.write("".join(str(z) for z in q) + '\n')
        file3.close()
        file3.close()
        rand=random.randint(1,99)
        with open("login credentials.txt",'r+') as file:
            username =file.read()
        curr_time = time.strftime("%H:%M", time.localtime())
        today = date.today()
        def insertorders(rand,username,today,curr_time):
            print("Inserting orders into orders table")
            try:
                connection = mysql.connector.connect(host='localhost',
                                                    database='deep',
                                                    user='root',
                                                    password='iamthebomb@123')

                cursor = connection.cursor()
                sql_insert_orders_query = """ INSERT INTO orders
                                (BillNo,username,Date,Time) VALUES (%s,%s,%s,%s)"""
                # Convert data into tuple format
                insert_orders_tuple = (rand,username,today,curr_time)
                result = cursor.execute(sql_insert_orders_query, insert_orders_tuple)
                connection.commit()
                print("Order Details inserted successfully into orders table", result)

            except mysql.connector.Error as error:
                print("Failed inserting data into MySQL table {}".format(error))

            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()
                    print("MySQL connection is closed")

        insertorders(rand,username,today,curr_time)
        def insertorders2(rand,today,curr_time,L,intsum):
            print("Inserting orders into orders table")
            try:
                connection = mysql.connector.connect(host='localhost',
                                                    database='deep',
                                                    user='root',
                                                    password='iamthebomb@123')

                cursor = connection.cursor()
                sql_insert_orders_query = """ INSERT INTO orders2
                                (BillNo,Date,Time,contents,Total) VALUES (%s,%s,%s,%s,%s)"""
                # Convert data into tuple format
                insert_orders_tuple = (rand,today,curr_time,L,intsum)
                result = cursor.execute(sql_insert_orders_query, insert_orders_tuple)
                connection.commit()
                print("Order Details inserted successfully into orders table", result)

            except mysql.connector.Error as error:
                print("Failed inserting data into MySQL table {}".format(error))

            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()
                    print("MySQL connection is closed")

        insertorders2(rand,today,curr_time,L,intsum)            
        with open("login credentials.txt",'r+') as file:
            r1 =file.read()
            #rea = Select * from users where username = r
        conn = mc.connect(host = 'localhost', user = 'root', password = 'iamthebomb@123', database = 'deep')
        mycursor = conn.cursor()
        mycursor.execute('Select * from users1')
        result = mycursor.fetchall()
        gk=[]
        credit1=[]
        for j in result:
            if j[1] == r1:
                gk.append(j)
                print(gk)
                print(gk[0][5])
                credit12 = (gk[0][5] + x_final)
                credit1.append(credit12)
                print('CREDIT',credit1)
                print('CREDIT',credit12)
                
        def updatecredit(credit12,r1):
            print("Inserting credit into users1 table")
            try:
                connection = mysql.connector.connect(host='localhost',
                                                    database='deep',
                                                    user='root',
                                                    password='iamthebomb@123')

                cursor = connection.cursor()
                sql_insert_users_query = """ UPDATE users1
                                SET Credit = %s where username = %s"""
                # Convert data into tuple format
                insert_users_tuple = (credit12,r1)
                result = cursor.execute(sql_insert_users_query, insert_users_tuple)
                connection.commit()
                print("Credit Details inserted successfully into users table", result)

            except mysql.connector.Error as error:
                print("Failed inserting data into MySQL table {}".format(error))

            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()
                    print("MySQL connection is closed")

        updatecredit(credit12,r1)  

                
        class Bill_App:
            def __init__(self, root):
                self.root = root
                self.root.geometry("1350x700+0+0")
                self.root.configure(bg="#d2ee82")
                self.root.title("Billing System")
                title = Label(self.root, text="Billing System", bd=12, relief=RIDGE, font=("Manrope Manrope", 20, "bold"), bg="#d2ee82",
                            fg="#043b5c").pack(fill=X)
            

                file2 = open("login credentials.txt",'r')
                self.c_name = file2.read()
                file2.close()
                self.bill_no=StringVar()
                global random_randint
                random_randint=random.randint(1000,9999)

                details = LabelFrame(self.root, text="Customer Details", font=("Manrope", 12,"bold"), bg="#d2ee82", fg="#043b5c",
                                    relief=GROOVE, bd=10)
                details.place(x=0, y=80, relwidth=1)
                cust_name = Label(details, text=("Username:",self.c_name), font=("Manrope ", 14,"bold"), bg="#d2ee82", fg="#043b5c").grid(
                    row=0, column=0, padx=15)

                bill_name = Label(details, text=("Bill.No:",rand), font=("Manrope ", 14,"bold"), bg="#d2ee82", fg="#043b5c").grid(row=0,
                                                                                                                    column=4,
                                                                                                                    padx=10)
            
                headingFont = ("Georgia", 20, 'italic')
                backFont = ("Manrope", 18, 'bold')
                typeFont = ("Cinzel", 35, 'bold')
                itemFont = ("Merriweather Light", 24, 'bold')
                buttonFont = ("Manrope", 15, 'italic', 'bold')
                priceFont = ("Merriweather", 18, 'italic')
                aboutFont = ('Open Sans Light', 15, 'italic')


                hygine = LabelFrame(self.root, text="Cart Items", font=("Manrope", 12,"bold"), relief=GROOVE, bd=10,
                                    bg="#d2ee82", fg="#043b5c")
                hygine.place(x=1, y=180, height=508, width=1010)

                Label(hygine, text="Item", font=priceFont, anchor='c', bg='white', fg='#333333').place(x=200, y=20)
                Label(hygine, text="Stock", font=priceFont, anchor='c', bg='white', fg='#333333').place(x=400, y=20)
                Label(hygine, text="Price", font=priceFont, anchor='c', bg='white', fg='#333333').place(x=600, y=20)
                Label(hygine, text="Cart Quantity", font=priceFont, anchor='c', bg='white', fg='#333333').place(x=800, y=20)

                frame = Frame(hygine, width=600, height=600)
                frame.pack(expand=True, fill=BOTH)  # .grid(row=0,column=0)
                canvas = Canvas(frame, bg='#ffffff', width=300, height=500, scrollregion=(0, 0, 2000, 2000))

                vbar = Scrollbar(frame, orient=VERTICAL)
                vbar.pack(side=RIGHT, fill=Y)
                vbar.config(command=canvas.yview)
                canvas.config(width=300, height=300)
                canvas.config(yscrollcommand=vbar.set)
                canvas.pack(side=LEFT, expand=True, fill=BOTH)

                canvas.create_text(420, 50, text="Checkout", fill="#333333", font=headingFont)
                
                file=open(r"dedented_textoutput.txt","r")
                x=file.read(None)           
                texty=x

                file=open(r"dedented_quantity.txt","r")
                x=file.read(None)           
                textz=x

                file=open(r"dedented_price.txt","r")
                x=file.read(None)           
                textm=x                                       
                
                canvas.create_text(200, 130, text="Item", fill="#333333", font=priceFont)
                canvas.create_text(400, 130, text="Quantity", fill="#333333", font=priceFont)
                canvas.create_text(600, 130, text="Price", fill="#333333", font=priceFont)
                canvas.create_text(200, 230, text=texty, fill="#333333", font=priceFont)
                canvas.create_text(400, 230, text=textz, fill="#333333", font=priceFont)
                canvas.create_text(600, 230, text=textm, fill="#333333", font=priceFont)
                    

                billarea = Frame(self.root, bd=10, relief=GROOVE, bg="#E5B4F3")
                billarea.place(x=1010, y=188, width=335, height=500)
                canvas1 = Canvas(billarea, bg='#ffffff', width=300, height=300, scrollregion=(0, 0, 2000, 2000))

                bill_title = Label(billarea, text="Bill Area", font=("Manrope ", 17,"bold"), bd=7, relief=GROOVE, bg="#d2ee82",
                                fg="#043b5c").pack(fill=X)              
                                            
                vbar1 = Scrollbar(billarea, orient=VERTICAL)
                vbar1.pack(side=RIGHT, fill=Y)
                vbar1.config(command=canvas1.yview)
                canvas1.config(width=335, height=500)
                canvas1.config(yscrollcommand=vbar1.set)
                canvas1.pack(side=RIGHT, expand=False, fill=BOTH)
                '''vbar2 = Scrollbar(billarea, orient=HORIZONTAL)
                vbar2.pack(side=BOTTOM, fill=X)
                vbar2.config(command=canvas1.xview)
                canvas1.config(width=335, height=500)
                canvas1.config(xscrollcommand=vbar2.set)
                canvas1.pack(side=BOTTOM, expand=False, fill=BOTH)'''

                canvas1.create_text(120,135,text=('Total Bill is Rs.',x_final), font=("Monaco", 11))
                canvas1.create_text(150,35,text="WELCOME TO \n Landline-No.739275410", font=("Monaco", 11))                                
                canvas1.create_text(105,75,text=("Customer Name : ",self.c_name), font=("Monaco", 11))
                canvas1.create_text(90,115,text=("Bill Number:",rand), font=("Monaco", 11))
                canvas1.create_text(138,95,text=("Date:",today,'Time:', curr_time), font=("Monaco", 11))
                canvas1.create_text(150,155,text="==============================", font=("Monaco", 11))
                canvas1.create_text(72,175,text="Item Name", font=("Monaco", 11))
                canvas1.create_text(210,175,text="Quantity", font=("Monaco", 11))
                canvas1.create_text(150,195,text="==============================", font=("Monaco", 11))
                canvas1.create_text(82,250,text=texty, font=("Monaco", 11))
                canvas1.create_text(220,250,text=textz, font=("Monaco", 11))

            
                self.bill_no.set(0)
                self.bill_no.set(0)
                dd.clear()
                a.clear()
                b.clear()
                c.clear()
                a11.clear()
                b11.clear()
                c11.clear()
                shopping1.clear()
                shopping2.clear()
                shopping3.clear()
                valuesoftheListB.clear()
                valuesoftheListE.clear()
                valuesoftheListS.clear()
     
        root=Tk()
        obj=Bill_App(root)
        root.mainloop()


    def electronics():
         
        
        electronics = Toplevel(COMPANY)
        electronics.title("Electronics Store")
        electronics.geometry('1366x768')
        electronics.resizable(False,False)
        electronics['bg']='#d2ee82'

#DBMS (ELECTRONICS)

        conn = mc.connect(host = 'localhost', user = 'root', password = 'iamthebomb@123', database = 'deep')
        mycursor = conn.cursor()
        mycursor.execute("SELECT * FROM electronics")
        myresult = mycursor.fetchall()
        g=[]
        for x in myresult:
            g.append(list(x))
        print(g)
        a=[]
        global elecitem
        elecitem=[]
        
        b=[]
        c=[]
        i=0
        for i in range(len(g)):
            a.append(g[i][0])
            b.append(g[i][1])
            c.append(g[i][2])
            elecitem.append(g[i][0])
            i=i+1
        print(a)
        print(b)
        print(c)

#ADD TO CART (ELECTRONICS)

        onn = mc.connect(host = 'localhost', user = 'root', password = 'iamthebomb@123', database = 'deep')
        mycursor = conn.cursor()
        mycursor.execute("SELECT * FROM electronics")
        myresult = mycursor.fetchall()
        frame=Frame(electronics,width=600,height=600)
        frame.pack(expand=True, fill=BOTH) #.grid(row=0,column=0)
        canvas=Canvas(frame,bg='#d2ee82',width=300,height=300,scrollregion=(0,0,2000,2000))
            
        vbar=Scrollbar(frame,orient=VERTICAL)
        vbar.pack(side=RIGHT,fill=Y)
        vbar.config(command=canvas.yview)
        canvas.config(width=300,height=300)
        canvas.config(yscrollcommand=vbar.set)
        canvas.pack(side=LEFT,expand=True,fill=BOTH)

        canvas.create_text(420, 50, text="Electronics", fill="#333333", font=headingFont)

        def hee(t):
            t=y.get()
            item.set(t)
            y.set("Item")

        y= StringVar(electronics)
        y.set("Item")
        options=a
        drop = OptionMenu(electronics,y,*options,command=hee)
        t=y.get()
        drop.config(bg = '#fffc7f', fg='#333333')
        drop.place(x=1090,y=580,height=35,width=100)
        
        j=0
        k=0
        canvas.create_text(200, 130, text="Item", fill="#333333", font=priceFont)
        canvas.create_text(400, 130, text="Stock", fill="#333333", font=priceFont)
        canvas.create_text(600, 130, text="Price", fill="#333333", font=priceFont)
        for j in range(len(a)):
            f=a[j]
            canvas.create_text(200, 200+k, text=f, fill="#333333", font=('Helvetica 15 bold'))
            j=j+1
            k=k+100
        t=0
        z=0
        for t in range(len(b)):
            m=b[t]
            canvas.create_text(400, 200+z, text=m, fill="#333333", font=backFont)
            t=t+1
            z=z+100
        p=0
        u=0
        for p in range(len(a)):
            n=c[p]
            canvas.create_text(600, 200+u, text=n, fill="#333333", font=('Helvetica 15 bold'))
            p=p+1
            u=u+100
            
        k=Button(electronics, text= "Back", bg= '#fffc7f',fg = '#043b5c', font= backFont, command= electronics.destroy)
        k.place(x=800,y=20,height=70,width=175)
        
        k1=Button(electronics, text= "Checkout", bg= '#fffc7f',fg = '#043b5c', font= backFont, command= checkouts)
        k1.place(x=1000,y=20,height=70,width=175)

        conn = mc.connect(host = 'localhost', user = 'root', password = 'iamthebomb@123', database = 'deep')
        mycursor = conn.cursor()
        mycursor.execute("SELECT * FROM electronics")
        myresult = mycursor.fetchall()
        global shopping1
        shopping1 = []
        def createListinListBox(shopping1):
            for elem in shopping1:
                theList.insert(END,elem[0] + "-" + str(elem[1]))

        def listIndex(shopping1, item):
            index = -1
            for i in range(len(shopping1)):
                if shopping1[i][0] == item:
                    index = i
            return index

        def addList(shopping1, item, index):
            if index == -1:
                shopping1.append([item,1])
            else:
                shopping1[index][1] += quantity.get()

        def removeList(shopping1, index):
            del(shopping1[index])
        def add():
            x=quantity.get()
            index = listIndex(shopping1, item.get())
            addList(shopping1, item.get(), index)
            if x==0:
                messagebox.showwarning('WARNINHG', 'Warning: Out of Stock!')    
            elif index >=0:
                theList.delete(index)
                x=shopping1[index][0]
                theList.insert(index,shopping1[index][0] + "--" + str(shopping1[index][1]) + "--" +str((int(shopping1[index][1]))*c[a.index(x)]))
        
            elif item.get() not in a:
                item.set(" ")
                messagebox.showerror(' Error', 'Error: Wrong input!')
            
            elif x>=b[a.index(item.get())]:
                quantity.set(1)
                messagebox.showerror(' Error', 'Error: Wrong input')
            else:
                x=shopping1[index][0]
            
                theList.insert(END,item.get() + "--" + str(quantity.get()) + "--" + str(c[a.index(x)]))
                a.append(item.get())
                print(a)
            
            global valuesoftheListE
            valuesoftheListe = (theList.get(0,END))
            valuesoftheListE= list(valuesoftheListe)
 

        def remove():
            y=theList.get(ANCHOR)
            z=y.split("--")
            
        
            
            l=int(z[1])
        
            z.remove(z[2])
            z.remove(z[1])
            
            z.append(l)
            
            shopping1.remove(z)
             
        
            valuesoftheList =  (theList.get(0,END))
            
            
            x=str(theList.get(ANCHOR))
            print(x)
            
            theList.delete(ANCHOR)

 
            for i in range(len(valuesoftheList)):
                b11.append(valuesoftheList[i])
                
            b11.remove(x)
            print(b11)
            
        theList = Listbox(electronics, selectmode=SINGLE,font= backFont)
        theList.place(x=790,y=130,height=400,width=400)

        '''for i in valuesoftheListB:
            theList.insert(END,i)'''
        for j in b11:
            theList.insert(END,j)
        createListinListBox(shopping1)

        item=StringVar(electronics)
        quantity=IntVar(electronics)
        quantity.set(1)

        Label(electronics, text="Item:", bg= '#d2ee82', fg = '#333333',font=('Helvetica 12 bold')).place(x=800,y=580)
        en1=Entry(electronics, textvariable=item).place(x=880,y=580,height=25,width=100)

        Label(electronics, text="Quantity:", bg= '#d2ee82', fg = '#333333',font=('Helvetica 12 bold')).place(x=800, y=610)
        en2=Entry(electronics, textvariable=quantity).place(x=880,y=610,height=25,width=100)

        Button(electronics, text="Add", command=add, bg = '#fffc7f', fg = '#333333').place(x=805,y=660,height=30,width=80)
        Button(electronics, text="Remove", command=remove, bg = '#fffc7f', fg = '#333333').place(x=900,y=660,height=30,width=80)

#books                    

    def books():
         
        books = Toplevel(COMPANY)
        books.title("Books Store")
        books.geometry('1366x768')
        books.resizable(False,False)
        books['bg']='#d2ee82'

# DBMS (books)

        conn = mc.connect(host = 'localhost', user = 'root', password = 'iamthebomb@123', database = 'deep')
        mycursor = conn.cursor()
        mycursor.execute("SELECT * FROM books")
        myresult = mycursor.fetchall()
        g=[]
        for x in myresult:
            g.append(list(x))
        print(g)
        global bookitem
        bookitem=[]
        a=[]
        b=[]
        c=[]
        i=0
        for i in range(len(g)):
            a.append(g[i][0])
            b.append(g[i][1])
            c.append(g[i][2])
            bookitem.append(g[i][0])
            i=i+1
        print(a)
        print(b)
        print(c)


#ADD TO CART (BOOKS)

        onn = mc.connect(host = 'localhost', user = 'root', password = 'iamthebomb@123', database = 'deep')
        mycursor = conn.cursor()
        mycursor.execute("SELECT * FROM books")
        myresult = mycursor.fetchall()
        frame=Frame(books,width=600,height=600)
        frame.pack(expand=True, fill=BOTH) #.grid(row=0,column=0)
        canvas=Canvas(frame,bg='#d2ee82',width=300,height=300,scrollregion=(0,0,2000,2000))
            
        vbar=Scrollbar(frame,orient=VERTICAL)
        vbar.pack(side=RIGHT,fill=Y)
        vbar.config(command=canvas.yview)
        canvas.config(width=300,height=300)
        canvas.config(yscrollcommand=vbar.set)
        canvas.pack(side=LEFT,expand=True,fill=BOTH)

        canvas.create_text(420, 50, text="Books", fill="#333333", font=headingFont)

        def hee(t):
            t=y.get()
            item.set(t)
            y.set("Item")

        y= StringVar(books)
        y.set("Item")
        options=a
        drop = OptionMenu(books,y,*options,command=hee)
        t=y.get()
        drop.config(bg = '#fffc7f', fg='#333333')
        drop.place(x=1090,y=580,height=35,width=100)
        
        j=0
        k=0
        canvas.create_text(200, 130, text="Item", fill="#333333", font=priceFont)
        canvas.create_text(400, 130, text="Stock", fill="#333333", font=priceFont)
        canvas.create_text(600, 130, text="Price", fill="#333333", font=priceFont)
        for j in range(len(a)):
            f=a[j]
            canvas.create_text(200, 200+k, text=f, fill="#333333", font=('Helvetica 15 bold'))
            j=j+1
            k=k+100
        t=0
        z=0
        for t in range(len(b)):
            m=b[t]
            canvas.create_text(400, 200+z, text=m, fill="#333333", font=backFont)
            t=t+1
            z=z+100
        p=0
        u=0
        for p in range(len(a)):
            n=c[p]
            canvas.create_text(600, 200+u, text=n, fill="#333333", font=('Helvetica 15 bold'))
            p=p+1
            u=u+100
            
        k=Button(books, text= "Back", bg= '#fffc7f',fg = '#043b5c', font= backFont, command= books.destroy)
        k.place(x=800,y=20,height=70,width=175)


        conn = mc.connect(host = 'localhost', user = 'root', password = 'iamthebomb@123', database = 'deep')
        mycursor = conn.cursor()
        mycursor.execute("SELECT * FROM books")
        myresult = mycursor.fetchall()
        global shopping2
        shopping2=[]
        def createListinListBox(shopping2):
            for elem in shopping2:
                theList.insert(END,elem[0] + "-" + str(elem[1]))

        def listIndex(shopping2, item):
            index = -1
            for i in range(len(shopping2)):
                if shopping2[i][0] == item:
                    index = i
            return index

        def addList(shopping2, item, index):
            if index == -1:
                shopping2.append([item,1])
            else:
                shopping2[index][1] += quantity.get()

        def removeList(shopping2, index):
            del(shopping2[index])
        def add():
            x=quantity.get()
            index = listIndex(shopping2, item.get())
            addList(shopping2, item.get(), index)
            if index >=0:
                theList.delete(index)
                x=shopping2[index][0]
                theList.insert(index,shopping2[index][0] + "--" + str(shopping2[index][1]) + "--" +str((int(shopping2[index][1]))*c[a.index(x)]))
        
            elif item.get() not in a:
                item.set(" ")
                messagebox.showerror(' Error', 'Error: Wrong input!')
            
            elif x>=b[a.index(item.get())]:
                quantity.set(1)
                messagebox.showerror(' Error', 'Error: Wrong input')
            else:
                x=shopping2[index][0]
                theList.insert(END,item.get() + "--" + str(quantity.get()) + "--" + str(c[a.index(x)]))
                a.append(item.get())
                print(a)
            
            global valuesoftheListB
            valuesoftheListb = (theList.get(0,END))
            valuesoftheListB=list(valuesoftheListb)

        def remove():
            y=theList.get(ANCHOR)
            z=y.split("--")
            
        
            
            l=int(z[1])
        
            z.remove(z[2])
            z.remove(z[1])
            
            z.append(l)
            
            shopping2.remove(z)
             
        
            valuesoftheList =  (theList.get(0,END))
            
            
            x=str(theList.get(ANCHOR))
            print(x)
            
            theList.delete(ANCHOR)

 
            for i in range(len(valuesoftheList)):
                a11.append(valuesoftheList[i])
                
            a11.remove(x)
            print(a11)
            

        theList = Listbox(books, selectmode=SINGLE,font = backFont)
        theList.place(x=790,y=130,height=400,width=400)
        '''for i in valuesoftheListE:
            theList.insert(END,i)'''
        for j in a11:
            theList.insert(END,j)
        createListinListBox(shopping2)

        item=StringVar(books)
        quantity=IntVar(books)
        quantity.set(1)

        Label(books, text="Item:", bg= '#d2ee82', fg = '#333333',font=('Helvetica 12 bold')).place(x=800,y=580)
        en1=Entry(books, textvariable=item).place(x=880,y=580,height=25,width=100)

        Label(books, text="Quantity:", bg= '#d2ee82', fg = '#333333',font=('Helvetica 12 bold')).place(x=800, y=610)
        en2=Entry(books, textvariable=quantity).place(x=880,y=610,height=25,width=100)

        Button(books, text="Add", command=add, bg = '#fffc7f', fg = '#333333').place(x=805,y=660,height=30,width=80)
        Button(books, text="Remove", command=remove, bg = '#fffc7f', fg = '#333333').place(x=900,y=660,height=30,width=80)

        k2=Button(books, text= "Checkout", bg= '#fffc7f',fg = '#043b5c', font= backFont, command= checkouts)
        k2.place(x=1000,y=20,height=70,width=175)

    def sports():
        sports = Toplevel(COMPANY)
        sports.title("Sports Store")
        sports.geometry('1366x768')
        sports.resizable(False,False)
        sports['bg']='#d2ee82'

# DBMS (SPORTS)

        conn = mc.connect(host = 'localhost', user = 'root', password = 'iamthebomb@123', database = 'deep')
        mycursor = conn.cursor()
        mycursor.execute("SELECT * FROM sports")
        myresult = mycursor.fetchall()
        g=[]
        for x in myresult:
            g.append(list(x))
        print(g)
        global sportitem
        sportitem=[]
        a=[]
        b=[]
        c=[]
        i=0
        for i in range(len(g)):
            a.append(g[i][0])
            b.append(g[i][1])
            c.append(g[i][2])
            sportitem.append(g[i][0])
            i=i+1
        print(a)
        print(b)
        print(c)


#ADD TO CART (SPORTS)

        onn = mc.connect(host = 'localhost', user = 'root', password = 'iamthebomb@123', database = 'deep')
        mycursor = conn.cursor()
        mycursor.execute("SELECT * FROM sports")
        myresult = mycursor.fetchall()

        frame=Frame(sports,width=600,height=600)
        frame.pack(expand=True, fill=BOTH) #.grid(row=0,column=0)
        canvas=Canvas(frame,bg='#d2ee82',width=300,height=300,scrollregion=(0,0,2000,2000))
            
        vbar=Scrollbar(frame,orient=VERTICAL)
        vbar.pack(side=RIGHT,fill=Y)
        vbar.config(command=canvas.yview)
        canvas.config(width=300,height=300)
        canvas.config(yscrollcommand=vbar.set)
        canvas.pack(side=LEFT,expand=True,fill=BOTH)

        canvas.create_text(420, 50, text="Sports & Fitness", fill="#333333", font=headingFont)

        def hee(t):
            t=y.get()
            item.set(t)
            y.set("Item")

        y= StringVar(sports)
        y.set("Item")
        options=a
        drop = OptionMenu(sports,y,*options,command=hee)
        t=y.get()
        drop.config(bg = '#fffc7f', fg='#333333')
        drop.place(x=1090,y=580,height=35,width=100)
        
        j=0
        k=0
        canvas.create_text(200, 130, text="Item", fill="#333333", font=priceFont)
        canvas.create_text(400, 130, text="Stock", fill="#333333", font=priceFont)
        canvas.create_text(600, 130, text="Price", fill="#333333", font=priceFont)
        for j in range(len(a)):
            f=a[j]
            canvas.create_text(200, 200+k, text=f, fill="#333333", font=('Helvetica 15 bold'))
            j=j+1
            k=k+100
        t=0
        z=0
        for t in range(len(b)):
            m=b[t]
            canvas.create_text(400, 200+z, text=m, fill="#333333", font=backFont)
            t=t+1
            z=z+100
        p=0
        u=0
        for p in range(len(a)):
            n=c[p]
            canvas.create_text(600, 200+u, text=n, fill="#333333", font=('Helvetica 15 bold'))
            p=p+1
            u=u+100
            
        k=Button(sports, text= "Back", bg= '#fffc7f',fg = '#043b5c', font= backFont, command= sports.destroy)
        k.place(x=800,y=20,height=70,width=175)


        conn = mc.connect(host = 'localhost', user = 'root', password = 'iamthebomb@123', database = 'deep')
        mycursor = conn.cursor()
        mycursor.execute("SELECT * FROM sports")
        myresult = mycursor.fetchall()
        global shopping3
        shopping3=[]
        def createListinListBox(shopping3):
            for elem in shopping3:
                theList.insert(END,elem[0] + "-" + str(elem[1]))

        def listIndex(shopping3, item):
            index = -1
            for i in range(len(shopping3)):
                if shopping3[i][0] == item:
                    index = i
            return index

        def addList(shopping3, item, index):
            if index == -1:
                shopping3.append([item,1])
            else:
                shopping3[index][1] += quantity.get()

        def removeList(shopping3, index):
            del(shopping3[index])

        def add():
            x=quantity.get()
            index = listIndex(shopping3, item.get())
            addList(shopping3, item.get(), index)
            if index >=0:
                theList.delete(index)
                x=shopping3[index][0]
                theList.insert(index,shopping3[index][0] + "--" + str(shopping3[index][1]) + "--" +str((int(shopping3[index][1]))*c[a.index(x)]))
        
            elif item.get() not in a:
                item.set(" ")
                messagebox.showerror(' Error', 'Error: Wrong input!')
            
            elif x>=b[a.index(item.get())]:
                quantity.set(1)
                messagebox.showerror(' Error', 'Error: Wrong input')
            else:
                x=shopping3[index][0]
            
                theList.insert(END,item.get() + "--" + str(quantity.get()) + "--" + str(c[a.index(x)]))
                a.append(item.get())
                print(a)

            global valuesoftheListS
            valuesoftheLists = (theList.get(0,END))   
            valuesoftheListS = list(valuesoftheLists)

        def remove():
            y=theList.get(ANCHOR)
            z=y.split("--")
            
            l=int(z[1])
        
            z.remove(z[2])
            z.remove(z[1])
            
            z.append(l)
            
            shopping3.remove(z)
        
            valuesoftheList =  (theList.get(0,END))
            
            x=str(theList.get(ANCHOR))
            print(x)
            
            theList.delete(ANCHOR)

 
            for i in range(len(valuesoftheList)):
                c11.append(valuesoftheList[i])
                
            c11.remove(x)
            print(c11)
            

        theList = Listbox(sports, selectmode=SINGLE, font = backFont)
        theList.place(x=790,y=130,height=400,width=400)
        '''for i in valuesoftheListB:
            theList.insert(END,i)'''
        for j in c11:
            theList.insert(END,j)

        createListinListBox(shopping3)

        item=StringVar(sports)
        quantity=IntVar(sports)
        quantity.set(1)

        Label(sports, text="Item:", bg= '#d2ee82', fg = '#333333',font=('Helvetica 12 bold')).place(x=800,y=580)
        en1=Entry(sports, textvariable=item).place(x=880,y=580,height=25,width=100)

        Label(sports, text="Quantity:", bg= '#d2ee82', fg = '#333333',font=('Helvetica 12 bold')).place(x=800, y=610)
        en2=Entry(sports, textvariable=quantity).place(x=880,y=610,height=25,width=100)

        Button(sports, text="Add", command=add, bg = '#fffc7f', fg = '#333333').place(x=805,y=660,height=30,width=80)
        Button(sports, text="Remove", command=remove, bg = '#fffc7f', fg = '#333333').place(x=900,y=660,height=30,width=80)

        k2=Button(sports, text= "Checkout", bg= '#fffc7f',fg = '#043b5c', font= backFont, command= checkouts)
        k2.place(x=1000,y=20,height=70,width=175)
    
#CATEGORIES

    def Categories():

        categories = Toplevel(COMPANY)
        categories.title("CATEGORIES")
        categories.geometry('860x500')
        categories.resizable(False,False)
        categories['bg']='#d2ee82'

        Label(categories, text= "QUICK CART", font=headingFont, anchor= 'c', bg= '#d2ee82', fg = '#043b5c').place(x=280,y=20)  # NAME OF COMPANY

        a = Button(categories, text="Electronics", font= buttonFont, bg='#fffc7f',fg = '#333333',relief = GROOVE, command = electronics)
        a.place(x=100,y=230,height=70,width=175)

        c = Button(categories, text="Books", font= buttonFont, bg='#fffc7f',fg = '#333333',relief = GROOVE, command = books)
        c.place(x=340,y=230,height=70,width=175)

        ctext='''Sports & Fitness'''         
        c = Button(categories, text=ctext, font= buttonFont, bg='#fffc7f',fg = '#333333',relief = GROOVE, command = sports)
        c.place(x=580,y=230,height=70,width=175)

        categoriesback=Button(categories, text= "Back", bg= '#fffc7f',fg = '#333333', font= backFont, command= categories.destroy).place(x=100,y=400)
        
# ABOUT US

    def About():
        about = Toplevel(COMPANY)
        about.title("About Us")
        about.geometry('904x679')
        about.resizable(FALSE,FALSE)
        about['bg']='#d2ee82'


        Label(about, text= "About Us", font=headingFont, anchor= 'c', bg= '#d2ee82', fg = '#043b5c').place(x=330,y=10)

        abouttext='We aim to revolutionize the customer experience by allowing them to bill their own items with a built in stock inventory which can be seamlessly updated using '

        Label(about, text=abouttext, font=aboutFont, bg='#d2ee82', fg = '#333333').place(x=145,y=230)

        aboutback=Button(about, text= "Back", bg= '#fffc7f',fg = '#043b5c', font= backFont,relief = SOLID, command= about.destroy).place(x=800,y=20)

    # Customer Service

    def Cservice():
        Cservice = Toplevel(COMPANY)
        Cservice.title("Customer Service")
        Cservice.geometry('904x679')
        Cservice.resizable(False,False)
        Cservice['bg']='#d2ee82'


        Label(Cservice, text= "Feedback", font=headingFont, anchor= 'c', bg= '#d2ee82', fg = '#043b5c').place(x=300,y=10)
        rating= [
            "Terrible   (1 ✰)",
            "Not good   (2✰ )",
            "Average   (3 ✰)",
            "Enjoyable   (4 ✰)",
            "Excellent   (5 ✰)",
            ]

        #Question
        def show3():
            Label(Cservice, text="Thank You For Submitting!", font=aboutFont, bg='#d2ee82', fg = '#043b5c').place(x=340,y=240)
            label3.config( text = choose3.get() )
        Label(Cservice, text="Did you enjoy your experience with us?", font=aboutFont, bg='#d2ee82', fg = '#333333').place(x=20,y=120)
        choose3 = StringVar(Cservice)
        choose3.set("Choose Rating")
        drop3 = OptionMenu(Cservice , choose3 , *rating)
        drop3.place(x=400,y=117)
        drop3.config(font= aboutFont,bg = '#d2ee82', fg='#333333')
        subResponse3 = Button( Cservice , text = "Submit Rating" , bg='#fffc7f', fg= '#043b5c', font= aboutFont, anchor= 'c', cursor= 'hand2',  command = show3 ).place(x=370,y=177)
        Label(Cservice, text="Rating given: ", font=aboutFont, bg='#d2ee82', fg = '#333333').place(x=260,y=290)
        label3= Label( Cservice , text = "---", font=aboutFont, bg='#d2ee82', fg = '#333333' ,padx=20)
        label3.place(x=377,y=290)
        
        Label(Cservice, text="Enter your feedback here: ", font=aboutFont, bg='#d2ee82', fg = '#333333').place(x=5,y=380)
        e1 = Entry(Cservice,width = 30, font = aboutFont)
        e1.pack()
        e1.place(x = 250, y = 385)
        def onclick():
            Label(Cservice, text="Thank You For Submitting!", font=aboutFont, bg='#d2ee82', fg = '#043b5c').place(x=340,y=500)    
            fb = e1.get()
            print(fb)

        submitbutton  = Button(Cservice, text= "Submit Feedback", bg= '#fffc7f',fg = '#043b5c', font= aboutFont, command= onclick).place(x=360,y=435)

        Cserviceback=Button(Cservice, text= "Back", bg= '#fffc7f',fg = '#043b5c', font= backFont,relief = SOLID, command= Cservice.destroy).place(x=800,y=20)


#Option Menu - Your Account

    def Profile(choice):
        if choice == "Profile":
            profile = Toplevel(COMPANY)
            profile.title("Your Profile")
            profile.geometry('904x679')
            profile.resizable(False,False)
            profile['bg']='#d2ee82'
            Label(profile, text= "YOUR PROFILE", font=typeFont, bg= '#d2ee82', fg = '#043b5c').place(x=300,y=10)
            
            with open("login credentials.txt",'r+') as file:
                r =file.read()
            #rea = Select * from users where username = r
            conn = mc.connect(host = 'localhost', user = 'root', password = 'iamthebomb@123', database = 'deep')
            mycursor = conn.cursor()
            mycursor.execute('Select * from users1')
            result = mycursor.fetchall()
            g=[]
            for j in result:
                if j[1] == r:
                    g.append(list(j))
            a=[]
            b=[]
            c=[]
            d=[]
            e=[]
            f = []
            for i in range(len(g)):
                a.append(g[i][0])
                b.append(g[i][1])
                c.append(g[i][2])
                d.append(g[i][3])
                e.append(g[i][4])
                f.append(g[i][5])
                i=i+1

            j=0
            k=0
            print("credit",f)
            Label(profile, text= "Full Name:", font=priceFont, anchor= 'c', bg= '#d2ee82', fg = '#333333').place(x=100,y=150)
            Label(profile, text= "Phone:", font=priceFont, anchor= 'c', bg= '#d2ee82', fg = '#333333').place(x=100,y=250)
            Label(profile, text= "Gender:", font=priceFont, anchor= 'c', bg= '#d2ee82', fg = '#333333').place(x=100,y=350)
            Label(profile, text= "Username:", font=priceFont, anchor= 'c', bg= '#d2ee82', fg = '#333333').place(x=500,y=150)
            Label(profile, text= "Password:", font=priceFont, anchor= 'c', bg= '#d2ee82', fg = '#333333').place(x=500,y=250)
            Label(profile, text= "Credit:", font=priceFont, anchor= 'c', bg= '#d2ee82', fg = '#333333').place(x=500,y=350)

            for j in range(len(a)):
                fv=a[j]
                Label(profile, text=fv , font=backFont, anchor= 'c', bg= '#d2ee82', fg = '#333333').place(x=100,y=(200+k))
                j=j+1
                k=k+100
            t=0
            z=0
            for t in range(len(b)):
                m=b[t]
                Label(profile, text=m , font=backFont, anchor= 'c', bg= '#d2ee82', fg = '#333333').place(x=500,y=(200+z))
                t=t+1
                z=z+100
            p=0
            u=0
            for p in range(len(c)):
                n=c[p]
                Label(profile, text=n , font=backFont, anchor= 'c', bg= '#d2ee82', fg = '#333333').place(x=500,y=(300+u))
                p=p+1
                u=u+100
            q=0
            s=0
            for q in range(len(d)):
                o=d[q]
                Label(profile, text=o , font=backFont, anchor= 'c', bg= '#d2ee82', fg = '#333333').place(x=100,y=(300+s))
                q=q+1
                s=s+100
            l=0
            h=0
            for l in range(len(e)):
                v=e[l]
                Label(profile, text=v , font=backFont, anchor= 'c', bg= '#d2ee82', fg = '#333333').place(x=100,y=(400+h))
                l=l+1
                h=h+100
            lk=0
            hk=0
            for lk in range(len(f)):
                vk=f[lk]
                Label(profile, text=vk , font=backFont, anchor= 'c', bg= '#d2ee82', fg = '#333333').place(x=500,y=(400+hk))
                lk=lk+1
                hk=hk+100    
            profileback=Button(profile, text= "Back", bg= '#fffc7f',fg = '#043b5c', font= backFont, relief = SOLID,command= profile.destroy).place(x=800,y=20)

        elif choice == "Orders":
            orders = Toplevel(COMPANY)
            orders.title("Your Orders")
            orders.geometry('904x679')
            orders.resizable(False,False)
            orders['bg']='#d2ee82'
            Label(orders, text= "YOUR ORDERS", font=typeFont, bg= '#d2ee82', fg = '#043b5c').place(x=330,y=10)
            def subentbill():
                getbill = entrybill.get()   
                order = Toplevel(COMPANY)
                order.geometry('904x679')
                order.resizable(False,False)
                order['bg']='#d2ee82'
                conn = mc.connect(host = 'localhost', user = 'root', password = 'iamthebomb@123', database = 'deep')
                mycursor = conn.cursor()
                mycursor.execute('Select * from orders2')
                result = mycursor.fetchall()
                g=[]
                for j in result:
                    if j[0] == int(getbill):
                        g.append(list(j))
                a=[]
                b=[]
                c=[]
                d=[]
                e=[]

                for i in range(len(g)):
                    a.append(g[i][0])
                    b.append(g[i][3])
                    c.append(g[i][4])
                    d.append(g[i][1])
                    e.append(g[i][2])
                    i=i+1

                j=0
                k=0
                Label(order, text= "Bill No:", font=priceFont, anchor= 'c', bg= '#d2ee82', fg = '#333333').place(x=100,y=15)
                Label(order, text= "Contents:", font=priceFont, anchor= 'c', bg= '#d2ee82', fg = '#333333').place(x=100,y=110)
                Label(order, text= "Total:", font=priceFont, anchor= 'c', bg= '#d2ee82', fg = '#333333').place(x=500,y=110)
                Label(order, text= "Date & Time:", font=priceFont, anchor= 'c', bg= '#d2ee82', fg = '#333333').place(x=500,y=15)

                for j in range(len(a)):
                    f=a[j]
                    Label(order, text=f , font=backFont, anchor= 'c', bg= '#d2ee82', fg = '#333333').place(x=100,y=(55+k))
                    j=j+1
                    k=k+10

                p=0
                u=0
                for p in range(len(c)):
                    n=c[p]
                    Label(order, text=n , font=backFont, anchor= 'c', bg= '#d2ee82', fg = '#333333').place(x=500,y=(150+u))
                    p=p+1
                    u=u+10
                q=0
                s=0

                for q in range(len(b)):
                    numb=b[q]
                    print(numb)
                    print(type(numb))
                    numbs = numb.split(",")
                    for i in range(len(numbs)):
                        joke1=numbs[i]
                        Label(order, text=joke1 , font=backFont, anchor= 'c', bg= '#d2ee82', fg = '#333333').place(x=100,y=(150+s))
                        q=q+1
                        s=s+50 

                t=0
                z=0
                for t in range(len(d)):
                    o=d[t]
                    Label(order, text=o , font=backFont, anchor= 'c', bg= '#d2ee82', fg = '#333333').place(x=500,y=(55+z))
                    t=t+1
                    z=z+100
                l=0
                h=0
                for l in range(len(e)):
                    v=e[l]
                    Label(order, text=v , font=backFont, anchor= 'c', bg= '#d2ee82', fg = '#333333').place(x=650,y=(55+h))
                    l=l+1
                    h=h+100                  

            with open("login credentials.txt",'r+') as file:
                username =file.read()        
            conn = mc.connect(host = 'localhost', user = 'root', password = 'iamthebomb@123', database = 'deep')
            mycursor = conn.cursor()
            mycursor.execute('Select * from orders')
            result = mycursor.fetchall()
            g1=[]
            for jk in result:
                if jk[1] == username:
                    g1.append(list(jk))
            billno=[]
            y1= IntVar(orders, value = 0 ,name = 'Bill No:')
            y1.set(0)
            for i in range(len(g1)):
                billno.append(g1[i][0])
            entrybill = Entry(orders,font = backFont, textvariable = y1)
            entrybill.place(x=350,y=300)
            Label(orders, text= 'Select your Bill No. for detailed order details: ', font=priceFont, anchor= 'c', bg= '#d2ee82', fg = '#333333').place(x=100,y=250)
            def hee(t1):
                t1=y1.get()
                y1.set(t1)

            options1=billno
            drop5 = OptionMenu(orders,y1,*options1,command=hee)
            drop5.config(bg = '#fffc7f', fg='#333333')
            drop5.place(x=750,y=255)
            subentbillb = Button(orders,text = 'Submit', bg= '#fffc7f',fg = '#043b5c', font= backFont, relief = SOLID,command= subentbill).place(x=400,y=350)
     
            with open("login credentials.txt",'r+') as file:
                username =file.read()
            
            Label(orders, text= "Username:", font=priceFont, anchor= 'c', bg= '#d2ee82', fg = '#333333').place(x=100,y=150)
            Label(orders, text= username, font=priceFont, anchor= 'c', bg= '#d2ee82', fg = '#333333').place(x=270,y=150)
            ordersback=Button(orders, text= "Back", bg= '#fffc7f',fg = '#043b5c', font= backFont,relief = SOLID, command= orders.destroy).place(x=800,y=20)

        elif choice == "Sign Out":
            COMPANY.destroy()
            
    # HOME PAGE MAIN PROG

    COMPANY = Tk('Placewindow.center')
    COMPANY.geometry('860x500')
    COMPANY.title("Welcome to Quick Cart")
    COMPANY['bg']= '#d2ee82'
    COMPANY.resizable(FALSE,FALSE)

    CATEGORY = Button(COMPANY, text="Categories", font= buttonFont, bg='#d2ee82',fg = '#043b5c',relief = FLAT, command = Categories)
    CATEGORY.place(x=50,y=10)

    ABOUT = Button(COMPANY, text="About us", font= buttonFont, bg='#d2ee82',fg = '#043b5c',relief = FLAT, command = About)
    ABOUT.place(x=235,y=10)

    SERVICE= Button(COMPANY, text="Customer Service", font= buttonFont, bg='#d2ee82',fg = '#043b5c',relief = FLAT, command = Cservice)
    SERVICE.place(x=390,y=10)

    menu= StringVar(COMPANY)
    menu.set("Your Account")

    options = ["Profile", "Orders", "Sign Out"]
    choice = menu.get()

    drop = OptionMenu(COMPANY,menu, *options, command = Profile)
    drop.place(x=645,y =10)
    drop.config(font= buttonFont,bg = '#d2ee82', fg='#043b5c')


    Label(COMPANY, text= "QUICK CART", font=headingFont, anchor= 'c', bg= '#d2ee82', fg = '#043b5c').place(x=240,y=240)

root = tk.Tk()
connection = mysql.connector.connect(host='localhost', user='root', 
                                     password='iamthebomb@123', database='deep')
c = connection.cursor()

w = 450
h = 525
bgcolor = "#2d545e"

# CENTER FORM 
root.overrideredirect(1)
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws-w)/2
y = (hs-h)/2
root.geometry("%dx%d+%d+%d" % (w, h, x, y))

# HEADER

headerframe = tk.Frame(root, highlightbackgroun='white', highlightcolor='white', 
                       highlightthickness=2, bg='#d2ee82', width=w, height=70)

title_label = tk.Label(headerframe, text='SIGN IN', padx=20, pady=5, bg='#d2ee82', 
                       fg='#000000', font=('Manrope',24), width=8).place(y = 28,relx =0.5, anchor = CENTER)
close_button = tk.Button(headerframe, text='X', borderwidth=1, relief='solid', 
                         font=('Manrope',12))

headerframe.pack()
close_button.pack()

close_button.place(x=410, y=10)

# close window
def close_win():
    root.withdraw()
    root.destroy()

close_button['command'] = close_win

#END HEADER

mainframe = tk.Frame(root, width=w, height=h)

# login Page
loginframe = tk.Frame(mainframe, width=w, height=h)
login_contentframe = tk.Frame(loginframe, padx=30, pady=100, 
                     highlightbackgroun='white', highlightcolor='white', 
                     highlightthickness=2, bg='#000000')

username_label = tk.Label(login_contentframe, text='Username:', 
                          font=('Manrope',16), bg='#000000',fg = 'white')
password_label = tk.Label(login_contentframe, text='Password:', 
                          font=('Manrope',16), bg='#000000',fg = 'white')

username_entry = tk.Entry(login_contentframe, font=('Manrope',16))
password_entry = tk.Entry(login_contentframe, font=('Manrope',16), show='*')

login_button = tk.Button(login_contentframe,text="Login", font=('Manrope',16), 
                         bg='#000000',fg='#d2ee82', padx=25, pady=10, width=25)

go_register_label = tk.Label(login_contentframe, 
                    text=">> Don't have an account? Create one" , 
                    font=('Manrope',10), bg='#000000', fg='#d2ee82')

mainframe.pack(fill='both', expand=1)
loginframe.pack(fill='both', expand=1)
login_contentframe.pack(fill='both', expand=1)

username_label.grid(row=0, column=0, pady=10)
username_entry.grid(row=0, column=1)

password_label.grid(row=1, column=0, pady=10)
password_entry.grid(row=1, column=1)

login_button.grid(row=2, column=0, columnspan=2, pady=40)

go_register_label.grid(row=3, column=0, columnspan=2, pady=20)


def go_to_register():
    loginframe.forget()
    registerframe.pack(fill="both", expand=1)

go_register_label.bind("<Button-1>", lambda page: go_to_register())


def login():
    username = username_entry.get().strip()
    password = password_entry.get().strip()
    vals = (username, password,)
    select_query = "SELECT * FROM `users1` WHERE `username` = %s and `password` = %s"
    c.execute(select_query, vals)
    user = c.fetchone()
    if user is not None:
        with open("login credentials.txt",'w+') as file:
            file.write(username)
        username_entry.delete(0, END)
        password_entry.delete(0,END)
        mainprog()

    else:
        messagebox.showwarning('Error','wrong username or password')

login_button['command'] = login


#Register

registerframe = tk.Frame(mainframe, width=w, height=h)
register_contentframe = tk.Frame(registerframe, padx=15, pady=15, 
                        highlightbackgroun='white', highlightcolor='white', 
                        highlightthickness=2, bg='#000000')

fullname_label_rg = tk.Label(register_contentframe, text='Fullname:', 
                             font=('Manrope',14), bg='#000000',fg = 'white')
username_label_rg = tk.Label(register_contentframe, text='Username:', 
                             font=('Manrope',14), bg='#000000',fg = 'white')
password_label_rg = tk.Label(register_contentframe, text='Password:', 
                             font=('Manrope',14), bg='#000000',fg = 'white')
confirmpass_label_rg = tk.Label(register_contentframe, text='Re-Password:', 
                                font=('Manrope',14), bg='#000000',fg = 'white')
phone_label_rg = tk.Label(register_contentframe, text='Phone:', 
                          font=('Manrope',14), bg='#000000',fg = 'white')
gender_label_rg = tk.Label(register_contentframe, text='Gender:', 
                           font=('Manrope',14), bg='#000000',fg = 'white')


fullname_entry_rg = tk.Entry(register_contentframe, font=('Manrope',14), width=22)
username_entry_rg = tk.Entry(register_contentframe, font=('Manrope',14), width=22)
password_entry_rg = tk.Entry(register_contentframe, font=('Manrope',14), width=22, 
                             show='*')
confirmpass_entry_rg = tk.Entry(register_contentframe, font=('Manrope',14), width=22, 
                                show='*')
phone_entry_rg = tk.Entry(register_contentframe, font=('Manrope',14), width=22)

radiosframe = tk.Frame(register_contentframe)
gender = StringVar(register_contentframe)

male_radiobutton = tk.Radiobutton(radiosframe, text='Male', font=('Manrope',14), 
                                  bg='#000000', fg = 'white',variable=gender, value='Male')
female_radiobutton = tk.Radiobutton(radiosframe, text='Female', font=('Manrope',14), 
                                    bg='#000000', fg = 'white',variable=gender, value='Female')

selectimage_frame = tk.Frame(register_contentframe, bg=bgcolor)
selectimage_button = tk.Button(selectimage_frame, text='select image', bg='#fff')


register_button = tk.Button(register_contentframe,text="Register", font=('Manrope',16)
                            , bg='#000000',fg='#fffc7f', padx=25, pady=10, width=25)

go_login_label = tk.Label(register_contentframe, 
                          text=">> Already have an account? Sign In" , 
                          font=('Manrope',10), bg='#000000', fg='#d2ee82')

register_contentframe.pack(fill='both', expand=1)

fullname_label_rg.grid(row=0, column=0, pady=5, sticky='e')
fullname_entry_rg.grid(row=0, column=1)

username_label_rg.grid(row=1, column=0, pady=5, sticky='e')
username_entry_rg.grid(row=1, column=1)

password_label_rg.grid(row=2, column=0, pady=5, sticky='e')
password_entry_rg.grid(row=2, column=1)

confirmpass_label_rg.grid(row=3, column=0, pady=5, sticky='e')
confirmpass_entry_rg.grid(row=3, column=1)

phone_label_rg.grid(row=4, column=0, pady=5, sticky='e')
phone_entry_rg.grid(row=4, column=1)

gender_label_rg.grid(row=5, column=0, pady=5, sticky='e')
radiosframe.grid(row=5, column=1)
male_radiobutton.grid(row=0, column=0)
female_radiobutton.grid(row=0, column=1)

register_button.grid(row=7, column=0, columnspan=2, pady=20)

go_login_label.grid(row=8, column=0, columnspan=2, pady=10)


def go_to_login():
    registerframe.forget()
    loginframe.pack(fill="both", expand=1)

go_login_label.bind("<Button-1>", lambda page: go_to_login())


def check_username(username):
    username = username_entry_rg.get().strip()
    vals = (username,)
    select_query = "SELECT * FROM `users1` WHERE `username` = %s"
    c.execute(select_query, vals)
    user = c.fetchone()
    if user is not None:
        return True
    else:
        return False

def register():

    fullname = fullname_entry_rg.get().strip() 
    username = username_entry_rg.get().strip()
    password = password_entry_rg.get().strip()
    confirm_password = confirmpass_entry_rg.get().strip()
    phone = phone_entry_rg.get().strip()
    gdr = gender.get()
    
    
    if len(fullname) > 0 and  len(username) > 0 and len(password) > 0 and len(phone) > 0:
        if check_username(username) == False: 
            if password == confirm_password:
                vals = (fullname, username, password, phone, gdr)
                insert_query = "INSERT INTO `users1`(`fullname`, `username`, `password`, `phone`, `gender`) VALUES (%s,%s,%s,%s,%s)"
                c.execute(insert_query, vals)
                connection.commit()
                messagebox.showinfo('Register','your account has been created successfully')
            else:
                messagebox.showwarning('Password','incorrect password confirmation')
        else:
            messagebox.showwarning('Duplicate Username','This Username Already Exists try another one')
    else:
        messagebox.showwarning('Empty Fields','make sure to enter all the information')

register_button['command'] = register


root.mainloop()
