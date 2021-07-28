from PyQt5.QtCore import *
# from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# from PyQt5 import QtCore
import sys
# import win32print
import pymysql
import datetime
from datetime import date

import os
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem
import subprocess
from Main import Ui_MainWindow as Main_Window




Name_List=[]
Phone_List=[]
Address_List=[]

class MainApp(QMainWindow , Main_Window):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_puttons()
        self.db = pymysql.connect(host='localhost', user='root', password='', db='db')
        self.cur = self.db.cursor()
        self.Meals()
        self.Category()
        self.Category_Button_1()
        self.Order_Num()
        self.Name_Complete()
        self.Phone_Complete()
        self.Address_Complete()
        self.Meals_price()
        self.show_employee()
        self.desabl_All()





    def Auto_Complete1(self,model):
        model.setStringList(Name_List)

    def Auto_Complete2(self,model):
        model.setStringList(Phone_List)

    def Auto_Complete3(self,model):
        model.setStringList(Address_List)





    def Name_Complete(self ):
        self.cur.execute("SELECT Customer_Name FROM customers")
        names = self.cur.fetchall()
        for name in names:
            Name_List.append(name[0])

        name_line_edit = self.lineEdit_12
        completer = QCompleter()
        name_line_edit.setCompleter(completer)
        model = QStringListModel()
        completer.setModel(model)
        self.Auto_Complete1(model)

    def Phone_Complete(self):
        self.cur.execute("SELECT Customer_Phone FROM customers")
        phones = self.cur.fetchall()
        for phone in phones :
            Phone_List.append(phone[0])

        phone_line_edit = self.lineEdit_10
        completer = QCompleter()
        phone_line_edit.setCompleter(completer)
        model = QStringListModel()
        completer.setModel(model)
        self.Auto_Complete2(model)

    def Address_Complete(self):
        self.cur.execute("SELECT Customer_Address FROM customers")
        adresss = self.cur.fetchall()
        for adress in adresss :
            Address_List.append(adress[0])

        address_line_edit = self.lineEdit_11
        completer = QCompleter()
        address_line_edit.setCompleter(completer)
        model = QStringListModel()
        completer.setModel(model)
        self.Auto_Complete3(model)







    def Handel_puttons(self):
        self.pushButton_26.clicked.connect(self.Button_26)
        self.pushButton_27.clicked.connect(self.Button_27)
        self.pushButton_28.clicked.connect(self.Button_28)
        self.pushButton_29.clicked.connect(self.Button_29)
        self.pushButton_30.clicked.connect(self.Button_30)
        self.pushButton_31.clicked.connect(self.Button_31)
        self.pushButton_32.clicked.connect(self.Button_32)
        self.pushButton_33.clicked.connect(self.Button_33)
        self.pushButton_34.clicked.connect(self.Button_34)
        self.pushButton_35.clicked.connect(self.Button_35)
        self.pushButton_36.clicked.connect(self.Button_36)
        self.pushButton_37.clicked.connect(self.Button_37)
        self.pushButton_38.clicked.connect(self.Button_38)
        self.pushButton_39.clicked.connect(self.Button_39)
        self.pushButton_40.clicked.connect(self.Button_40)
        self.pushButton_41.clicked.connect(self.Button_41)
        self.pushButton_42.clicked.connect(self.Button_42)
        self.pushButton_43.clicked.connect(self.Button_43)
        self.pushButton_44.clicked.connect(self.Button_44)
        self.pushButton_45.clicked.connect(self.Button_45)
        self.pushButton_46.clicked.connect(self.Button_46)
        self.pushButton_47.clicked.connect(self.Button_47)
        self.pushButton_48.clicked.connect(self.Button_48)
        self.pushButton_49.clicked.connect(self.Button_49)
        self.pushButton_50.clicked.connect(self.Button_50)
        self.pushButton_51.clicked.connect(self.Button_51)
        self.pushButton_52.clicked.connect(self.Button_52)
        self.pushButton_53.clicked.connect(self.Button_53)
        self.pushButton_54.clicked.connect(self.Button_54)
        self.pushButton_55.clicked.connect(self.Button_55)
        self.pushButton_117.clicked.connect(self.Button_117)
        self.pushButton_20.clicked.connect(self.Equal)

        self.pushButton_18.clicked.connect(self.Num_0)
        self.pushButton_9.clicked.connect(self.Num_1)
        self.pushButton_10.clicked.connect(self.Num_2)
        self.pushButton_11.clicked.connect(self.Num_3)
        self.pushButton_12.clicked.connect(self.Num_4)
        self.pushButton_13.clicked.connect(self.Num_5)
        self.pushButton_14.clicked.connect(self.Num_6)
        self.pushButton_17.clicked.connect(self.Num_7)
        self.pushButton_15.clicked.connect(self.Num_8)
        self.pushButton_16.clicked.connect(self.Num_9)
        self.pushButton_5.clicked.connect(self.Clear_All)
        self.pushButton_4.clicked.connect(self.remove)
        self.pushButton_57.clicked.connect(self.Add_Meal)
        self.pushButton_115.clicked.connect(self.Add_Category)
        self.pushButton_21.clicked.connect(self.Category_Button_1)
        self.pushButton_22.clicked.connect(self.Category_Button_2)
        self.pushButton_23.clicked.connect(self.Category_Button_3)
        self.pushButton_24.clicked.connect(self.Category_Button_4)
        self.pushButton_25.clicked.connect(self.Category_Button_5)
        self.pushButton_2.clicked.connect(self.Add_Customer)
        self.pushButton_116.clicked.connect(self.Find_Customer)
        self.pushButton_6.clicked.connect(self.Delete_Customer)
        self.pushButton_3.clicked.connect(self.Update_Customer)
        self.pushButton_181.clicked.connect(self.Add_Meal_Price)
        self.pushButton_182.clicked.connect(self.Delivery)
        self.pushButton_183.clicked.connect(self.report)
        self.pushButton_185.clicked.connect(self.report_invoice)
        self.pushButton_189.clicked.connect(self.permisions)
        self.pushButton_188.clicked.connect(self.add_employee)
        self.pushButton_186.clicked.connect(self.edit_employee)
        self.pushButton_187.clicked.connect(self.save_edit_employee)
        self.pushButton_191.clicked.connect(self.delete_employee)
        self.pushButton_56.clicked.connect(self.login)
        self.pushButton.clicked.connect(self.logout)
        self.pushButton_8.clicked.connect(self.receipt_Button)
        self.pushButton_7.clicked.connect(self.receipt_Kitchen_prev)
        self.pushButton_193.clicked.connect(self.report_invoice_adv)
        self.pushButton_194.clicked.connect(self.receipt_packup)
        self.pushButton_195.clicked.connect(self.receipt_Kitchen_Packup)



    def desabl_All(self):
        self.tabWidget.setTabEnabled(1,False)
        self.tabWidget.setTabEnabled(2,False)
        self.tabWidget.setTabEnabled(3,False)
        self.tabWidget.setTabEnabled(4,False)
        self.tabWidget.setTabEnabled(5,False)

    def login(self):
        user = self.lineEdit_2.text()
        password = self.lineEdit_3.text()
        self.cur.execute(" SELECT Employee_Name , Password1 FROM employees WHERE Employee_Name = %s", (user))
        data = self.cur.fetchone()
        try:
            if user == data[0] and password == data[1]:
                self.tabWidget.setTabEnabled(1, True)
                self.tabWidget.setTabEnabled(2, True)
                self.tabWidget.setTabEnabled(3, True)
                self.tabWidget.setTabEnabled(4, True)
                self.tabWidget.setTabEnabled(5, True)
                self.cur.execute(" SELECT * FROM permisions WHERE Employee_Name =%s", (user))
                per=self.cur.fetchone()
                if per[1] == 1:
                    self.groupBox_13.setEnabled(True)
                if per[2] == 1:
                    self.groupBox_14.setEnabled(True)
                if per[3] == 1:
                    self.groupBox_11.setEnabled(True)
                if per[4] == 1:
                    self.groupBox_10.setEnabled(True)
                if per[5] == 1:
                    self.groupBox_12.setEnabled(True)
                if per[6] == 1:
                    self.groupBox_15.setEnabled(True)
                if per[7] == 1:
                    self.groupBox_16.setEnabled(True)
                if per[8] == 1:
                    self.groupBox_18.setEnabled(True)
                self.lineEdit_2.setText("")
                self.lineEdit_3.setText("")

                self.tabWidget.setCurrentIndex(1)
                self.tabWidget.setTabEnabled(0, False)

        except:
            return

    def logout(self):
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.setTabEnabled(1,False)
        self.tabWidget.setTabEnabled(2,False)
        self.tabWidget.setTabEnabled(3,False)
        self.tabWidget.setTabEnabled(4,False)
        self.tabWidget.setTabEnabled(5,False)

        self.groupBox_13.setEnabled(False)
        self.groupBox_14.setEnabled(False)
        self.groupBox_11.setEnabled(False)
        self.groupBox_10.setEnabled(False)
        self.groupBox_12.setEnabled(False)
        self.groupBox_15.setEnabled(False)
        self.groupBox_16.setEnabled(False)
        self.groupBox_18.setEnabled(False)
        self.tabWidget.setTabEnabled(0, True)

    def Add_Customer(self):
        phone=self.lineEdit_10.text()
        name=self.lineEdit_12.text()
        address=self.lineEdit_11.text()
        try:
            sql =("INSERT INTO customers (Customer_Name,Customer_Address,Customer_Phone) VALUES (%s, %s ,%s)")
            val = (name , address , phone)
            self.cur.execute(sql,val)
            self.db.commit()
        except:
            return
        Name_List.clear()
        Phone_List.clear()
        Address_List.clear()
        self.Name_Complete()
        self.Phone_Complete()
        self.Address_Complete()


    def Find_Customer(self):
        phone=self.lineEdit_10.text()
        name=self.lineEdit_12.text()
        address=self.lineEdit_11.text()

        try:
            if phone != "":
                sql=("SELECT Customer_Name,Customer_Address FROM customers WHERE Customer_Phone = %s")
                self.cur.execute(sql,phone)
                val = self.cur.fetchall()
                self.lineEdit_12.setText(val[0][0])
                self.lineEdit_11.setText(val[0][1])

            elif name != "" :
                sql = "SELECT Customer_Phone,Customer_Address FROM customers WHERE Customer_Name = %s"
                self.cur.execute(sql,name)
                val = self.cur.fetchall()
                self.lineEdit_10.setText(val[0][0])
                self.lineEdit_11.setText(val[0][1])

            elif address != "" :
                sql = "SELECT Customer_Name,Customer_Phone FROM customers WHERE Customer_Address = %s"
                self.cur.execute(sql,address)
                val = self.cur.fetchall()
                self.lineEdit_12.setText(val[0][0])
                self.lineEdit_10.setText(val[0][1])

            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("")
                msg.setInformativeText(' Not Found')
                msg.setWindowTitle("Not Found")
                msg.exec_()
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("")
            msg.setInformativeText(' Not Found')
            msg.setWindowTitle("Not Found")
            msg.exec_()


    def Delete_Customer(self):
        phone=self.lineEdit_10.text()
        name=self.lineEdit_12.text()
        address=self.lineEdit_11.text()
        sql = "DELETE FROM customers WHERE Customer_Name = %s OR Customer_Phone= %s OR Customer_Address = %s"
        self.cur.execute(sql,(name,phone,address))
        self.db.commit()
        Name_List.clear()
        Phone_List.clear()
        Address_List.clear()

        self.Name_Complete()
        self.Phone_Complete()
        self.Address_Complete()


    def Update_Customer(self):
        phone=self.lineEdit_10.text()
        name=self.lineEdit_12.text()
        address=self.lineEdit_11.text()

        sql = "UPDATE customers SET Customer_Name = %s , Customer_Address = %s , Customer_Phone = %s   WHERE Customer_Name = %s OR Customer_Address = %s OR Customer_Phone = %s"
        self.cur.execute(sql , (name,address,phone,name,address,phone))
        self.db.commit()
        Name_List.clear()
        Phone_List.clear()
        Address_List.clear()

        self.Name_Complete()
        self.Phone_Complete()
        self.Address_Complete()

    def Num_0(self):
        Button_18 = self.label.setNum(0)

    def Num_1(self):
        Button_9 = self.label.setNum(1)

    def Num_2(self):
        Button_10 = self.label.setNum(2)

    def Num_3(self):
        Button_11 = self.label.setNum(3)

    def Num_4(self):
        Button_12 = self.label.setNum(4)

    def Num_5(self):
        Button_13 = self.label.setNum(5)

    def Num_6(self):
        Button_14 = self.label.setNum(6)

    def Num_7(self):
        Button_17 = self.label.setNum(7)

    def Num_8(self):
        Button_15 = self.label.setNum(8)

    def Num_9(self):
        Button_16 = self.label.setNum(9)

    def Button_26(self):
        self.cur.execute(''' SELECT Meal_Price FROM meals WHERE Meal_ID = 1 ''')
        data = self.cur.fetchone()
        y=(int(data[0]))
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)
        self.tableWidget.setItem(row_position, 0, QTableWidgetItem(str( self.pushButton_26.text())))
        self.tableWidget.setItem(row_position, 1, QTableWidgetItem(str(y)))
        self.tableWidget.setItem(row_position, 2, QTableWidgetItem(self.label.text()))
        self.tableWidget.setItem(row_position, 3, QTableWidgetItem(""))
        self.tableWidget.setItem(row_position, 4, QTableWidgetItem(""))
        self.Quantaty()
        self.label.setNum(1)
        self.Price()

    def Button_33(self):
        self.cur.execute(''' SELECT Meal_Price FROM meals WHERE Meal_ID = 2 ''')
        data = self.cur.fetchone()
        y=(int(data[0]))
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)
        self.tableWidget.setItem(row_position, 0, QTableWidgetItem(str( self.pushButton_33.text())))
        self.tableWidget.setItem(row_position, 1, QTableWidgetItem(str(y)))
        self.tableWidget.setItem(row_position, 2, QTableWidgetItem(self.label.text()))
        self.tableWidget.setItem(row_position, 3, QTableWidgetItem(""))
        self.tableWidget.setItem(row_position, 4, QTableWidgetItem(""))
        self.Quantaty()
        self.label.setNum(1)
        self.Price()

    def Button_36(self):
        self.cur.execute(''' SELECT Meal_Price FROM meals WHERE Meal_ID = 3 ''')
        data = self.cur.fetchone()
        y=(int(data[0]))
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)
        self.tableWidget.setItem(row_position, 0, QTableWidgetItem(str( self.pushButton_36.text())))
        self.tableWidget.setItem(row_position, 1, QTableWidgetItem(str(y)))
        self.tableWidget.setItem(row_position, 2, QTableWidgetItem(self.label.text()))
        self.tableWidget.setItem(row_position, 3, QTableWidgetItem(""))
        self.tableWidget.setItem(row_position, 4, QTableWidgetItem(""))
        self.Quantaty()
        self.label.setNum(1)
        self.Price()

    def Button_42(self):
        self.cur.execute(''' SELECT Meal_Price FROM meals WHERE Meal_ID = 4 ''')
        data = self.cur.fetchone()
        y=(int(data[0]))
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)
        self.tableWidget.setItem(row_position, 0, QTableWidgetItem(str( self.pushButton_42.text())))
        self.tableWidget.setItem(row_position, 1, QTableWidgetItem(str(y)))
        self.tableWidget.setItem(row_position, 2, QTableWidgetItem(self.label.text()))
        self.tableWidget.setItem(row_position, 3, QTableWidgetItem(""))
        self.tableWidget.setItem(row_position, 4, QTableWidgetItem(""))
        self.Quantaty()
        self.label.setNum(1)
        self.Price()

    def Button_46(self):
        self.cur.execute(''' SELECT Meal_Price FROM meals WHERE Meal_ID = 5 ''')
        data = self.cur.fetchone()
        y=(int(data[0]))
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)
        self.tableWidget.setItem(row_position, 0, QTableWidgetItem(str( self.pushButton_46.text())))
        self.tableWidget.setItem(row_position, 1, QTableWidgetItem(str(y)))
        self.tableWidget.setItem(row_position, 2, QTableWidgetItem(self.label.text()))
        self.tableWidget.setItem(row_position, 3, QTableWidgetItem(""))
        self.tableWidget.setItem(row_position, 4, QTableWidgetItem(""))
        self.Quantaty()
        self.label.setNum(1)
        self.Price()

    def Button_53(self):
        self.cur.execute(''' SELECT Meal_Price FROM meals WHERE Meal_ID = 6 ''')
        data = self.cur.fetchone()
        y=(int(data[0]))
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)
        self.tableWidget.setItem(row_position, 0, QTableWidgetItem(str( self.pushButton_53.text())))
        self.tableWidget.setItem(row_position, 1, QTableWidgetItem(str(y)))
        self.tableWidget.setItem(row_position, 2, QTableWidgetItem(self.label.text()))
        self.tableWidget.setItem(row_position, 3, QTableWidgetItem(""))
        self.tableWidget.setItem(row_position, 4, QTableWidgetItem(""))
        self.Quantaty()
        self.label.setNum(1)
        self.Price()

    def Button_27(self):
        self.cur.execute(''' SELECT Meal_Price FROM meals WHERE Meal_ID = 7 ''')
        data = self.cur.fetchone()
        y=(int(data[0]))
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)
        self.tableWidget.setItem(row_position, 0, QTableWidgetItem(str( self.pushButton_27.text())))
        self.tableWidget.setItem(row_position, 1, QTableWidgetItem(str(y)))
        self.tableWidget.setItem(row_position, 2, QTableWidgetItem(self.label.text()))
        self.tableWidget.setItem(row_position, 3, QTableWidgetItem(""))
        self.tableWidget.setItem(row_position, 4, QTableWidgetItem(""))
        self.Quantaty()
        self.label.setNum(1)
        self.Price()

    def Button_32(self):
        self.cur.execute(''' SELECT Meal_Price FROM meals WHERE Meal_ID = 8 ''')
        data = self.cur.fetchone()
        y=(int(data[0]))
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)
        self.tableWidget.setItem(row_position, 0, QTableWidgetItem(str( self.pushButton_32.text())))
        self.tableWidget.setItem(row_position, 1, QTableWidgetItem(str(y)))
        self.tableWidget.setItem(row_position, 2, QTableWidgetItem(self.label.text()))
        self.tableWidget.setItem(row_position, 3, QTableWidgetItem(""))
        self.tableWidget.setItem(row_position, 4, QTableWidgetItem(""))
        self.Quantaty()
        self.label.setNum(1)
        self.Price()

    def Button_37(self):
        self.cur.execute(''' SELECT Meal_Price FROM meals WHERE Meal_ID = 9 ''')
        data = self.cur.fetchone()
        y=(int(data[0]))
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)
        self.tableWidget.setItem(row_position, 0, QTableWidgetItem(str( self.pushButton_37.text())))
        self.tableWidget.setItem(row_position, 1, QTableWidgetItem(str(y)))
        self.tableWidget.setItem(row_position, 2, QTableWidgetItem(self.label.text()))
        self.tableWidget.setItem(row_position, 3, QTableWidgetItem(""))
        self.tableWidget.setItem(row_position, 4, QTableWidgetItem(""))
        self.Quantaty()
        self.label.setNum(1)
        self.Price()

    def Button_44(self):
        self.cur.execute(''' SELECT Meal_Price FROM meals WHERE Meal_ID = 10 ''')
        data = self.cur.fetchone()
        y=(int(data[0]))
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)
        self.tableWidget.setItem(row_position, 0, QTableWidgetItem(str( self.pushButton_44.text())))
        self.tableWidget.setItem(row_position, 1, QTableWidgetItem(str(y)))
        self.tableWidget.setItem(row_position, 2, QTableWidgetItem(self.label.text()))
        self.tableWidget.setItem(row_position, 3, QTableWidgetItem(""))
        self.tableWidget.setItem(row_position, 4, QTableWidgetItem(""))
        self.Quantaty()
        self.label.setNum(1)
        self.Price()

    def Button_48(self):
        self.cur.execute(''' SELECT Meal_Price FROM meals WHERE Meal_ID = 11 ''')
        data = self.cur.fetchone()
        y=(int(data[0]))
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)
        self.tableWidget.setItem(row_position, 0, QTableWidgetItem(str( self.pushButton_48.text())))
        self.tableWidget.setItem(row_position, 1, QTableWidgetItem(str(y)))
        self.tableWidget.setItem(row_position, 2, QTableWidgetItem(self.label.text()))
        self.tableWidget.setItem(row_position, 3, QTableWidgetItem(""))
        self.tableWidget.setItem(row_position, 4, QTableWidgetItem(""))
        self.Quantaty()
        self.label.setNum(1)
        self.Price()

    def Button_55(self):
        self.cur.execute(''' SELECT Meal_Price FROM meals WHERE Meal_ID = 12 ''')
        data = self.cur.fetchone()
        y=(int(data[0]))
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)
        self.tableWidget.setItem(row_position, 0, QTableWidgetItem(str( self.pushButton_55.text())))
        self.tableWidget.setItem(row_position, 1, QTableWidgetItem(str(y)))
        self.tableWidget.setItem(row_position, 2, QTableWidgetItem(self.label.text()))
        self.tableWidget.setItem(row_position, 3, QTableWidgetItem(""))
        self.tableWidget.setItem(row_position, 4, QTableWidgetItem(""))
        self.Quantaty()
        self.label.setNum(1)
        self.Price()

    def Button_28(self):
        self.cur.execute(''' SELECT Meal_Price FROM meals WHERE Meal_ID = 13 ''')
        data = self.cur.fetchone()
        y=(int(data[0]))
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)
        self.tableWidget.setItem(row_position, 0, QTableWidgetItem(str( self.pushButton_28.text())))
        self.tableWidget.setItem(row_position, 1, QTableWidgetItem(str(y)))
        self.tableWidget.setItem(row_position, 2, QTableWidgetItem(self.label.text()))
        self.tableWidget.setItem(row_position, 3, QTableWidgetItem(""))
        self.tableWidget.setItem(row_position, 4, QTableWidgetItem(""))
        self.Quantaty()
        self.label.setNum(1)
        self.Price()

    def Button_35(self):
        self.cur.execute(''' SELECT Meal_Price FROM meals WHERE Meal_ID = 14 ''')
        data = self.cur.fetchone()
        y=(int(data[0]))
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)
        self.tableWidget.setItem(row_position, 0, QTableWidgetItem(str( self.pushButton_35.text())))
        self.tableWidget.setItem(row_position, 1, QTableWidgetItem(str(y)))
        self.tableWidget.setItem(row_position, 2, QTableWidgetItem(self.label.text()))
        self.tableWidget.setItem(row_position, 3, QTableWidgetItem(""))
        self.tableWidget.setItem(row_position, 4, QTableWidgetItem(""))
        self.Quantaty()
        self.label.setNum(1)
        self.Price()

    def Button_38(self):
        self.cur.execute(''' SELECT Meal_Price FROM meals WHERE Meal_ID = 15 ''')
        data = self.cur.fetchone()
        y=(int(data[0]))
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)
        self.tableWidget.setItem(row_position, 0, QTableWidgetItem(str( self.pushButton_38.text())))
        self.tableWidget.setItem(row_position, 1, QTableWidgetItem(str(y)))
        self.tableWidget.setItem(row_position, 2, QTableWidgetItem(self.label.text()))
        self.tableWidget.setItem(row_position, 3, QTableWidgetItem(""))
        self.tableWidget.setItem(row_position, 4, QTableWidgetItem(""))
        self.Quantaty()
        self.label.setNum(1)
        self.Price()


    def Button_41(self):
        self.cur.execute(''' SELECT Meal_Price FROM meals WHERE Meal_ID = 16 ''')
        data = self.cur.fetchone()
        y=(int(data[0]))
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)
        self.tableWidget.setItem(row_position, 0, QTableWidgetItem(str( self.pushButton_41.text())))
        self.tableWidget.setItem(row_position, 1, QTableWidgetItem(str(y)))
        self.tableWidget.setItem(row_position, 2, QTableWidgetItem(self.label.text()))
        self.tableWidget.setItem(row_position, 3, QTableWidgetItem(""))
        self.tableWidget.setItem(row_position, 4, QTableWidgetItem(""))
        self.Quantaty()
        self.label.setNum(1)
        self.Price()

    def Button_50(self):
        self.cur.execute(''' SELECT Meal_Price FROM meals WHERE Meal_ID = 17 ''')
        data = self.cur.fetchone()
        y=(int(data[0]))
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)
        self.tableWidget.setItem(row_position, 0, QTableWidgetItem(str( self.pushButton_50.text())))
        self.tableWidget.setItem(row_position, 1, QTableWidgetItem(str(y)))
        self.tableWidget.setItem(row_position, 2, QTableWidgetItem(self.label.text()))
        self.tableWidget.setItem(row_position, 3, QTableWidgetItem(""))
        self.tableWidget.setItem(row_position, 4, QTableWidgetItem(""))
        self.Quantaty()
        self.label.setNum(1)
        self.Price()

    def Button_51(self):
        self.cur.execute(''' SELECT Meal_Price FROM meals WHERE Meal_ID = 18 ''')
        data = self.cur.fetchone()
        y=(int(data[0]))
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)
        self.tableWidget.setItem(row_position, 0, QTableWidgetItem(str( self.pushButton_51.text())))
        self.tableWidget.setItem(row_position, 1, QTableWidgetItem(str(y)))
        self.tableWidget.setItem(row_position, 2, QTableWidgetItem(self.label.text()))
        self.tableWidget.setItem(row_position, 3, QTableWidgetItem(""))
        self.tableWidget.setItem(row_position, 4, QTableWidgetItem(""))
        self.Quantaty()
        self.label.setNum(1)
        self.Price()


    def Button_29(self):
        self.cur.execute(''' SELECT Meal_Price FROM meals WHERE Meal_ID = 19 ''')
        data = self.cur.fetchone()
        y=(int(data[0]))
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)
        self.tableWidget.setItem(row_position, 0, QTableWidgetItem(str( self.pushButton_29.text())))
        self.tableWidget.setItem(row_position, 1, QTableWidgetItem(str(y)))
        self.tableWidget.setItem(row_position, 2, QTableWidgetItem(self.label.text()))
        self.tableWidget.setItem(row_position, 3, QTableWidgetItem(""))
        self.tableWidget.setItem(row_position, 4, QTableWidgetItem(""))
        self.Quantaty()
        self.label.setNum(1)
        self.Price()


    def Button_34(self):
        self.cur.execute(''' SELECT Meal_Price FROM meals WHERE Meal_ID = 20 ''')
        data = self.cur.fetchone()
        y=(int(data[0]))
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)
        self.tableWidget.setItem(row_position, 0, QTableWidgetItem(str( self.pushButton_34.text())))
        self.tableWidget.setItem(row_position, 1, QTableWidgetItem(str(y)))
        self.tableWidget.setItem(row_position, 2, QTableWidgetItem(self.label.text()))
        self.tableWidget.setItem(row_position, 3, QTableWidgetItem(""))
        self.tableWidget.setItem(row_position, 4, QTableWidgetItem(""))
        self.Quantaty()
        self.label.setNum(1)
        self.Price()


    def Button_40(self):
        self.cur.execute(''' SELECT Meal_Price FROM meals WHERE Meal_ID = 21 ''')
        data = self.cur.fetchone()
        y=(int(data[0]))
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)
        self.tableWidget.setItem(row_position, 0, QTableWidgetItem(str( self.pushButton_40.text())))
        self.tableWidget.setItem(row_position, 1, QTableWidgetItem(str(y)))
        self.tableWidget.setItem(row_position, 2, QTableWidgetItem(self.label.text()))
        self.tableWidget.setItem(row_position, 3, QTableWidgetItem(""))
        self.tableWidget.setItem(row_position, 4, QTableWidgetItem(""))
        self.Quantaty()
        self.label.setNum(1)
        self.Price()

    def Button_43(self):
        self.cur.execute(''' SELECT Meal_Price FROM meals WHERE Meal_ID = 22 ''')
        data = self.cur.fetchone()
        y=(int(data[0]))
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)
        self.tableWidget.setItem(row_position, 0, QTableWidgetItem(str( self.pushButton_43.text())))
        self.tableWidget.setItem(row_position, 1, QTableWidgetItem(str(y)))
        self.tableWidget.setItem(row_position, 2, QTableWidgetItem(self.label.text()))
        self.tableWidget.setItem(row_position, 3, QTableWidgetItem(""))
        self.tableWidget.setItem(row_position, 4, QTableWidgetItem(""))
        self.Quantaty()
        self.label.setNum(1)
        self.Price()

    def Button_49(self):
        self.cur.execute(''' SELECT Meal_Price FROM meals WHERE Meal_ID = 23 ''')
        data = self.cur.fetchone()
        y=(int(data[0]))
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)
        self.tableWidget.setItem(row_position, 0, QTableWidgetItem(str( self.pushButton_49.text())))
        self.tableWidget.setItem(row_position, 1, QTableWidgetItem(str(y)))
        self.tableWidget.setItem(row_position, 2, QTableWidgetItem(self.label.text()))
        self.tableWidget.setItem(row_position, 3, QTableWidgetItem(""))
        self.tableWidget.setItem(row_position, 4, QTableWidgetItem(""))
        self.Quantaty()
        self.label.setNum(1)
        self.Price()

    def Button_54(self):
        self.cur.execute(''' SELECT Meal_Price FROM meals WHERE Meal_ID = 24 ''')
        data = self.cur.fetchone()
        y=(int(data[0]))
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)
        self.tableWidget.setItem(row_position, 0, QTableWidgetItem(str( self.pushButton_54.text())))
        self.tableWidget.setItem(row_position, 1, QTableWidgetItem(str(y)))
        self.tableWidget.setItem(row_position, 2, QTableWidgetItem(self.label.text()))
        self.tableWidget.setItem(row_position, 3, QTableWidgetItem(""))
        self.tableWidget.setItem(row_position, 4, QTableWidgetItem(""))
        self.Quantaty()
        self.label.setNum(1)
        self.Price()

    def Button_30(self):
        self.cur.execute(''' SELECT Meal_Price FROM meals WHERE Meal_ID = 25 ''')
        data = self.cur.fetchone()
        y=(int(data[0]))
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)
        self.tableWidget.setItem(row_position, 0, QTableWidgetItem(str( self.pushButton_30.text())))
        self.tableWidget.setItem(row_position, 1, QTableWidgetItem(str(y)))
        self.tableWidget.setItem(row_position, 2, QTableWidgetItem(self.label.text()))
        self.tableWidget.setItem(row_position, 3, QTableWidgetItem(""))
        self.tableWidget.setItem(row_position, 4, QTableWidgetItem(""))
        self.Quantaty()
        self.label.setNum(1)
        self.Price()

    def Button_31(self):
        self.cur.execute(''' SELECT Meal_Price FROM meals WHERE Meal_ID = 26 ''')
        data = self.cur.fetchone()
        y=(int(data[0]))
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)
        self.tableWidget.setItem(row_position, 0, QTableWidgetItem(str( self.pushButton_31.text())))
        self.tableWidget.setItem(row_position, 1, QTableWidgetItem(str(y)))
        self.tableWidget.setItem(row_position, 2, QTableWidgetItem(self.label.text()))
        self.tableWidget.setItem(row_position, 3, QTableWidgetItem(""))
        self.tableWidget.setItem(row_position, 4, QTableWidgetItem(""))
        self.Quantaty()
        self.label.setNum(1)
        self.Price()


    def Button_39(self):
        self.cur.execute(''' SELECT Meal_Price FROM meals WHERE Meal_ID = 27 ''')
        data = self.cur.fetchone()
        y=(int(data[0]))
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)
        self.tableWidget.setItem(row_position, 0, QTableWidgetItem(str( self.pushButton_39.text())))
        self.tableWidget.setItem(row_position, 1, QTableWidgetItem(str(y)))
        self.tableWidget.setItem(row_position, 2, QTableWidgetItem(self.label.text()))
        self.tableWidget.setItem(row_position, 3, QTableWidgetItem(""))
        self.tableWidget.setItem(row_position, 4, QTableWidgetItem(""))
        self.Quantaty()
        self.label.setNum(1)
        self.Price()

    def Button_45(self):
        self.cur.execute(''' SELECT Meal_Price FROM meals WHERE Meal_ID = 28 ''')
        data = self.cur.fetchone()
        y=(int(data[0]))
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)
        self.tableWidget.setItem(row_position, 0, QTableWidgetItem(str( self.pushButton_45.text())))
        self.tableWidget.setItem(row_position, 1, QTableWidgetItem(str(y)))
        self.tableWidget.setItem(row_position, 2, QTableWidgetItem(self.label.text()))
        self.tableWidget.setItem(row_position, 3, QTableWidgetItem(""))
        self.tableWidget.setItem(row_position, 4, QTableWidgetItem(""))
        self.Quantaty()
        self.label.setNum(1)
        self.Price()

    def Button_47(self):
        self.cur.execute(''' SELECT Meal_Price FROM meals WHERE Meal_ID = 29 ''')
        data = self.cur.fetchone()
        y=(int(data[0]))
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)
        self.tableWidget.setItem(row_position, 0, QTableWidgetItem(str( self.pushButton_47.text())))
        self.tableWidget.setItem(row_position, 1, QTableWidgetItem(str(y)))
        self.tableWidget.setItem(row_position, 2, QTableWidgetItem(self.label.text()))
        self.tableWidget.setItem(row_position, 3, QTableWidgetItem(""))
        self.tableWidget.setItem(row_position, 4, QTableWidgetItem(""))
        self.Quantaty()
        self.label.setNum(1)
        self.Price()

    def Button_52(self):
        self.cur.execute(''' SELECT Meal_Price FROM meals WHERE Meal_ID = 30 ''')
        data = self.cur.fetchone()
        y=(int(data[0]))
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)
        self.tableWidget.setItem(row_position, 0, QTableWidgetItem(str( self.pushButton_52.text())))
        self.tableWidget.setItem(row_position, 1, QTableWidgetItem(str(y)))
        self.tableWidget.setItem(row_position, 2, QTableWidgetItem(self.label.text()))
        self.tableWidget.setItem(row_position, 3, QTableWidgetItem(""))
        self.tableWidget.setItem(row_position, 4, QTableWidgetItem(""))
        self.Quantaty()
        self.label.setNum(1)
        self.Price()

    def Button_117(self):
        self.cur.execute(''' SELECT Delivery FROM meals WHERE Meal_ID = 1 ''')
        data = self.cur.fetchone()
        y=(int(data[0]))
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)
        self.tableWidget.setItem(row_position, 0, QTableWidgetItem(str("Delivery")))
        self.tableWidget.setItem(row_position, 1, QTableWidgetItem(str(y)))
        self.tableWidget.setItem(row_position, 2, QTableWidgetItem("1"))
        self.tableWidget.setItem(row_position, 3, QTableWidgetItem(str(y)))
        self.tableWidget.setItem(row_position, 4, QTableWidgetItem(" "))
        self.Price()

    def Equal(self):
        if self.tableWidget.rowCount() == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Error")
            msg.setInformativeText("No Data")
            msg.setWindowTitle("Data Error")
            msg.exec_()
        else:
            x = self.label_6.text()
            y = self.lineEdit.text()
            if y != "" :
                z = int(y) - int(x)
                if z < 0:
                    self.label_2.setNum(z)
                    buttonReply = QMessageBox.question(self, 'PyQt5 message', "Check What you Wrote or Paid !! Do you want to continuo",
                                                       QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
                                                       QMessageBox.Cancel)
                    # print(int(buttonReply))
                    if buttonReply == QMessageBox.Yes:
                        self.Save_Data()
                        self.Clear_All()
                        self.label_2.setNum(0)

                    if buttonReply == QMessageBox.No:
                        return
                    if buttonReply == QMessageBox.Cancel:
                        return
                elif z==0:
                    self.label_2.setNum(z)
                    self.Save_Data()
                    self.Clear_All()
                    self.label_2.setNum(0)
                else:
                    self.label_2.setNum(z)
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Give him")
                    msg.setInformativeText(str(z))
                    msg.setWindowTitle("Remaining amount")
                    msg.exec_()
                    self.Save_Data()
            else:
                z=0
                self.label_2.setNum(z)
                buttonReply = QMessageBox.question(self, 'PyQt5 message', "Do you want to Continuo?",
                                                   QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
                                                   QMessageBox.Cancel)
                # print(int(buttonReply))
                if buttonReply == QMessageBox.Yes:
                    self.Save_Data()
                    self.Clear_All()
                    self.label_2.setNum(0)
                if buttonReply == QMessageBox.No:
                    return
                if buttonReply == QMessageBox.Cancel:
                    return
            self.receipt()
            self.receipt_Kitchen()
        self.Clear_All()
        self.Order_Num()

#######################################################################################################################
###################################### Get data from Qtable Widget ####################################################

    def Quantaty(self):
        nrows = self.tableWidget.rowCount()
        z=0

        for row in range(0, nrows):
            item = self.tableWidget.item(row, 2)
            item_text = item.text()
           # item_text += item
            y=(int(item_text))
            z= z + y
        self.label_5.setNum(z)

    def Price(self):
        nrows = self.tableWidget.rowCount()
        p_a=0
        for row in range(0, nrows):
            item = self.tableWidget.item(row, 2)
            item_text = item.text()
            x = (int(item_text))

            for row in range(0, nrows):
                item = self.tableWidget.item(row, 1)
                item_text = item.text()
                y=(int(item_text))
                z= y *x
            item = self.tableWidget.item(row, 3)
            item_text = item.setText(str(z))

        for row in range(0, nrows):
            item = self.tableWidget.item(row, 3)
            item_text = item.text()
            o=(int(item_text))
            p_a= p_a + o
        self.label_6.setNum(p_a)

    def Clear_All(self):
        nrows = self.tableWidget.rowCount()
        self.lineEdit.setText("")
        try:
            while nrows > 0:

                for row in range(0, nrows):
                    item = self.tableWidget.item(0, 0)
                    item_text = item.text()
                    self.tableWidget.removeRow(row)
        except:
            self.statusBar().showMessage('لا يوجد معلومات للحذف')
        self.Price()
        self.Quantaty()
        self.lineEdit_10.setText("")
        self.lineEdit_12.setText("")
        self.lineEdit_11.setText("")
        self.label_2.setText("")

    def remove(self):
            self.tableWidget.removeRow(self.tableWidget.currentRow())
            self.Price()



    def Category_Button_1(self):
        self.groupBox_6.hide()
        self.groupBox_7.hide()
        self.groupBox_8.hide()
        self.groupBox_9.hide()
        self.groupBox_3.show()
    def Category_Button_2(self):
        self.groupBox_3.hide()
        self.groupBox_7.hide()
        self.groupBox_8.hide()
        self.groupBox_9.hide()
        self.groupBox_6.show()
    def Category_Button_3(self):
        self.groupBox_6.hide()
        self.groupBox_3.hide()
        self.groupBox_8.hide()
        self.groupBox_9.hide()
        self.groupBox_7.show()
    def Category_Button_4(self):
        self.groupBox_6.hide()
        self.groupBox_7.hide()
        self.groupBox_3.hide()
        self.groupBox_9.hide()
        self.groupBox_8.show()
    def Category_Button_5(self):
        self.groupBox_6.hide()
        self.groupBox_7.hide()
        self.groupBox_8.hide()
        self.groupBox_3.hide()
        self.groupBox_9.show()

    def Category(self):
        for x in range(1,6):
            sql = "SELECT Category_Name FROM category WHERE Category_ID = %s "
            self.cur.execute(sql,x)
            myresult = self.cur.fetchone()

            if x==1:
                self.pushButton_21.setText(myresult[0])
            if x==2:
                self.pushButton_22.setText(myresult[0])
            if x==3:
                self.pushButton_23.setText(myresult[0])
            if x==4:
                self.pushButton_24.setText(myresult[0])
            if x==5:
                self.pushButton_25.setText(myresult[0])

        self.cur.execute(''' SELECT category_name FROM category ''')
        data = self.cur.fetchall()
        for category in data:
            self.comboBox_3.addItem(category[0])
            self.comboBox_4.addItem(category[0])
            self.comboBox_5.addItem(category[0])


    def Meals(self):
        self.comboBox.clear()
        y=self.comboBox_4.currentIndex()
        if y == 1:
            for x in range(1, 31):
                sql = ''' SELECT Meal_Name FROM meals WHERE Meal_ID = %s '''
                self.cur.execute(sql , x)
                data = self.cur.fetchall()
                for meal in data:
                    self.comboBox.addItem(meal[0])
        if y == 2:
            for x in range(150, 180):
                sql = ''' SELECT Meal_Name FROM meals WHERE Meal_ID = %s '''
                self.cur.execute(sql , x)
                data = self.cur.fetchall()
                for meal in data:
                    self.comboBox.addItem(meal[0])
        if y == 3:
            for x in range(180, 210):
                sql = ''' SELECT Meal_Name FROM meals WHERE Meal_ID = %s '''
                self.cur.execute(sql , x)
                data = self.cur.fetchall()
                for meal in data:
                    self.comboBox.addItem(meal[0])
        if y == 4:
            for x in range(210,240):
                sql = ''' SELECT Meal_Name FROM meals WHERE Meal_ID = %s '''
                self.cur.execute(sql , x)
                data = self.cur.fetchall()
                for meal in data:
                    self.comboBox.addItem(meal[0])
        if y == 5:
            for x in range(240, 270):
                sql = ''' SELECT Meal_Name FROM meals WHERE Meal_ID = %s '''
                self.cur.execute(sql , x)
                data = self.cur.fetchall()
                for meal in data:
                    self.comboBox.addItem(meal[0])


        self.comboBox_4.currentIndexChanged[str].connect(self.Meals)



        for x in range(1,31):
            sql = "SELECT Meal_Name FROM meals WHERE Meal_ID = %s "
            self.cur.execute(sql,x)
            myresult = self.cur.fetchone()

            if x==1 :
                self.pushButton_26.setText(myresult[0])
            if x==2 :
                self.pushButton_33.setText(myresult[0])
            if x==3 :
                self.pushButton_36.setText(myresult[0])
            if x==4 :
                self.pushButton_42.setText(myresult[0])
            if x==5 :
                self.pushButton_46.setText(myresult[0])
            if x==6 :
                self.pushButton_53.setText(myresult[0])
            if x==7 :
                self.pushButton_27.setText(myresult[0])
            if x==8 :
                self.pushButton_32.setText(myresult[0])
            if x==9 :
                self.pushButton_37.setText(myresult[0])
            if x==10 :
                self.pushButton_44.setText(myresult[0])
            if x==11:
                self.pushButton_48.setText(myresult[0])
            if x==12 :
                self.pushButton_55.setText(myresult[0])
            if x==13 :
                self.pushButton_28.setText(myresult[0])
            if x==14 :
                self.pushButton_35.setText(myresult[0])
            if x==15 :
                self.pushButton_38.setText(myresult[0])
            if x==16 :
                self.pushButton_41.setText(myresult[0])
            if x==17 :
                self.pushButton_50.setText(myresult[0])
            if x==18 :
                self.pushButton_51.setText(myresult[0])
            if x==19 :
                self.pushButton_29.setText(myresult[0])
            if x==20 :
                self.pushButton_34.setText(myresult[0])
            if x==21 :
                self.pushButton_40.setText(myresult[0])
            if x==22 :
                self.pushButton_43.setText(myresult[0])
            if x==23 :
                self.pushButton_49.setText(myresult[0])
            if x==24 :
                self.pushButton_54.setText(myresult[0])
            if x==25 :
                self.pushButton_30.setText(myresult[0])
            if x==26 :
                self.pushButton_31.setText(myresult[0])
            if x==27 :
                self.pushButton_39.setText(myresult[0])
            if x==28 :
                self.pushButton_45.setText(myresult[0])
            if x==29 :
                self.pushButton_47.setText(myresult[0])
            if x==30 :
                self.pushButton_52.setText(myresult[0])
        for x in range(150, 270):
            sql = "SELECT Meal_Name FROM meals WHERE Meal_ID = %s "
            self.cur.execute(sql, x)
            myresult = self.cur.fetchone()
            if x==150 :
                self.pushButton_58.setText(myresult[0])
            if x==151 :
                self.pushButton_65.setText(myresult[0])
            if x==152 :
                self.pushButton_68.setText(myresult[0])
            if x==153 :
                self.pushButton_74.setText(myresult[0])
            if x==154 :
                self.pushButton_78.setText(myresult[0])
            if x==155 :
                self.pushButton_85.setText(myresult[0])
            if x==156 :
                self.pushButton_59.setText(myresult[0])
            if x==157 :
                self.pushButton_64.setText(myresult[0])
            if x==158 :
                self.pushButton_69.setText(myresult[0])
            if x==159 :
                self.pushButton_76.setText(myresult[0])
            if x==160 :
                self.pushButton_80.setText(myresult[0])
            if x==161 :
                self.pushButton_87.setText(myresult[0])
            if x==162 :
                self.pushButton_60.setText(myresult[0])
            if x==163 :
                self.pushButton_67.setText(myresult[0])
            if x==164 :
                self.pushButton_70.setText(myresult[0])
            if x==165 :
                self.pushButton_73.setText(myresult[0])
            if x==166 :
                self.pushButton_82.setText(myresult[0])
            if x==167 :
                self.pushButton_83.setText(myresult[0])
            if x==168 :
                self.pushButton_61.setText(myresult[0])
            if x==169 :
                self.pushButton_66.setText(myresult[0])
            if x==170 :
                self.pushButton_72.setText(myresult[0])
            if x==171 :
                self.pushButton_75.setText(myresult[0])
            if x==172 :
                self.pushButton_81.setText(myresult[0])
            if x==173:
                self.pushButton_86.setText(myresult[0])
            if x==174:
                self.pushButton_62.setText(myresult[0])
            if x==175:
                self.pushButton_63.setText(myresult[0])
            if x==176:
                self.pushButton_71.setText(myresult[0])
            if x==177:
                self.pushButton_77.setText(myresult[0])
            if x==178:
                self.pushButton_79.setText(myresult[0])
            if x==179:
                self.pushButton_84.setText(myresult[0])
            if x==180:
                self.pushButton_88.setText(myresult[0])
            if x==181:
                self.pushButton_95.setText(myresult[0])
            if x==182:
                self.pushButton_98.setText(myresult[0])
            if x==183:
                self.pushButton_104.setText(myresult[0])
            if x==184:
                self.pushButton_108.setText(myresult[0])
            if x==185:
                self.pushButton_118.setText(myresult[0])
            if x==186:
                self.pushButton_89.setText(myresult[0])
            if x==187:
                self.pushButton_94.setText(myresult[0])
            if x==188:
                self.pushButton_99.setText(myresult[0])
            if x==189:
                self.pushButton_106.setText(myresult[0])
            if x==190:
                self.pushButton_110.setText(myresult[0])
            if x==191:
                self.pushButton_120.setText(myresult[0])
            if x==192:
                self.pushButton_90.setText(myresult[0])
            if x==193:
                self.pushButton_97.setText(myresult[0])
            if x==194:
                self.pushButton_100.setText(myresult[0])
            if x==195:
                self.pushButton_103.setText(myresult[0])
            if x==196:
                self.pushButton_112.setText(myresult[0])
            if x==197:
                self.pushButton_113.setText(myresult[0])
            if x==198:
                self.pushButton_91.setText(myresult[0])
            if x==199:
                self.pushButton_96.setText(myresult[0])
            if x==200:
                self.pushButton_102.setText(myresult[0])
            if x==201:
                self.pushButton_105.setText(myresult[0])
            if x==202:
                self.pushButton_111.setText(myresult[0])
            if x==203:
                self.pushButton_119.setText(myresult[0])
            if x==204:
                self.pushButton_92.setText(myresult[0])
            if x==205:
                self.pushButton_93.setText(myresult[0])
            if x==206:
                self.pushButton_101.setText(myresult[0])
            if x==207:
                self.pushButton_107.setText(myresult[0])
            if x==208:
                self.pushButton_109.setText(myresult[0])
            if x==209:
                self.pushButton_114.setText(myresult[0])
            if x==210:
                self.pushButton_121.setText(myresult[0])
            if x==211:
                self.pushButton_128.setText(myresult[0])
            if x==212:
                self.pushButton_131.setText(myresult[0])
            if x==213:
                self.pushButton_137.setText(myresult[0])
            if x==214:
                self.pushButton_141.setText(myresult[0])
            if x==215:
                self.pushButton_148.setText(myresult[0])
            if x==216:
                self.pushButton_122.setText(myresult[0])
            if x==217:
                self.pushButton_127.setText(myresult[0])
            if x==218:
                self.pushButton_132.setText(myresult[0])
            if x==219:
                self.pushButton_139.setText(myresult[0])
            if x==220:
                self.pushButton_143.setText(myresult[0])
            if x==221:
                self.pushButton_150.setText(myresult[0])
            if x==222:
                self.pushButton_123.setText(myresult[0])
            if x==223:
                self.pushButton_130.setText(myresult[0])
            if x==224:
                self.pushButton_133.setText(myresult[0])
            if x==225:
                self.pushButton_136.setText(myresult[0])
            if x==226:
                self.pushButton_145.setText(myresult[0])
            if x==227:
                self.pushButton_146.setText(myresult[0])
            if x==228:
                self.pushButton_124.setText(myresult[0])
            if x==229:
                self.pushButton_129.setText(myresult[0])
            if x==230:
                self.pushButton_135.setText(myresult[0])
            if x==231:
                self.pushButton_138.setText(myresult[0])
            if x==232:
                self.pushButton_144.setText(myresult[0])
            if x==233:
                self.pushButton_149.setText(myresult[0])
            if x==234:
                self.pushButton_125.setText(myresult[0])
            if x==235:
                self.pushButton_126.setText(myresult[0])
            if x==236:
                self.pushButton_134.setText(myresult[0])
            if x==237:
                self.pushButton_140.setText(myresult[0])
            if x==238:
                self.pushButton_142.setText(myresult[0])
            if x==239:
                self.pushButton_147.setText(myresult[0])
            if x==240:
                self.pushButton_151.setText(myresult[0])
            if x==241:
                self.pushButton_158.setText(myresult[0])
            if x==242:
                self.pushButton_161.setText(myresult[0])
            if x==243:
                self.pushButton_167.setText(myresult[0])
            if x==244:
                self.pushButton_171.setText(myresult[0])
            if x==245:
                self.pushButton_178.setText(myresult[0])
            if x==246:
                self.pushButton_152.setText(myresult[0])
            if x==247:
                self.pushButton_157.setText(myresult[0])
            if x==248:
                self.pushButton_162.setText(myresult[0])
            if x==249:
                self.pushButton_169.setText(myresult[0])
            if x==250:
                self.pushButton_173.setText(myresult[0])
            if x==251:
                self.pushButton_180.setText(myresult[0])
            if x==252:
                self.pushButton_153.setText(myresult[0])
            if x==253:
                self.pushButton_160.setText(myresult[0])
            if x==254:
                self.pushButton_163.setText(myresult[0])
            if x==255:
                self.pushButton_166.setText(myresult[0])
            if x==256:
                self.pushButton_175.setText(myresult[0])
            if x==257:
                self.pushButton_176.setText(myresult[0])
            if x==258:
                self.pushButton_154.setText(myresult[0])
            if x==259:
                self.pushButton_159.setText(myresult[0])
            if x==260:
                self.pushButton_165.setText(myresult[0])
            if x==261:
                self.pushButton_168.setText(myresult[0])
            if x==262:
                self.pushButton_174.setText(myresult[0])
            if x==263:
                self.pushButton_179.setText(myresult[0])
            if x==264:
                self.pushButton_155.setText(myresult[0])
            if x==265:
                self.pushButton_156.setText(myresult[0])
            if x==266:
                self.pushButton_164.setText(myresult[0])
            if x==267:
                self.pushButton_170.setText(myresult[0])
            if x==268:
                self.pushButton_172.setText(myresult[0])
            if x==269:
                self.pushButton_177.setText(myresult[0])
       # self.statusBar().showMessage('تم اضافة الوجبة بنجاح')


    def Meals_price(self):
        self.comboBox_2.clear()
        y = self.comboBox_5.currentIndex()
        if y == 1:
            for x in range(1, 31):
                sql = ''' SELECT Meal_Name FROM meals WHERE Meal_ID = %s '''
                self.cur.execute(sql, x)
                data = self.cur.fetchall()
                for meal in data:
                    self.comboBox_2.addItem(meal[0])
        if y == 2:
            for x in range(150, 180):
                sql = ''' SELECT Meal_Name FROM meals WHERE Meal_ID = %s '''
                self.cur.execute(sql, x)
                data = self.cur.fetchall()
                for meal in data:
                    self.comboBox_2.addItem(meal[0])
        if y == 3:
            for x in range(180, 210):
                sql = ''' SELECT Meal_Name FROM meals WHERE Meal_ID = %s '''
                self.cur.execute(sql, x)
                data = self.cur.fetchall()
                for meal in data:
                    self.comboBox_2.addItem(meal[0])
        if y == 4:
            for x in range(210, 240):
                sql = ''' SELECT Meal_Name FROM meals WHERE Meal_ID = %s '''
                self.cur.execute(sql, x)
                data = self.cur.fetchall()
                for meal in data:
                    self.comboBox_2.addItem(meal[0])
        if y == 5:
            for x in range(240, 270):
                sql = ''' SELECT Meal_Name FROM meals WHERE Meal_ID = %s '''
                self.cur.execute(sql, x)
                data = self.cur.fetchall()
                for meal in data:
                    self.comboBox_2.addItem(meal[0])

        self.comboBox_5.currentIndexChanged[str].connect(self.Meals_price)

        for x in range(1, 31):
            sql = "SELECT Meal_Name FROM meals WHERE Meal_ID = %s "
            self.cur.execute(sql, x)
            myresult = self.cur.fetchone()

            if x == 1:
                self.pushButton_26.setText(myresult[0])
            if x == 2:
                self.pushButton_33.setText(myresult[0])
            if x == 3:
                self.pushButton_36.setText(myresult[0])
            if x == 4:
                self.pushButton_42.setText(myresult[0])
            if x == 5:
                self.pushButton_46.setText(myresult[0])
            if x == 6:
                self.pushButton_53.setText(myresult[0])
            if x == 7:
                self.pushButton_27.setText(myresult[0])
            if x == 8:
                self.pushButton_32.setText(myresult[0])
            if x == 9:
                self.pushButton_37.setText(myresult[0])
            if x == 10:
                self.pushButton_44.setText(myresult[0])
            if x == 11:
                self.pushButton_48.setText(myresult[0])
            if x == 12:
                self.pushButton_55.setText(myresult[0])
            if x == 13:
                self.pushButton_28.setText(myresult[0])
            if x == 14:
                self.pushButton_35.setText(myresult[0])
            if x == 15:
                self.pushButton_38.setText(myresult[0])
            if x == 16:
                self.pushButton_41.setText(myresult[0])
            if x == 17:
                self.pushButton_50.setText(myresult[0])
            if x == 18:
                self.pushButton_51.setText(myresult[0])
            if x == 19:
                self.pushButton_29.setText(myresult[0])
            if x == 20:
                self.pushButton_34.setText(myresult[0])
            if x == 21:
                self.pushButton_40.setText(myresult[0])
            if x == 22:
                self.pushButton_43.setText(myresult[0])
            if x == 23:
                self.pushButton_49.setText(myresult[0])
            if x == 24:
                self.pushButton_54.setText(myresult[0])
            if x == 25:
                self.pushButton_30.setText(myresult[0])
            if x == 26:
                self.pushButton_31.setText(myresult[0])
            if x == 27:
                self.pushButton_39.setText(myresult[0])
            if x == 28:
                self.pushButton_45.setText(myresult[0])
            if x == 29:
                self.pushButton_47.setText(myresult[0])
            if x == 30:
                self.pushButton_52.setText(myresult[0])
        for x in range(150, 270):
            sql = "SELECT Meal_Name FROM meals WHERE Meal_ID = %s "
            self.cur.execute(sql, x)
            myresult = self.cur.fetchone()
            if x == 150:
                self.pushButton_58.setText(myresult[0])
            if x == 151:
                self.pushButton_65.setText(myresult[0])
            if x == 152:
                self.pushButton_68.setText(myresult[0])
            if x == 153:
                self.pushButton_74.setText(myresult[0])
            if x == 154:
                self.pushButton_78.setText(myresult[0])
            if x == 155:
                self.pushButton_85.setText(myresult[0])
            if x == 156:
                self.pushButton_59.setText(myresult[0])
            if x == 157:
                self.pushButton_64.setText(myresult[0])
            if x == 158:
                self.pushButton_69.setText(myresult[0])
            if x == 159:
                self.pushButton_76.setText(myresult[0])
            if x == 160:
                self.pushButton_80.setText(myresult[0])
            if x == 161:
                self.pushButton_87.setText(myresult[0])
            if x == 162:
                self.pushButton_60.setText(myresult[0])
            if x == 163:
                self.pushButton_67.setText(myresult[0])
            if x == 164:
                self.pushButton_70.setText(myresult[0])
            if x == 165:
                self.pushButton_73.setText(myresult[0])
            if x == 166:
                self.pushButton_82.setText(myresult[0])
            if x == 167:
                self.pushButton_83.setText(myresult[0])
            if x == 168:
                self.pushButton_61.setText(myresult[0])
            if x == 169:
                self.pushButton_66.setText(myresult[0])
            if x == 170:
                self.pushButton_72.setText(myresult[0])
            if x == 171:
                self.pushButton_75.setText(myresult[0])
            if x == 172:
                self.pushButton_81.setText(myresult[0])
            if x == 173:
                self.pushButton_86.setText(myresult[0])
            if x == 174:
                self.pushButton_62.setText(myresult[0])
            if x == 175:
                self.pushButton_63.setText(myresult[0])
            if x == 176:
                self.pushButton_71.setText(myresult[0])
            if x == 177:
                self.pushButton_77.setText(myresult[0])
            if x == 178:
                self.pushButton_79.setText(myresult[0])
            if x == 179:
                self.pushButton_84.setText(myresult[0])
            if x == 180:
                self.pushButton_88.setText(myresult[0])
            if x == 181:
                self.pushButton_95.setText(myresult[0])
            if x == 182:
                self.pushButton_98.setText(myresult[0])
            if x == 183:
                self.pushButton_104.setText(myresult[0])
            if x == 184:
                self.pushButton_108.setText(myresult[0])
            if x == 185:
                self.pushButton_118.setText(myresult[0])
            if x == 186:
                self.pushButton_89.setText(myresult[0])
            if x == 187:
                self.pushButton_94.setText(myresult[0])
            if x == 188:
                self.pushButton_99.setText(myresult[0])
            if x == 189:
                self.pushButton_106.setText(myresult[0])
            if x == 190:
                self.pushButton_110.setText(myresult[0])
            if x == 191:
                self.pushButton_120.setText(myresult[0])
            if x == 192:
                self.pushButton_90.setText(myresult[0])
            if x == 193:
                self.pushButton_97.setText(myresult[0])
            if x == 194:
                self.pushButton_100.setText(myresult[0])
            if x == 195:
                self.pushButton_103.setText(myresult[0])
            if x == 196:
                self.pushButton_112.setText(myresult[0])
            if x == 197:
                self.pushButton_113.setText(myresult[0])
            if x == 198:
                self.pushButton_91.setText(myresult[0])
            if x == 199:
                self.pushButton_96.setText(myresult[0])
            if x == 200:
                self.pushButton_102.setText(myresult[0])
            if x == 201:
                self.pushButton_105.setText(myresult[0])
            if x == 202:
                self.pushButton_111.setText(myresult[0])
            if x == 203:
                self.pushButton_119.setText(myresult[0])
            if x == 204:
                self.pushButton_92.setText(myresult[0])
            if x == 205:
                self.pushButton_93.setText(myresult[0])
            if x == 206:
                self.pushButton_101.setText(myresult[0])
            if x == 207:
                self.pushButton_107.setText(myresult[0])
            if x == 208:
                self.pushButton_109.setText(myresult[0])
            if x == 209:
                self.pushButton_114.setText(myresult[0])
            if x == 210:
                self.pushButton_121.setText(myresult[0])
            if x == 211:
                self.pushButton_128.setText(myresult[0])
            if x == 212:
                self.pushButton_131.setText(myresult[0])
            if x == 213:
                self.pushButton_137.setText(myresult[0])
            if x == 214:
                self.pushButton_141.setText(myresult[0])
            if x == 215:
                self.pushButton_148.setText(myresult[0])
            if x == 216:
                self.pushButton_122.setText(myresult[0])
            if x == 217:
                self.pushButton_127.setText(myresult[0])
            if x == 218:
                self.pushButton_132.setText(myresult[0])
            if x == 219:
                self.pushButton_139.setText(myresult[0])
            if x == 220:
                self.pushButton_143.setText(myresult[0])
            if x == 221:
                self.pushButton_150.setText(myresult[0])
            if x == 222:
                self.pushButton_123.setText(myresult[0])
            if x == 223:
                self.pushButton_130.setText(myresult[0])
            if x == 224:
                self.pushButton_133.setText(myresult[0])
            if x == 225:
                self.pushButton_136.setText(myresult[0])
            if x == 226:
                self.pushButton_145.setText(myresult[0])
            if x == 227:
                self.pushButton_146.setText(myresult[0])
            if x == 228:
                self.pushButton_124.setText(myresult[0])
            if x == 229:
                self.pushButton_129.setText(myresult[0])
            if x == 230:
                self.pushButton_135.setText(myresult[0])
            if x == 231:
                self.pushButton_138.setText(myresult[0])
            if x == 232:
                self.pushButton_144.setText(myresult[0])
            if x == 233:
                self.pushButton_149.setText(myresult[0])
            if x == 234:
                self.pushButton_125.setText(myresult[0])
            if x == 235:
                self.pushButton_126.setText(myresult[0])
            if x == 236:
                self.pushButton_134.setText(myresult[0])
            if x == 237:
                self.pushButton_140.setText(myresult[0])
            if x == 238:
                self.pushButton_142.setText(myresult[0])
            if x == 239:
                self.pushButton_147.setText(myresult[0])
            if x == 240:
                self.pushButton_151.setText(myresult[0])
            if x == 241:
                self.pushButton_158.setText(myresult[0])
            if x == 242:
                self.pushButton_161.setText(myresult[0])
            if x == 243:
                self.pushButton_167.setText(myresult[0])
            if x == 244:
                self.pushButton_171.setText(myresult[0])
            if x == 245:
                self.pushButton_178.setText(myresult[0])
            if x == 246:
                self.pushButton_152.setText(myresult[0])
            if x == 247:
                self.pushButton_157.setText(myresult[0])
            if x == 248:
                self.pushButton_162.setText(myresult[0])
            if x == 249:
                self.pushButton_169.setText(myresult[0])
            if x == 250:
                self.pushButton_173.setText(myresult[0])
            if x == 251:
                self.pushButton_180.setText(myresult[0])
            if x == 252:
                self.pushButton_153.setText(myresult[0])
            if x == 253:
                self.pushButton_160.setText(myresult[0])
            if x == 254:
                self.pushButton_163.setText(myresult[0])
            if x == 255:
                self.pushButton_166.setText(myresult[0])
            if x == 256:
                self.pushButton_175.setText(myresult[0])
            if x == 257:
                self.pushButton_176.setText(myresult[0])
            if x == 258:
                self.pushButton_154.setText(myresult[0])
            if x == 259:
                self.pushButton_159.setText(myresult[0])
            if x == 260:
                self.pushButton_165.setText(myresult[0])
            if x == 261:
                self.pushButton_168.setText(myresult[0])
            if x == 262:
                self.pushButton_174.setText(myresult[0])
            if x == 263:
                self.pushButton_179.setText(myresult[0])
            if x == 264:
                self.pushButton_155.setText(myresult[0])
            if x == 265:
                self.pushButton_156.setText(myresult[0])
            if x == 266:
                self.pushButton_164.setText(myresult[0])
            if x == 267:
                self.pushButton_170.setText(myresult[0])
            if x == 268:
                self.pushButton_172.setText(myresult[0])
            if x == 269:
                self.pushButton_177.setText(myresult[0])

    # self.statusBar().showMessage('تم اضافة الوجبة بنجاح')
    def Add_Meal(self):
        x = self.comboBox_4.currentIndex()
        y = self.comboBox_4.currentIndex()
        if y == 1:
            meal_index = self.comboBox.currentIndex()
            meal_name = self.lineEdit_4.text()
            sql = "UPDATE meals SET Meal_Name = %s WHERE Meal_ID = %s"
            val = (meal_name, (meal_index+1))
            self.cur.execute(sql,val)
            self.db.commit()
            self.Meals()
        if y == 2 :
            meal_index = self.comboBox.currentIndex()
            meal_name = self.lineEdit_4.text()
            sql = "UPDATE meals SET Meal_Name = %s WHERE Meal_ID = %s"
            val = (meal_name, (meal_index+150))
            self.cur.execute(sql, val)
            self.db.commit()
            self.Meals()
        if y ==3 :
            meal_index = self.comboBox.currentIndex()
            meal_name = self.lineEdit_4.text()
            sql = "UPDATE meals SET Meal_Name = %s WHERE Meal_ID = %s"
            val = (meal_name, (meal_index+180))
            self.cur.execute(sql, val)
            self.db.commit()
            self.Meals()
        if y == 4 :
            meal_index = self.comboBox.currentIndex()
            meal_name = self.lineEdit_4.text()
            sql = "UPDATE meals SET Meal_Name = %s WHERE Meal_ID = %s"
            val = (meal_name, (meal_index+210))
            self.cur.execute(sql, val)
            self.db.commit()
            self.Meals()
        if y == 5 :
            meal_index = self.comboBox.currentIndex()
            meal_name = self.lineEdit_4.text()
            sql = "UPDATE meals SET Meal_Name = %s WHERE Meal_ID = %s"
            val = (meal_name, (meal_index+240))
            self.cur.execute(sql, val)
            self.db.commit()
            self.Meals()
        self.statusBar().showMessage('تم اضافة الوجبة بنجاح')

    def Add_Meal_Price(self):
        x = self.comboBox_4.currentIndex()
        y = self.comboBox_5.currentIndex()
        meal_index = self.comboBox_2.currentIndex()
        meal_price = self.lineEdit_5.text()
        if y == 1:
            sql = "UPDATE meals SET Meal_Price = %s WHERE Meal_ID = %s"
            val = (meal_price, (meal_index + 1))
            self.cur.execute(sql, val)
            self.db.commit()
            self.Meals()
        if y == 2:
            sql = "UPDATE meals SET Meal_Price = %s WHERE Meal_ID = %s"
            val = (meal_price, (meal_index + 150))
            self.cur.execute(sql, val)
            self.db.commit()
            self.Meals()
        if y == 3:
            sql = "UPDATE meals SET Meal_Price = %s WHERE Meal_ID = %s"
            val = (meal_price, (meal_index + 180))
            self.cur.execute(sql, val)
            self.db.commit()
            self.Meals()
        if y == 4:
            sql = "UPDATE meals SET Meal_Price = %s WHERE Meal_ID = %s"
            val = (meal_price, (meal_index + 210))
            self.cur.execute(sql, val)
            self.db.commit()
            self.Meals()
        if y == 5:
            sql = "UPDATE meals SET Meal_Price = %s WHERE Meal_ID = %s"
            val = (meal_price, (meal_index + 240))
            self.cur.execute(sql, val)
            self.db.commit()
            self.Meals()
        self.statusBar().showMessage('تم اضافة الوجبة بنجاح')

    def Delivery(self):
        y=self.lineEdit_6.text()
        sql= "UPDATE meals SET Delivery = %s WHERE Meal_ID = 1"
        self.cur.execute(sql , y)
        self.db.commit()



    def Add_Category(self):
        Catogery_index = self.comboBox_3.currentIndex()
        Category_name = self.lineEdit_9.text()
        sql = "UPDATE category SET Category_Name = %s WHERE Category_ID = %s"
        val = (Category_name,Catogery_index)
        self.cur.execute(sql, val)
        self.db.commit()
        self.Category()


    def Save_Data(self):
        name=self.lineEdit_12.text()
        phone=self.lineEdit_10.text()
        address=self.lineEdit_11.text()
        Num=int(self.label_7.text())
        x=0
        M1=0; M1_P=0; M1_Q=0; M1_T=0;M2=0; M2_P=0; M2_Q=0; M2_T=0; M3=0; M3_P=0; M3_Q=0; M3_T=0; M4=0; M4_P=0; M4_Q=0; M4_T=0; M5=0; M5_P=0; M5_Q=0; M5_T=0; M6=0; M6_P=0; M6_Q=0; M6_T=0; M7=0; M7_P=0; M7_Q=0; M7_T=0; M8=0; M8_P=0; M8_Q=0; M8_T=0; M9=0; M9_P=0; M9_Q=0; M9_T=0; M10=0; M10_P=0; M10_Q=0; M10_T=0; M11=0; M11_P=0; M11_Q=0; M11_T=0; M12=0; M12_P=0; M12_Q=0; M12_T=0; M13=0; M13_P=0; M13_Q=0; M13_T=0; M14=0; M14_P=0; M14_Q=0; M14_T=0; M15=0; M15_P=0; M15_Q=0; M15_T=0; M16=0; M16_P=0; M16_Q=0; M16_T=0; M17=0; M17_P=0; M17_Q=0; M17_T=0; M18=0; M18_P=0; M18_Q=0; M18_T=0; M19=0; M19_P=0; M19_Q=0; M19_T=0; M20=0; M20_P=0; M20_Q=0; M20_T=0; M1_Y=0; M2_Y=0; M3_Y=0; M4_Y=0; M5_Y=0; M6_Y=0; M7_Y=0; M8_Y=0; M9_Y=0; M10_Y=0; M11_Y=0; M12_Y=0; M13_Y=0; M14_Y=0; M15_Y=0; M16_Y=0; M17_Y=0; M18_Y=0; M19_Y=0; M20_Y=0;

        # row_1 =[self.tableWidget.item(0,column).text() for column in range(self.tableWidget.columnCount())]
        for x in range(self.tableWidget.rowCount()):
            row_1 =[self.tableWidget.item(x,column).text() for column in range(self.tableWidget.columnCount())]
            # e=[row_1[0],row_1[1],row_1[2],row_1[3]]
            # print(row_1[4])
            e=row_1[0]
            d=row_1[1]
            f=row_1[2]
            g=row_1[3]
            h=row_1[4]

            if x==0:
                # sql_1=("INSERT INTO invotery (Meal_1,Meal_1_Price,Meal_1_Quantaty,Meal_1_Total) VALUES (%s,%s,%s,%s) ")
                # we=self.cur.execute(sql_1,(e,d,f,g))
                M1=e
                M1_P=d
                M1_Q=f
                M1_T=g
                M1_Y=h
            if x==1:

                M2=e
                M2_P=d
                M2_Q=f
                M2_T=g
                M2_Y=h
            #     # sql_2=("INSERT INTO invotery (Meal_2,Meal_2_Price,Meal_2_Quantaty,Meal_2_Total) VALUES (%s,%s,%s,%s) ")
            #     # self.cur.execute(sql_2,(e,d,f,g))
            if x == 2:
                M3 = e
                M3_P = d
                M3_Q = f
                M3_T = g
                M3_Y = h

            if x == 3:
                M4 = e
                M4_P = d
                M4_Q = f
                M4_T = g
                M4_Y = h
            if x == 4:
                M5 = e
                M5_P = d
                M5_Q = f
                M5_T = g
                M5_Y = h
            if x == 5:
                M6 = e
                M6_P = d
                M6_Q = f
                M6_T = g
                M6_Y = h
            if x == 6:
                M7 = e
                M7_P = d
                M7_Q = f
                M7_T = g
                M7_Y = h
            if x == 7:
                M8 = e
                M8_P = d
                M8_Q = f
                M8_T = g
                M8_Y = h
            if x == 8:
                M9 = e
                M9_P = d
                M9_Q = f
                M9_T = g
                M9_Y = h
            if x == 9:
                M10 = e
                M10_P = d
                M10_Q = f
                M10_T = g
                M10_Y = h
            if x == 10:
                M11 = e
                M11_P = d
                M11_Q = f
                M11_T = g
                M11_Y = h
            if x == 11:
                M12 = e
                M12_P = d
                M12_Q = f
                M12_T = g
                M12_Y = h
            if x == 12:
                M13 = e
                M13_P = d
                M13_Q = f
                M13_T = g
                M13_Y = h
            if x == 13:
                M14 = e
                M14_P = d
                M14_Q = f
                M14_T = g
                M14_Y = h
            if x == 14:
                M15 = e
                M15_P = d
                M15_Q = f
                M15_T = g
                M15_Y = h
            if x == 15:
                M16 = e
                M16_P = d
                M16_Q = f
                M16_T = g
                M16_Y = h
            if x == 16:
                M17 = e
                M17_P = d
                M17_Q = f
                M17_T = g
                M17_Y = h
            if x == 17:
                M18 = e
                M18_P = d
                M18_Q = f
                M18_T = g
                M18_Y = h
            if x == 18:
                M19 = e
                M19_P = d
                M19_Q = f
                M19_T = g
                M19_Y = h
            if x == 19:
                M20 = e
                M20_P = d
                M20_Q = f
                M20_T = g
                M20_Y = h

        total= int(self.label_6.text())
        self.cur.execute('''
            INSERT INTO invotery(Meal_1,Meal_1_Price,Meal_1_Quantaty,Meal_1_Total,Meal_1_Type,Meal_2,Meal_2_Price,Meal_2_Quantaty,Meal_2_Total,Meal_2_Type,Meal_3,Meal_3_Price,Meal_3_Quantaty,Meal_3_Total,Meal_3_Type,Meal_4,Meal_4_Price,Meal_4_Quantaty,Meal_4_Total,Meal_4_Type,Meal_5,Meal_5_Price,Meal_5_Quantaty,Meal_5_Total,Meal_5_Type,Meal_6,Meal_6_Price,Meal_6_Quantaty,Meal_6_Total,Meal_6_Type,Meal_7,Meal_7_Price,Meal_7_Quantaty,Meal_7_Total,Meal_7_Type,Meal_8,Meal_8_Price,Meal_8_Quantaty,Meal_8_Total,Meal_8_Type,Meal_9,Meal_9_Price,Meal_9_Quantaty,Meal_9_Total,Meal_9_Type,Meal_10,Meal_10_Price,Meal_10_Quantaty,Meal_10_Total,Meal_10_Type,Meal_11,Meal_11_Price,Meal_11_Quantaty,Meal_11_Total,Meal_11_Type,Meal_12,Meal_12_Price,Meal_12_Quantaty,Meal_12_Total,Meal_12_Type,Meal_13,Meal_13_Price,Meal_13_Quantaty,Meal_13_Total,Meal_13_Type,Meal_14,Meal_14_Price,Meal_14_Quantaty,Meal_14_Total,Meal_14_Type,Meal_15,Meal_15_Price,Meal_15_Quantaty,Meal_15_Total,Meal_15_Type,Meal_16,Meal_16_Price,Meal_16_Quantaty,Meal_16_Total,Meal_16_Type,Meal_17,Meal_17_Price,Meal_17_Quantaty,Meal_17_Total,Meal_17_Type,Meal_18,Meal_18_Price,Meal_18_Quantaty,Meal_18_Total,Meal_18_Type,Meal_19,Meal_19_Price,Meal_19_Quantaty,Meal_19_Total,Meal_19_Type,Meal_20,Meal_20_Price,Meal_20_Quantaty,Meal_20_Total,Meal_20_Type,Total,Date , Customer_Name , Customer_Phone , Customer_Address ,Invoice_Num )
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,current_date(),%s,%s,%s, %s)
        ''' , (M1,M1_P,M1_Q,M1_T,M1_Y,M2,M2_P,M2_Q,M2_T,M2_Y,M3,M3_P,M3_Q,M3_T,M3_Y,M4,M4_P,M4_Q,M4_T,M4_Y,M5,M5_P,M5_Q,M5_T,M5_Y,M6,M6_P,M6_Q,M6_T,M6_Y,M7,M7_P,M7_Q,M7_T,M7_Y,M8,M8_P,M8_Q,M8_T,M8_Y,M9,M9_P,M9_Q,M9_T,M9_Y,M10,M10_P,M10_Q,M10_T,M10_Y,M11,M11_P,M11_Q,M11_T,M11_Y,M12,M12_P,M12_Q,M12_T,M12_Y,M13,M13_P,M13_Q,M13_T,M13_Y,M14,M14_P,M14_Q,M14_T,M14_Y,M15,M15_P,M15_Q,M15_T,M15_Y,M16,M16_P,M16_Q,M16_T,M16_Y,M17,M17_P,M17_Q,M17_T,M17_Y,M18,M18_P,M18_Q,M18_T,M18_Y,M19,M19_P,M19_Q,M19_T,M19_Y,M20,M20_P,M20_Q,M20_T,M20_Y,total, name , phone , address , Num))
        self.db.commit()



    def total(self):
        to = self.label_6.text()


    def Order_Num(self):
# ##################################################################################################
#         self.cur.execute("SELECT MAX(Invotery_ID) AS maximum FROM invotery")
#         result = self.cur.fetchone()
#         z=int(result[0])
#         self.label_7.setNum(z+1)
# ##################################################################################################
        self.cur.execute("SELECT Invoice_Num From invotery")
        data =self.cur.fetchall()

        n=date.today()
        l=data[-1][0]
        self.cur.execute("SELECT Date From invotery ")
        tata= self.cur.fetchall()

        if tata[-1][0] == n:
            self.label_7.setNum(data[-1][0]+1)
        else:
            num = 1
            self.label_7.setNum(num)


    def report(self):
        nrows = self.tableWidget_2.rowCount()
        try:
            while nrows > 0:
                for row in range(0, nrows):
                    item = self.tableWidget_2.item(0, 0)
                    item_text = item.text()
                    self.tableWidget_2.removeRow(row)
        except:
            self.statusBar().showMessage('لا يوجد معلومات ok ')

        d=self.comboBox_6.currentText()
        m=self.comboBox_7.currentText()
        y=self.comboBox_8.currentText()


        if d != "Day":
            try:
                d=int(d)
                m=int(m)
                y=int(y)
                t2 = datetime.datetime(y, m, d)
                statment = "SELECT * FROM invotery WHERE Date = %s"
                self.cur.execute(statment,t2)
                data = self.cur.fetchall()
                for x in data:
                    M1 = 0;
                    M1_P = 0;
                    M1_Q = 0;
                    M1_T = 0;
                    M2 = 0;
                    M2_P = 0;
                    M2_Q = 0;
                    M2_T = 0;
                    M3 = 0;
                    M3_P = 0;
                    M3_Q = 0;
                    M3_T = 0;
                    M4 = 0;
                    M4_P = 0;
                    M4_Q = 0;
                    M4_T = 0;
                    M5 = 0;
                    M5_P = 0;
                    M5_Q = 0;
                    M5_T = 0;
                    M6 = 0;
                    M6_P = 0;
                    M6_Q = 0;
                    M6_T = 0;
                    M7 = 0;
                    M7_P = 0;
                    M7_Q = 0;
                    M7_T = 0;
                    M8 = 0;
                    M8_P = 0;
                    M8_Q = 0;
                    M8_T = 0;
                    M9 = 0;
                    M9_P = 0;
                    M9_Q = 0;
                    M9_T = 0;
                    M10 = 0;
                    M10_P = 0;
                    M10_Q = 0;
                    M10_T = 0;
                    M11 = 0;
                    M11_P = 0;
                    M11_Q = 0;
                    M11_T = 0;
                    M12 = 0;
                    M12_P = 0;
                    M12_Q = 0;
                    M12_T = 0;
                    M13 = 0;
                    M13_P = 0;
                    M13_Q = 0;
                    M13_T = 0;
                    M14 = 0;
                    M14_P = 0;
                    M14_Q = 0;
                    M14_T = 0;
                    M15 = 0;
                    M15_P = 0;
                    M15_Q = 0;
                    M15_T = 0;
                    M16 = 0;
                    M16_P = 0;
                    M16_Q = 0;
                    M16_T = 0;
                    M17 = 0;
                    M17_P = 0;
                    M17_Q = 0;
                    M17_T = 0;
                    M18 = 0;
                    M18_P = 0;
                    M18_Q = 0;
                    M18_T = 0;
                    M19 = 0;
                    M19_P = 0;
                    M19_Q = 0;
                    M19_T = 0;
                    M20 = 0;
                    M20_P = 0;
                    M20_Q = 0;
                    M20_T = 0;

                    if x[1] != "" and x[1] != '0':
                        M1=x[1]
                        if x[2] != "" and x[2] != '0': M1_P=x[2]
                        if x[3] != "" and x[3] != '0': M1_Q=x[3]
                        if x[4] != "" and x[4] != '0': M1_T=x[4]
                        if x[0] != "" and x[0] != '0': MID_T=x[0]
                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                        self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M1_Q))
                        self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M1))
                        self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M1_P))
                        self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M1_T))
                        self.tableWidget_2.setItem(row_position, 4, QTableWidgetItem(str(MID_T)))

                    if x[6] != "" and x[6] != '0':
                        M2=x[6]
                        if x[7] != "" and x[7] != '0': M2_P=x[7]
                        if x[8] != "" and x[8] != '0': M2_Q=x[8]
                        if x[9] != "" and x[9] != '0': M2_T=x[9]
                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                        self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M2_Q))
                        self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M2))
                        self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M2_P))
                        self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M2_T))


                    if x[11] != "" and x[11] != '0':
                        M3=x[11]
                        if x[12] != "" and x[12] != '0': M3_P=x[12]
                        if x[13] != "" and x[13] != '0': M3_Q=x[13]
                        if x[14] != "" and x[14] != '0': M3_T=x[14]
                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                        self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M3_Q))
                        self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M3))
                        self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M3_P))
                        self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M3_T))


                    if x[16] != "" and x[16] != '0':
                        M4=x[16]
                        if x[17] != "" and x[17] != '0': M4_P=x[17]
                        if x[18] != "" and x[18] != '0': M4_Q=x[18]
                        if x[19] != "" and x[19] != '0': M4_T=x[19]
                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                        self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M4_Q))
                        self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M4))
                        self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M4_P))
                        self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M4_T))


                    if x[21] != "" and x[21] != '0':
                        M5=x[21]
                        if x[22] != "" and x[22] != '0': M5_P=x[22]
                        if x[23] != "" and x[23] != '0': M5_Q=x[23]
                        if x[24] != "" and x[24] != '0': M5_T=x[24]
                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                        self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M5_Q))
                        self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M5))
                        self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M5_P))
                        self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M5_T))



                    if x[26] != "" and x[26] != '0':
                        M6=x[26]
                        if x[27] != "" and x[27] != '0': M6_P=x[27]
                        if x[28] != "" and x[28] != '0': M6_Q=x[28]
                        if x[29] != "" and x[29] != '0': M6_T=x[29]
                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                        self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M6_Q))
                        self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M6))
                        self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M6_P))
                        self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M6_T))



                    if x[31] != "" and x[31] != '0':
                        M7=x[31]
                        if x[32] != "" and x[32] != '0': M7_P=x[32]
                        if x[33] != "" and x[33] != '0': M7_Q=x[33]
                        if x[34] != "" and x[34] != '0': M7_T=x[34]
                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                        self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M7_Q))
                        self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M7))
                        self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M7_P))
                        self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M7_T))


                    if x[36] != "" and x[36] != '0':
                        M8=x[36]
                        if x[37] != "" and x[37] != '0': M8_P=x[37]
                        if x[38] != "" and x[38] != '0': M8_Q=x[38]
                        if x[39] != "" and x[39] != '0':
                            M8_T=x[39]
                            row_position = self.tableWidget_2.rowCount()
                            self.tableWidget_2.insertRow(row_position)
                            self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M8_Q))
                            self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M8))
                            self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M8_P))
                            self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M8_T))


                    if x[41] != "" and x[41] != '0':
                        M9=x[41]
                        if x[42] != "" and x[42] != '0': M9_P=x[42]
                        if x[43] != "" and x[43] != '0': M9_Q=x[43]
                        if x[44] != "" and x[44] != '0': M9_T=x[44]
                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                        self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M9_Q))
                        self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M9))
                        self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M9_P))
                        self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M9_T))


                    if x[46] != "" and x[46] != '0':
                        M10=x[46]
                        if x[47] != "" and x[47] != '0': M10_P=x[47]
                        if x[48] != "" and x[48] != '0': M10_Q=x[48]
                        if x[49] != "" and x[49] != '0': M10_T=x[49]
                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                        self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M10_Q))
                        self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M10))
                        self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M10_P))
                        self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M10_T))


                    if x[51] != "" and x[51] != '0':
                        M11=x[51]
                        if x[52] != "" and x[52] != '0': M11_P=x[52]
                        if x[53] != "" and x[53] != '0': M11_Q=x[53]
                        if x[54] != "" and x[54] != '0': M11_T=x[54]
                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                        self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M11_Q))
                        self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M11))
                        self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M11_P))
                        self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M11_T))


                    if x[56] != "" and x[56] != '0':
                        M12=x[56]
                        if x[57] != "" and x[57] != '0': M12_P=x[57]
                        if x[58] != "" and x[58] != '0': M12_Q=x[58]
                        if x[59] != "" and x[59] != '0': M12_T=x[59]
                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                        self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M12_Q))
                        self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M12))
                        self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M12_P))
                        self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M12_T))

                    if x[61] != "" and x[61] != '0':
                        M13=x[61]
                        if x[62] != "" and x[62] != '0': M13_P=x[62]
                        if x[63] != "" and x[63] != '0': M13_Q=x[63]
                        if x[64] != "" and x[64] != '0': M13_T=x[64]
                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                        self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M13_Q))
                        self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M13))
                        self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M13_P))
                        self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M13_T))


                    if x[66] != "" and x[66] != '0':
                        M14=x[66]
                        if x[67] != "" and x[67] != '0': M14_P=x[67]
                        if x[68] != "" and x[68] != '0': M14_Q=x[68]
                        if x[69] != "" and x[69] != '0': M14_T=x[69]
                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                        self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M14_Q))
                        self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M14))
                        self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M14_P))
                        self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M14_T))

                    if x[71] != "" and x[71] != '0':
                        M15=x[71]
                        if x[72] != "" and x[72] != '0': M15_P=x[72]
                        if x[73] != "" and x[73] != '0': M15_Q=x[73]
                        if x[74] != "" and x[74] != '0': M15_T=x[74]
                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                        self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M15_Q))
                        self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M15))
                        self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M15_P))
                        self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M15_T))


                    if x[76] != "" and x[76] != '0':
                        M16=x[76]
                        if x[77] != "" and x[77] != '0': M16_P=x[77]
                        if x[78] != "" and x[78] != '0': M16_Q=x[78]
                        if x[79] != "" and x[79] != '0': M16_T=x[79]
                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                        self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M16_Q))
                        self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M16))
                        self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M16_P))
                        self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M16_T))



                    if x[81] != "" and x[81] != '0':
                        M17=x[81]
                        if x[82] != "" and x[82] != '0': M17_P=x[82]
                        if x[83] != "" and x[83] != '0': M17_Q=x[83]
                        if x[84] != "" and x[84] != '0': M17_T=x[84]
                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                        self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M17_Q))
                        self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M17))
                        self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M17_P))
                        self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M17_T))




                    if x[86] != "" and x[86] != '0':
                        M18=x[86]
                        if x[87] != "" and x[87] != '0': M18_P=x[87]
                        if x[88] != "" and x[88] != '0': M18_Q=x[88]
                        if x[89] != "" and x[89] != '0': M18_T=x[89]
                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                        self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M18_Q))
                        self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M18))
                        self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M18_P))
                        self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M18_T))



                    if x[91] != "" and x[91] != '0':
                        M19=x[91]
                        if x[92] != "" and x[92] != '0': M19_P=x[92]
                        if x[93] != "" and x[93] != '0': M19_Q=x[93]
                        if x[94] != "" and x[94] != '0': M19_T=x[94]
                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                        self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M19_Q))
                        self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M19))
                        self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M19_P))
                        self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M19_T))


                    if x[96] != "" and x[96] != '0':
                        M20=x[96]
                        if x[97] != "" and x[97] != '0': M20_P=x[97]
                        if x[98] != "" and x[98] != '0': M20_Q=x[98]
                        if x[99] != "" and x[99] != '0': M20_T=x[99]
                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                        self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M20_Q))
                        self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M20))
                        self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M20_P))
                        self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M20_T))

            except:
                self.statusBar().showMessage('لا يوجد معلومات ')
            self.report_total()
        if d == "Day" and m !="Month":
            try:
                d=1
                m=int(m)
                if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
                    s =31
                elif m == 2:
                    s=28
                else:
                    s = 30
                y=int(y)
                t1 = datetime.datetime(y, m, d)
                t2 = datetime.datetime(y, m, s)
                # statment = "SELECT * FROM invotery WHERE Date = %s"
                statment="SELECT * FROM invotery WHERE Date BETWEEN %s and %s"
                self.cur.execute(statment, (t1,t2))
                data = self.cur.fetchall()
                for x in data:
                    M1 = 0;
                    M1_P = 0;
                    M1_Q = 0;
                    M1_T = 0;
                    M2 = 0;
                    M2_P = 0;
                    M2_Q = 0;
                    M2_T = 0;
                    M3 = 0;
                    M3_P = 0;
                    M3_Q = 0;
                    M3_T = 0;
                    M4 = 0;
                    M4_P = 0;
                    M4_Q = 0;
                    M4_T = 0;
                    M5 = 0;
                    M5_P = 0;
                    M5_Q = 0;
                    M5_T = 0;
                    M6 = 0;
                    M6_P = 0;
                    M6_Q = 0;
                    M6_T = 0;
                    M7 = 0;
                    M7_P = 0;
                    M7_Q = 0;
                    M7_T = 0;
                    M8 = 0;
                    M8_P = 0;
                    M8_Q = 0;
                    M8_T = 0;
                    M9 = 0;
                    M9_P = 0;
                    M9_Q = 0;
                    M9_T = 0;
                    M10 = 0;
                    M10_P = 0;
                    M10_Q = 0;
                    M10_T = 0;
                    M11 = 0;
                    M11_P = 0;
                    M11_Q = 0;
                    M11_T = 0;
                    M12 = 0;
                    M12_P = 0;
                    M12_Q = 0;
                    M12_T = 0;
                    M13 = 0;
                    M13_P = 0;
                    M13_Q = 0;
                    M13_T = 0;
                    M14 = 0;
                    M14_P = 0;
                    M14_Q = 0;
                    M14_T = 0;
                    M15 = 0;
                    M15_P = 0;
                    M15_Q = 0;
                    M15_T = 0;
                    M16 = 0;
                    M16_P = 0;
                    M16_Q = 0;
                    M16_T = 0;
                    M17 = 0;
                    M17_P = 0;
                    M17_Q = 0;
                    M17_T = 0;
                    M18 = 0;
                    M18_P = 0;
                    M18_Q = 0;
                    M18_T = 0;
                    M19 = 0;
                    M19_P = 0;
                    M19_Q = 0;
                    M19_T = 0;
                    M20 = 0;
                    M20_P = 0;
                    M20_Q = 0;
                    M20_T = 0;

                    if x[1] != "" and x[1] != '0':
                        M1=x[1]
                        if x[2] != "" and x[2] != '0': M1_P=x[2]
                        if x[3] != "" and x[3] != '0': M1_Q=x[3]
                        if x[4] != "" and x[4] != '0': M1_T=x[4]
                        if x[0] != "" and x[0] != '0': MID_T=x[0]
                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                        self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M1_Q))
                        self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M1))
                        self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M1_P))
                        self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M1_T))
                        self.tableWidget_2.setItem(row_position, 4, QTableWidgetItem(str(MID_T)))

                    if x[6] != "" and x[6] != '0':
                        M2=x[6]
                        if x[7] != "" and x[7] != '0': M2_P=x[7]
                        if x[8] != "" and x[8] != '0': M2_Q=x[8]
                        if x[9] != "" and x[9] != '0': M2_T=x[9]
                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                        self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M2_Q))
                        self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M2))
                        self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M2_P))
                        self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M2_T))


                    if x[11] != "" and x[11] != '0':
                        M3=x[11]
                        if x[12] != "" and x[12] != '0': M3_P=x[12]
                        if x[13] != "" and x[13] != '0': M3_Q=x[13]
                        if x[14] != "" and x[14] != '0': M3_T=x[14]
                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                        self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M3_Q))
                        self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M3))
                        self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M3_P))
                        self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M3_T))


                    if x[16] != "" and x[16] != '0':
                        M4=x[16]
                        if x[17] != "" and x[17] != '0': M4_P=x[17]
                        if x[18] != "" and x[18] != '0': M4_Q=x[18]
                        if x[19] != "" and x[19] != '0': M4_T=x[19]
                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                        self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M4_Q))
                        self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M4))
                        self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M4_P))
                        self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M4_T))


                    if x[21] != "" and x[21] != '0':
                        M5=x[21]
                        if x[22] != "" and x[22] != '0': M5_P=x[22]
                        if x[23] != "" and x[23] != '0': M5_Q=x[23]
                        if x[24] != "" and x[24] != '0': M5_T=x[24]
                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                        self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M5_Q))
                        self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M5))
                        self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M5_P))
                        self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M5_T))



                    if x[26] != "" and x[26] != '0':
                        M6=x[26]
                        if x[27] != "" and x[27] != '0': M6_P=x[27]
                        if x[28] != "" and x[28] != '0': M6_Q=x[28]
                        if x[29] != "" and x[29] != '0': M6_T=x[29]
                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                        self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M6_Q))
                        self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M6))
                        self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M6_P))
                        self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M6_T))



                    if x[31] != "" and x[31] != '0':
                        M7=x[31]
                        if x[32] != "" and x[32] != '0': M7_P=x[32]
                        if x[33] != "" and x[33] != '0': M7_Q=x[33]
                        if x[34] != "" and x[34] != '0': M7_T=x[34]
                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                        self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M7_Q))
                        self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M7))
                        self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M7_P))
                        self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M7_T))


                    if x[36] != "" and x[36] != '0':
                        M8=x[36]
                        if x[37] != "" and x[37] != '0': M8_P=x[37]
                        if x[38] != "" and x[38] != '0': M8_Q=x[38]
                        if x[39] != "" and x[39] != '0':
                            M8_T=x[39]
                            row_position = self.tableWidget_2.rowCount()
                            self.tableWidget_2.insertRow(row_position)
                            self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M8_Q))
                            self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M8))
                            self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M8_P))
                            self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M8_T))


                    if x[41] != "" and x[41] != '0':
                        M9=x[41]
                        if x[42] != "" and x[42] != '0': M9_P=x[42]
                        if x[43] != "" and x[43] != '0': M9_Q=x[43]
                        if x[44] != "" and x[44] != '0': M9_T=x[44]
                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                        self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M9_Q))
                        self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M9))
                        self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M9_P))
                        self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M9_T))


                    if x[46] != "" and x[46] != '0':
                        M10=x[46]
                        if x[47] != "" and x[47] != '0': M10_P=x[47]
                        if x[48] != "" and x[48] != '0': M10_Q=x[48]
                        if x[49] != "" and x[49] != '0': M10_T=x[49]
                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                        self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M10_Q))
                        self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M10))
                        self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M10_P))
                        self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M10_T))


                    if x[51] != "" and x[51] != '0':
                        M11=x[51]
                        if x[52] != "" and x[52] != '0': M11_P=x[52]
                        if x[53] != "" and x[53] != '0': M11_Q=x[53]
                        if x[54] != "" and x[54] != '0': M11_T=x[54]
                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                        self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M11_Q))
                        self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M11))
                        self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M11_P))
                        self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M11_T))


                    if x[56] != "" and x[56] != '0':
                        M12=x[56]
                        if x[57] != "" and x[57] != '0': M12_P=x[57]
                        if x[58] != "" and x[58] != '0': M12_Q=x[58]
                        if x[59] != "" and x[59] != '0': M12_T=x[59]
                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                        self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M12_Q))
                        self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M12))
                        self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M12_P))
                        self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M12_T))

                    if x[61] != "" and x[61] != '0':
                        M13=x[61]
                        if x[62] != "" and x[62] != '0': M13_P=x[62]
                        if x[63] != "" and x[63] != '0': M13_Q=x[63]
                        if x[64] != "" and x[64] != '0': M13_T=x[64]
                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                        self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M13_Q))
                        self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M13))
                        self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M13_P))
                        self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M13_T))


                    if x[66] != "" and x[66] != '0':
                        M14=x[66]
                        if x[67] != "" and x[67] != '0': M14_P=x[67]
                        if x[68] != "" and x[68] != '0': M14_Q=x[68]
                        if x[69] != "" and x[69] != '0': M14_T=x[69]
                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                        self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M14_Q))
                        self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M14))
                        self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M14_P))
                        self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M14_T))

                    if x[71] != "" and x[71] != '0':
                        M15=x[71]
                        if x[72] != "" and x[72] != '0': M15_P=x[72]
                        if x[73] != "" and x[73] != '0': M15_Q=x[73]
                        if x[74] != "" and x[74] != '0': M15_T=x[74]
                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                        self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M15_Q))
                        self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M15))
                        self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M15_P))
                        self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M15_T))


                    if x[76] != "" and x[76] != '0':
                        M16=x[76]
                        if x[77] != "" and x[77] != '0': M16_P=x[77]
                        if x[78] != "" and x[78] != '0': M16_Q=x[78]
                        if x[79] != "" and x[79] != '0': M16_T=x[79]
                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                        self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M16_Q))
                        self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M16))
                        self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M16_P))
                        self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M16_T))



                    if x[81] != "" and x[81] != '0':
                        M17=x[81]
                        if x[82] != "" and x[82] != '0': M17_P=x[82]
                        if x[83] != "" and x[83] != '0': M17_Q=x[83]
                        if x[84] != "" and x[84] != '0': M17_T=x[84]
                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                        self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M17_Q))
                        self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M17))
                        self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M17_P))
                        self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M17_T))




                    if x[86] != "" and x[86] != '0':
                        M18=x[86]
                        if x[87] != "" and x[87] != '0': M18_P=x[87]
                        if x[88] != "" and x[88] != '0': M18_Q=x[88]
                        if x[89] != "" and x[89] != '0': M18_T=x[89]
                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                        self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M18_Q))
                        self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M18))
                        self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M18_P))
                        self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M18_T))



                    if x[91] != "" and x[91] != '0':
                        M19=x[91]
                        if x[92] != "" and x[92] != '0': M19_P=x[92]
                        if x[93] != "" and x[93] != '0': M19_Q=x[93]
                        if x[94] != "" and x[94] != '0': M19_T=x[94]
                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                        self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M19_Q))
                        self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M19))
                        self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M19_P))
                        self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M19_T))


                    if x[96] != "" and x[96] != '0':
                        M20=x[96]
                        if x[97] != "" and x[97] != '0': M20_P=x[97]
                        if x[98] != "" and x[98] != '0': M20_Q=x[98]
                        if x[99] != "" and x[99] != '0': M20_T=x[99]
                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                        self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M20_Q))
                        self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M20))
                        self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M20_P))
                        self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M20_T))

            except:
                self.statusBar().showMessage('لا يوجد معلومات ')
            self.report_total()
        if d == "Day" and m == "Month":
            try:
                d=1
                s=31
                m=1
                n=12
                y=int(y)
                t1 = datetime.datetime(y, m, d)
                t2 = datetime.datetime(y, n, s)
                # statment = "SELECT * FROM invotery WHERE Date = %s"
                statment="SELECT * FROM invotery WHERE Date BETWEEN %s and %s"
                self.cur.execute(statment, (t1,t2))
                data = self.cur.fetchall()
                for x in data:
                    M1 = 0;
                    M1_P = 0;
                    M1_Q = 0;
                    M1_T = 0;
                    M2 = 0;
                    M2_P = 0;
                    M2_Q = 0;
                    M2_T = 0;
                    M3 = 0;
                    M3_P = 0;
                    M3_Q = 0;
                    M3_T = 0;
                    M4 = 0;
                    M4_P = 0;
                    M4_Q = 0;
                    M4_T = 0;
                    M5 = 0;
                    M5_P = 0;
                    M5_Q = 0;
                    M5_T = 0;
                    M6 = 0;
                    M6_P = 0;
                    M6_Q = 0;
                    M6_T = 0;
                    M7 = 0;
                    M7_P = 0;
                    M7_Q = 0;
                    M7_T = 0;
                    M8 = 0;
                    M8_P = 0;
                    M8_Q = 0;
                    M8_T = 0;
                    M9 = 0;
                    M9_P = 0;
                    M9_Q = 0;
                    M9_T = 0;
                    M10 = 0;
                    M10_P = 0;
                    M10_Q = 0;
                    M10_T = 0;
                    M11 = 0;
                    M11_P = 0;
                    M11_Q = 0;
                    M11_T = 0;
                    M12 = 0;
                    M12_P = 0;
                    M12_Q = 0;
                    M12_T = 0;
                    M13 = 0;
                    M13_P = 0;
                    M13_Q = 0;
                    M13_T = 0;
                    M14 = 0;
                    M14_P = 0;
                    M14_Q = 0;
                    M14_T = 0;
                    M15 = 0;
                    M15_P = 0;
                    M15_Q = 0;
                    M15_T = 0;
                    M16 = 0;
                    M16_P = 0;
                    M16_Q = 0;
                    M16_T = 0;
                    M17 = 0;
                    M17_P = 0;
                    M17_Q = 0;
                    M17_T = 0;
                    M18 = 0;
                    M18_P = 0;
                    M18_Q = 0;
                    M18_T = 0;
                    M19 = 0;
                    M19_P = 0;
                    M19_Q = 0;
                    M19_T = 0;
                    M20 = 0;
                    M20_P = 0;
                    M20_Q = 0;
                    M20_T = 0;

                    if x[1] != "" and x[1] != '0':
                        M1=x[1]
                        if x[2] != "" and x[2] != '0': M1_P=x[2]
                        if x[3] != "" and x[3] != '0': M1_Q=x[3]
                        if x[4] != "" and x[4] != '0': M1_T=x[4]
                        if x[0] != "" and x[0] != '0': MID_T=x[0]
                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                        self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M1_Q))
                        self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M1))
                        self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M1_P))
                        self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M1_T))
                        self.tableWidget_2.setItem(row_position, 4, QTableWidgetItem(str(MID_T)))

                    if x[6] != "" and x[6] != '0':
                        M2=x[6]
                        if x[7] != "" and x[7] != '0': M2_P=x[7]
                        if x[8] != "" and x[8] != '0': M2_Q=x[8]
                        if x[9] != "" and x[9] != '0': M2_T=x[9]
                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                        self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M2_Q))
                        self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M2))
                        self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M2_P))
                        self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M2_T))


                    if x[11] != "" and x[11] != '0':
                        M3=x[11]
                        if x[12] != "" and x[12] != '0': M3_P=x[12]
                        if x[13] != "" and x[13] != '0': M3_Q=x[13]
                        if x[14] != "" and x[14] != '0': M3_T=x[14]
                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                        self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M3_Q))
                        self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M3))
                        self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M3_P))
                        self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M3_T))


                    if x[16] != "" and x[16] != '0':
                        M4=x[16]
                        if x[17] != "" and x[17] != '0': M4_P=x[17]
                        if x[18] != "" and x[18] != '0': M4_Q=x[18]
                        if x[19] != "" and x[19] != '0': M4_T=x[19]
                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                        self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M4_Q))
                        self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M4))
                        self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M4_P))
                        self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M4_T))


                    if x[21] != "" and x[21] != '0':
                        M5=x[21]
                        if x[22] != "" and x[22] != '0': M5_P=x[22]
                        if x[23] != "" and x[23] != '0': M5_Q=x[23]
                        if x[24] != "" and x[24] != '0': M5_T=x[24]
                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                        self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M5_Q))
                        self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M5))
                        self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M5_P))
                        self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M5_T))



                    if x[26] != "" and x[26] != '0':
                        M6=x[26]
                        if x[27] != "" and x[27] != '0': M6_P=x[27]
                        if x[28] != "" and x[28] != '0': M6_Q=x[28]
                        if x[29] != "" and x[29] != '0': M6_T=x[29]
                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                        self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M6_Q))
                        self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M6))
                        self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M6_P))
                        self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M6_T))



                    if x[31] != "" and x[31] != '0':
                        M7=x[31]
                        if x[32] != "" and x[32] != '0': M7_P=x[32]
                        if x[33] != "" and x[33] != '0': M7_Q=x[33]
                        if x[34] != "" and x[34] != '0': M7_T=x[34]
                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                        self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M7_Q))
                        self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M7))
                        self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M7_P))
                        self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M7_T))


                    if x[36] != "" and x[36] != '0':
                        M8=x[36]
                        if x[37] != "" and x[37] != '0': M8_P=x[37]
                        if x[38] != "" and x[38] != '0': M8_Q=x[38]
                        if x[39] != "" and x[39] != '0':
                            M8_T=x[39]
                            row_position = self.tableWidget_2.rowCount()
                            self.tableWidget_2.insertRow(row_position)
                            self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M8_Q))
                            self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M8))
                            self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M8_P))
                            self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M8_T))


                    if x[41] != "" and x[41] != '0':
                        M9=x[41]
                        if x[42] != "" and x[42] != '0': M9_P=x[42]
                        if x[43] != "" and x[43] != '0': M9_Q=x[43]
                        if x[44] != "" and x[44] != '0': M9_T=x[44]
                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                        self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M9_Q))
                        self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M9))
                        self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M9_P))
                        self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M9_T))


                    if x[46] != "" and x[46] != '0':
                        M10=x[46]
                        if x[47] != "" and x[47] != '0': M10_P=x[47]
                        if x[48] != "" and x[48] != '0': M10_Q=x[48]
                        if x[49] != "" and x[49] != '0': M10_T=x[49]
                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                        self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M10_Q))
                        self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M10))
                        self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M10_P))
                        self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M10_T))


                    if x[51] != "" and x[51] != '0':
                        M11=x[51]
                        if x[52] != "" and x[52] != '0': M11_P=x[52]
                        if x[53] != "" and x[53] != '0': M11_Q=x[53]
                        if x[54] != "" and x[54] != '0': M11_T=x[54]
                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                        self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M11_Q))
                        self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M11))
                        self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M11_P))
                        self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M11_T))


                    if x[56] != "" and x[56] != '0':
                        M12=x[56]
                        if x[57] != "" and x[57] != '0': M12_P=x[57]
                        if x[58] != "" and x[58] != '0': M12_Q=x[58]
                        if x[59] != "" and x[59] != '0': M12_T=x[59]
                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                        self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M12_Q))
                        self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M12))
                        self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M12_P))
                        self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M12_T))

                    if x[61] != "" and x[61] != '0':
                        M13=x[61]
                        if x[62] != "" and x[62] != '0': M13_P=x[62]
                        if x[63] != "" and x[63] != '0': M13_Q=x[63]
                        if x[64] != "" and x[64] != '0': M13_T=x[64]
                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                        self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M13_Q))
                        self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M13))
                        self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M13_P))
                        self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M13_T))


                    if x[66] != "" and x[66] != '0':
                        M14=x[66]
                        if x[67] != "" and x[67] != '0': M14_P=x[67]
                        if x[68] != "" and x[68] != '0': M14_Q=x[68]
                        if x[69] != "" and x[69] != '0': M14_T=x[69]
                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                        self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M14_Q))
                        self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M14))
                        self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M14_P))
                        self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M14_T))

                    if x[71] != "" and x[71] != '0':
                        M15=x[71]
                        if x[72] != "" and x[72] != '0': M15_P=x[72]
                        if x[73] != "" and x[73] != '0': M15_Q=x[73]
                        if x[74] != "" and x[74] != '0': M15_T=x[74]
                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                        self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M15_Q))
                        self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M15))
                        self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M15_P))
                        self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M15_T))


                    if x[76] != "" and x[76] != '0':
                        M16=x[76]
                        if x[77] != "" and x[77] != '0': M16_P=x[77]
                        if x[78] != "" and x[78] != '0': M16_Q=x[78]
                        if x[79] != "" and x[79] != '0': M16_T=x[79]
                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                        self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M16_Q))
                        self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M16))
                        self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M16_P))
                        self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M16_T))



                    if x[81] != "" and x[81] != '0':
                        M17=x[81]
                        if x[82] != "" and x[82] != '0': M17_P=x[82]
                        if x[83] != "" and x[83] != '0': M17_Q=x[83]
                        if x[84] != "" and x[84] != '0': M17_T=x[84]
                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                        self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M17_Q))
                        self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M17))
                        self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M17_P))
                        self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M17_T))




                    if x[86] != "" and x[86] != '0':
                        M18=x[86]
                        if x[87] != "" and x[87] != '0': M18_P=x[87]
                        if x[88] != "" and x[88] != '0': M18_Q=x[88]
                        if x[89] != "" and x[89] != '0': M18_T=x[89]
                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                        self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M18_Q))
                        self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M18))
                        self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M18_P))
                        self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M18_T))



                    if x[91] != "" and x[91] != '0':
                        M19=x[91]
                        if x[92] != "" and x[92] != '0': M19_P=x[92]
                        if x[93] != "" and x[93] != '0': M19_Q=x[93]
                        if x[94] != "" and x[94] != '0': M19_T=x[94]
                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                        self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M19_Q))
                        self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M19))
                        self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M19_P))
                        self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M19_T))


                    if x[96] != "" and x[96] != '0':
                        M20=x[96]
                        if x[97] != "" and x[97] != '0': M20_P=x[97]
                        if x[98] != "" and x[98] != '0': M20_Q=x[98]
                        if x[99] != "" and x[99] != '0': M20_T=x[99]
                        row_position = self.tableWidget_2.rowCount()
                        self.tableWidget_2.insertRow(row_position)
                        self.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(M20_Q))
                        self.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(M20))
                        self.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(M20_P))
                        self.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(M20_T))

            except:
                self.statusBar().showMessage('لا يوجد معلومات  ')
            self.report_total()
        self.without_delivery()
    def without_delivery(self):
        m=0
        n=0
        nrows = self.tableWidget_2.rowCount()
        for x in range(self.tableWidget_2.rowCount()):
            # row_1 =[self.tableWidget.item(x,column).text() for column in range(self.tableWidget.columnCount())]
            row_1 =self.tableWidget_2.item(x,1).text()
            if row_1 == "Delivery":
                n= int(self.tableWidget_2.item(x,3).text())
                m += n
        self.label_31.setNum(m)
        T=int(self.label_10.text())
        D=int(self.label_31.text())
        total = T - D
        self.label_34.setNum(total)





    def report_total(self):
        M=0
        for x in range(self.tableWidget_2.rowCount()):
            row_1 = int(self.tableWidget_2.item(x, 3).text())
            M += row_1
        self.label_10.setText(str(M))


    def report_invoice(self):
        nrows = self.tableWidget_4.rowCount()
        try:
            while nrows > 0:
                for row in range(0, nrows):
                    item = self.tableWidget_4.item(0, 0)
                    item_text = item.text()
                    self.tableWidget_4.removeRow(row)
        except:
            self.statusBar().showMessage('لا يوجد معلومات ok ')
        invoice=self.lineEdit_7.text()
        statment = "SELECT * FROM invotery WHERE Invotery_ID = %s"

        self.cur.execute(statment, invoice)
        data = self.cur.fetchall()
        for x in data:
            M1 = 0;
            M1_P = 0;
            M1_Q = 0;
            M1_T = 0;
            M2 = 0;
            M2_P = 0;
            M2_Q = 0;
            M2_T = 0;
            M3 = 0;
            M3_P = 0;
            M3_Q = 0;
            M3_T = 0;
            M4 = 0;
            M4_P = 0;
            M4_Q = 0;
            M4_T = 0;
            M5 = 0;
            M5_P = 0;
            M5_Q = 0;
            M5_T = 0;
            M6 = 0;
            M6_P = 0;
            M6_Q = 0;
            M6_T = 0;
            M7 = 0;
            M7_P = 0;
            M7_Q = 0;
            M7_T = 0;
            M8 = 0;
            M8_P = 0;
            M8_Q = 0;
            M8_T = 0;
            M9 = 0;
            M9_P = 0;
            M9_Q = 0;
            M9_T = 0;
            M10 = 0;
            M10_P = 0;
            M10_Q = 0;
            M10_T = 0;
            M11 = 0;
            M11_P = 0;
            M11_Q = 0;
            M11_T = 0;
            M12 = 0;
            M12_P = 0;
            M12_Q = 0;
            M12_T = 0;
            M13 = 0;
            M13_P = 0;
            M13_Q = 0;
            M13_T = 0;
            M14 = 0;
            M14_P = 0;
            M14_Q = 0;
            M14_T = 0;
            M15 = 0;
            M15_P = 0;
            M15_Q = 0;
            M15_T = 0;
            M16 = 0;
            M16_P = 0;
            M16_Q = 0;
            M16_T = 0;
            M17 = 0;
            M17_P = 0;
            M17_Q = 0;
            M17_T = 0;
            M18 = 0;
            M18_P = 0;
            M18_Q = 0;
            M18_T = 0;
            M19 = 0;
            M19_P = 0;
            M19_Q = 0;
            M19_T = 0;
            M20 = 0;
            M20_P = 0;
            M20_Q = 0;
            M20_T = 0;

            if x[1] != "" and x[1] != '0':
                M1 = x[1]
                if x[2] != "" and x[2] != '0': M1_P = x[2]
                if x[3] != "" and x[3] != '0': M1_Q = x[3]
                if x[4] != "" and x[4] != '0': M1_T = x[4]
                row_position = self.tableWidget_4.rowCount()
                self.tableWidget_4.insertRow(row_position)
                self.tableWidget_4.setItem(row_position, 0, QTableWidgetItem(M1_Q))
                self.tableWidget_4.setItem(row_position, 1, QTableWidgetItem(M1))
                self.tableWidget_4.setItem(row_position, 2, QTableWidgetItem(M1_P))
                self.tableWidget_4.setItem(row_position, 3, QTableWidgetItem(M1_T))


            if x[6] != "" and x[6] != '0':
                M2 = x[6]
                if x[7] != "" and x[7] != '0': M2_P = x[7]
                if x[8] != "" and x[8] != '0': M2_Q = x[8]
                if x[9] != "" and x[9] != '0': M2_T = x[9]
                row_position = self.tableWidget_4.rowCount()
                self.tableWidget_4.insertRow(row_position)
                self.tableWidget_4.setItem(row_position, 0, QTableWidgetItem(M2_Q))
                self.tableWidget_4.setItem(row_position, 1, QTableWidgetItem(M2))
                self.tableWidget_4.setItem(row_position, 2, QTableWidgetItem(M2_P))
                self.tableWidget_4.setItem(row_position, 3, QTableWidgetItem(M2_T))

            if x[11] != "" and x[11] != '0':
                M3 = x[11]
                if x[12] != "" and x[12] != '0': M3_P = x[12]
                if x[13] != "" and x[13] != '0': M3_Q = x[13]
                if x[14] != "" and x[14] != '0': M3_T = x[14]
                row_position = self.tableWidget_4.rowCount()
                self.tableWidget_4.insertRow(row_position)
                self.tableWidget_4.setItem(row_position, 0, QTableWidgetItem(M3_Q))
                self.tableWidget_4.setItem(row_position, 1, QTableWidgetItem(M3))
                self.tableWidget_4.setItem(row_position, 2, QTableWidgetItem(M3_P))
                self.tableWidget_4.setItem(row_position, 3, QTableWidgetItem(M3_T))

            if x[16] != "" and x[16] != '0':
                M4 = x[16]
                if x[17] != "" and x[17] != '0': M4_P = x[17]
                if x[18] != "" and x[18] != '0': M4_Q = x[18]
                if x[19] != "" and x[19] != '0': M4_T = x[19]
                row_position = self.tableWidget_4.rowCount()
                self.tableWidget_4.insertRow(row_position)
                self.tableWidget_4.setItem(row_position, 0, QTableWidgetItem(M4_Q))
                self.tableWidget_4.setItem(row_position, 1, QTableWidgetItem(M4))
                self.tableWidget_4.setItem(row_position, 2, QTableWidgetItem(M4_P))
                self.tableWidget_4.setItem(row_position, 3, QTableWidgetItem(M4_T))

            if x[21] != "" and x[21] != '0':
                M5 = x[21]
                if x[22] != "" and x[22] != '0': M5_P = x[22]
                if x[23] != "" and x[23] != '0': M5_Q = x[23]
                if x[24] != "" and x[24] != '0': M5_T = x[24]
                row_position = self.tableWidget_4.rowCount()
                self.tableWidget_4.insertRow(row_position)
                self.tableWidget_4.setItem(row_position, 0, QTableWidgetItem(M5_Q))
                self.tableWidget_4.setItem(row_position, 1, QTableWidgetItem(M5))
                self.tableWidget_4.setItem(row_position, 2, QTableWidgetItem(M5_P))
                self.tableWidget_4.setItem(row_position, 3, QTableWidgetItem(M5_T))

            if x[26] != "" and x[26] != '0':
                M6 = x[26]
                if x[27] != "" and x[27] != '0': M6_P = x[27]
                if x[28] != "" and x[28] != '0': M6_Q = x[28]
                if x[29] != "" and x[29] != '0': M6_T = x[29]
                row_position = self.tableWidget_4.rowCount()
                self.tableWidget_4.insertRow(row_position)
                self.tableWidget_4.setItem(row_position, 0, QTableWidgetItem(M6_Q))
                self.tableWidget_4.setItem(row_position, 1, QTableWidgetItem(M6))
                self.tableWidget_4.setItem(row_position, 2, QTableWidgetItem(M6_P))
                self.tableWidget_4.setItem(row_position, 3, QTableWidgetItem(M6_T))

            if x[31] != "" and x[31] != '0':
                M7 = x[31]
                if x[32] != "" and x[32] != '0': M7_P = x[32]
                if x[33] != "" and x[33] != '0': M7_Q = x[33]
                if x[34] != "" and x[34] != '0': M7_T = x[34]
                row_position = self.tableWidget_4.rowCount()
                self.tableWidget_4.insertRow(row_position)
                self.tableWidget_4.setItem(row_position, 0, QTableWidgetItem(M7_Q))
                self.tableWidget_4.setItem(row_position, 1, QTableWidgetItem(M7))
                self.tableWidget_4.setItem(row_position, 2, QTableWidgetItem(M7_P))
                self.tableWidget_4.setItem(row_position, 3, QTableWidgetItem(M7_T))

            if x[36] != "" and x[36] != '0':
                M8 = x[36]
                if x[37] != "" and x[37] != '0': M8_P = x[37]
                if x[38] != "" and x[38] != '0': M8_Q = x[38]
                if x[39] != "" and x[39] != '0':
                    M8_T = x[39]
                    row_position = self.tableWidget_4.rowCount()
                    self.tableWidget_4.insertRow(row_position)
                    self.tableWidget_4.setItem(row_position, 0, QTableWidgetItem(M8_Q))
                    self.tableWidget_4.setItem(row_position, 1, QTableWidgetItem(M8))
                    self.tableWidget_4.setItem(row_position, 2, QTableWidgetItem(M8_P))
                    self.tableWidget_4.setItem(row_position, 3, QTableWidgetItem(M8_T))

            if x[41] != "" and x[41] != '0':
                M9 = x[41]
                if x[42] != "" and x[42] != '0': M9_P = x[42]
                if x[43] != "" and x[43] != '0': M9_Q = x[43]
                if x[44] != "" and x[44] != '0': M9_T = x[44]
                row_position = self.tableWidget_4.rowCount()
                self.tableWidget_4.insertRow(row_position)
                self.tableWidget_4.setItem(row_position, 0, QTableWidgetItem(M9_Q))
                self.tableWidget_4.setItem(row_position, 1, QTableWidgetItem(M9))
                self.tableWidget_4.setItem(row_position, 2, QTableWidgetItem(M9_P))
                self.tableWidget_4.setItem(row_position, 3, QTableWidgetItem(M9_T))

            if x[46] != "" and x[46] != '0':
                M10 = x[46]
                if x[47] != "" and x[47] != '0': M10_P = x[47]
                if x[48] != "" and x[48] != '0': M10_Q = x[48]
                if x[49] != "" and x[49] != '0': M10_T = x[49]
                row_position = self.tableWidget_4.rowCount()
                self.tableWidget_4.insertRow(row_position)
                self.tableWidget_4.setItem(row_position, 0, QTableWidgetItem(M10_Q))
                self.tableWidget_4.setItem(row_position, 1, QTableWidgetItem(M10))
                self.tableWidget_4.setItem(row_position, 2, QTableWidgetItem(M10_P))
                self.tableWidget_4.setItem(row_position, 3, QTableWidgetItem(M10_T))

            if x[51] != "" and x[51] != '0':
                M11 = x[51]
                if x[52] != "" and x[52] != '0': M11_P = x[52]
                if x[53] != "" and x[53] != '0': M11_Q = x[53]
                if x[54] != "" and x[54] != '0': M11_T = x[54]
                row_position = self.tableWidget_4.rowCount()
                self.tableWidget_4.insertRow(row_position)
                self.tableWidget_4.setItem(row_position, 0, QTableWidgetItem(M11_Q))
                self.tableWidget_4.setItem(row_position, 1, QTableWidgetItem(M11))
                self.tableWidget_4.setItem(row_position, 2, QTableWidgetItem(M11_P))
                self.tableWidget_4.setItem(row_position, 3, QTableWidgetItem(M11_T))

            if x[56] != "" and x[56] != '0':
                M12 = x[56]
                if x[57] != "" and x[57] != '0': M12_P = x[57]
                if x[58] != "" and x[58] != '0': M12_Q = x[58]
                if x[59] != "" and x[59] != '0': M12_T = x[59]
                row_position = self.tableWidget_4.rowCount()
                self.tableWidget_4.insertRow(row_position)
                self.tableWidget_4.setItem(row_position, 0, QTableWidgetItem(M12_Q))
                self.tableWidget_4.setItem(row_position, 1, QTableWidgetItem(M12))
                self.tableWidget_4.setItem(row_position, 2, QTableWidgetItem(M12_P))
                self.tableWidget_4.setItem(row_position, 3, QTableWidgetItem(M12_T))

            if x[61] != "" and x[61] != '0':
                M13 = x[61]
                if x[62] != "" and x[62] != '0': M13_P = x[62]
                if x[63] != "" and x[63] != '0': M13_Q = x[63]
                if x[64] != "" and x[64] != '0': M13_T = x[64]
                row_position = self.tableWidget_4.rowCount()
                self.tableWidget_4.insertRow(row_position)
                self.tableWidget_4.setItem(row_position, 0, QTableWidgetItem(M13_Q))
                self.tableWidget_4.setItem(row_position, 1, QTableWidgetItem(M13))
                self.tableWidget_4.setItem(row_position, 2, QTableWidgetItem(M13_P))
                self.tableWidget_4.setItem(row_position, 3, QTableWidgetItem(M13_T))

            if x[66] != "" and x[66] != '0':
                M14 = x[66]
                if x[67] != "" and x[67] != '0': M14_P = x[67]
                if x[68] != "" and x[68] != '0': M14_Q = x[68]
                if x[69] != "" and x[69] != '0': M14_T = x[69]
                row_position = self.tableWidget_4.rowCount()
                self.tableWidget_4.insertRow(row_position)
                self.tableWidget_4.setItem(row_position, 0, QTableWidgetItem(M14_Q))
                self.tableWidget_4.setItem(row_position, 1, QTableWidgetItem(M14))
                self.tableWidget_4.setItem(row_position, 2, QTableWidgetItem(M14_P))
                self.tableWidget_4.setItem(row_position, 3, QTableWidgetItem(M14_T))

            if x[71] != "" and x[71] != '0':
                M15 = x[71]
                if x[72] != "" and x[72] != '0': M15_P = x[72]
                if x[73] != "" and x[73] != '0': M15_Q = x[73]
                if x[74] != "" and x[74] != '0': M15_T = x[74]
                row_position = self.tableWidget_4.rowCount()
                self.tableWidget_4.insertRow(row_position)
                self.tableWidget_4.setItem(row_position, 0, QTableWidgetItem(M15_Q))
                self.tableWidget_4.setItem(row_position, 1, QTableWidgetItem(M15))
                self.tableWidget_4.setItem(row_position, 2, QTableWidgetItem(M15_P))
                self.tableWidget_4.setItem(row_position, 3, QTableWidgetItem(M15_T))

            if x[76] != "" and x[76] != '0':
                M16 = x[76]
                if x[77] != "" and x[77] != '0': M16_P = x[77]
                if x[78] != "" and x[78] != '0': M16_Q = x[78]
                if x[79] != "" and x[79] != '0': M16_T = x[79]
                row_position = self.tableWidget_4.rowCount()
                self.tableWidget_4.insertRow(row_position)
                self.tableWidget_4.setItem(row_position, 0, QTableWidgetItem(M16_Q))
                self.tableWidget_4.setItem(row_position, 1, QTableWidgetItem(M16))
                self.tableWidget_4.setItem(row_position, 2, QTableWidgetItem(M16_P))
                self.tableWidget_4.setItem(row_position, 3, QTableWidgetItem(M16_T))

            if x[81] != "" and x[81] != '0':
                M17 = x[81]
                if x[82] != "" and x[82] != '0': M17_P = x[82]
                if x[83] != "" and x[83] != '0': M17_Q = x[83]
                if x[84] != "" and x[84] != '0': M17_T = x[84]
                row_position = self.tableWidget_4.rowCount()
                self.tableWidget_4.insertRow(row_position)
                self.tableWidget_4.setItem(row_position, 0, QTableWidgetItem(M17_Q))
                self.tableWidget_4.setItem(row_position, 1, QTableWidgetItem(M17))
                self.tableWidget_4.setItem(row_position, 2, QTableWidgetItem(M17_P))
                self.tableWidget_4.setItem(row_position, 3, QTableWidgetItem(M17_T))

            if x[86] != "" and x[86] != '0':
                M18 = x[86]
                if x[87] != "" and x[87] != '0': M18_P = x[87]
                if x[88] != "" and x[88] != '0': M18_Q = x[88]
                if x[89] != "" and x[89] != '0': M18_T = x[89]
                row_position = self.tableWidget_4.rowCount()
                self.tableWidget_4.insertRow(row_position)
                self.tableWidget_4.setItem(row_position, 0, QTableWidgetItem(M18_Q))
                self.tableWidget_4.setItem(row_position, 1, QTableWidgetItem(M18))
                self.tableWidget_4.setItem(row_position, 2, QTableWidgetItem(M18_P))
                self.tableWidget_4.setItem(row_position, 3, QTableWidgetItem(M18_T))

            if x[91] != "" and x[91] != '0':
                M19 = x[91]
                if x[92] != "" and x[92] != '0': M19_P = x[92]
                if x[93] != "" and x[93] != '0': M19_Q = x[93]
                if x[94] != "" and x[94] != '0': M19_T = x[94]
                row_position = self.tableWidget_4.rowCount()
                self.tableWidget_4.insertRow(row_position)
                self.tableWidget_4.setItem(row_position, 0, QTableWidgetItem(M19_Q))
                self.tableWidget_4.setItem(row_position, 1, QTableWidgetItem(M19))
                self.tableWidget_4.setItem(row_position, 2, QTableWidgetItem(M19_P))
                self.tableWidget_4.setItem(row_position, 3, QTableWidgetItem(M19_T))

            if x[96] != "" and x[96] != '0':
                M20 = x[96]
                if x[97] != "" and x[97] != '0': M20_P = x[97]
                if x[98] != "" and x[98] != '0': M20_Q = x[98]
                if x[99] != "" and x[99] != '0': M20_T = x[99]
                row_position = self.tableWidget_4.rowCount()
                self.tableWidget_4.insertRow(row_position)
                self.tableWidget_4.setItem(row_position, 0, QTableWidgetItem(M20_Q))
                self.tableWidget_4.setItem(row_position, 1, QTableWidgetItem(M20))
                self.tableWidget_4.setItem(row_position, 2, QTableWidgetItem(M20_P))
                self.tableWidget_4.setItem(row_position, 3, QTableWidgetItem(M20_T))

        M=0
        for x in range(self.tableWidget_4.rowCount()):
            row_1 = int(self.tableWidget_4.item(x, 3).text())
            M += row_1
        self.label_15.setText(str(M))
        self.label_36.setText(str(data[0][102]))
        self.label_12.setText(str(data[0][104]))
        self.label_13.setText(str(data[0][105]))
        self.label_35.setText(str(data[0][106]))


    def report_invoice_adv(self):
        nrows = self.tableWidget_3.rowCount()
        d=self.comboBox_10.currentText()
        m=self.comboBox_11.currentText()
        y=self.comboBox_9.currentText()

        try:
            while nrows > 0:
                for row in range(0, nrows):
                    item = self.tableWidget_3.item(0, 0)
                    item_text = item.text()
                    self.tableWidget_3.removeRow(row)
        except:
            self.statusBar().showMessage('لا يوجد معلومات ok ')
        invoice=self.lineEdit_8.text()
        if d != "Day" and m != "Month" and invoice != "" and invoice != 0:
            try:
                d=int(d)
                m=int(m)
                y=int(y)
                t2 = datetime.datetime(y, m, d)
                statment = "SELECT * FROM invotery WHERE Invoice_Num = %s AND Date = %s"

                self.cur.execute(statment, (invoice,t2))
                data = self.cur.fetchall()
                for x in data:
                    M1 = 0;
                    M1_P = 0;
                    M1_Q = 0;
                    M1_T = 0;
                    M2 = 0;
                    M2_P = 0;
                    M2_Q = 0;
                    M2_T = 0;
                    M3 = 0;
                    M3_P = 0;
                    M3_Q = 0;
                    M3_T = 0;
                    M4 = 0;
                    M4_P = 0;
                    M4_Q = 0;
                    M4_T = 0;
                    M5 = 0;
                    M5_P = 0;
                    M5_Q = 0;
                    M5_T = 0;
                    M6 = 0;
                    M6_P = 0;
                    M6_Q = 0;
                    M6_T = 0;
                    M7 = 0;
                    M7_P = 0;
                    M7_Q = 0;
                    M7_T = 0;
                    M8 = 0;
                    M8_P = 0;
                    M8_Q = 0;
                    M8_T = 0;
                    M9 = 0;
                    M9_P = 0;
                    M9_Q = 0;
                    M9_T = 0;
                    M10 = 0;
                    M10_P = 0;
                    M10_Q = 0;
                    M10_T = 0;
                    M11 = 0;
                    M11_P = 0;
                    M11_Q = 0;
                    M11_T = 0;
                    M12 = 0;
                    M12_P = 0;
                    M12_Q = 0;
                    M12_T = 0;
                    M13 = 0;
                    M13_P = 0;
                    M13_Q = 0;
                    M13_T = 0;
                    M14 = 0;
                    M14_P = 0;
                    M14_Q = 0;
                    M14_T = 0;
                    M15 = 0;
                    M15_P = 0;
                    M15_Q = 0;
                    M15_T = 0;
                    M16 = 0;
                    M16_P = 0;
                    M16_Q = 0;
                    M16_T = 0;
                    M17 = 0;
                    M17_P = 0;
                    M17_Q = 0;
                    M17_T = 0;
                    M18 = 0;
                    M18_P = 0;
                    M18_Q = 0;
                    M18_T = 0;
                    M19 = 0;
                    M19_P = 0;
                    M19_Q = 0;
                    M19_T = 0;
                    M20 = 0;
                    M20_P = 0;
                    M20_Q = 0;
                    M20_T = 0;

                    if x[1] != "" and x[1] != '0':
                        M1 = x[1]
                        if x[2] != "" and x[2] != '0': M1_P = x[2]
                        if x[3] != "" and x[3] != '0': M1_Q = x[3]
                        if x[4] != "" and x[4] != '0': M1_T = x[4]
                        row_position = self.tableWidget_3.rowCount()
                        self.tableWidget_3.insertRow(row_position)
                        self.tableWidget_3.setItem(row_position, 0, QTableWidgetItem(M1_Q))
                        # self.tableWidget_3.setItemAlignment(Qt.AlignHCenter) # change the alignment
                        self.tableWidget_3.setItem(row_position, 1, QTableWidgetItem(M1))
                        self.tableWidget_3.setItem(row_position, 2, QTableWidgetItem(M1_P))
                        self.tableWidget_3.setItem(row_position, 3, QTableWidgetItem(M1_T))


                    if x[6] != "" and x[6] != '0':
                        M2 = x[6]
                        if x[7] != "" and x[7] != '0': M2_P = x[7]
                        if x[8] != "" and x[8] != '0': M2_Q = x[8]
                        if x[9] != "" and x[9] != '0': M2_T = x[9]
                        row_position = self.tableWidget_3.rowCount()
                        self.tableWidget_3.insertRow(row_position)
                        self.tableWidget_3.setItem(row_position, 0, QTableWidgetItem(M2_Q))
                        self.tableWidget_3.setItem(row_position, 1, QTableWidgetItem(M2))
                        self.tableWidget_3.setItem(row_position, 2, QTableWidgetItem(M2_P))
                        self.tableWidget_3.setItem(row_position, 3, QTableWidgetItem(M2_T))

                    if x[11] != "" and x[11] != '0':
                        M3 = x[11]
                        if x[12] != "" and x[12] != '0': M3_P = x[12]
                        if x[13] != "" and x[13] != '0': M3_Q = x[13]
                        if x[14] != "" and x[14] != '0': M3_T = x[14]
                        row_position = self.tableWidget_3.rowCount()
                        self.tableWidget_3.insertRow(row_position)
                        self.tableWidget_3.setItem(row_position, 0, QTableWidgetItem(M3_Q))
                        self.tableWidget_3.setItem(row_position, 1, QTableWidgetItem(M3))
                        self.tableWidget_3.setItem(row_position, 2, QTableWidgetItem(M3_P))
                        self.tableWidget_3.setItem(row_position, 3, QTableWidgetItem(M3_T))

                    if x[16] != "" and x[16] != '0':
                        M4 = x[16]
                        if x[17] != "" and x[17] != '0': M4_P = x[17]
                        if x[18] != "" and x[18] != '0': M4_Q = x[18]
                        if x[19] != "" and x[19] != '0': M4_T = x[19]
                        row_position = self.tableWidget_3.rowCount()
                        self.tableWidget_3.insertRow(row_position)
                        self.tableWidget_3.setItem(row_position, 0, QTableWidgetItem(M4_Q))
                        self.tableWidget_3.setItem(row_position, 1, QTableWidgetItem(M4))
                        self.tableWidget_3.setItem(row_position, 2, QTableWidgetItem(M4_P))
                        self.tableWidget_3.setItem(row_position, 3, QTableWidgetItem(M4_T))

                    if x[21] != "" and x[21] != '0':
                        M5 = x[21]
                        if x[22] != "" and x[22] != '0': M5_P = x[22]
                        if x[23] != "" and x[23] != '0': M5_Q = x[23]
                        if x[24] != "" and x[24] != '0': M5_T = x[24]
                        row_position = self.tableWidget_3.rowCount()
                        self.tableWidget_3.insertRow(row_position)
                        self.tableWidget_3.setItem(row_position, 0, QTableWidgetItem(M5_Q))
                        self.tableWidget_3.setItem(row_position, 1, QTableWidgetItem(M5))
                        self.tableWidget_3.setItem(row_position, 2, QTableWidgetItem(M5_P))
                        self.tableWidget_3.setItem(row_position, 3, QTableWidgetItem(M5_T))

                    if x[26] != "" and x[26] != '0':
                        M6 = x[26]
                        if x[27] != "" and x[27] != '0': M6_P = x[27]
                        if x[28] != "" and x[28] != '0': M6_Q = x[28]
                        if x[29] != "" and x[29] != '0': M6_T = x[29]
                        row_position = self.tableWidget_3.rowCount()
                        self.tableWidget_3.insertRow(row_position)
                        self.tableWidget_3.setItem(row_position, 0, QTableWidgetItem(M6_Q))
                        self.tableWidget_3.setItem(row_position, 1, QTableWidgetItem(M6))
                        self.tableWidget_3.setItem(row_position, 2, QTableWidgetItem(M6_P))
                        self.tableWidget_3.setItem(row_position, 3, QTableWidgetItem(M6_T))

                    if x[31] != "" and x[31] != '0':
                        M7 = x[31]
                        if x[32] != "" and x[32] != '0': M7_P = x[32]
                        if x[33] != "" and x[33] != '0': M7_Q = x[33]
                        if x[34] != "" and x[34] != '0': M7_T = x[34]
                        row_position = self.tableWidget_3.rowCount()
                        self.tableWidget_3.insertRow(row_position)
                        self.tableWidget_3.setItem(row_position, 0, QTableWidgetItem(M7_Q))
                        self.tableWidget_3.setItem(row_position, 1, QTableWidgetItem(M7))
                        self.tableWidget_3.setItem(row_position, 2, QTableWidgetItem(M7_P))
                        self.tableWidget_3.setItem(row_position, 3, QTableWidgetItem(M7_T))

                    if x[36] != "" and x[36] != '0':
                        M8 = x[36]
                        if x[37] != "" and x[37] != '0': M8_P = x[37]
                        if x[38] != "" and x[38] != '0': M8_Q = x[38]
                        if x[39] != "" and x[39] != '0':
                            M8_T = x[39]
                            row_position = self.tableWidget_3.rowCount()
                            self.tableWidget_3.insertRow(row_position)
                            self.tableWidget_3.setItem(row_position, 0, QTableWidgetItem(M8_Q))
                            self.tableWidget_3.setItem(row_position, 1, QTableWidgetItem(M8))
                            self.tableWidget_3.setItem(row_position, 2, QTableWidgetItem(M8_P))
                            self.tableWidget_3.setItem(row_position, 3, QTableWidgetItem(M8_T))

                    if x[41] != "" and x[41] != '0':
                        M9 = x[41]
                        if x[42] != "" and x[42] != '0': M9_P = x[42]
                        if x[43] != "" and x[43] != '0': M9_Q = x[43]
                        if x[44] != "" and x[44] != '0': M9_T = x[44]
                        row_position = self.tableWidget_3.rowCount()
                        self.tableWidget_3.insertRow(row_position)
                        self.tableWidget_3.setItem(row_position, 0, QTableWidgetItem(M9_Q))
                        self.tableWidget_3.setItem(row_position, 1, QTableWidgetItem(M9))
                        self.tableWidget_3.setItem(row_position, 2, QTableWidgetItem(M9_P))
                        self.tableWidget_3.setItem(row_position, 3, QTableWidgetItem(M9_T))

                    if x[46] != "" and x[46] != '0':
                        M10 = x[46]
                        if x[47] != "" and x[47] != '0': M10_P = x[47]
                        if x[48] != "" and x[48] != '0': M10_Q = x[48]
                        if x[49] != "" and x[49] != '0': M10_T = x[49]
                        row_position = self.tableWidget_3.rowCount()
                        self.tableWidget_3.insertRow(row_position)
                        self.tableWidget_3.setItem(row_position, 0, QTableWidgetItem(M10_Q))
                        self.tableWidget_3.setItem(row_position, 1, QTableWidgetItem(M10))
                        self.tableWidget_3.setItem(row_position, 2, QTableWidgetItem(M10_P))
                        self.tableWidget_3.setItem(row_position, 3, QTableWidgetItem(M10_T))

                    if x[51] != "" and x[51] != '0':
                        M11 = x[51]
                        if x[52] != "" and x[52] != '0': M11_P = x[52]
                        if x[53] != "" and x[53] != '0': M11_Q = x[53]
                        if x[54] != "" and x[54] != '0': M11_T = x[54]
                        row_position = self.tableWidget_3.rowCount()
                        self.tableWidget_3.insertRow(row_position)
                        self.tableWidget_3.setItem(row_position, 0, QTableWidgetItem(M11_Q))
                        self.tableWidget_3.setItem(row_position, 1, QTableWidgetItem(M11))
                        self.tableWidget_3.setItem(row_position, 2, QTableWidgetItem(M11_P))
                        self.tableWidget_3.setItem(row_position, 3, QTableWidgetItem(M11_T))

                    if x[56] != "" and x[56] != '0':
                        M12 = x[56]
                        if x[57] != "" and x[57] != '0': M12_P = x[57]
                        if x[58] != "" and x[58] != '0': M12_Q = x[58]
                        if x[59] != "" and x[59] != '0': M12_T = x[59]
                        row_position = self.tableWidget_3.rowCount()
                        self.tableWidget_3.insertRow(row_position)
                        self.tableWidget_3.setItem(row_position, 0, QTableWidgetItem(M12_Q))
                        self.tableWidget_3.setItem(row_position, 1, QTableWidgetItem(M12))
                        self.tableWidget_3.setItem(row_position, 2, QTableWidgetItem(M12_P))
                        self.tableWidget_3.setItem(row_position, 3, QTableWidgetItem(M12_T))

                    if x[61] != "" and x[61] != '0':
                        M13 = x[61]
                        if x[62] != "" and x[62] != '0': M13_P = x[62]
                        if x[63] != "" and x[63] != '0': M13_Q = x[63]
                        if x[64] != "" and x[64] != '0': M13_T = x[64]
                        row_position = self.tableWidget_3.rowCount()
                        self.tableWidget_3.insertRow(row_position)
                        self.tableWidget_3.setItem(row_position, 0, QTableWidgetItem(M13_Q))
                        self.tableWidget_3.setItem(row_position, 1, QTableWidgetItem(M13))
                        self.tableWidget_3.setItem(row_position, 2, QTableWidgetItem(M13_P))
                        self.tableWidget_3.setItem(row_position, 3, QTableWidgetItem(M13_T))

                    if x[66] != "" and x[66] != '0':
                        M14 = x[66]
                        if x[67] != "" and x[67] != '0': M14_P = x[67]
                        if x[68] != "" and x[68] != '0': M14_Q = x[68]
                        if x[69] != "" and x[69] != '0': M14_T = x[69]
                        row_position = self.tableWidget_3.rowCount()
                        self.tableWidget_3.insertRow(row_position)
                        self.tableWidget_3.setItem(row_position, 0, QTableWidgetItem(M14_Q))
                        self.tableWidget_3.setItem(row_position, 1, QTableWidgetItem(M14))
                        self.tableWidget_3.setItem(row_position, 2, QTableWidgetItem(M14_P))
                        self.tableWidget_3.setItem(row_position, 3, QTableWidgetItem(M14_T))

                    if x[71] != "" and x[71] != '0':
                        M15 = x[71]
                        if x[72] != "" and x[72] != '0': M15_P = x[72]
                        if x[73] != "" and x[73] != '0': M15_Q = x[73]
                        if x[74] != "" and x[74] != '0': M15_T = x[74]
                        row_position = self.tableWidget_3.rowCount()
                        self.tableWidget_3.insertRow(row_position)
                        self.tableWidget_3.setItem(row_position, 0, QTableWidgetItem(M15_Q))
                        self.tableWidget_3.setItem(row_position, 1, QTableWidgetItem(M15))
                        self.tableWidget_3.setItem(row_position, 2, QTableWidgetItem(M15_P))
                        self.tableWidget_3.setItem(row_position, 3, QTableWidgetItem(M15_T))

                    if x[76] != "" and x[76] != '0':
                        M16 = x[76]
                        if x[77] != "" and x[77] != '0': M16_P = x[77]
                        if x[78] != "" and x[78] != '0': M16_Q = x[78]
                        if x[79] != "" and x[79] != '0': M16_T = x[79]
                        row_position = self.tableWidget_3.rowCount()
                        self.tableWidget_3.insertRow(row_position)
                        self.tableWidget_3.setItem(row_position, 0, QTableWidgetItem(M16_Q))
                        self.tableWidget_3.setItem(row_position, 1, QTableWidgetItem(M16))
                        self.tableWidget_3.setItem(row_position, 2, QTableWidgetItem(M16_P))
                        self.tableWidget_3.setItem(row_position, 3, QTableWidgetItem(M16_T))

                    if x[81] != "" and x[81] != '0':
                        M17 = x[81]
                        if x[82] != "" and x[82] != '0': M17_P = x[82]
                        if x[83] != "" and x[83] != '0': M17_Q = x[83]
                        if x[84] != "" and x[84] != '0': M17_T = x[84]
                        row_position = self.tableWidget_3.rowCount()
                        self.tableWidget_3.insertRow(row_position)
                        self.tableWidget_3.setItem(row_position, 0, QTableWidgetItem(M17_Q))
                        self.tableWidget_3.setItem(row_position, 1, QTableWidgetItem(M17))
                        self.tableWidget_3.setItem(row_position, 2, QTableWidgetItem(M17_P))
                        self.tableWidget_3.setItem(row_position, 3, QTableWidgetItem(M17_T))

                    if x[86] != "" and x[86] != '0':
                        M18 = x[86]
                        if x[87] != "" and x[87] != '0': M18_P = x[87]
                        if x[88] != "" and x[88] != '0': M18_Q = x[88]
                        if x[89] != "" and x[89] != '0': M18_T = x[89]
                        row_position = self.tableWidget_3.rowCount()
                        self.tableWidget_3.insertRow(row_position)
                        self.tableWidget_3.setItem(row_position, 0, QTableWidgetItem(M18_Q))
                        self.tableWidget_3.setItem(row_position, 1, QTableWidgetItem(M18))
                        self.tableWidget_3.setItem(row_position, 2, QTableWidgetItem(M18_P))
                        self.tableWidget_3.setItem(row_position, 3, QTableWidgetItem(M18_T))

                    if x[91] != "" and x[91] != '0':
                        M19 = x[91]
                        if x[92] != "" and x[92] != '0': M19_P = x[92]
                        if x[93] != "" and x[93] != '0': M19_Q = x[93]
                        if x[94] != "" and x[94] != '0': M19_T = x[94]
                        row_position = self.tableWidget_3.rowCount()
                        self.tableWidget_3.insertRow(row_position)
                        self.tableWidget_3.setItem(row_position, 0, QTableWidgetItem(M19_Q))
                        self.tableWidget_3.setItem(row_position, 1, QTableWidgetItem(M19))
                        self.tableWidget_3.setItem(row_position, 2, QTableWidgetItem(M19_P))
                        self.tableWidget_3.setItem(row_position, 3, QTableWidgetItem(M19_T))

                    if x[96] != "" and x[96] != '0':
                        M20 = x[96]
                        if x[97] != "" and x[97] != '0': M20_P = x[97]
                        if x[98] != "" and x[98] != '0': M20_Q = x[98]
                        if x[99] != "" and x[99] != '0': M20_T = x[99]
                        row_position = self.tableWidget_3.rowCount()
                        self.tableWidget_3.insertRow(row_position)
                        self.tableWidget_3.setItem(row_position, 0, QTableWidgetItem(M20_Q))
                        self.tableWidget_3.setItem(row_position, 1, QTableWidgetItem(M20))
                        self.tableWidget_3.setItem(row_position, 2, QTableWidgetItem(M20_P))
                        self.tableWidget_3.setItem(row_position, 3, QTableWidgetItem(M20_T))
                M = 0
                for x in range(self.tableWidget_3.rowCount()):
                    row_1 = int(self.tableWidget_3.item(x, 3).text())
                    M += row_1
                self.label_38.setText(str(M))
                self.label_39.setText(str(data[0][102]))
                self.label_41.setText(str(data[0][104]))
                self.label_40.setText(str(data[0][105]))
                self.label_42.setText(str(data[0][106]))

            except:
                self.statusBar().showMessage('لا يوجد معلومات ')







    def receipt(self):
        invoice = int(self.label_7.text())
        self.db = pymysql.connect(host='localhost', user='root', password='', db='db')
        self.cur = self.db.cursor()
        statment = "SELECT * FROM invotery WHERE Invoice_Num = %s AND Date=CURRENT_DATE()"

        self.cur.execute(statment, invoice)
        data = self.cur.fetchall()
        for x in data:
            M1 = ""; M1_P = ""; M1_Q = ""; M1_T = 0; M2 = ""; M2_P = ""; M2_Q = ""; M2_T = 0; M3 = ""; M3_P = ""; M3_Q = ""; M3_T = 0; M4 = ""; M4_P = ""; M4_Q = ""; M4_T = 0; M5 = ""; M5_P = ""; M5_Q = ""; M5_T = 0; M6 = ""; M6_P = ""; M6_Q = ""; M6_T = 0;
            M7 = ""; M7_P = ""; M7_Q = ""; M7_T = 0; M8 = ""; M8_P = ""; M8_Q = ""; M8_T = 0; M9 = ""; M9_P = ""; M9_Q = ""; M9_T = 0; M10 = ""; M10_P = ""; M10_Q = "";  M10_T = 0; M11 = "";  M11_P = ""; M11_Q = ""; M11_T = 0; M12 = ""; M12_P = "";
            M12_Q = ""; M12_T = 0; M13 = ""; M13_P = ""; M13_Q = ""; M13_T = 0; M14 = ""; M14_P = ""; M14_Q = ""; M14_T = 0; M15 = ""; M15_P = ""; M15_Q = ""; M15_T = 0; M16 = ""; M16_P = ""; M16_Q = ""; M16_T = 0; M17 = ""; M17_P = ""; M17_Q = "";
            M17_T = 0; M18 = ""; M18_P = ""; M18_Q = ""; M18_T = 0; M19 = ""; M19_P = ""; M19_Q = ""; M19_T = 0; M20 = ""; M20_P = ""; M20_Q = ""; M20_T = 0; M1_Y = "";  M2_Y = ""; M3_Y = ""; M4_Y = ""; M5_Y = ""; M6_Y = ""; M7_Y = ""; M8_Y = "";
            M9_Y = ""; M10_Y = ""; M11_Y = ""; M12_Y = ""; M13_Y = ""; M14_Y = ""; M15_Y = ""; M16_Y = ""; M17_Y = ""; M18_Y = ""; M19_Y = ""; M20_Y = "";
            if x[1] != "" and x[1] != '0':
                M1 = x[1]
                if x[2] != "" and x[2] != '0': M1_P = x[2]
                if x[3] != "" and x[3] != '0': M1_Q = x[3]
                if x[4] != "" and x[4] != '0': M1_T = x[4]

            if x[6] != "" and x[6] != '0':
                M2 = x[6]
                if x[7] != "" and x[7] != '0': M2_P = x[7]
                if x[8] != "" and x[8] != '0': M2_Q = x[8]
                if x[9] != "" and x[9] != '0': M2_T = x[9]

            if x[11] != "" and x[11] != '0':
                M3 = x[11]
                if x[12] != "" and x[12] != '0': M3_P = x[12]
                if x[13] != "" and x[13] != '0': M3_Q = x[13]
                if x[14] != "" and x[14] != '0': M3_T = x[14]

            if x[16] != "" and x[16] != '0':
                M4 = x[16]
                if x[17] != "" and x[17] != '0': M4_P = x[17]
                if x[18] != "" and x[18] != '0': M4_Q = x[18]
                if x[19] != "" and x[19] != '0': M4_T = x[19]

            if x[21] != "" and x[21] != '0':
                M5 = x[21]
                if x[22] != "" and x[22] != '0': M5_P = x[22]
                if x[23] != "" and x[23] != '0': M5_Q = x[23]
                if x[24] != "" and x[24] != '0': M5_T = x[24]

            if x[26] != "" and x[26] != '0':
                M6 = x[26]
                if x[27] != "" and x[27] != '0': M6_P = x[27]
                if x[28] != "" and x[28] != '0': M6_Q = x[28]
                if x[29] != "" and x[29] != '0': M6_T = x[29]

            if x[31] != "" and x[31] != '0':
                M7 = x[31]
                if x[32] != "" and x[32] != '0': M7_P = x[32]
                if x[33] != "" and x[33] != '0': M7_Q = x[33]
                if x[34] != "" and x[34] != '0': M7_T = x[34]

            if x[36] != "" and x[36] != '0':
                M8 = x[36]
                if x[37] != "" and x[37] != '0': M8_P = x[37]
                if x[38] != "" and x[38] != '0': M8_Q = x[38]
                if x[39] != "" and x[39] != '0': M8_T = x[39]

            if x[41] != "" and x[41] != '0':
                M9 = x[41]
                if x[42] != "" and x[42] != '0': M9_P = x[42]
                if x[43] != "" and x[43] != '0': M9_Q = x[43]
                if x[44] != "" and x[44] != '0': M9_T = x[44]

            if x[46] != "" and x[46] != '0':
                M10 = x[46]
                if x[47] != "" and x[47] != '0': M10_P = x[47]
                if x[48] != "" and x[48] != '0': M10_Q = x[48]
                if x[49] != "" and x[49] != '0': M10_T = x[49]

            if x[51] != "" and x[51] != '0':
                M11 = x[51]
                if x[52] != "" and x[52] != '0': M11_P = x[52]
                if x[53] != "" and x[53] != '0': M11_Q = x[53]
                if x[54] != "" and x[54] != '0': M11_T = x[54]

            if x[56] != "" and x[56] != '0':
                M12 = x[56]
                if x[57] != "" and x[57] != '0': M12_P = x[57]
                if x[58] != "" and x[58] != '0': M12_Q = x[58]
                if x[59] != "" and x[59] != '0': M12_T = x[59]

            if x[61] != "" and x[61] != '0':
                M13 = x[61]
                if x[62] != "" and x[62] != '0': M13_P = x[62]
                if x[63] != "" and x[63] != '0': M13_Q = x[63]
                if x[64] != "" and x[64] != '0': M13_T = x[64]

            if x[66] != "" and x[66] != '0':
                M14 = x[66]
                if x[67] != "" and x[67] != '0': M14_P = x[67]
                if x[68] != "" and x[68] != '0': M14_Q = x[68]
                if x[69] != "" and x[69] != '0': M14_T = x[69]

            if x[71] != "" and x[71] != '0':
                M15 = x[71]
                if x[72] != "" and x[72] != '0': M15_P = x[72]
                if x[73] != "" and x[73] != '0': M15_Q = x[73]
                if x[74] != "" and x[74] != '0': M15_T = x[74]

            if x[76] != "" and x[76] != '0':
                M16 = x[76]
                if x[77] != "" and x[77] != '0': M16_P = x[77]
                if x[78] != "" and x[78] != '0': M16_Q = x[78]
                if x[79] != "" and x[79] != '0': M16_T = x[79]

            if x[81] != "" and x[81] != '0':
                M17 = x[81]
                if x[82] != "" and x[82] != '0': M17_P = x[82]
                if x[83] != "" and x[83] != '0': M17_Q = x[83]
                if x[84] != "" and x[84] != '0': M17_T = x[84]

            if x[86] != "" and x[86] != '0':
                M18 = x[86]
                if x[87] != "" and x[87] != '0': M18_P = x[87]
                if x[88] != "" and x[88] != '0': M18_Q = x[88]
                if x[89] != "" and x[89] != '0': M18_T = x[89]

            if x[91] != "" and x[91] != '0':
                M19 = x[91]
                if x[92] != "" and x[92] != '0': M19_P = x[92]
                if x[93] != "" and x[93] != '0': M19_Q = x[93]
                if x[94] != "" and x[94] != '0': M19_T = x[94]

            if x[96] != "" and x[96] != '0':
                M20 = x[96]
                if x[97] != "" and x[97] != '0': M20_P = x[97]
                if x[98] != "" and x[98] != '0': M20_Q = x[98]
                if x[99] != "" and x[99] != '0': M20_T = x[99]
        # print(M1 , M1_P , M1_Q ,M1_T ,"\n",M2 , M2_P , M2_Q ,M2_T ,"\n",M3 , M3_P , M3_Q ,M3_T ,"\n",M4 , M4_P , M4_Q ,M4_T ,"\n",M5 , M5_P , M5_Q ,M5_T ,"\n",M6 , M6_P , M6_Q ,M6_T ,"\n",M7 , M7_P , M7_Q ,M7_T ,"\n",M8 , M8_P , M8_Q ,M8_T ,"\n",M9 , M9_P , M9_Q ,M9_T ,"\n",M10 , M10_P , M10_Q ,M10_T ,"\n",M11 , M11_P , M11_Q ,M11_T ,"\n",M12 , M12_P , M12_Q ,M12_T ,"\n",M13 , M13_P , M13_Q ,M13_T ,"\n",M14 , M14_P , M14_Q ,M14_T ,"\n",M15 , M15_P , M15_Q ,M15_T ,"\n",M16 , M16_P , M16_Q ,M16_T ,"\n",M17 , M17_P , M17_Q ,M17_T ,"\n",M18 , M18_P , M18_Q ,M18_T ,"\n",M19 , M19_P , M19_Q ,M19_T ,"\n",M20 , M20_P , M20_Q ,M20_T )
        auto=M1 , M1_P , M1_Q ,M1_T ,M2 , M2_P , M2_Q ,M2_T ,M3 , M3_P , M3_Q ,M3_T ,M4 , M4_P , M4_Q ,M4_T ,M5 , M5_P , M5_Q ,M5_T ,M6 , M6_P , M6_Q ,M6_T ,M7 , M7_P , M7_Q ,M7_T ,M8 , M8_P , M8_Q ,M8_T ,M9 , M9_P , M9_Q ,M9_T ,M10 , M10_P , M10_Q ,M10_T ,M11 , M11_P , M11_Q ,M11_T ,M12 , M12_P , M12_Q ,M12_T ,M13 , M13_P , M13_Q ,M13_T ,M14 , M14_P , M14_Q ,M14_T ,M15 , M15_P , M15_Q ,M15_T ,M16 , M16_P , M16_Q ,M16_T ,M17 , M17_P , M17_Q ,M17_T ,M18 , M18_P , M18_Q ,M18_T ,M19 , M19_P , M19_Q ,M19_T ,M20 , M20_P , M20_Q ,M20_T
        filename = "Receipt.txt"
        myFile= open("Receipt.txt","wt",encoding='utf-8')
        myFile.write(str(data[0][102]) )
        myFile.write("               ")
        myFile.write(str(invoice))
        myFile.write("\n")
        myFile.write("Name: ")
        myFile.write( str(data[0][104]))
        myFile.write("\n")
        myFile.write("Phone: ")
        myFile.write( str(data[0][105]))
        myFile.write("\n")
        myFile.write("Address: ")
        if len(data[0][106]) > 26:
            myFile.write("\n")
            myFile.write(str(data[0][106] ))
        else:
            myFile.write( str(data[0][106]))
        # print(len(data[0][106]))
        myFile.write("\n")
        myFile.write("**************************************************\n")
        myFile.write("\t       Chicken Zinger \t\t\n")
        myFile.write("**************************************************\n")
        myFile.write("-----------------------------------------------------------------\n")
        myFile.write("ITEM  \t           PRICE   QUANTITY  TOTAL \n")
        myFile.write("-----------------------------------------------------------------\n")
        if M1 !="":
            if len(auto[0]) >8 :
                myFile.write(auto[0] + "\t")
            else:
                myFile.write(auto[0]+"\t\t")
            myFile.write(auto[1]+"\t")
            myFile.write(auto[2]+"\t")
            myFile.write(auto[3]+"\n")
        if M2 !="":
            if len(auto[4]) >8 :
                myFile.write(auto[4]+"\t")
            else:
                myFile.write(auto[4] + "\t\t")
            myFile.write(auto[5] + "\t")
            myFile.write(auto[6] + "\t")
            myFile.write(auto[7] + "\n")
        if M3 !="":
            if len(auto[8]) >8 :
                myFile.write(auto[8]+"\t")
            else:
                myFile.write(auto[8] + "\t\t")
            myFile.write(auto[9] + "\t")
            myFile.write(auto[10] + "\t")
            myFile.write(auto[11] + "\n")
        if M4 !="":
            if len(auto[12]) >8 :
                myFile.write(auto[12]+"\t")
            else:
                myFile.write(auto[12] + "\t\t")
            myFile.write(auto[13] + "\t")
            myFile.write(auto[14] + "\t")
            myFile.write(auto[15] + "\n")
        if M5 !="":
            if len(auto[16]) >8 :
                myFile.write(auto[16]+"\t")
            else:
                myFile.write(auto[16] + "\t\t")
            myFile.write(auto[17] + "\t")
            myFile.write(auto[18] + "\t")
            myFile.write(auto[19] + "\n")
        if M6 !="":
            if len(auto[20]) >8 :
                myFile.write(auto[20]+"\t")
            else:
                myFile.write(auto[20]+"\t\t")
            myFile.write(auto[21]+"\t")
            myFile.write(auto[22]+"\t")
            myFile.write(auto[23]+"\n")
        if M7 !="":
            if len(auto[24]) >8 :
                myFile.write(auto[24]+"\t")
            else:
                myFile.write(auto[24] + "\t\t")
            myFile.write(auto[25] + "\t")
            myFile.write(auto[26] + "\t")
            myFile.write(auto[27] + "\n")
        if M8 !="":
            if len(auto[28]) >8 :
                myFile.write(auto[28]+"\t")
            else:
                myFile.write(auto[28]+"\t\t")
            myFile.write(auto[29]+"\t")
            myFile.write(auto[30]+"\t")
            myFile.write(auto[31]+"\n")
        if M9 !="":
            if len(auto[32]) >8 :
                myFile.write(auto[32] + "\t")
            else:
                myFile.write(auto[32]+"\t\t")
            myFile.write(auto[33]+"\t")
            myFile.write(auto[34]+"\t")
            myFile.write(auto[35]+"\n")
        if M10 !="":
            if len(auto[36]) >8 :
                myFile.write(auto[36]+"\t")
            else:
                myFile.write(auto[36]+"\t\t")
            myFile.write(auto[37]+"\t")
            myFile.write(auto[38]+"\t")
            myFile.write(auto[39]+"\n")
        if M11 !="":
            if len(auto[40]) >8 :
                myFile.write(auto[40]+"\t")
            else:
                myFile.write(auto[40] + "\t\t")
            myFile.write(auto[41] + "\t")
            myFile.write(auto[42] + "\t")
            myFile.write(auto[43] + "\n")
        if M12 !="":
            if len(auto[44]) >8 :
                myFile.write(auto[44]+"\t")
            else:
                myFile.write(auto[44] + "\t\t")
            myFile.write(auto[45] + "\t")
            myFile.write(auto[46] + "\t")
            myFile.write(auto[47] + "\n")
        if M13 !="":
            if len(auto[48]) >8 :
                myFile.write(auto[48]+"\t")
            else:
                myFile.write(auto[48] + "\t\t")
            myFile.write(auto[49] + "\t")
            myFile.write(auto[50] + "\t")
            myFile.write(auto[51] + "\n")
        if M14 !="":
            if len(auto[52]) >8 :
                myFile.write(auto[52]+"\t")
            else:
                myFile.write(auto[52] + "\t\t")
            myFile.write(auto[53] + "\t")
            myFile.write(auto[54] + "\t")
            myFile.write(auto[55] + "\n")
        if M15 !="":
            if len(auto[56]) >8 :
                myFile.write(auto[56]+"\t")
            else:
                myFile.write(auto[56] + "\t\t")
            myFile.write(auto[57] + "\t")
            myFile.write(auto[58] + "\t")
            myFile.write(auto[59] + "\n")
        if M16 !="":
            if len(auto[60]) >8 :
                myFile.write(auto[60]+"\t")
            else:
                myFile.write(auto[60] + "\t\t")
            myFile.write(auto[61] + "\t")
            myFile.write(auto[62] + "\t")
            myFile.write(auto[63] + "\n")
        if M17 !="":
            if len(auto[64]) >8 :
                myFile.write(auto[64]+"\t")
            else:
                myFile.write(auto[64]+"\t\t")
            myFile.write(auto[65]+"\t")
            myFile.write(auto[66]+"\t")
            myFile.write(auto[67]+"\n")
        if M18 !="":
            if len(auto[68]) >8 :
                myFile.write(auto[68]+"\t")
            else:
                myFile.write(auto[68]+"\t\t")
            myFile.write(auto[69]+"\t")
            myFile.write(auto[70]+"\t")
            myFile.write(auto[71]+"\n")
        if M19 !="":
            if len(auto[72]) >8 :
                myFile.write(auto[72]+"\t")
            else:
                myFile.write(auto[72]+"\t\t")
            myFile.write(auto[73]+"\t")
            myFile.write(auto[74]+"\t")
            myFile.write(auto[75]+"\n")
        if M20 !="":
            if len(auto[76]) >8 :
                myFile.write(auto[76]+"\t")
            else:
                myFile.write(auto[76] + "\t\t")
            myFile.write(auto[77] + "\t")
            myFile.write(auto[78] + "\t")
            myFile.write(auto[79] + "\n")
        total = int(M1_T) +int( M2_T)+int(M3_T) + int(M4_T) + int(M5_T) + int(M6_T) + int(M7_T) + int(M8_T) + int(M9_T) + int(M10_T) + int(M11_T) + int(M12_T) + int(M13_T) + int(M14_T) + int(M15_T) + int(M16_T) + int(M17_T) + int(M18_T) + int(M19_T)+ int(M20_T)
        myFile.write("---------------------------------------------------------------\n")
        myFile.write("\t\t\tTOTAL = "+ str(total))
        myFile.write("\n")
        myFile.write("***********************************************\n")
        myFile.write("        We wish a delicious meal for you \n")
        myFile.write("***********************************************\n")
        myFile.write("   Delivery : 01140959192 - 01020550641 ")
        myFile.close()
        subprocess.call(['notepad', '/p', filename])



    def receipt_packup(self):
        invoice = self.lineEdit_8.text()
        d=self.comboBox_10.currentText()
        m=self.comboBox_11.currentText()
        y=self.comboBox_9.currentText()
        # statment = "SELECT * FROM invotery WHERE Invoice_Num = %s AND Date=CURRENT_DATE()"
        if d != "Day" and m != "Month" and invoice != "" and invoice != 0:
            try:
                d=int(d)
                m=int(m)
                y=int(y)
                invoice = int(invoice)
                t2 = datetime.datetime(y, m, d)
                self.db = pymysql.connect(host='localhost', user='root', password='', db='db')
                self.cur = self.db.cursor()
                statment = "SELECT * FROM invotery WHERE Invoice_Num = %s AND Date = %s"
                self.cur.execute(statment, (invoice,t2))

                data = self.cur.fetchall()
                for x in data:
                    M1 = ""; M1_P = ""; M1_Q = ""; M1_T = 0; M2 = ""; M2_P = ""; M2_Q = ""; M2_T = 0; M3 = ""; M3_P = ""; M3_Q = ""; M3_T = 0; M4 = ""; M4_P = ""; M4_Q = ""; M4_T = 0; M5 = ""; M5_P = ""; M5_Q = ""; M5_T = 0; M6 = ""; M6_P = ""; M6_Q = ""; M6_T = 0;
                    M7 = ""; M7_P = ""; M7_Q = ""; M7_T = 0; M8 = ""; M8_P = ""; M8_Q = ""; M8_T = 0; M9 = ""; M9_P = ""; M9_Q = ""; M9_T = 0; M10 = ""; M10_P = ""; M10_Q = "";  M10_T = 0; M11 = "";  M11_P = ""; M11_Q = ""; M11_T = 0; M12 = ""; M12_P = "";
                    M12_Q = ""; M12_T = 0; M13 = ""; M13_P = ""; M13_Q = ""; M13_T = 0; M14 = ""; M14_P = ""; M14_Q = ""; M14_T = 0; M15 = ""; M15_P = ""; M15_Q = ""; M15_T = 0; M16 = ""; M16_P = ""; M16_Q = ""; M16_T = 0; M17 = ""; M17_P = ""; M17_Q = "";
                    M17_T = 0; M18 = ""; M18_P = ""; M18_Q = ""; M18_T = 0; M19 = ""; M19_P = ""; M19_Q = ""; M19_T = 0; M20 = ""; M20_P = ""; M20_Q = ""; M20_T = 0; M1_Y = "";  M2_Y = ""; M3_Y = ""; M4_Y = ""; M5_Y = ""; M6_Y = ""; M7_Y = ""; M8_Y = "";
                    M9_Y = ""; M10_Y = ""; M11_Y = ""; M12_Y = ""; M13_Y = ""; M14_Y = ""; M15_Y = ""; M16_Y = ""; M17_Y = ""; M18_Y = ""; M19_Y = ""; M20_Y = "";
                    if x[1] != "" and x[1] != '0':
                        M1 = x[1]
                        if x[2] != "" and x[2] != '0': M1_P = x[2]
                        if x[3] != "" and x[3] != '0': M1_Q = x[3]
                        if x[4] != "" and x[4] != '0': M1_T = x[4]

                    if x[6] != "" and x[6] != '0':
                        M2 = x[6]
                        if x[7] != "" and x[7] != '0': M2_P = x[7]
                        if x[8] != "" and x[8] != '0': M2_Q = x[8]
                        if x[9] != "" and x[9] != '0': M2_T = x[9]

                    if x[11] != "" and x[11] != '0':
                        M3 = x[11]
                        if x[12] != "" and x[12] != '0': M3_P = x[12]
                        if x[13] != "" and x[13] != '0': M3_Q = x[13]
                        if x[14] != "" and x[14] != '0': M3_T = x[14]

                    if x[16] != "" and x[16] != '0':
                        M4 = x[16]
                        if x[17] != "" and x[17] != '0': M4_P = x[17]
                        if x[18] != "" and x[18] != '0': M4_Q = x[18]
                        if x[19] != "" and x[19] != '0': M4_T = x[19]

                    if x[21] != "" and x[21] != '0':
                        M5 = x[21]
                        if x[22] != "" and x[22] != '0': M5_P = x[22]
                        if x[23] != "" and x[23] != '0': M5_Q = x[23]
                        if x[24] != "" and x[24] != '0': M5_T = x[24]

                    if x[26] != "" and x[26] != '0':
                        M6 = x[26]
                        if x[27] != "" and x[27] != '0': M6_P = x[27]
                        if x[28] != "" and x[28] != '0': M6_Q = x[28]
                        if x[29] != "" and x[29] != '0': M6_T = x[29]

                    if x[31] != "" and x[31] != '0':
                        M7 = x[31]
                        if x[32] != "" and x[32] != '0': M7_P = x[32]
                        if x[33] != "" and x[33] != '0': M7_Q = x[33]
                        if x[34] != "" and x[34] != '0': M7_T = x[34]

                    if x[36] != "" and x[36] != '0':
                        M8 = x[36]
                        if x[37] != "" and x[37] != '0': M8_P = x[37]
                        if x[38] != "" and x[38] != '0': M8_Q = x[38]
                        if x[39] != "" and x[39] != '0': M8_T = x[39]

                    if x[41] != "" and x[41] != '0':
                        M9 = x[41]
                        if x[42] != "" and x[42] != '0': M9_P = x[42]
                        if x[43] != "" and x[43] != '0': M9_Q = x[43]
                        if x[44] != "" and x[44] != '0': M9_T = x[44]

                    if x[46] != "" and x[46] != '0':
                        M10 = x[46]
                        if x[47] != "" and x[47] != '0': M10_P = x[47]
                        if x[48] != "" and x[48] != '0': M10_Q = x[48]
                        if x[49] != "" and x[49] != '0': M10_T = x[49]

                    if x[51] != "" and x[51] != '0':
                        M11 = x[51]
                        if x[52] != "" and x[52] != '0': M11_P = x[52]
                        if x[53] != "" and x[53] != '0': M11_Q = x[53]
                        if x[54] != "" and x[54] != '0': M11_T = x[54]

                    if x[56] != "" and x[56] != '0':
                        M12 = x[56]
                        if x[57] != "" and x[57] != '0': M12_P = x[57]
                        if x[58] != "" and x[58] != '0': M12_Q = x[58]
                        if x[59] != "" and x[59] != '0': M12_T = x[59]

                    if x[61] != "" and x[61] != '0':
                        M13 = x[61]
                        if x[62] != "" and x[62] != '0': M13_P = x[62]
                        if x[63] != "" and x[63] != '0': M13_Q = x[63]
                        if x[64] != "" and x[64] != '0': M13_T = x[64]

                    if x[66] != "" and x[66] != '0':
                        M14 = x[66]
                        if x[67] != "" and x[67] != '0': M14_P = x[67]
                        if x[68] != "" and x[68] != '0': M14_Q = x[68]
                        if x[69] != "" and x[69] != '0': M14_T = x[69]

                    if x[71] != "" and x[71] != '0':
                        M15 = x[71]
                        if x[72] != "" and x[72] != '0': M15_P = x[72]
                        if x[73] != "" and x[73] != '0': M15_Q = x[73]
                        if x[74] != "" and x[74] != '0': M15_T = x[74]

                    if x[76] != "" and x[76] != '0':
                        M16 = x[76]
                        if x[77] != "" and x[77] != '0': M16_P = x[77]
                        if x[78] != "" and x[78] != '0': M16_Q = x[78]
                        if x[79] != "" and x[79] != '0': M16_T = x[79]

                    if x[81] != "" and x[81] != '0':
                        M17 = x[81]
                        if x[82] != "" and x[82] != '0': M17_P = x[82]
                        if x[83] != "" and x[83] != '0': M17_Q = x[83]
                        if x[84] != "" and x[84] != '0': M17_T = x[84]

                    if x[86] != "" and x[86] != '0':
                        M18 = x[86]
                        if x[87] != "" and x[87] != '0': M18_P = x[87]
                        if x[88] != "" and x[88] != '0': M18_Q = x[88]
                        if x[89] != "" and x[89] != '0': M18_T = x[89]

                    if x[91] != "" and x[91] != '0':
                        M19 = x[91]
                        if x[92] != "" and x[92] != '0': M19_P = x[92]
                        if x[93] != "" and x[93] != '0': M19_Q = x[93]
                        if x[94] != "" and x[94] != '0': M19_T = x[94]

                    if x[96] != "" and x[96] != '0':
                        M20 = x[96]
                        if x[97] != "" and x[97] != '0': M20_P = x[97]
                        if x[98] != "" and x[98] != '0': M20_Q = x[98]
                        if x[99] != "" and x[99] != '0': M20_T = x[99]
                # print(M1 , M1_P , M1_Q ,M1_T ,"\n",M2 , M2_P , M2_Q ,M2_T ,"\n",M3 , M3_P , M3_Q ,M3_T ,"\n",M4 , M4_P , M4_Q ,M4_T ,"\n",M5 , M5_P , M5_Q ,M5_T ,"\n",M6 , M6_P , M6_Q ,M6_T ,"\n",M7 , M7_P , M7_Q ,M7_T ,"\n",M8 , M8_P , M8_Q ,M8_T ,"\n",M9 , M9_P , M9_Q ,M9_T ,"\n",M10 , M10_P , M10_Q ,M10_T ,"\n",M11 , M11_P , M11_Q ,M11_T ,"\n",M12 , M12_P , M12_Q ,M12_T ,"\n",M13 , M13_P , M13_Q ,M13_T ,"\n",M14 , M14_P , M14_Q ,M14_T ,"\n",M15 , M15_P , M15_Q ,M15_T ,"\n",M16 , M16_P , M16_Q ,M16_T ,"\n",M17 , M17_P , M17_Q ,M17_T ,"\n",M18 , M18_P , M18_Q ,M18_T ,"\n",M19 , M19_P , M19_Q ,M19_T ,"\n",M20 , M20_P , M20_Q ,M20_T )
                auto=M1 , M1_P , M1_Q ,M1_T ,M2 , M2_P , M2_Q ,M2_T ,M3 , M3_P , M3_Q ,M3_T ,M4 , M4_P , M4_Q ,M4_T ,M5 , M5_P , M5_Q ,M5_T ,M6 , M6_P , M6_Q ,M6_T ,M7 , M7_P , M7_Q ,M7_T ,M8 , M8_P , M8_Q ,M8_T ,M9 , M9_P , M9_Q ,M9_T ,M10 , M10_P , M10_Q ,M10_T ,M11 , M11_P , M11_Q ,M11_T ,M12 , M12_P , M12_Q ,M12_T ,M13 , M13_P , M13_Q ,M13_T ,M14 , M14_P , M14_Q ,M14_T ,M15 , M15_P , M15_Q ,M15_T ,M16 , M16_P , M16_Q ,M16_T ,M17 , M17_P , M17_Q ,M17_T ,M18 , M18_P , M18_Q ,M18_T ,M19 , M19_P , M19_Q ,M19_T ,M20 , M20_P , M20_Q ,M20_T
                name=str(data[0][104])
                phone=str(data[0][105])
                address=str(data[0][106])
                filename = "Receipt.txt"
                myFile= open("Receipt.txt","wt",encoding='utf-8')
                myFile.write(str(data[0][102]) )
                myFile.write("               ")
                myFile.write(str(invoice))
                myFile.write("\n")
                myFile.write("Name: ")
                myFile.write(name)
                myFile.write("\n")
                myFile.write("Phone: ")
                myFile.write(phone)
                myFile.write("\n")
                myFile.write("Address: ")
                if len(data[0][106]) > 26:
                    myFile.write("\n")
                    myFile.write(address)
                else:
                    myFile.write(address)
                # print(len(data[0][106]))
                myFile.write("\n")
                myFile.write("**************************************************\n")
                myFile.write("\t       Chicken Zinger \t\t\n")
                myFile.write("**************************************************\n")
                myFile.write("-----------------------------------------------------------------\n")
                myFile.write("ITEM  \t           PRICE   QUANTITY  TOTAL \n")
                myFile.write("-----------------------------------------------------------------\n")
                if M1 !="":
                    if len(auto[0]) >8 :
                        myFile.write(auto[0] + "\t")
                    else:
                        myFile.write(auto[0]+"\t\t")
                    myFile.write(auto[1]+"\t")
                    myFile.write(auto[2]+"\t")
                    myFile.write(auto[3]+"\n")
                if M2 !="":
                    if len(auto[4]) >8 :
                        myFile.write(auto[4]+"\t")
                    else:
                        myFile.write(auto[4] + "\t\t")
                    myFile.write(auto[5] + "\t")
                    myFile.write(auto[6] + "\t")
                    myFile.write(auto[7] + "\n")
                if M3 !="":
                    if len(auto[8]) >8 :
                        myFile.write(auto[8]+"\t")
                    else:
                        myFile.write(auto[8] + "\t\t")
                    myFile.write(auto[9] + "\t")
                    myFile.write(auto[10] + "\t")
                    myFile.write(auto[11] + "\n")
                if M4 !="":
                    if len(auto[12]) >8 :
                        myFile.write(auto[12]+"\t")
                    else:
                        myFile.write(auto[12] + "\t\t")
                    myFile.write(auto[13] + "\t")
                    myFile.write(auto[14] + "\t")
                    myFile.write(auto[15] + "\n")
                if M5 !="":
                    if len(auto[16]) >8 :
                        myFile.write(auto[16]+"\t")
                    else:
                        myFile.write(auto[16] + "\t\t")
                    myFile.write(auto[17] + "\t")
                    myFile.write(auto[18] + "\t")
                    myFile.write(auto[19] + "\n")
                if M6 !="":
                    if len(auto[20]) >8 :
                        myFile.write(auto[20]+"\t")
                    else:
                        myFile.write(auto[20]+"\t\t")
                    myFile.write(auto[21]+"\t")
                    myFile.write(auto[22]+"\t")
                    myFile.write(auto[23]+"\n")
                if M7 !="":
                    if len(auto[24]) >8 :
                        myFile.write(auto[24]+"\t")
                    else:
                        myFile.write(auto[24] + "\t\t")
                    myFile.write(auto[25] + "\t")
                    myFile.write(auto[26] + "\t")
                    myFile.write(auto[27] + "\n")
                if M8 !="":
                    if len(auto[28]) >8 :
                        myFile.write(auto[28]+"\t")
                    else:
                        myFile.write(auto[28]+"\t\t")
                    myFile.write(auto[29]+"\t")
                    myFile.write(auto[30]+"\t")
                    myFile.write(auto[31]+"\n")
                if M9 !="":
                    if len(auto[32]) >8 :
                        myFile.write(auto[32] + "\t")
                    else:
                        myFile.write(auto[32]+"\t\t")
                    myFile.write(auto[33]+"\t")
                    myFile.write(auto[34]+"\t")
                    myFile.write(auto[35]+"\n")
                if M10 !="":
                    if len(auto[36]) >8 :
                        myFile.write(auto[36]+"\t")
                    else:
                        myFile.write(auto[36]+"\t\t")
                    myFile.write(auto[37]+"\t")
                    myFile.write(auto[38]+"\t")
                    myFile.write(auto[39]+"\n")
                if M11 !="":
                    if len(auto[40]) >8 :
                        myFile.write(auto[40]+"\t")
                    else:
                        myFile.write(auto[40] + "\t\t")
                    myFile.write(auto[41] + "\t")
                    myFile.write(auto[42] + "\t")
                    myFile.write(auto[43] + "\n")
                if M12 !="":
                    if len(auto[44]) >8 :
                        myFile.write(auto[44]+"\t")
                    else:
                        myFile.write(auto[44] + "\t\t")
                    myFile.write(auto[45] + "\t")
                    myFile.write(auto[46] + "\t")
                    myFile.write(auto[47] + "\n")
                if M13 !="":
                    if len(auto[48]) >8 :
                        myFile.write(auto[48]+"\t")
                    else:
                        myFile.write(auto[48] + "\t\t")
                    myFile.write(auto[49] + "\t")
                    myFile.write(auto[50] + "\t")
                    myFile.write(auto[51] + "\n")
                if M14 !="":
                    if len(auto[52]) >8 :
                        myFile.write(auto[52]+"\t")
                    else:
                        myFile.write(auto[52] + "\t\t")
                    myFile.write(auto[53] + "\t")
                    myFile.write(auto[54] + "\t")
                    myFile.write(auto[55] + "\n")
                if M15 !="":
                    if len(auto[56]) >8 :
                        myFile.write(auto[56]+"\t")
                    else:
                        myFile.write(auto[56] + "\t\t")
                    myFile.write(auto[57] + "\t")
                    myFile.write(auto[58] + "\t")
                    myFile.write(auto[59] + "\n")
                if M16 !="":
                    if len(auto[60]) >8 :
                        myFile.write(auto[60]+"\t")
                    else:
                        myFile.write(auto[60] + "\t\t")
                    myFile.write(auto[61] + "\t")
                    myFile.write(auto[62] + "\t")
                    myFile.write(auto[63] + "\n")
                if M17 !="":
                    if len(auto[64]) >8 :
                        myFile.write(auto[64]+"\t")
                    else:
                        myFile.write(auto[64]+"\t\t")
                    myFile.write(auto[65]+"\t")
                    myFile.write(auto[66]+"\t")
                    myFile.write(auto[67]+"\n")
                if M18 !="":
                    if len(auto[68]) >8 :
                        myFile.write(auto[68]+"\t")
                    else:
                        myFile.write(auto[68]+"\t\t")
                    myFile.write(auto[69]+"\t")
                    myFile.write(auto[70]+"\t")
                    myFile.write(auto[71]+"\n")
                if M19 !="":
                    if len(auto[72]) >8 :
                        myFile.write(auto[72]+"\t")
                    else:
                        myFile.write(auto[72]+"\t\t")
                    myFile.write(auto[73]+"\t")
                    myFile.write(auto[74]+"\t")
                    myFile.write(auto[75]+"\n")
                if M20 !="":
                    if len(auto[76]) >8 :
                        myFile.write(auto[76]+"\t")
                    else:
                        myFile.write(auto[76] + "\t\t")
                    myFile.write(auto[77] + "\t")
                    myFile.write(auto[78] + "\t")
                    myFile.write(auto[79] + "\n")
                total = int(M1_T) +int( M2_T)+int(M3_T) + int(M4_T) + int(M5_T) + int(M6_T) + int(M7_T) + int(M8_T) + int(M9_T) + int(M10_T) + int(M11_T) + int(M12_T) + int(M13_T) + int(M14_T) + int(M15_T) + int(M16_T) + int(M17_T) + int(M18_T) + int(M19_T)+ int(M20_T)
                myFile.write("---------------------------------------------------------------\n")
                myFile.write("\t\t\tTOTAL = "+ str(total))
                myFile.write("\n")
                myFile.write("***********************************************\n")
                myFile.write("        We wish a delicious meal for you \n")
                myFile.write("***********************************************\n")
                myFile.write("   Delivery : 01140959192 - 01020550641 ")
                myFile.close()
                subprocess.call(['notepad', '/p', filename])

            except:
                self.statusBar().showMessage('لا يوجد معلومات ')


    def receipt_Button(self):
        invoice = int(self.label_7.text()) -1
        self.db = pymysql.connect(host='localhost', user='root', password='', db='db')
        self.cur = self.db.cursor()
        statment = "SELECT * FROM invotery WHERE Invoice_Num = %s AND Date=CURRENT_DATE()"

        self.cur.execute(statment, invoice)
        data = self.cur.fetchall()
        for x in data:
            M1 = ""; M1_P = ""; M1_Q = ""; M1_T = 0; M2 = ""; M2_P = ""; M2_Q = ""; M2_T = 0; M3 = ""; M3_P = ""; M3_Q = ""; M3_T = 0; M4 = ""; M4_P = ""; M4_Q = ""; M4_T = 0; M5 = ""; M5_P = ""; M5_Q = ""; M5_T = 0; M6 = ""; M6_P = ""; M6_Q = ""; M6_T = 0;
            M7 = ""; M7_P = ""; M7_Q = ""; M7_T = 0; M8 = ""; M8_P = ""; M8_Q = ""; M8_T = 0; M9 = ""; M9_P = ""; M9_Q = ""; M9_T = 0; M10 = ""; M10_P = ""; M10_Q = "";  M10_T = 0; M11 = "";  M11_P = ""; M11_Q = ""; M11_T = 0; M12 = ""; M12_P = "";
            M12_Q = ""; M12_T = 0; M13 = ""; M13_P = ""; M13_Q = ""; M13_T = 0; M14 = ""; M14_P = ""; M14_Q = ""; M14_T = 0; M15 = ""; M15_P = ""; M15_Q = ""; M15_T = 0; M16 = ""; M16_P = ""; M16_Q = ""; M16_T = 0; M17 = ""; M17_P = ""; M17_Q = "";
            M17_T = 0; M18 = ""; M18_P = ""; M18_Q = ""; M18_T = 0; M19 = ""; M19_P = ""; M19_Q = ""; M19_T = 0; M20 = ""; M20_P = ""; M20_Q = ""; M20_T = 0; M1_Y = "";  M2_Y = ""; M3_Y = ""; M4_Y = ""; M5_Y = ""; M6_Y = ""; M7_Y = ""; M8_Y = "";
            M9_Y = ""; M10_Y = ""; M11_Y = ""; M12_Y = ""; M13_Y = ""; M14_Y = ""; M15_Y = ""; M16_Y = ""; M17_Y = ""; M18_Y = ""; M19_Y = ""; M20_Y = "";
            if x[1] != "" and x[1] != '0':
                M1 = x[1]
                if x[2] != "" and x[2] != '0': M1_P = x[2]
                if x[3] != "" and x[3] != '0': M1_Q = x[3]
                if x[4] != "" and x[4] != '0': M1_T = x[4]

            if x[6] != "" and x[6] != '0':
                M2 = x[6]
                if x[7] != "" and x[7] != '0': M2_P = x[7]
                if x[8] != "" and x[8] != '0': M2_Q = x[8]
                if x[9] != "" and x[9] != '0': M2_T = x[9]

            if x[11] != "" and x[11] != '0':
                M3 = x[11]
                if x[12] != "" and x[12] != '0': M3_P = x[12]
                if x[13] != "" and x[13] != '0': M3_Q = x[13]
                if x[14] != "" and x[14] != '0': M3_T = x[14]

            if x[16] != "" and x[16] != '0':
                M4 = x[16]
                if x[17] != "" and x[17] != '0': M4_P = x[17]
                if x[18] != "" and x[18] != '0': M4_Q = x[18]
                if x[19] != "" and x[19] != '0': M4_T = x[19]

            if x[21] != "" and x[21] != '0':
                M5 = x[21]
                if x[22] != "" and x[22] != '0': M5_P = x[22]
                if x[23] != "" and x[23] != '0': M5_Q = x[23]
                if x[24] != "" and x[24] != '0': M5_T = x[24]

            if x[26] != "" and x[26] != '0':
                M6 = x[26]
                if x[27] != "" and x[27] != '0': M6_P = x[27]
                if x[28] != "" and x[28] != '0': M6_Q = x[28]
                if x[29] != "" and x[29] != '0': M6_T = x[29]

            if x[31] != "" and x[31] != '0':
                M7 = x[31]
                if x[32] != "" and x[32] != '0': M7_P = x[32]
                if x[33] != "" and x[33] != '0': M7_Q = x[33]
                if x[34] != "" and x[34] != '0': M7_T = x[34]

            if x[36] != "" and x[36] != '0':
                M8 = x[36]
                if x[37] != "" and x[37] != '0': M8_P = x[37]
                if x[38] != "" and x[38] != '0': M8_Q = x[38]
                if x[39] != "" and x[39] != '0': M8_T = x[39]

            if x[41] != "" and x[41] != '0':
                M9 = x[41]
                if x[42] != "" and x[42] != '0': M9_P = x[42]
                if x[43] != "" and x[43] != '0': M9_Q = x[43]
                if x[44] != "" and x[44] != '0': M9_T = x[44]

            if x[46] != "" and x[46] != '0':
                M10 = x[46]
                if x[47] != "" and x[47] != '0': M10_P = x[47]
                if x[48] != "" and x[48] != '0': M10_Q = x[48]
                if x[49] != "" and x[49] != '0': M10_T = x[49]

            if x[51] != "" and x[51] != '0':
                M11 = x[51]
                if x[52] != "" and x[52] != '0': M11_P = x[52]
                if x[53] != "" and x[53] != '0': M11_Q = x[53]
                if x[54] != "" and x[54] != '0': M11_T = x[54]

            if x[56] != "" and x[56] != '0':
                M12 = x[56]
                if x[57] != "" and x[57] != '0': M12_P = x[57]
                if x[58] != "" and x[58] != '0': M12_Q = x[58]
                if x[59] != "" and x[59] != '0': M12_T = x[59]

            if x[61] != "" and x[61] != '0':
                M13 = x[61]
                if x[62] != "" and x[62] != '0': M13_P = x[62]
                if x[63] != "" and x[63] != '0': M13_Q = x[63]
                if x[64] != "" and x[64] != '0': M13_T = x[64]

            if x[66] != "" and x[66] != '0':
                M14 = x[66]
                if x[67] != "" and x[67] != '0': M14_P = x[67]
                if x[68] != "" and x[68] != '0': M14_Q = x[68]
                if x[69] != "" and x[69] != '0': M14_T = x[69]

            if x[71] != "" and x[71] != '0':
                M15 = x[71]
                if x[72] != "" and x[72] != '0': M15_P = x[72]
                if x[73] != "" and x[73] != '0': M15_Q = x[73]
                if x[74] != "" and x[74] != '0': M15_T = x[74]

            if x[76] != "" and x[76] != '0':
                M16 = x[76]
                if x[77] != "" and x[77] != '0': M16_P = x[77]
                if x[78] != "" and x[78] != '0': M16_Q = x[78]
                if x[79] != "" and x[79] != '0': M16_T = x[79]

            if x[81] != "" and x[81] != '0':
                M17 = x[81]
                if x[82] != "" and x[82] != '0': M17_P = x[82]
                if x[83] != "" and x[83] != '0': M17_Q = x[83]
                if x[84] != "" and x[84] != '0': M17_T = x[84]

            if x[86] != "" and x[86] != '0':
                M18 = x[86]
                if x[87] != "" and x[87] != '0': M18_P = x[87]
                if x[88] != "" and x[88] != '0': M18_Q = x[88]
                if x[89] != "" and x[89] != '0': M18_T = x[89]

            if x[91] != "" and x[91] != '0':
                M19 = x[91]
                if x[92] != "" and x[92] != '0': M19_P = x[92]
                if x[93] != "" and x[93] != '0': M19_Q = x[93]
                if x[94] != "" and x[94] != '0': M19_T = x[94]

            if x[96] != "" and x[96] != '0':
                M20 = x[96]
                if x[97] != "" and x[97] != '0': M20_P = x[97]
                if x[98] != "" and x[98] != '0': M20_Q = x[98]
                if x[99] != "" and x[99] != '0': M20_T = x[99]
        # print(M1 , M1_P , M1_Q ,M1_T ,"\n",M2 , M2_P , M2_Q ,M2_T ,"\n",M3 , M3_P , M3_Q ,M3_T ,"\n",M4 , M4_P , M4_Q ,M4_T ,"\n",M5 , M5_P , M5_Q ,M5_T ,"\n",M6 , M6_P , M6_Q ,M6_T ,"\n",M7 , M7_P , M7_Q ,M7_T ,"\n",M8 , M8_P , M8_Q ,M8_T ,"\n",M9 , M9_P , M9_Q ,M9_T ,"\n",M10 , M10_P , M10_Q ,M10_T ,"\n",M11 , M11_P , M11_Q ,M11_T ,"\n",M12 , M12_P , M12_Q ,M12_T ,"\n",M13 , M13_P , M13_Q ,M13_T ,"\n",M14 , M14_P , M14_Q ,M14_T ,"\n",M15 , M15_P , M15_Q ,M15_T ,"\n",M16 , M16_P , M16_Q ,M16_T ,"\n",M17 , M17_P , M17_Q ,M17_T ,"\n",M18 , M18_P , M18_Q ,M18_T ,"\n",M19 , M19_P , M19_Q ,M19_T ,"\n",M20 , M20_P , M20_Q ,M20_T )
        auto=M1 , M1_P , M1_Q ,M1_T ,M2 , M2_P , M2_Q ,M2_T ,M3 , M3_P , M3_Q ,M3_T ,M4 , M4_P , M4_Q ,M4_T ,M5 , M5_P , M5_Q ,M5_T ,M6 , M6_P , M6_Q ,M6_T ,M7 , M7_P , M7_Q ,M7_T ,M8 , M8_P , M8_Q ,M8_T ,M9 , M9_P , M9_Q ,M9_T ,M10 , M10_P , M10_Q ,M10_T ,M11 , M11_P , M11_Q ,M11_T ,M12 , M12_P , M12_Q ,M12_T ,M13 , M13_P , M13_Q ,M13_T ,M14 , M14_P , M14_Q ,M14_T ,M15 , M15_P , M15_Q ,M15_T ,M16 , M16_P , M16_Q ,M16_T ,M17 , M17_P , M17_Q ,M17_T ,M18 , M18_P , M18_Q ,M18_T ,M19 , M19_P , M19_Q ,M19_T ,M20 , M20_P , M20_Q ,M20_T
        filename = "Receipt.txt"
        myFile= open("Receipt.txt","wt",encoding='utf-8')
        myFile.write(str(data[0][102]) )
        myFile.write("               ")
        myFile.write(str(invoice))
        myFile.write("\n")
        myFile.write("Name: ")
        myFile.write( str(data[0][104]))
        myFile.write("\n")
        myFile.write("Phone: ")
        myFile.write( str(data[0][105]))
        myFile.write("\n")
        myFile.write("Address: ")
        if len(data[0][106]) > 26:
            myFile.write("\n")
            myFile.write(str(data[0][106] ))
        else:
            myFile.write( str(data[0][106]))
        # print(len(data[0][106]))
        myFile.write("\n")
        myFile.write("**************************************************\n")
        myFile.write("\t       Chicken Zinger \t\t\n")
        myFile.write("**************************************************\n")
        myFile.write("-----------------------------------------------------------------\n")
        myFile.write("ITEM  \t           PRICE   QUANTITY  TOTAL \n")
        myFile.write("-----------------------------------------------------------------\n")
        if M1 !="":
            if len(auto[0]) >8 :
                myFile.write(auto[0] + "\t")
            else:
                myFile.write(auto[0]+"\t\t")
            myFile.write(auto[1]+"\t")
            myFile.write(auto[2]+"\t")
            myFile.write(auto[3]+"\n")
        if M2 !="":
            if len(auto[4]) >8 :
                myFile.write(auto[4]+"\t")
            else:
                myFile.write(auto[4] + "\t\t")
            myFile.write(auto[5] + "\t")
            myFile.write(auto[6] + "\t")
            myFile.write(auto[7] + "\n")
        if M3 !="":
            if len(auto[8]) >8 :
                myFile.write(auto[8]+"\t")
            else:
                myFile.write(auto[8] + "\t\t")
            myFile.write(auto[9] + "\t")
            myFile.write(auto[10] + "\t")
            myFile.write(auto[11] + "\n")
        if M4 !="":
            if len(auto[12]) >8 :
                myFile.write(auto[12]+"\t")
            else:
                myFile.write(auto[12] + "\t\t")
            myFile.write(auto[13] + "\t")
            myFile.write(auto[14] + "\t")
            myFile.write(auto[15] + "\n")
        if M5 !="":
            if len(auto[16]) >8 :
                myFile.write(auto[16]+"\t")
            else:
                myFile.write(auto[16] + "\t\t")
            myFile.write(auto[17] + "\t")
            myFile.write(auto[18] + "\t")
            myFile.write(auto[19] + "\n")
        if M6 !="":
            if len(auto[20]) >8 :
                myFile.write(auto[20]+"\t")
            else:
                myFile.write(auto[20]+"\t\t")
            myFile.write(auto[21]+"\t")
            myFile.write(auto[22]+"\t")
            myFile.write(auto[23]+"\n")
        if M7 !="":
            if len(auto[24]) >8 :
                myFile.write(auto[24]+"\t")
            else:
                myFile.write(auto[24] + "\t\t")
            myFile.write(auto[25] + "\t")
            myFile.write(auto[26] + "\t")
            myFile.write(auto[27] + "\n")
        if M8 !="":
            if len(auto[28]) >8 :
                myFile.write(auto[28]+"\t")
            else:
                myFile.write(auto[28]+"\t\t")
            myFile.write(auto[29]+"\t")
            myFile.write(auto[30]+"\t")
            myFile.write(auto[31]+"\n")
        if M9 !="":
            if len(auto[32]) >8 :
                myFile.write(auto[32] + "\t")
            else:
                myFile.write(auto[32]+"\t\t")
            myFile.write(auto[33]+"\t")
            myFile.write(auto[34]+"\t")
            myFile.write(auto[35]+"\n")
        if M10 !="":
            if len(auto[36]) >8 :
                myFile.write(auto[36]+"\t")
            else:
                myFile.write(auto[36]+"\t\t")
            myFile.write(auto[37]+"\t")
            myFile.write(auto[38]+"\t")
            myFile.write(auto[39]+"\n")
        if M11 !="":
            if len(auto[40]) >8 :
                myFile.write(auto[40]+"\t")
            else:
                myFile.write(auto[40] + "\t\t")
            myFile.write(auto[41] + "\t")
            myFile.write(auto[42] + "\t")
            myFile.write(auto[43] + "\n")
        if M12 !="":
            if len(auto[44]) >8 :
                myFile.write(auto[44]+"\t")
            else:
                myFile.write(auto[44] + "\t\t")
            myFile.write(auto[45] + "\t")
            myFile.write(auto[46] + "\t")
            myFile.write(auto[47] + "\n")
        if M13 !="":
            if len(auto[48]) >8 :
                myFile.write(auto[48]+"\t")
            else:
                myFile.write(auto[48] + "\t\t")
            myFile.write(auto[49] + "\t")
            myFile.write(auto[50] + "\t")
            myFile.write(auto[51] + "\n")
        if M14 !="":
            if len(auto[52]) >8 :
                myFile.write(auto[52]+"\t")
            else:
                myFile.write(auto[52] + "\t\t")
            myFile.write(auto[53] + "\t")
            myFile.write(auto[54] + "\t")
            myFile.write(auto[55] + "\n")
        if M15 !="":
            if len(auto[56]) >8 :
                myFile.write(auto[56]+"\t")
            else:
                myFile.write(auto[56] + "\t\t")
            myFile.write(auto[57] + "\t")
            myFile.write(auto[58] + "\t")
            myFile.write(auto[59] + "\n")
        if M16 !="":
            if len(auto[60]) >8 :
                myFile.write(auto[60]+"\t")
            else:
                myFile.write(auto[60] + "\t\t")
            myFile.write(auto[61] + "\t")
            myFile.write(auto[62] + "\t")
            myFile.write(auto[63] + "\n")
        if M17 !="":
            if len(auto[64]) >8 :
                myFile.write(auto[64]+"\t")
            else:
                myFile.write(auto[64]+"\t\t")
            myFile.write(auto[65]+"\t")
            myFile.write(auto[66]+"\t")
            myFile.write(auto[67]+"\n")
        if M18 !="":
            if len(auto[68]) >8 :
                myFile.write(auto[68]+"\t")
            else:
                myFile.write(auto[68]+"\t\t")
            myFile.write(auto[69]+"\t")
            myFile.write(auto[70]+"\t")
            myFile.write(auto[71]+"\n")
        if M19 !="":
            if len(auto[72]) >8 :
                myFile.write(auto[72]+"\t")
            else:
                myFile.write(auto[72]+"\t\t")
            myFile.write(auto[73]+"\t")
            myFile.write(auto[74]+"\t")
            myFile.write(auto[75]+"\n")
        if M20 !="":
            if len(auto[76]) >8 :
                myFile.write(auto[76]+"\t")
            else:
                myFile.write(auto[76] + "\t\t")
            myFile.write(auto[77] + "\t")
            myFile.write(auto[78] + "\t")
            myFile.write(auto[79] + "\n")
        total = int(M1_T) +int( M2_T)+int(M3_T) + int(M4_T) + int(M5_T) + int(M6_T) + int(M7_T) + int(M8_T) + int(M9_T) + int(M10_T) + int(M11_T) + int(M12_T) + int(M13_T) + int(M14_T) + int(M15_T) + int(M16_T) + int(M17_T) + int(M18_T) + int(M19_T)+ int(M20_T)
        myFile.write("---------------------------------------------------------------\n")
        myFile.write("\t\t\tTOTAL = "+ str(total))
        myFile.write("\n")
        myFile.write("***********************************************\n")
        myFile.write("        We wish a delicious meal for you \n")
        myFile.write("***********************************************\n")
        myFile.write("   Delivery : 01140959192 - 01020550641 ")
        myFile.close()
        subprocess.call(['notepad', '/p', filename])

    def receipt_Kitchen(self):
        invoice = int(self.label_7.text())
        self.db = pymysql.connect(host='localhost', user='root', password='', db='db')
        self.cur = self.db.cursor()
        statment = "SELECT * FROM invotery WHERE Invoice_Num = %s AND Date=CURRENT_DATE()"

        self.cur.execute(statment, invoice)
        data = self.cur.fetchall()
        for x in data:
            M1 = ""; M1_P = ""; M1_Q = 0; M1_T = 0; M2 = ""; M2_P = ""; M2_Q = 0; M2_T = 0; M3 = ""; M3_P = ""; M3_Q = 0; M3_T = 0; M4 = ""; M4_P = ""; M4_Q = 0; M4_T = 0; M5 = ""; M5_P = ""; M5_Q = 0; M5_T = 0; M6 = ""; M6_P = ""; M6_Q = 0; M6_T = 0;
            M7 = ""; M7_P = ""; M7_Q = 0; M7_T = 0; M8 = ""; M8_P = ""; M8_Q = 0; M8_T = 0; M9 = ""; M9_P = ""; M9_Q = 0; M9_T = 0; M10 = ""; M10_P = ""; M10_Q = 0;  M10_T = 0; M11 = "";  M11_P = ""; M11_Q = 0; M11_T = 0; M12 = ""; M12_P = "";
            M12_Q = 0; M12_T = 0; M13 = ""; M13_P = ""; M13_Q = 0; M13_T = 0; M14 = ""; M14_P = ""; M14_Q = 0; M14_T = 0; M15 = ""; M15_P = ""; M15_Q = 0; M15_T = 0; M16 = ""; M16_P = ""; M16_Q = 0; M16_T = 0; M17 = ""; M17_P = ""; M17_Q = 0;
            M17_T = 0; M18 = ""; M18_P = ""; M18_Q = 0; M18_T = 0; M19 = ""; M19_P = ""; M19_Q = 0; M19_T = 0; M20 = ""; M20_P = ""; M20_Q = 0; M20_T = 0; M1_Y = "";  M2_Y = ""; M3_Y = ""; M4_Y = ""; M5_Y = ""; M6_Y = ""; M7_Y = ""; M8_Y = "";
            M9_Y = ""; M10_Y = ""; M11_Y = ""; M12_Y = ""; M13_Y = ""; M14_Y = ""; M15_Y = ""; M16_Y = ""; M17_Y = ""; M18_Y = ""; M19_Y = ""; M20_Y = "";
            if x[1] != "" and x[1] != '0':
                M1 = x[1]
                if x[3] != "" and x[3] != '0': M1_Q = x[3]
                if x[5] != "" and x[5] != '0': M1_T = x[5]

            if x[6] != "" and x[6] != '0':
                M2 = x[6]
                if x[8] != "" and x[8] != '0': M2_Q = x[8]
                if x[10] != "" and x[10] != '0': M2_T = x[10]

            if x[11] != "" and x[11] != '0':
                M3 = x[11]
                if x[13] != "" and x[13] != '0': M3_Q = x[13]
                if x[15] != "" and x[15] != '0': M3_T = x[15]

            if x[16] != "" and x[16] != '0':
                M4 = x[16]
                if x[18] != "" and x[18] != '0': M4_Q = x[18]
                if x[20] != "" and x[20] != '0': M4_T = x[20]

            if x[21] != "" and x[21] != '0':
                M5 = x[21]
                if x[23] != "" and x[23] != '0': M5_Q = x[23]
                if x[25] != "" and x[25] != '0': M5_T = x[25]

            if x[26] != "" and x[26] != '0':
                M6 = x[26]
                if x[28] != "" and x[28] != '0': M6_Q = x[28]
                if x[30] != "" and x[30] != '0': M6_T = x[30]

            if x[31] != "" and x[31] != '0':
                M7 = x[31]
                if x[33] != "" and x[33] != '0': M7_Q = x[33]
                if x[35] != "" and x[35] != '0': M7_T = x[35]

            if x[36] != "" and x[36] != '0':
                M8 = x[36]
                if x[38] != "" and x[38] != '0': M8_Q = x[38]
                if x[40] != "" and x[40] != '0': M8_T = x[40]

            if x[41] != "" and x[41] != '0':
                M9 = x[41]
                if x[43] != "" and x[43] != '0': M9_Q = x[43]
                if x[45] != "" and x[45] != '0': M9_T = x[45]

            if x[46] != "" and x[46] != '0':
                M10 = x[46]
                if x[48] != "" and x[48] != '0': M10_Q = x[48]
                if x[50] != "" and x[50] != '0': M10_T = x[50]

            if x[51] != "" and x[51] != '0':
                M11 = x[51]
                if x[53] != "" and x[53] != '0': M11_Q = x[53]
                if x[55] != "" and x[55] != '0': M11_T = x[55]

            if x[56] != "" and x[56] != '0':
                M12 = x[56]
                if x[58] != "" and x[58] != '0': M12_Q = x[58]
                if x[60] != "" and x[60] != '0': M12_T = x[60]

            if x[61] != "" and x[61] != '0':
                M13 = x[61]
                if x[63] != "" and x[63] != '0': M13_Q = x[63]
                if x[65] != "" and x[65] != '0': M13_T = x[65]

            if x[66] != "" and x[66] != '0':
                M14 = x[66]
                if x[68] != "" and x[68] != '0': M14_Q = x[68]
                if x[70] != "" and x[70] != '0': M14_T = x[70]

            if x[71] != "" and x[71] != '0':
                M15 = x[71]
                if x[73] != "" and x[73] != '0': M15_Q = x[73]
                if x[75] != "" and x[75] != '0': M15_T = x[75]

            if x[76] != "" and x[76] != '0':
                M16 = x[76]
                if x[78] != "" and x[78] != '0': M16_Q = x[78]
                if x[80] != "" and x[80] != '0': M16_T = x[80]

            if x[81] != "" and x[81] != '0':
                M17 = x[81]
                if x[83] != "" and x[83] != '0': M17_Q = x[83]
                if x[85] != "" and x[85] != '0': M17_T = x[85]

            if x[86] != "" and x[86] != '0':
                M18 = x[86]
                if x[88] != "" and x[88] != '0': M18_Q = x[88]
                if x[90] != "" and x[90] != '0': M18_T = x[90]

            if x[91] != "" and x[91] != '0':
                M19 = x[91]
                if x[93] != "" and x[93] != '0': M19_Q = x[93]
                if x[95] != "" and x[95] != '0': M19_T = x[95]

            if x[96] != "" and x[96] != '0':
                M20 = x[96]
                if x[98] != "" and x[98] != '0': M20_Q = x[98]
                if x[100] != "" and x[100] != '0': M20_T = x[100]
        # print(M1 , M1_P , M1_Q ,M1_T ,"\n",M2 , M2_P , M2_Q ,M2_T ,"\n",M3 , M3_P , M3_Q ,M3_T ,"\n",M4 , M4_P , M4_Q ,M4_T ,"\n",M5 , M5_P , M5_Q ,M5_T ,"\n",M6 , M6_P , M6_Q ,M6_T ,"\n",M7 , M7_P , M7_Q ,M7_T ,"\n",M8 , M8_P , M8_Q ,M8_T ,"\n",M9 , M9_P , M9_Q ,M9_T ,"\n",M10 , M10_P , M10_Q ,M10_T ,"\n",M11 , M11_P , M11_Q ,M11_T ,"\n",M12 , M12_P , M12_Q ,M12_T ,"\n",M13 , M13_P , M13_Q ,M13_T ,"\n",M14 , M14_P , M14_Q ,M14_T ,"\n",M15 , M15_P , M15_Q ,M15_T ,"\n",M16 , M16_P , M16_Q ,M16_T ,"\n",M17 , M17_P , M17_Q ,M17_T ,"\n",M18 , M18_P , M18_Q ,M18_T ,"\n",M19 , M19_P , M19_Q ,M19_T ,"\n",M20 , M20_P , M20_Q ,M20_T )
        auto=M1 , M1_P , M1_Q ,M1_T ,M2 , M2_P , M2_Q ,M2_T ,M3 , M3_P , M3_Q ,M3_T ,M4 , M4_P , M4_Q ,M4_T ,M5 , M5_P , M5_Q ,M5_T ,M6 , M6_P , M6_Q ,M6_T ,M7 , M7_P , M7_Q ,M7_T ,M8 , M8_P , M8_Q ,M8_T ,M9 , M9_P , M9_Q ,M9_T ,M10 , M10_P , M10_Q ,M10_T ,M11 , M11_P , M11_Q ,M11_T ,M12 , M12_P , M12_Q ,M12_T ,M13 , M13_P , M13_Q ,M13_T ,M14 , M14_P , M14_Q ,M14_T ,M15 , M15_P , M15_Q ,M15_T ,M16 , M16_P , M16_Q ,M16_T ,M17 , M17_P , M17_Q ,M17_T ,M18 , M18_P , M18_Q ,M18_T ,M19 , M19_P , M19_Q ,M19_T ,M20 , M20_P , M20_Q ,M20_T
        filename = "Receipt Kitchen.txt"
        myFile= open("Receipt Kitchen.txt","wt",encoding='utf-8')
        myFile.write(str(data[0][102]) )
        myFile.write("               ")
        myFile.write(str(invoice))
        myFile.write("\n")
        myFile.write("Name: ")
        myFile.write( str(data[0][104]))
        myFile.write("\n")
        myFile.write("**************************************************\n")
        myFile.write("\t       Chicken Zinger \t\t\n")
        myFile.write("**************************************************\n")
        myFile.write("-----------------------------------------------------------------\n")
        myFile.write("ITEM  \t            QUANTITY  NOTES \n")
        myFile.write("-----------------------------------------------------------------\n")
        if M1 !="":
            if len(auto[0]) >8 :
                myFile.write(auto[0] + "\t")
            else:
                myFile.write(auto[0]+"\t\t")
            myFile.write(auto[2]+"\t")
            myFile.write(str(auto[3])+"\n")
            myFile.write("---------------------------------------------------------------\n")
        if M2 !="":
            if len(auto[4]) >8 :
                myFile.write(auto[4]+"\t")
            else:
                myFile.write(auto[4] + "\t\t")
            myFile.write(auto[6] + "\t")
            myFile.write(str(auto[7]) + "\n")
            myFile.write("---------------------------------------------------------------\n")
        if M3 !="":
            if len(auto[8]) >8 :
                myFile.write(auto[8]+"\t")
            else:
                myFile.write(auto[8] + "\t\t")
            myFile.write(auto[10] + "\t")
            myFile.write(str(auto[11]) + "\n")
            myFile.write("---------------------------------------------------------------\n")
        if M4 !="":
            if len(auto[12]) >8 :
                myFile.write(auto[12]+"\t")
            else:
                myFile.write(auto[12] + "\t\t")
            myFile.write(auto[14] + "\t")
            myFile.write(str(auto[15]) + "\n")
            myFile.write("---------------------------------------------------------------\n")
        if M5 !="":
            if len(auto[16]) >8 :
                myFile.write(auto[16]+"\t")
            else:
                myFile.write(auto[16] + "\t\t")
            myFile.write(auto[18] + "\t")
            myFile.write(str(auto[19]) + "\n")
            myFile.write("---------------------------------------------------------------\n")
        if M6 !="":
            if len(auto[20]) >8 :
                myFile.write(auto[20]+"\t")
            else:
                myFile.write(auto[20]+"\t\t")
            myFile.write(auto[22]+"\t")
            myFile.write(str(auto[23])+"\n")
            myFile.write("---------------------------------------------------------------\n")
        if M7 !="":
            if len(auto[24]) >8 :
                myFile.write(auto[24]+"\t")
            else:
                myFile.write(auto[24] + "\t\t")
            myFile.write(auto[26] + "\t")
            myFile.write(str(auto[27]) + "\n")
            myFile.write("---------------------------------------------------------------\n")
        if M8 !="":
            if len(auto[28]) >8 :
                myFile.write(auto[28]+"\t")
            else:
                myFile.write(auto[28]+"\t\t")
            myFile.write(auto[30]+"\t")
            myFile.write(str(auto[31])+"\n")
            myFile.write("---------------------------------------------------------------\n")
        if M9 !="":
            if len(auto[32]) >8 :
                myFile.write(auto[32] + "\t")
            else:
                myFile.write(auto[32]+"\t\t")
            myFile.write(auto[34]+"\t")
            myFile.write(str(auto[35])+"\n")
            myFile.write("---------------------------------------------------------------\n")
        if M10 !="":
            if len(auto[36]) >8 :
                myFile.write(auto[36]+"\t")
            else:
                myFile.write(auto[36]+"\t\t")
            myFile.write(auto[38]+"\t")
            myFile.write(str(auto[39])+"\n")
            myFile.write("---------------------------------------------------------------\n")
        if M11 !="":
            if len(auto[40]) >8 :
                myFile.write(auto[40]+"\t")
            else:
                myFile.write(auto[40] + "\t\t")
            myFile.write(auto[42] + "\t")
            myFile.write(str(auto[43]) + "\n")
            myFile.write("---------------------------------------------------------------\n")
        if M12 !="":
            if len(auto[44]) >8 :
                myFile.write(auto[44]+"\t")
            else:
                myFile.write(auto[44] + "\t\t")
            myFile.write(auto[46] + "\t")
            myFile.write(str(auto[47]) + "\n")
            myFile.write("---------------------------------------------------------------\n")
        if M13 !="":
            if len(auto[48]) >8 :
                myFile.write(auto[48]+"\t")
            else:
                myFile.write(auto[48] + "\t\t")
            myFile.write(auto[50] + "\t")
            myFile.write(str(auto[51]) + "\n")
            myFile.write("---------------------------------------------------------------\n")
        if M14 !="":
            if len(auto[52]) >8 :
                myFile.write(auto[52]+"\t")
            else:
                myFile.write(auto[52] + "\t\t")
            myFile.write(auto[54] + "\t")
            myFile.write(str(auto[55]) + "\n")
            myFile.write("---------------------------------------------------------------\n")
        if M15 !="":
            if len(auto[56]) >8 :
                myFile.write(auto[56]+"\t")
            else:
                myFile.write(auto[56] + "\t\t")
            myFile.write(auto[58] + "\t")
            myFile.write(str(auto[59]) + "\n")
            myFile.write("---------------------------------------------------------------\n")
        if M16 !="":
            if len(auto[60]) >8 :
                myFile.write(auto[60]+"\t")
            else:
                myFile.write(auto[60] + "\t\t")
            myFile.write(auto[62] + "\t")
            myFile.write(str(auto[63]) + "\n")
            myFile.write("---------------------------------------------------------------\n")
        if M17 !="":
            if len(auto[64]) >8 :
                myFile.write(auto[64]+"\t")
            else:
                myFile.write(auto[64]+"\t\t")
            myFile.write(auto[66]+"\t")
            myFile.write(str(auto[67])+"\n")
            myFile.write("---------------------------------------------------------------\n")
        if M18 !="":
            if len(auto[68]) >8 :
                myFile.write(auto[68]+"\t")
            else:
                myFile.write(auto[68]+"\t\t")
            myFile.write(auto[70]+"\t")
            myFile.write(str(auto[71])+"\n")
            myFile.write("---------------------------------------------------------------\n")
        if M19 !="":
            if len(auto[72]) >8 :
                myFile.write(auto[72]+"\t")
            else:
                myFile.write(auto[72]+"\t\t")
            myFile.write(auto[74]+"\t")
            myFile.write(str(auto[75])+"\n")
            myFile.write("---------------------------------------------------------------\n")
        if M20 !="":
            if len(auto[76]) >8 :
                myFile.write(auto[76]+"\t")
            else:
                myFile.write(auto[76] + "\t\t")
            myFile.write(auto[78] + "\t")
            myFile.write(str(auto[79]) + "\n")
        total = int(M1_Q) +int( M2_Q)+int(M3_Q) + int(M4_Q) + int(M5_Q) + int(M6_Q) + int(M7_Q) + int(M8_Q) + int(M9_Q) + int(M10_Q) + int(M11_Q) + int(M12_Q) + int(M13_Q) + int(M14_Q) + int(M15_Q) + int(M16_Q) + int(M17_Q) + int(M18_Q) + int(M19_Q)+ int(M20_Q)
        myFile.write("***********************************************\n")
        nan = total -1
        if M1 or M2 or M3 or M4 or M5 or M6 or M7 or M8 or M9 or M10 or M11 or M12 or M13 or M14 or M15 or M16 or M17 or M18 or M19 or M20 == "Delivery":
            myFile.write("\tTOTAL Item = "+ str(nan))
        else:
            myFile.write("\tTOTAL Item = " + str(total))
        myFile.write("\n")
        myFile.write("***********************************************\n")
        myFile.close()
        subprocess.call(['notepad', '/p', filename])


    def receipt_Kitchen_prev(self):
        invoice = int(self.label_7.text()) -1
        self.db = pymysql.connect(host='localhost', user='root', password='', db='db')
        self.cur = self.db.cursor()
        statment = "SELECT * FROM invotery WHERE Invoice_Num = %s AND Date=CURRENT_DATE()"

        self.cur.execute(statment, invoice)
        data = self.cur.fetchall()
        for x in data:
            M1 = ""; M1_P = ""; M1_Q = 0; M1_T = 0; M2 = ""; M2_P = ""; M2_Q = 0; M2_T = 0; M3 = ""; M3_P = ""; M3_Q = 0; M3_T = 0; M4 = ""; M4_P = ""; M4_Q = 0; M4_T = 0; M5 = ""; M5_P = ""; M5_Q = 0; M5_T = 0; M6 = ""; M6_P = ""; M6_Q = 0; M6_T = 0;
            M7 = ""; M7_P = ""; M7_Q = 0; M7_T = 0; M8 = ""; M8_P = ""; M8_Q = 0; M8_T = 0; M9 = ""; M9_P = ""; M9_Q = 0; M9_T = 0; M10 = ""; M10_P = ""; M10_Q = 0;  M10_T = 0; M11 = "";  M11_P = ""; M11_Q = 0; M11_T = 0; M12 = ""; M12_P = "";
            M12_Q = 0; M12_T = 0; M13 = ""; M13_P = ""; M13_Q = 0; M13_T = 0; M14 = ""; M14_P = ""; M14_Q = 0; M14_T = 0; M15 = ""; M15_P = ""; M15_Q = 0; M15_T = 0; M16 = ""; M16_P = ""; M16_Q = 0; M16_T = 0; M17 = ""; M17_P = ""; M17_Q = 0;
            M17_T = 0; M18 = ""; M18_P = ""; M18_Q = 0; M18_T = 0; M19 = ""; M19_P = ""; M19_Q = 0; M19_T = 0; M20 = ""; M20_P = ""; M20_Q = 0; M20_T = 0; M1_Y = "";  M2_Y = ""; M3_Y = ""; M4_Y = ""; M5_Y = ""; M6_Y = ""; M7_Y = ""; M8_Y = "";
            M9_Y = ""; M10_Y = ""; M11_Y = ""; M12_Y = ""; M13_Y = ""; M14_Y = ""; M15_Y = ""; M16_Y = ""; M17_Y = ""; M18_Y = ""; M19_Y = ""; M20_Y = "";
            if x[1] != "" and x[1] != '0':
                M1 = x[1]
                if x[3] != "" and x[3] != '0': M1_Q = x[3]
                if x[5] != "" and x[5] != '0': M1_T = x[5]

            if x[6] != "" and x[6] != '0':
                M2 = x[6]
                if x[8] != "" and x[8] != '0': M2_Q = x[8]
                if x[10] != "" and x[10] != '0': M2_T = x[10]

            if x[11] != "" and x[11] != '0':
                M3 = x[11]
                if x[13] != "" and x[13] != '0': M3_Q = x[13]
                if x[15] != "" and x[15] != '0': M3_T = x[15]

            if x[16] != "" and x[16] != '0':
                M4 = x[16]
                if x[18] != "" and x[18] != '0': M4_Q = x[18]
                if x[20] != "" and x[20] != '0': M4_T = x[20]

            if x[21] != "" and x[21] != '0':
                M5 = x[21]
                if x[23] != "" and x[23] != '0': M5_Q = x[23]
                if x[25] != "" and x[25] != '0': M5_T = x[25]

            if x[26] != "" and x[26] != '0':
                M6 = x[26]
                if x[28] != "" and x[28] != '0': M6_Q = x[28]
                if x[30] != "" and x[30] != '0': M6_T = x[30]

            if x[31] != "" and x[31] != '0':
                M7 = x[31]
                if x[33] != "" and x[33] != '0': M7_Q = x[33]
                if x[35] != "" and x[35] != '0': M7_T = x[35]

            if x[36] != "" and x[36] != '0':
                M8 = x[36]
                if x[38] != "" and x[38] != '0': M8_Q = x[38]
                if x[40] != "" and x[40] != '0': M8_T = x[40]

            if x[41] != "" and x[41] != '0':
                M9 = x[41]
                if x[43] != "" and x[43] != '0': M9_Q = x[43]
                if x[45] != "" and x[45] != '0': M9_T = x[45]

            if x[46] != "" and x[46] != '0':
                M10 = x[46]
                if x[48] != "" and x[48] != '0': M10_Q = x[48]
                if x[50] != "" and x[50] != '0': M10_T = x[50]

            if x[51] != "" and x[51] != '0':
                M11 = x[51]
                if x[53] != "" and x[53] != '0': M11_Q = x[53]
                if x[55] != "" and x[55] != '0': M11_T = x[55]

            if x[56] != "" and x[56] != '0':
                M12 = x[56]
                if x[58] != "" and x[58] != '0': M12_Q = x[58]
                if x[60] != "" and x[60] != '0': M12_T = x[60]

            if x[61] != "" and x[61] != '0':
                M13 = x[61]
                if x[63] != "" and x[63] != '0': M13_Q = x[63]
                if x[65] != "" and x[65] != '0': M13_T = x[65]

            if x[66] != "" and x[66] != '0':
                M14 = x[66]
                if x[68] != "" and x[68] != '0': M14_Q = x[68]
                if x[70] != "" and x[70] != '0': M14_T = x[70]

            if x[71] != "" and x[71] != '0':
                M15 = x[71]
                if x[73] != "" and x[73] != '0': M15_Q = x[73]
                if x[75] != "" and x[75] != '0': M15_T = x[75]

            if x[76] != "" and x[76] != '0':
                M16 = x[76]
                if x[78] != "" and x[78] != '0': M16_Q = x[78]
                if x[80] != "" and x[80] != '0': M16_T = x[80]

            if x[81] != "" and x[81] != '0':
                M17 = x[81]
                if x[83] != "" and x[83] != '0': M17_Q = x[83]
                if x[85] != "" and x[85] != '0': M17_T = x[85]

            if x[86] != "" and x[86] != '0':
                M18 = x[86]
                if x[88] != "" and x[88] != '0': M18_Q = x[88]
                if x[90] != "" and x[90] != '0': M18_T = x[90]

            if x[91] != "" and x[91] != '0':
                M19 = x[91]
                if x[93] != "" and x[93] != '0': M19_Q = x[93]
                if x[95] != "" and x[95] != '0': M19_T = x[95]

            if x[96] != "" and x[96] != '0':
                M20 = x[96]
                if x[98] != "" and x[98] != '0': M20_Q = x[98]
                if x[100] != "" and x[100] != '0': M20_T = x[100]
        # print(M1 , M1_P , M1_Q ,M1_T ,"\n",M2 , M2_P , M2_Q ,M2_T ,"\n",M3 , M3_P , M3_Q ,M3_T ,"\n",M4 , M4_P , M4_Q ,M4_T ,"\n",M5 , M5_P , M5_Q ,M5_T ,"\n",M6 , M6_P , M6_Q ,M6_T ,"\n",M7 , M7_P , M7_Q ,M7_T ,"\n",M8 , M8_P , M8_Q ,M8_T ,"\n",M9 , M9_P , M9_Q ,M9_T ,"\n",M10 , M10_P , M10_Q ,M10_T ,"\n",M11 , M11_P , M11_Q ,M11_T ,"\n",M12 , M12_P , M12_Q ,M12_T ,"\n",M13 , M13_P , M13_Q ,M13_T ,"\n",M14 , M14_P , M14_Q ,M14_T ,"\n",M15 , M15_P , M15_Q ,M15_T ,"\n",M16 , M16_P , M16_Q ,M16_T ,"\n",M17 , M17_P , M17_Q ,M17_T ,"\n",M18 , M18_P , M18_Q ,M18_T ,"\n",M19 , M19_P , M19_Q ,M19_T ,"\n",M20 , M20_P , M20_Q ,M20_T )
        auto=M1 , M1_P , M1_Q ,M1_T ,M2 , M2_P , M2_Q ,M2_T ,M3 , M3_P , M3_Q ,M3_T ,M4 , M4_P , M4_Q ,M4_T ,M5 , M5_P , M5_Q ,M5_T ,M6 , M6_P , M6_Q ,M6_T ,M7 , M7_P , M7_Q ,M7_T ,M8 , M8_P , M8_Q ,M8_T ,M9 , M9_P , M9_Q ,M9_T ,M10 , M10_P , M10_Q ,M10_T ,M11 , M11_P , M11_Q ,M11_T ,M12 , M12_P , M12_Q ,M12_T ,M13 , M13_P , M13_Q ,M13_T ,M14 , M14_P , M14_Q ,M14_T ,M15 , M15_P , M15_Q ,M15_T ,M16 , M16_P , M16_Q ,M16_T ,M17 , M17_P , M17_Q ,M17_T ,M18 , M18_P , M18_Q ,M18_T ,M19 , M19_P , M19_Q ,M19_T ,M20 , M20_P , M20_Q ,M20_T
        filename = "Receipt Kitchen.txt"
        myFile= open("Receipt Kitchen.txt","wt",encoding='utf-8')
        myFile.write(str(data[0][102]) )
        myFile.write("               ")
        myFile.write(str(invoice))
        myFile.write("\n")
        myFile.write("Name: ")
        myFile.write( str(data[0][104]))
        myFile.write("\n")
        myFile.write("**************************************************\n")
        myFile.write("\t       Chicken Zinger \t\t\n")
        myFile.write("**************************************************\n")
        myFile.write("-----------------------------------------------------------------\n")
        myFile.write("ITEM  \t            QUANTITY  NOTES \n")
        myFile.write("-----------------------------------------------------------------\n")
        if M1 !="":
            if len(auto[0]) >8 :
                myFile.write(auto[0] + "\t")
            else:
                myFile.write(auto[0]+"\t\t")
            myFile.write(auto[2]+"\t")
            myFile.write(str(auto[3])+"\n")
            myFile.write("---------------------------------------------------------------\n")
        if M2 !="":
            if len(auto[4]) >8 :
                myFile.write(auto[4]+"\t")
            else:
                myFile.write(auto[4] + "\t\t")
            myFile.write(auto[6] + "\t")
            myFile.write(str(auto[7]) + "\n")
            myFile.write("---------------------------------------------------------------\n")
        if M3 !="":
            if len(auto[8]) >8 :
                myFile.write(auto[8]+"\t")
            else:
                myFile.write(auto[8] + "\t\t")
            myFile.write(auto[10] + "\t")
            myFile.write(str(auto[11]) + "\n")
            myFile.write("---------------------------------------------------------------\n")
        if M4 !="":
            if len(auto[12]) >8 :
                myFile.write(auto[12]+"\t")
            else:
                myFile.write(auto[12] + "\t\t")
            myFile.write(auto[14] + "\t")
            myFile.write(str(auto[15]) + "\n")
            myFile.write("---------------------------------------------------------------\n")
        if M5 !="":
            if len(auto[16]) >8 :
                myFile.write(auto[16]+"\t")
            else:
                myFile.write(auto[16] + "\t\t")
            myFile.write(auto[18] + "\t")
            myFile.write(str(auto[19]) + "\n")
            myFile.write("---------------------------------------------------------------\n")
        if M6 !="":
            if len(auto[20]) >8 :
                myFile.write(auto[20]+"\t")
            else:
                myFile.write(auto[20]+"\t\t")
            myFile.write(auto[22]+"\t")
            myFile.write(str(auto[23])+"\n")
            myFile.write("---------------------------------------------------------------\n")
        if M7 !="":
            if len(auto[24]) >8 :
                myFile.write(auto[24]+"\t")
            else:
                myFile.write(auto[24] + "\t\t")
            myFile.write(auto[26] + "\t")
            myFile.write(str(auto[27]) + "\n")
            myFile.write("---------------------------------------------------------------\n")
        if M8 !="":
            if len(auto[28]) >8 :
                myFile.write(auto[28]+"\t")
            else:
                myFile.write(auto[28]+"\t\t")
            myFile.write(auto[30]+"\t")
            myFile.write(str(auto[31])+"\n")
            myFile.write("---------------------------------------------------------------\n")
        if M9 !="":
            if len(auto[32]) >8 :
                myFile.write(auto[32] + "\t")
            else:
                myFile.write(auto[32]+"\t\t")
            myFile.write(auto[34]+"\t")
            myFile.write(str(auto[35])+"\n")
            myFile.write("---------------------------------------------------------------\n")
        if M10 !="":
            if len(auto[36]) >8 :
                myFile.write(auto[36]+"\t")
            else:
                myFile.write(auto[36]+"\t\t")
            myFile.write(auto[38]+"\t")
            myFile.write(str(auto[39])+"\n")
            myFile.write("---------------------------------------------------------------\n")
        if M11 !="":
            if len(auto[40]) >8 :
                myFile.write(auto[40]+"\t")
            else:
                myFile.write(auto[40] + "\t\t")
            myFile.write(auto[42] + "\t")
            myFile.write(str(auto[43]) + "\n")
            myFile.write("---------------------------------------------------------------\n")
        if M12 !="":
            if len(auto[44]) >8 :
                myFile.write(auto[44]+"\t")
            else:
                myFile.write(auto[44] + "\t\t")
            myFile.write(auto[46] + "\t")
            myFile.write(str(auto[47]) + "\n")
            myFile.write("---------------------------------------------------------------\n")
        if M13 !="":
            if len(auto[48]) >8 :
                myFile.write(auto[48]+"\t")
            else:
                myFile.write(auto[48] + "\t\t")
            myFile.write(auto[50] + "\t")
            myFile.write(str(auto[51]) + "\n")
            myFile.write("---------------------------------------------------------------\n")
        if M14 !="":
            if len(auto[52]) >8 :
                myFile.write(auto[52]+"\t")
            else:
                myFile.write(auto[52] + "\t\t")
            myFile.write(auto[54] + "\t")
            myFile.write(str(auto[55]) + "\n")
            myFile.write("---------------------------------------------------------------\n")
        if M15 !="":
            if len(auto[56]) >8 :
                myFile.write(auto[56]+"\t")
            else:
                myFile.write(auto[56] + "\t\t")
            myFile.write(auto[58] + "\t")
            myFile.write(str(auto[59]) + "\n")
            myFile.write("---------------------------------------------------------------\n")
        if M16 !="":
            if len(auto[60]) >8 :
                myFile.write(auto[60]+"\t")
            else:
                myFile.write(auto[60] + "\t\t")
            myFile.write(auto[62] + "\t")
            myFile.write(str(auto[63]) + "\n")
            myFile.write("---------------------------------------------------------------\n")
        if M17 !="":
            if len(auto[64]) >8 :
                myFile.write(auto[64]+"\t")
            else:
                myFile.write(auto[64]+"\t\t")
            myFile.write(auto[66]+"\t")
            myFile.write(str(auto[67])+"\n")
            myFile.write("---------------------------------------------------------------\n")
        if M18 !="":
            if len(auto[68]) >8 :
                myFile.write(auto[68]+"\t")
            else:
                myFile.write(auto[68]+"\t\t")
            myFile.write(auto[70]+"\t")
            myFile.write(str(auto[71])+"\n")
            myFile.write("---------------------------------------------------------------\n")
        if M19 !="":
            if len(auto[72]) >8 :
                myFile.write(auto[72]+"\t")
            else:
                myFile.write(auto[72]+"\t\t")
            myFile.write(auto[74]+"\t")
            myFile.write(str(auto[75])+"\n")
            myFile.write("---------------------------------------------------------------\n")
        if M20 !="":
            if len(auto[76]) >8 :
                myFile.write(auto[76]+"\t")
            else:
                myFile.write(auto[76] + "\t\t")
            myFile.write(auto[78] + "\t")
            myFile.write(str(auto[79]) + "\n")
        total = int(M1_Q) +int( M2_Q)+int(M3_Q) + int(M4_Q) + int(M5_Q) + int(M6_Q) + int(M7_Q) + int(M8_Q) + int(M9_Q) + int(M10_Q) + int(M11_Q) + int(M12_Q) + int(M13_Q) + int(M14_Q) + int(M15_Q) + int(M16_Q) + int(M17_Q) + int(M18_Q) + int(M19_Q)+ int(M20_Q)
        myFile.write("***********************************************\n")
        nan = total -1
        if M1 or M2 or M3 or M4 or M5 or M6 or M7 or M8 or M9 or M10 or M11 or M12 or M13 or M14 or M15 or M16 or M17 or M18 or M19 or M20 == "Delivery":
            myFile.write("\tTOTAL Item = "+ str(nan))
        else:
            myFile.write("\tTOTAL Item = " + str(total))
        myFile.write("\n")
        myFile.write("***********************************************\n")
        myFile.close()
        subprocess.call(['notepad', '/p', filename])


    def receipt_Kitchen_Packup(self):
        invoice = self.lineEdit_8.text()
        d=self.comboBox_10.currentText()
        m=self.comboBox_11.currentText()
        y=self.comboBox_9.currentText()
        # statment = "SELECT * FROM invotery WHERE Invoice_Num = %s AND Date=CURRENT_DATE()"
        if d != "Day" and m != "Month" and invoice != "" and invoice != 0:
            try:
                d=int(d)
                m=int(m)
                y=int(y)
                invoice = int(invoice)
                t2 = datetime.datetime(y, m, d)
                self.db = pymysql.connect(host='localhost', user='root', password='', db='db')
                self.cur = self.db.cursor()
                statment = "SELECT * FROM invotery WHERE Invoice_Num = %s AND Date = %s"
                self.cur.execute(statment, (invoice,t2))

                data = self.cur.fetchall()
                for x in data:
                    M1 = ""; M1_P = ""; M1_Q = 0; M1_T = 0; M2 = ""; M2_P = ""; M2_Q = 0; M2_T = 0; M3 = ""; M3_P = ""; M3_Q = 0; M3_T = 0; M4 = ""; M4_P = ""; M4_Q = 0; M4_T = 0; M5 = ""; M5_P = ""; M5_Q = 0; M5_T = 0; M6 = ""; M6_P = ""; M6_Q = 0; M6_T = 0;
                    M7 = ""; M7_P = ""; M7_Q = 0; M7_T = 0; M8 = ""; M8_P = ""; M8_Q = 0; M8_T = 0; M9 = ""; M9_P = ""; M9_Q = 0; M9_T = 0; M10 = ""; M10_P = ""; M10_Q = 0;  M10_T = 0; M11 = "";  M11_P = ""; M11_Q = 0; M11_T = 0; M12 = ""; M12_P = "";
                    M12_Q = 0; M12_T = 0; M13 = ""; M13_P = ""; M13_Q = 0; M13_T = 0; M14 = ""; M14_P = ""; M14_Q = 0; M14_T = 0; M15 = ""; M15_P = ""; M15_Q = 0; M15_T = 0; M16 = ""; M16_P = ""; M16_Q = 0; M16_T = 0; M17 = ""; M17_P = ""; M17_Q = 0;
                    M17_T = 0; M18 = ""; M18_P = ""; M18_Q = 0; M18_T = 0; M19 = ""; M19_P = ""; M19_Q = 0; M19_T = 0; M20 = ""; M20_P = ""; M20_Q = 0; M20_T = 0; M1_Y = "";  M2_Y = ""; M3_Y = ""; M4_Y = ""; M5_Y = ""; M6_Y = ""; M7_Y = ""; M8_Y = "";
                    M9_Y = ""; M10_Y = ""; M11_Y = ""; M12_Y = ""; M13_Y = ""; M14_Y = ""; M15_Y = ""; M16_Y = ""; M17_Y = ""; M18_Y = ""; M19_Y = ""; M20_Y = "";
                    if x[1] != "" and x[1] != '0':
                        M1 = x[1]
                        if x[3] != "" and x[3] != '0': M1_Q = x[3]
                        if x[5] != "" and x[5] != '0': M1_T = x[5]

                    if x[6] != "" and x[6] != '0':
                        M2 = x[6]
                        if x[8] != "" and x[8] != '0': M2_Q = x[8]
                        if x[10] != "" and x[10] != '0': M2_T = x[10]

                    if x[11] != "" and x[11] != '0':
                        M3 = x[11]
                        if x[13] != "" and x[13] != '0': M3_Q = x[13]
                        if x[15] != "" and x[15] != '0': M3_T = x[15]

                    if x[16] != "" and x[16] != '0':
                        M4 = x[16]
                        if x[18] != "" and x[18] != '0': M4_Q = x[18]
                        if x[20] != "" and x[20] != '0': M4_T = x[20]

                    if x[21] != "" and x[21] != '0':
                        M5 = x[21]
                        if x[23] != "" and x[23] != '0': M5_Q = x[23]
                        if x[25] != "" and x[25] != '0': M5_T = x[25]

                    if x[26] != "" and x[26] != '0':
                        M6 = x[26]
                        if x[28] != "" and x[28] != '0': M6_Q = x[28]
                        if x[30] != "" and x[30] != '0': M6_T = x[30]

                    if x[31] != "" and x[31] != '0':
                        M7 = x[31]
                        if x[33] != "" and x[33] != '0': M7_Q = x[33]
                        if x[35] != "" and x[35] != '0': M7_T = x[35]

                    if x[36] != "" and x[36] != '0':
                        M8 = x[36]
                        if x[38] != "" and x[38] != '0': M8_Q = x[38]
                        if x[40] != "" and x[40] != '0': M8_T = x[40]

                    if x[41] != "" and x[41] != '0':
                        M9 = x[41]
                        if x[43] != "" and x[43] != '0': M9_Q = x[43]
                        if x[45] != "" and x[45] != '0': M9_T = x[45]

                    if x[46] != "" and x[46] != '0':
                        M10 = x[46]
                        if x[48] != "" and x[48] != '0': M10_Q = x[48]
                        if x[50] != "" and x[50] != '0': M10_T = x[50]

                    if x[51] != "" and x[51] != '0':
                        M11 = x[51]
                        if x[53] != "" and x[53] != '0': M11_Q = x[53]
                        if x[55] != "" and x[55] != '0': M11_T = x[55]

                    if x[56] != "" and x[56] != '0':
                        M12 = x[56]
                        if x[58] != "" and x[58] != '0': M12_Q = x[58]
                        if x[60] != "" and x[60] != '0': M12_T = x[60]

                    if x[61] != "" and x[61] != '0':
                        M13 = x[61]
                        if x[63] != "" and x[63] != '0': M13_Q = x[63]
                        if x[65] != "" and x[65] != '0': M13_T = x[65]

                    if x[66] != "" and x[66] != '0':
                        M14 = x[66]
                        if x[68] != "" and x[68] != '0': M14_Q = x[68]
                        if x[70] != "" and x[70] != '0': M14_T = x[70]

                    if x[71] != "" and x[71] != '0':
                        M15 = x[71]
                        if x[73] != "" and x[73] != '0': M15_Q = x[73]
                        if x[75] != "" and x[75] != '0': M15_T = x[75]

                    if x[76] != "" and x[76] != '0':
                        M16 = x[76]
                        if x[78] != "" and x[78] != '0': M16_Q = x[78]
                        if x[80] != "" and x[80] != '0': M16_T = x[80]

                    if x[81] != "" and x[81] != '0':
                        M17 = x[81]
                        if x[83] != "" and x[83] != '0': M17_Q = x[83]
                        if x[85] != "" and x[85] != '0': M17_T = x[85]

                    if x[86] != "" and x[86] != '0':
                        M18 = x[86]
                        if x[88] != "" and x[88] != '0': M18_Q = x[88]
                        if x[90] != "" and x[90] != '0': M18_T = x[90]

                    if x[91] != "" and x[91] != '0':
                        M19 = x[91]
                        if x[93] != "" and x[93] != '0': M19_Q = x[93]
                        if x[95] != "" and x[95] != '0': M19_T = x[95]

                    if x[96] != "" and x[96] != '0':
                        M20 = x[96]
                        if x[98] != "" and x[98] != '0': M20_Q = x[98]
                        if x[100] != "" and x[100] != '0': M20_T = x[100]
                # print(M1 , M1_P , M1_Q ,M1_T ,"\n",M2 , M2_P , M2_Q ,M2_T ,"\n",M3 , M3_P , M3_Q ,M3_T ,"\n",M4 , M4_P , M4_Q ,M4_T ,"\n",M5 , M5_P , M5_Q ,M5_T ,"\n",M6 , M6_P , M6_Q ,M6_T ,"\n",M7 , M7_P , M7_Q ,M7_T ,"\n",M8 , M8_P , M8_Q ,M8_T ,"\n",M9 , M9_P , M9_Q ,M9_T ,"\n",M10 , M10_P , M10_Q ,M10_T ,"\n",M11 , M11_P , M11_Q ,M11_T ,"\n",M12 , M12_P , M12_Q ,M12_T ,"\n",M13 , M13_P , M13_Q ,M13_T ,"\n",M14 , M14_P , M14_Q ,M14_T ,"\n",M15 , M15_P , M15_Q ,M15_T ,"\n",M16 , M16_P , M16_Q ,M16_T ,"\n",M17 , M17_P , M17_Q ,M17_T ,"\n",M18 , M18_P , M18_Q ,M18_T ,"\n",M19 , M19_P , M19_Q ,M19_T ,"\n",M20 , M20_P , M20_Q ,M20_T )
                auto=M1 , M1_P , M1_Q ,M1_T ,M2 , M2_P , M2_Q ,M2_T ,M3 , M3_P , M3_Q ,M3_T ,M4 , M4_P , M4_Q ,M4_T ,M5 , M5_P , M5_Q ,M5_T ,M6 , M6_P , M6_Q ,M6_T ,M7 , M7_P , M7_Q ,M7_T ,M8 , M8_P , M8_Q ,M8_T ,M9 , M9_P , M9_Q ,M9_T ,M10 , M10_P , M10_Q ,M10_T ,M11 , M11_P , M11_Q ,M11_T ,M12 , M12_P , M12_Q ,M12_T ,M13 , M13_P , M13_Q ,M13_T ,M14 , M14_P , M14_Q ,M14_T ,M15 , M15_P , M15_Q ,M15_T ,M16 , M16_P , M16_Q ,M16_T ,M17 , M17_P , M17_Q ,M17_T ,M18 , M18_P , M18_Q ,M18_T ,M19 , M19_P , M19_Q ,M19_T ,M20 , M20_P , M20_Q ,M20_T
                filename = "Receipt Kitchen.txt"
                myFile= open("Receipt Kitchen.txt","wt",encoding='utf-8')
                myFile.write(str(data[0][102]) )
                myFile.write("               ")
                myFile.write(str(invoice))
                myFile.write("\n")
                myFile.write("Name: ")
                myFile.write( str(data[0][104]))
                myFile.write("\n")
                myFile.write("**************************************************\n")
                myFile.write("\t       Chicken Zinger \t\t\n")
                myFile.write("**************************************************\n")
                myFile.write("-----------------------------------------------------------------\n")
                myFile.write("ITEM  \t            QUANTITY  NOTES \n")
                myFile.write("-----------------------------------------------------------------\n")
                if M1 !="":
                    if len(auto[0]) >8 :
                        myFile.write(auto[0] + "\t")
                    else:
                        myFile.write(auto[0]+"\t\t")
                    myFile.write(auto[2]+"\t")
                    myFile.write(str(auto[3])+"\n")
                    myFile.write("---------------------------------------------------------------\n")
                if M2 !="":
                    if len(auto[4]) >8 :
                        myFile.write(auto[4]+"\t")
                    else:
                        myFile.write(auto[4] + "\t\t")
                    myFile.write(auto[6] + "\t")
                    myFile.write(str(auto[7]) + "\n")
                    myFile.write("---------------------------------------------------------------\n")
                if M3 !="":
                    if len(auto[8]) >8 :
                        myFile.write(auto[8]+"\t")
                    else:
                        myFile.write(auto[8] + "\t\t")
                    myFile.write(auto[10] + "\t")
                    myFile.write(str(auto[11]) + "\n")
                    myFile.write("---------------------------------------------------------------\n")
                if M4 !="":
                    if len(auto[12]) >8 :
                        myFile.write(auto[12]+"\t")
                    else:
                        myFile.write(auto[12] + "\t\t")
                    myFile.write(auto[14] + "\t")
                    myFile.write(str(auto[15]) + "\n")
                    myFile.write("---------------------------------------------------------------\n")
                if M5 !="":
                    if len(auto[16]) >8 :
                        myFile.write(auto[16]+"\t")
                    else:
                        myFile.write(auto[16] + "\t\t")
                    myFile.write(auto[18] + "\t")
                    myFile.write(str(auto[19]) + "\n")
                    myFile.write("---------------------------------------------------------------\n")
                if M6 !="":
                    if len(auto[20]) >8 :
                        myFile.write(auto[20]+"\t")
                    else:
                        myFile.write(auto[20]+"\t\t")
                    myFile.write(auto[22]+"\t")
                    myFile.write(str(auto[23])+"\n")
                    myFile.write("---------------------------------------------------------------\n")
                if M7 !="":
                    if len(auto[24]) >8 :
                        myFile.write(auto[24]+"\t")
                    else:
                        myFile.write(auto[24] + "\t\t")
                    myFile.write(auto[26] + "\t")
                    myFile.write(str(auto[27]) + "\n")
                    myFile.write("---------------------------------------------------------------\n")
                if M8 !="":
                    if len(auto[28]) >8 :
                        myFile.write(auto[28]+"\t")
                    else:
                        myFile.write(auto[28]+"\t\t")
                    myFile.write(auto[30]+"\t")
                    myFile.write(str(auto[31])+"\n")
                    myFile.write("---------------------------------------------------------------\n")
                if M9 !="":
                    if len(auto[32]) >8 :
                        myFile.write(auto[32] + "\t")
                    else:
                        myFile.write(auto[32]+"\t\t")
                    myFile.write(auto[34]+"\t")
                    myFile.write(str(auto[35])+"\n")
                    myFile.write("---------------------------------------------------------------\n")
                if M10 !="":
                    if len(auto[36]) >8 :
                        myFile.write(auto[36]+"\t")
                    else:
                        myFile.write(auto[36]+"\t\t")
                    myFile.write(auto[38]+"\t")
                    myFile.write(str(auto[39])+"\n")
                    myFile.write("---------------------------------------------------------------\n")
                if M11 !="":
                    if len(auto[40]) >8 :
                        myFile.write(auto[40]+"\t")
                    else:
                        myFile.write(auto[40] + "\t\t")
                    myFile.write(auto[42] + "\t")
                    myFile.write(str(auto[43]) + "\n")
                    myFile.write("---------------------------------------------------------------\n")
                if M12 !="":
                    if len(auto[44]) >8 :
                        myFile.write(auto[44]+"\t")
                    else:
                        myFile.write(auto[44] + "\t\t")
                    myFile.write(auto[46] + "\t")
                    myFile.write(str(auto[47]) + "\n")
                    myFile.write("---------------------------------------------------------------\n")
                if M13 !="":
                    if len(auto[48]) >8 :
                        myFile.write(auto[48]+"\t")
                    else:
                        myFile.write(auto[48] + "\t\t")
                    myFile.write(auto[50] + "\t")
                    myFile.write(str(auto[51]) + "\n")
                    myFile.write("---------------------------------------------------------------\n")
                if M14 !="":
                    if len(auto[52]) >8 :
                        myFile.write(auto[52]+"\t")
                    else:
                        myFile.write(auto[52] + "\t\t")
                    myFile.write(auto[54] + "\t")
                    myFile.write(str(auto[55]) + "\n")
                    myFile.write("---------------------------------------------------------------\n")
                if M15 !="":
                    if len(auto[56]) >8 :
                        myFile.write(auto[56]+"\t")
                    else:
                        myFile.write(auto[56] + "\t\t")
                    myFile.write(auto[58] + "\t")
                    myFile.write(str(auto[59]) + "\n")
                    myFile.write("---------------------------------------------------------------\n")
                if M16 !="":
                    if len(auto[60]) >8 :
                        myFile.write(auto[60]+"\t")
                    else:
                        myFile.write(auto[60] + "\t\t")
                    myFile.write(auto[62] + "\t")
                    myFile.write(str(auto[63]) + "\n")
                    myFile.write("---------------------------------------------------------------\n")
                if M17 !="":
                    if len(auto[64]) >8 :
                        myFile.write(auto[64]+"\t")
                    else:
                        myFile.write(auto[64]+"\t\t")
                    myFile.write(auto[66]+"\t")
                    myFile.write(str(auto[67])+"\n")
                    myFile.write("---------------------------------------------------------------\n")
                if M18 !="":
                    if len(auto[68]) >8 :
                        myFile.write(auto[68]+"\t")
                    else:
                        myFile.write(auto[68]+"\t\t")
                    myFile.write(auto[70]+"\t")
                    myFile.write(str(auto[71])+"\n")
                    myFile.write("---------------------------------------------------------------\n")
                if M19 !="":
                    if len(auto[72]) >8 :
                        myFile.write(auto[72]+"\t")
                    else:
                        myFile.write(auto[72]+"\t\t")
                    myFile.write(auto[74]+"\t")
                    myFile.write(str(auto[75])+"\n")
                    myFile.write("---------------------------------------------------------------\n")
                if M20 !="":
                    if len(auto[76]) >8 :
                        myFile.write(auto[76]+"\t")
                    else:
                        myFile.write(auto[76] + "\t\t")
                    myFile.write(auto[78] + "\t")
                    myFile.write(str(auto[79]) + "\n")
                total = int(M1_Q) +int( M2_Q)+int(M3_Q) + int(M4_Q) + int(M5_Q) + int(M6_Q) + int(M7_Q) + int(M8_Q) + int(M9_Q) + int(M10_Q) + int(M11_Q) + int(M12_Q) + int(M13_Q) + int(M14_Q) + int(M15_Q) + int(M16_Q) + int(M17_Q) + int(M18_Q) + int(M19_Q)+ int(M20_Q)
                myFile.write("***********************************************\n")
                nan = total -1
                if M1 or M2 or M3 or M4 or M5 or M6 or M7 or M8 or M9 or M10 or M11 or M12 or M13 or M14 or M15 or M16 or M17 or M18 or M19 or M20 == "Delivery":
                    myFile.write("\tTOTAL Item = "+ str(nan))
                else:
                    myFile.write("\tTOTAL Item = " + str(total))
                myFile.write("\n")
                myFile.write("***********************************************\n")
                myFile.close()
                subprocess.call(['notepad', '/p', filename])
            except:
                self.statusBar().showMessage('لا يوجد معلومات ')



    def show_employee(self):
        self.comboBox_12.clear()
        self.cur.execute("SELECT Employee_Name FROM employees")
        employees = self.cur.fetchall()
        for employee in employees:
            self.comboBox_12.addItem(employee[0])



    def permisions(self):

        Total_reports = 0
        Invoice_Report = 0
        Add_Catogery = 0
        Add_Meals = 0
        Add_Change_Meals_Price = 0
        Add_Employee = 0
        Edit_Employee = 0
        Add_Edit_Permissions = 0
        All_Permisions = 0
        Employee_Name = str(self.comboBox_12.currentText())


        if self.checkBox_9.isChecked() == True:
            Total_reports = 1 ; Invoice_Report = 1; Add_Catogery = 1; Add_Meals = 1 ; Add_Change_Meals_Price = 1 ; Add_Employee = 1; Add_Edit_Permissions =1 ; All_Permisions =1
        else:
            if self.checkBox.isChecked() == True:
                Total_reports = 1
            if self.checkBox_2.isChecked() == True:
                Invoice_Report = 1
            if self.checkBox_3.isChecked() == True:
                Add_Catogery = 1
            if self.checkBox_4.isChecked() == True:
                Add_Meals = 1
            if self.checkBox_8.isChecked() == True:
                Add_Change_Meals_Price = 1
            if self.checkBox_5.isChecked() == True:
                Add_Employee = 1
            if self.checkBox_6.isChecked() == True:
                Edit_Employee = 1
            if self.checkBox_7.isChecked() == True:
                Add_Edit_Permissions = 1

        self.cur.execute(" SELECT Employee_Name FROM permisions ")
        employees = self.cur.fetchall()
        list=[]
        for employee in employees:
            # if Employee_Name == employee[0]:
            list.append(employee[0])
        if Employee_Name in list:
            sql = "UPDATE permisions SET Total_reports = %s , Invoice_Report = %s , Catogery = %s , Add_Meals =%s, Add_Change_Meals_Price=%s, AddEmployee =%s, EditEmployee =%s, Permissions =%s, All_Permisions =%s WHERE Employee_Name = %s "
            val = (Total_reports , Invoice_Report , Add_Catogery ,Add_Meals , Add_Change_Meals_Price , Add_Employee , Edit_Employee , Add_Edit_Permissions , All_Permisions,Employee_Name)
            self.cur.execute(sql , val)
            self.db.commit()
            # self.checkBox.setCheckState(False)
            # self.checkBox_2.setCheckState(False)
            # self.checkBox_3.setCheckState(False)
            # self.checkBox_4.setCheckState(False)
            # self.checkBox_8.setCheckState(False)
            # self.checkBox_5.setCheckState(False)
            # self.checkBox_6.setCheckState(False)
            # self.checkBox_7.setCheckState(False)
            # self.checkBox_9.setCheckState(False)
        else:
            try:
                self.cur.execute('''
                    INSERT INTO permisions (Total_reports , Invoice_Report ,Catogery,Add_Meals , Add_Change_Meals_Price , AddEmployee , EditEmployee ,Permissions, All_Permisions,Employee_Name )
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ''' , (Total_reports , Invoice_Report , Add_Catogery ,Add_Meals , Add_Change_Meals_Price , Add_Employee , Edit_Employee , Add_Edit_Permissions , All_Permisions,Employee_Name))
                self.db.commit()
                self.checkBox.setCheckState(False)
                self.checkBox_2.setCheckState(False)
                self.checkBox_3.setCheckState(False)
                self.checkBox_4.setCheckState(False)
                self.checkBox_8.setCheckState(False)
                self.checkBox_5.setCheckState(False)
                self.checkBox_6.setCheckState(False)
                self.checkBox_7.setCheckState(False)
                self.checkBox_9.setCheckState(False)
            except:
                return


    def add_employee(self):
        name = self.lineEdit_13.text()
        phone = self.lineEdit_14.text()
        address = self.lineEdit_15.text()
        Nationa_Id= self.lineEdit_16.text()
        password = self.lineEdit_17.text()
        password2 = self.lineEdit_18.text()
        date = self.lineEdit_19.text()
        self.cur.execute(" SELECT Employee_Name FROM employees ")
        employees = self.cur.fetchall()
        list=[]
        for employee in employees:
            list.append(employee[0])
        if name in list:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText(name)
            msg.setInformativeText(' Employee Found')
            msg.setWindowTitle("Founded")
            msg.exec_()
        elif password != password2 :
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error in Password or")
            msg.setInformativeText('Confirm password')
            msg.setWindowTitle("Check your password")
            msg.exec_()

        else:
            try:
                self.cur.execute("INSERT INTO employees (Employee_Name , Employee_Phone , Employee_Address, National_ID, Password1 , Password2 , date) VALUES (%s,%s,%s,%s,%s,%s,%s)",(name , phone , address , Nationa_Id , password , password2,date))
                self.db.commit()
                self.show_employee()
                self.lineEdit_13.setText("")
                self.lineEdit_14.setText("")
                self.lineEdit_15.setText("")
                self.lineEdit_16.setText("")
                self.lineEdit_17.setText("")
                self.lineEdit_18.setText("")
                self.lineEdit_19.setText("")
            except:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error in Name or National ID")
                msg.setInformativeText('Check All your Information')
                msg.setWindowTitle("Error in your Information")
                msg.exec_()


    def edit_employee(self):
        name = self.lineEdit_20.text()
        password = self.lineEdit_21.text()
        try:
            sql =(" SELECT * FROM employees WHERE Employee_Name = %s" )
            self.cur.execute(sql , name)
            employees = self.cur.fetchall()
            if employees[0][5] == password :
                self.groupBox_17.setEnabled(True)
                self.lineEdit_28.setText(name)
                self.lineEdit_22.setText(employees[0][2])
                self.lineEdit_23.setText(employees[0][3])
                self.lineEdit_24.setText(str(employees[0][4]))
                self.lineEdit_25.setText(employees[0][5])
                self.lineEdit_26.setText(employees[0][6])
                self.lineEdit_27.setText(employees[0][7])

        except:
            return


    def save_edit_employee(self):
        name=self.lineEdit_28.text()
        phone=self.lineEdit_22.text()
        address=self.lineEdit_23.text()
        national_id=self.lineEdit_24.text()
        password=self.lineEdit_25.text()
        password2=self.lineEdit_26.text()
        date=self.lineEdit_27.text()
        if password == password2:
            sql = "UPDATE employees SET Employee_Name = %s , Employee_Phone = %s , Employee_Address = %s , National_ID =%s, Password1 =%s, Password2 =%s, date =%s WHERE Employee_Name= %s"
            val = (name , phone , address , national_id , password , password2 , date , name)
            self.cur.execute(sql , val)
            self.db.commit()
            self.lineEdit_28.setText("")
            self.lineEdit_20.setText("")
            self.lineEdit_21.setText("")
            self.lineEdit_22.setText("")
            self.lineEdit_23.setText("")
            self.lineEdit_24.setText("")
            self.lineEdit_25.setText("")
            self.lineEdit_26.setText("")
            self.lineEdit_27.setText("")
            self.groupBox_17.setEnabled(False)
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error in password or Confirm")
            msg.setInformativeText('Check All your Information')
            msg.setWindowTitle("Error in your Information")
            msg.exec_()

    def delete_employee(self):
        name=self.lineEdit_28.text()
        sql = "DELETE FROM employees WHERE Employee_Name = %s"
        self.cur.execute(sql, name)
        self.db.commit()
        self.lineEdit_28.setText("")
        self.lineEdit_20.setText("")
        self.lineEdit_21.setText("")
        self.lineEdit_22.setText("")
        self.lineEdit_23.setText("")
        self.lineEdit_24.setText("")
        self.lineEdit_25.setText("")
        self.lineEdit_26.setText("")
        self.lineEdit_27.setText("")
        self.groupBox_17.setEnabled(False)




def main():

    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
