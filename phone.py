#git clone https://github.com/PhonePe/pulse.git

import os
import json
import mysql.connector as mysql
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px

#aggregated_insurance

path1="C:/Users/Karthck/Documents/phonepe/pulse/data/aggregated/insurance/country/india/state/"
agg_insur_st_list=os.listdir(path1)

data1={"States":[],"Years":[],"Quarter":[],"Name":[],"Type":[],"Count":[],"Amount":[]}

for state in agg_insur_st_list:
    states1=path1+state+"/"
    agg_year_list=os.listdir(states1)
    
    for year in agg_year_list:
        years1=states1+year+"/"
        agg_file_list=os.listdir(years1)
        
        for file in agg_file_list:
            files1=years1+file
            data=open(files1,"r")
            
            J=json.load(data)
            for i in J["data"]["transactionData"]:
                Name=i["name"]
                Type=i["paymentInstruments"][0]["type"]
                Count=i["paymentInstruments"][0]["count"]
                Amount=i["paymentInstruments"][0]["amount"]
                data1["Name"].append(Name)
                data1["Type"].append(Type)
                data1["Count"].append(Count)
                data1["Amount"].append(Amount)
                data1["States"].append(state)
                data1["Years"].append(year)
                data1["Quarter"].append(int(file.strip(".json")))

agg_insurance=pd.DataFrame(data1)
agg_insurance["States"]=agg_insurance["States"].str.replace("-"," ")
agg_insurance["States"]=agg_insurance["States"].str.title()
agg_insurance["States"]=agg_insurance["States"].str.replace("&","and")

#aggregated transaction

path2="C:/Users/Karthck/Documents/phonepe/pulse/data/aggregated/transaction/country/india/state/"
agg_trans_st_list=os.listdir(path2)

data2={"States":[],"Years":[],"Quarter":[],"Transaction_Type":[],"Transaction_Count":[],"Transaction_Amount":[]}

for state in agg_trans_st_list:
    states1=path2+state+"/"
    agg_year_list=os.listdir(states1)
    
    for year in agg_year_list:
        years1=states1+year+"/"
        agg_file_list=os.listdir(years1)
        
        for file in agg_file_list:
            files1=years1+file
            data=open(files1,"r")
            
            K=json.load(data)
            for i in K["data"]["transactionData"]:
                Name=i["name"]
                Count=i["paymentInstruments"][0]["count"]
                Amount=i["paymentInstruments"][0]["amount"]
                data2["Transaction_Type"].append(Name)
                data2["Transaction_Count"].append(Count)
                data2["Transaction_Amount"].append(Amount)
                data2["States"].append(state)
                data2["Years"].append(year)
                data2["Quarter"].append(int(file.strip(".json")))

agg_transaction=pd.DataFrame(data2)
agg_transaction["States"]=agg_transaction["States"].str.replace("-"," ")
agg_transaction["States"]=agg_transaction["States"].str.title()
agg_transaction["States"]=agg_transaction["States"].str.replace("&","and")

#aggregated user
path3="C:/Users/Karthck/Documents/phonepe/pulse/data/aggregated/user/country/india/state/"
agg_user_st_list=os.listdir(path3)

data3={"States":[],"Years":[],"Quarter":[],"Brand":[],"Count":[],"Percentage":[]}

for state in agg_user_st_list:
    states1=path3+state+"/"
    agg_year_list=os.listdir(states1)
    
    for year in agg_year_list:
        years1=states1+year+"/"
        agg_file_list=os.listdir(years1)
        
        for file in agg_file_list:
            files1=years1+file
            data=open(files1,"r")
            
            try:            
                L=json.load(data)
                for i in L["data"]["usersByDevice"]:
                    brand=i["brand"]
                    Count=i["count"]
                    Percentage=i["percentage"]
                    data3["Brand"].append(brand)
                    data3["Count"].append(Count)
                    data3["Percentage"].append(Percentage)
                    data3["States"].append(state)
                    data3["Years"].append(year)
                    data3["Quarter"].append(int(file.strip(".json")))
            except:
                pass

agg_user=pd.DataFrame(data3)
agg_user["States"]=agg_user["States"].str.replace("-"," ")
agg_user["States"]=agg_user["States"].str.title()
agg_user["States"]=agg_user["States"].str.replace("&","and")

#map_insurance
path4="C:/Users/Karthck/Documents/phonepe/pulse/data/map/insurance/hover/country/india/state/"
map_insur_hover_st_list=os.listdir(path4)

data4={"States":[],"Years":[],"Quarter":[],"District_Names":[],"Type":[],"Count":[],"Amount":[]}

for state in map_insur_hover_st_list:
    states1=path4+state+"/"
    map_year_list=os.listdir(states1)
    
    for year in map_year_list:
        years1=states1+year+"/"
        map_file_list=os.listdir(years1)
        
        for file in map_file_list:
            files1=years1+file
            data=open(files1,"r")
            
            A=json.load(data)
            for i in A["data"]["hoverDataList"]:
                Name=i["name"]
                Type=i["metric"][0]["type"]
                Count=i["metric"][0]["count"]
                Amount=i["metric"][0]["amount"]
                data4["District_Names"].append(Name)
                data4["Type"].append(Type)
                data4["Count"].append(Count)
                data4["Amount"].append(Amount)
                data4["States"].append(state)
                data4["Years"].append(year)
                data4["Quarter"].append(int(file.strip(".json")))

map_insur_hover=pd.DataFrame(data4)
map_insur_hover["States"]=map_insur_hover["States"].str.replace("-"," ")
map_insur_hover["States"]=map_insur_hover["States"].str.title()
map_insur_hover["States"]=map_insur_hover["States"].str.replace("&","and")
map_insur_hover["District_Names"]=map_insur_hover["District_Names"].str.replace("district","")
map_insur_hover["District_Names"]=map_insur_hover["District_Names"].str.title()

#map_transaction
path5="C:/Users/Karthck/Documents/phonepe/pulse/data/map/transaction/hover/country/india/state/"
map_trans_hover_st_list=os.listdir(path5)

data5={"States":[],"Years":[],"Quarter":[],"District_Names":[],"Type":[],"Transaction_Count":[],"Transaction_Amount":[]}

for state in map_trans_hover_st_list:
    states1=path5+state+"/"
    map_year_list=os.listdir(states1)
    
    for year in map_year_list:
        years1=states1+year+"/"
        map_file_list=os.listdir(years1)
        
        for file in map_file_list:
            files1=years1+file
            data=open(files1,"r")
            
            B=json.load(data)
            for i in B["data"]["hoverDataList"]:
                Name=i["name"]
                Type=i["metric"][0]["type"]
                Count=i["metric"][0]["count"]
                Amount=i["metric"][0]["amount"]
                data5["District_Names"].append(Name)
                data5["Type"].append(Type)
                data5["Transaction_Count"].append(Count)
                data5["Transaction_Amount"].append(Amount)
                data5["States"].append(state)
                data5["Years"].append(year)
                data5["Quarter"].append(int(file.strip(".json")))

map_trans_hover=pd.DataFrame(data5)
map_trans_hover["States"]=map_trans_hover["States"].str.replace("-"," ")
map_trans_hover["States"]=map_trans_hover["States"].str.title()
map_trans_hover["States"]=map_trans_hover["States"].str.replace("&","and")
map_trans_hover["District_Names"]=map_trans_hover["District_Names"].str.replace("district","")
map_trans_hover["District_Names"]=map_trans_hover["District_Names"].str.title()

#map_user
path6="C:/Users/Karthck/Documents/phonepe/pulse/data/map/user/hover/country/india/state/"
map_user_hover_st_list=os.listdir(path6)

data6={"States":[],"Years":[],"Quarter":[],"District_Names":[],"Registered Users":[],"Apps Open":[]}

for state in map_user_hover_st_list:
    states1=path6+state+"/"
    map_year_list=os.listdir(states1)
    
    for year in map_year_list:
        years1=states1+year+"/"
        map_file_list=os.listdir(years1)
        
        for file in map_file_list:
            files1=years1+file
            data=open(files1,"r")
            
            C=json.load(data)
            for i in C["data"]["hoverData"].items():
                Name=i[0]
                user=i[1]["registeredUsers"]
                apps=i[1]["appOpens"]
                data6["District_Names"].append(Name)
                data6["Registered Users"].append(user)
                data6["Apps Open"].append(apps)
                data6["States"].append(state)
                data6["Years"].append(year)
                data6["Quarter"].append(int(file.strip(".json")))

map_user_hover=pd.DataFrame(data6)
map_user_hover["States"]=map_user_hover["States"].str.replace("-"," ")
map_user_hover["States"]=map_user_hover["States"].str.title()
map_user_hover["States"]=map_user_hover["States"].str.replace("&","and")
map_user_hover["District_Names"]=map_user_hover["District_Names"].str.replace("district","")
map_user_hover["District_Names"]=map_user_hover["District_Names"].str.title()

#top insurance_districts
path7d="C:/Users/Karthck/Documents/phonepe/pulse/data/top/insurance/country/india/state/"
top_insur_st_list=os.listdir(path7d)

data7d={"States":[],"Years":[],"Quarter":[],"District_Names":[],"Type":[],"Transaction_Count":[],"Transaction_Amount":[]}

for state in top_insur_st_list:
    states1=path7d+state+"/"
    top_year_list=os.listdir(states1)
    
    for year in top_year_list:
        years1=states1+year+"/"
        top_file_list=os.listdir(years1)
        
        for file in top_file_list:
            files1=years1+file
            data=open(files1,"r")
            
            DD=json.load(data)
            for i in DD["data"]["districts"]:
                Name=i["entityName"]
                Type=i["metric"]["type"]
                Count=i["metric"]["count"]
                Amount=i["metric"]["amount"]
                data7d["District_Names"].append(Name)
                data7d["Type"].append(Type)
                data7d["Transaction_Count"].append(Count)
                data7d["Transaction_Amount"].append(Amount)
                data7d["States"].append(state)
                data7d["Years"].append(year)
                data7d["Quarter"].append(int(file.strip(".json")))

top_insurance_districts=pd.DataFrame(data7d)
top_insurance_districts["States"]=top_insurance_districts["States"].str.replace("-"," ")
top_insurance_districts["States"]=top_insurance_districts["States"].str.title()
top_insurance_districts["States"]=top_insurance_districts["States"].str.replace("&","and")
top_insurance_districts["District_Names"]=top_insurance_districts["District_Names"].str.replace("district","")
top_insurance_districts["District_Names"]=top_insurance_districts["District_Names"].str.title()

#top insurance_pincode
path7="C:/Users/Karthck/Documents/phonepe/pulse/data/top/insurance/country/india/state/"
top_insur_hover_st_list=os.listdir(path7)

data7={"States":[],"Years":[],"Quarter":[],"Pincodes":[],"Type":[],"Transaction_Count":[],"Transaction_Amount":[]}

for state in top_insur_hover_st_list:
    states1=path7+state+"/"
    top_year_list=os.listdir(states1)
    
    for year in top_year_list:
        years1=states1+year+"/"
        top_file_list=os.listdir(years1)
        
        for file in top_file_list:
            files1=years1+file
            data=open(files1,"r")
            
            D=json.load(data)
            for i in D["data"]["pincodes"]:
                Name=i["entityName"]
                Type=i["metric"]["type"]
                Count=i["metric"]["count"]
                Amount=i["metric"]["amount"]
                data7["Pincodes"].append(Name)
                data7["Type"].append(Type)
                data7["Transaction_Count"].append(Count)
                data7["Transaction_Amount"].append(Amount)
                data7["States"].append(state)
                data7["Years"].append(year)
                data7["Quarter"].append(int(file.strip(".json")))

top_insurance_pincode=pd.DataFrame(data7)
top_insurance_pincode["States"]=top_insurance_pincode["States"].str.replace("-"," ")
top_insurance_pincode["States"]=top_insurance_pincode["States"].str.title()
top_insurance_pincode["States"]=top_insurance_pincode["States"].str.replace("&","and")

#top transaction districts
path8d="C:/Users/Karthck/Documents/phonepe/pulse/data/top/transaction/country/india/state/"
top_insur_st_list=os.listdir(path8d)

data8d={"States":[],"Years":[],"Quarter":[],"District_Names":[],"Type":[],"Transaction_Count":[],"Transaction_Amount":[]}

for state in top_insur_st_list:
    states1=path8d+state+"/"
    top_year_list=os.listdir(states1)
    
    for year in top_year_list:
        years1=states1+year+"/"
        top_file_list=os.listdir(years1)
        
        for file in top_file_list:
            files1=years1+file
            data=open(files1,"r")
            
            EE=json.load(data)
            for i in EE["data"]["districts"]:
                Name=i["entityName"]
                Type=i["metric"]["type"]
                Count=i["metric"]["count"]
                Amount=i["metric"]["amount"]
                data8d["District_Names"].append(Name)
                data8d["Type"].append(Type)
                data8d["Transaction_Count"].append(Count)
                data8d["Transaction_Amount"].append(Amount)
                data8d["States"].append(state)
                data8d["Years"].append(year)
                data8d["Quarter"].append(int(file.strip(".json")))
                
top_transaction_districts=pd.DataFrame(data8d)
top_transaction_districts["States"]=top_transaction_districts["States"].str.replace("-"," ")
top_transaction_districts["States"]=top_transaction_districts["States"].str.title()
top_transaction_districts["States"]=top_transaction_districts["States"].str.replace("&","and")
top_transaction_districts["District_Names"]=top_transaction_districts["District_Names"].str.title()

#top transaction pincode
path8="C:/Users/Karthck/Documents/phonepe/pulse/data/top/transaction/country/india/state/"
top_insur_hover_st_list=os.listdir(path8)

data8={"States":[],"Years":[],"Quarter":[],"Pincodes":[],"Type":[],"Transaction_Count":[],"Transaction_Amount":[]}

for state in top_insur_hover_st_list:
    states1=path8+state+"/"
    top_year_list=os.listdir(states1)
    
    for year in top_year_list:
        years1=states1+year+"/"
        top_file_list=os.listdir(years1)
        
        for file in top_file_list:
            files1=years1+file
            data=open(files1,"r")
            
            E=json.load(data)
            for i in E["data"]["pincodes"]:
                Name=i["entityName"]
                Type=i["metric"]["type"]
                Count=i["metric"]["count"]
                Amount=i["metric"]["amount"]
                data8["Pincodes"].append(Name)
                data8["Type"].append(Type)
                data8["Transaction_Count"].append(Count)
                data8["Transaction_Amount"].append(Amount)
                data8["States"].append(state)
                data8["Years"].append(year)
                data8["Quarter"].append(int(file.strip(".json")))
                
top_transaction_pincode=pd.DataFrame(data8)
top_transaction_pincode["States"]=top_transaction_pincode["States"].str.replace("-"," ")
top_transaction_pincode["States"]=top_transaction_pincode["States"].str.title()
top_transaction_pincode["States"]=top_transaction_pincode["States"].str.replace("&","and")

#top user districts
path9d="C:/Users/Karthck/Documents/phonepe/pulse/data/top/user/country/india/state/"
top_user_list=os.listdir(path9d)

data9d={"States":[],"Years":[],"Quarter":[],"District_Names":[],"Registered Users":[]}

for state in top_user_list:
    states1=path9d+state+"/"
    top_year_list=os.listdir(states1)
    
    for year in top_year_list:
        years1=states1+year+"/"
        top_file_list=os.listdir(years1)
        
        for file in top_file_list:
            files1=years1+file
            data=open(files1,"r")
            
            FF=json.load(data)
            for i in FF["data"]["districts"]:
                Name=i["name"]
                user=i["registeredUsers"]
                data9d["District_Names"].append(Name)
                data9d["Registered Users"].append(user)
                data9d["States"].append(state)
                data9d["Years"].append(year)
                data9d["Quarter"].append(int(file.strip(".json")))
                
top_user_districts=pd.DataFrame(data9d)
top_user_districts["States"]=top_user_districts["States"].str.replace("-"," ")
top_user_districts["States"]=top_user_districts["States"].str.title()
top_user_districts["States"]=top_user_districts["States"].str.replace("&","and")
top_user_districts["District_Names"]=top_user_districts["District_Names"].str.title()

#top user pincodes
path9="C:/Users/Karthck/Documents/phonepe/pulse/data/top/user/country/india/state/"
top_user_st_list=os.listdir(path9)

data9={"States":[],"Years":[],"Quarter":[],"Pincodes":[],"Registered Users":[]}

for state in top_user_st_list:
    states1=path9+state+"/"
    top_year_list=os.listdir(states1)
    
    for year in top_year_list:
        years1=states1+year+"/"
        top_file_list=os.listdir(years1)
        
        for file in top_file_list:
            files1=years1+file
            data=open(files1,"r")
            
            F=json.load(data)
            for i in F["data"]["pincodes"]:
                Name=i["name"]
                user=i["registeredUsers"]
                data9["Pincodes"].append(Name)
                data9["Registered Users"].append(user)
                data9["States"].append(state)
                data9["Years"].append(year)
                data9["Quarter"].append(int(file.strip(".json")))
                
top_user_pincode=pd.DataFrame(data9)
top_user_pincode["States"]=top_user_pincode["States"].str.replace("-"," ")
top_user_pincode["States"]=top_user_pincode["States"].str.title()
top_user_pincode["States"]=top_user_pincode["States"].str.replace("&","and")

#connection to sql
mydb =mysql.connect(host="localhost",
                user="root",
                password="",
                )
mycursor = mydb.cursor(buffered=True)
mycursor.execute("CREATE DATABASE if not exists phonepepulse")
try:
    mydb =mysql.connect(host="localhost",
                    user="root",
                    password="",
                    database="phonepepulse"
                    
                    )
    mycursor = mydb.cursor(buffered=True)

    #creating table for agg_transaction

    mycursor.execute('''
        CREATE TABLE IF NOT EXISTS agg_transaction (
            ID INT AUTO_INCREMENT PRIMARY KEY,
            States VARCHAR(100),
            Years INT,
            Quarter INT,
            Transaction_type VARCHAR(100),
            Transaction_count INT,
            Transaction_amount DOUBLE,
            UNIQUE KEY idx_unique_entry (States, Years, Quarter, Transaction_type)
        )
    ''')

    query = "INSERT INTO agg_transaction (States, Years, Quarter, Transaction_type, Transaction_count, Transaction_amount) VALUES (%s, %s, %s, %s, %s, %s)"

    values = [tuple(row) for _, row in agg_transaction.iterrows()]

    mycursor.executemany(query, values)
    mydb.commit()

    mycursor.close()
    mydb.close()
except:
    pass

#creating table for agg_insurance
try:
    #connection to sql
    mydb =mysql.connect(host="localhost",
                    user="root",
                    password="",
                    database="phonepepulse"
                    )
    mycursor = mydb.cursor(buffered=True)

    mycursor.execute('''
        CREATE TABLE IF NOT EXISTS agg_insurance (
            ID INT AUTO_INCREMENT PRIMARY KEY,
            States VARCHAR(100),
            Years INT,
            Quarter INT,
            Name VARCHAR(100),
            Type VARCHAR(10),
            Count INT,
            Amount DOUBLE,
            UNIQUE KEY idx_unique_entry (States, Years, Quarter,Count)
        )
    ''')

    query1 = "INSERT INTO agg_insurance (States, Years, Quarter, Name, Type, Count, Amount) VALUES (%s, %s, %s, %s, %s, %s, %s)"

    values = [tuple(row) for _, row in agg_insurance.iterrows()]


    mycursor.executemany(query1, values)
    mydb.commit()
    mycursor.close()
    mydb.close()
except:
    pass

#creating table for agg_user
try:
    #connection to sql
    mydb =mysql.connect(host="localhost",
                    user="root",
                    password="",
                    database="phonepepulse"
                    )
    mycursor = mydb.cursor(buffered=True)

    mycursor.execute('''create table if not exists agg_user (ID int auto_increment primary key,States varchar(100), Years int, Quarter int, Brand varchar(100),
                        Count int, Percentage double, unique key idx_unique_entry(States,Years, Quarter,Brand))''')

    query2="insert into agg_user(States,Years,Quarter,Brand,Count,Percentage) values (%s,%s,%s,%s,%s,%s)"
    values=[tuple(row) for _,row in agg_user.iterrows()]
    mycursor.executemany(query2,values)
    mydb.commit()
    mycursor.close()
    mydb.close()
except:
    pass

#creating table for map_insurance
try:
    #connection to sql
    mydb =mysql.connect(host="localhost",
                    user="root",
                    password="",
                    database="phonepepulse"
                    )
    mycursor = mydb.cursor(buffered=True)

    mycursor.execute('''
            CREATE TABLE IF NOT EXISTS map_insurance (
                ID INT AUTO_INCREMENT PRIMARY KEY,
                States VARCHAR(100),
                Years INT,
                Quarter INT,
                District_Names VARCHAR(100),
                Types VARCHAR(10),
                Count INT,
                Amount DOUBLE,
                UNIQUE KEY idx_unique_entry (States, Years, Quarter, District_Names, Types)
            )
        ''')
    query3 = "INSERT INTO map_insurance (States, Years, Quarter, District_Names, Types, Count, Amount) VALUES (%s, %s, %s, %s, %s, %s, %s)"

    values = [tuple(row) for _, row in map_insur_hover.iterrows()]

    mycursor.executemany(query3, values)
    mydb.commit()
    mycursor.close()
    mydb.close()
except:
    pass

#creating table for map_transaction
try:
    #connection to sql
    mydb =mysql.connect(host="localhost",
                    user="root",
                    password="",
                    database="phonepepulse"
                    )
    mycursor = mydb.cursor(buffered=True)

    mycursor.execute('''
            CREATE TABLE IF NOT EXISTS map_transaction (
                ID INT AUTO_INCREMENT PRIMARY KEY,
                States VARCHAR(100),
                Years INT,
                Quarter INT,
                District_Names VARCHAR(100),
                Type VARCHAR(10),
                Transaction_Count INT,
                Transaction_Amount DOUBLE,
                UNIQUE KEY idx_unique_entry (States, Years, Quarter, District_Names, Type)
            )
        ''')

    query4 = "INSERT INTO map_transaction (States, Years, Quarter, District_Names, Type, Transaction_Count, Transaction_Amount) VALUES (%s, %s, %s, %s, %s, %s, %s)"

    values = [tuple(row) for _, row in map_trans_hover.iterrows()]

    mycursor.executemany(query4, values)
    mydb.commit()

    mycursor.close()
    mydb.close()
except:
    pass

#creating table for map_user
try:
    #connection to sql
    mydb =mysql.connect(host="localhost",
                    user="root",
                    password="",
                    database="phonepepulse"
                    )
    mycursor = mydb.cursor(buffered=True)

    mycursor.execute('''
            CREATE TABLE IF NOT EXISTS map_user (
                ID INT AUTO_INCREMENT PRIMARY KEY,
                States VARCHAR(100),
                Years INT,
                Quarter INT,
                District_Names VARCHAR(100),
                Registered_Users DOUBLE,
                Apps_Open DOUBLE,
                UNIQUE KEY idx_unique_entry (States, Years, Quarter, District_Names)
            )
        ''')
    query5 = "INSERT INTO map_user (States, Years, Quarter, District_Names, Registered_Users, Apps_Open) VALUES (%s, %s, %s, %s, %s, %s)"
    values = [tuple(row) for _, row in map_user_hover.iterrows()]

    mycursor.executemany(query5, values)
    mydb.commit()

    mycursor.close()
    mydb.close()
except:
    pass

#creating table for top_insurance_districts
try:
    #connection to sql
    mydb =mysql.connect(host="localhost",
                    user="root",
                    password="",
                    database="phonepepulse"
                    )
    mycursor = mydb.cursor(buffered=True)

    mycursor.execute('''
            CREATE TABLE IF NOT EXISTS top_insurance_districts (
                ID INT AUTO_INCREMENT PRIMARY KEY,
                States VARCHAR(100),
                Years INT,
                Quarter INT,
                District_Names VARCHAR(100),
                Type VARCHAR(10),
                Transaction_Count INT,
                Transaction_Amount DOUBLE,
                UNIQUE KEY idx_unique_entry (States, Years, Quarter, District_Names, Type)
            )
        ''')

    query6 = "INSERT INTO top_insurance_districts (States, Years, Quarter, District_Names, Type, Transaction_Count, Transaction_Amount) VALUES (%s, %s, %s, %s, %s, %s, %s)"

    values = [tuple(row) for _, row in top_insurance_districts.iterrows()]

    mycursor.executemany(query6, values)
    mydb.commit()
    mycursor.close()
    mydb.close()
except:
    pass

#creating table for top_insurance_Pincode
try:
    #connection to sql
    mydb =mysql.connect(host="localhost",
                    user="root",
                    password="",
                    database="phonepepulse"
                    )
    mycursor = mydb.cursor(buffered=True)

    mycursor.execute('''
            CREATE TABLE IF NOT EXISTS top_insurance_pincode (
                ID INT AUTO_INCREMENT PRIMARY KEY,
                States VARCHAR(100),
                Years INT,
                Quarter INT,
                Pincodes VARCHAR(100),
                Type VARCHAR(10),
                Transaction_Count INT,
                Transaction_Amount DOUBLE,
                UNIQUE KEY idx_unique_entry (States, Years, Quarter, Pincodes, Type)
            )
        ''')

    query7 = "INSERT INTO top_insurance_pincode (States, Years, Quarter, Pincodes, Type, Transaction_Count, Transaction_Amount) VALUES (%s, %s, %s, %s, %s, %s, %s)"

    values = [tuple(row) for _, row in top_insurance_pincode.iterrows()]

    mycursor.executemany(query7, values)
    mydb.commit()

    mycursor.close()
    mydb.close()
except:
    pass

#creating table for top_transaction_Districts
try:
    #connection to sql
    mydb =mysql.connect(host="localhost",
                    user="root",
                    password="",
                    database="phonepepulse"
                    )
    mycursor = mydb.cursor(buffered=True)

    mycursor.execute('''
            CREATE TABLE IF NOT EXISTS top_transaction_districts (
                ID INT AUTO_INCREMENT PRIMARY KEY,
                States VARCHAR(100),
                Years INT,
                Quarter INT,
                District_Names VARCHAR(100),
                Type VARCHAR(10),
                Transaction_Count INT,
                Transaction_Amount DOUBLE,
                UNIQUE KEY idx_unique_entry (States, Years, Quarter, District_Names, Type)
            )
        ''')

    query8 = "INSERT INTO top_transaction_districts (States, Years, Quarter, District_Names, Type, Transaction_Count, Transaction_Amount) VALUES (%s, %s, %s, %s, %s, %s, %s)"

    values = [tuple(row) for _, row in top_transaction_districts.iterrows()]

    mycursor.executemany(query8, values)
    mydb.commit()

    mycursor.close()
    mydb.close()
except:
    pass

#creating table for top_transaction_Pincode
try:
    #connection to sql
    mydb =mysql.connect(host="localhost",
                    user="root",
                    password="",
                    database="phonepepulse"
                    )
    mycursor = mydb.cursor(buffered=True)

    mycursor.execute('''
            CREATE TABLE IF NOT EXISTS top_transaction_pincode (
                ID INT AUTO_INCREMENT PRIMARY KEY,
                States VARCHAR(100),
                Years INT,
                Quarter INT,
                Pincodes VARCHAR(100),
                Type VARCHAR(10),
                Transaction_Count INT,
                Transaction_Amount DOUBLE,
                UNIQUE KEY idx_unique_entry (States, Years, Quarter, Pincodes, Type)
            )
        ''')

    query9 = "INSERT INTO top_transaction_pincode (States, Years, Quarter, Pincodes, Type, Transaction_Count, Transaction_Amount) VALUES (%s, %s, %s, %s, %s, %s, %s)"

    values = [tuple(row) for _, row in top_transaction_pincode.iterrows()]

    mycursor.executemany(query9, values)
    mydb.commit()

    mycursor.close()
    mydb.close()
except:
    pass

#creating table for top_user_districts
try:
    #connection to sql
    mydb =mysql.connect(host="localhost",
                    user="root",
                    password="",
                    database="phonepepulse"
                    )
    mycursor = mydb.cursor(buffered=True)

    mycursor.execute('''
            CREATE TABLE IF NOT EXISTS top_user_districts (
                ID INT AUTO_INCREMENT PRIMARY KEY,
                States VARCHAR(100),
                Years INT,
                Quarter INT,
                District_Names VARCHAR(100),
                Registered_Users DOUBLE,
                UNIQUE KEY idx_unique_entry (States, Years, Quarter, District_Names)
            )
        ''')

    query10 = "INSERT INTO top_user_districts (States, Years, Quarter, District_Names, Registered_Users) VALUES (%s, %s, %s, %s, %s)"

    values = [tuple(row) for _, row in top_user_districts.iterrows()]

    mycursor.executemany(query10, values)
    mydb.commit()

    mycursor.close()
    mydb.close()
except:
    pass

#creating table for top_user_pincode
try:
    #connection to sql
    mydb =mysql.connect(host="localhost",
                    user="root",
                    password="",
                    database="phonepepulse"
                    )
    mycursor = mydb.cursor(buffered=True)

    mycursor.execute('''
            CREATE TABLE IF NOT EXISTS top_user_pincode (
                ID INT AUTO_INCREMENT PRIMARY KEY,
                States VARCHAR(100),
                Years INT,
                Quarter INT,
                Pincodes VARCHAR(100),
                Registered_Users DOUBLE,
                UNIQUE KEY idx_unique_entry (States, Years, Quarter, Pincodes)
            )
        ''')

    query11 = "INSERT INTO top_user_pincode (States, Years, Quarter, Pincodes, Registered_Users) VALUES (%s, %s, %s, %s, %s)"

    values = [tuple(row) for _, row in top_user_pincode.iterrows()]

    mycursor.executemany(query11, values)
    mydb.commit()

    mycursor.close()
    mydb.close()
except:
    pass


#connection to sql
mydb =mysql.connect(host="localhost",
                user="root",
                password="",
                database="phonepepulse"
                )
mycursor = mydb.cursor(buffered=True)


#STREAMLIT APP

st.set_page_config (layout= "wide")
#icon_image ="images.png"  
#st.image(icon_image, width=250) 

st.title(":violet[Phonepe Data Visualization and Exploration]")

with st.sidebar:
    select=option_menu("Menu",["Home","Data Exploration","Top Charts"])
    
# MENU 1 - HOME
if select == "Home":

    st.header(":red[A User-Friendly Tool Using Streamlit and Plotly]")
    st.write("### :green[Technologies used :] Github Cloning, Python, Pandas, MySQL, Streamlit, and Plotly.")
    st.write("### :green[Overview :] In this streamlit web app you can visualize the phonepe pulse data and gain lot of insights on transactions, number of users, top 10 state, district, pincode and which brand has most number of users and so on.")
    

elif select=="Data Exploration":
    st.header(":red[Data Exploration]")
    Type = st.sidebar.selectbox("**Type**", ("Insurance","Transaction","Users"))
    Year = st.sidebar.slider("**Year**", min_value=2018, max_value=2023)
    Quarter = st.sidebar.slider("**Quarter**", min_value=1, max_value=4)
    
    
    if Type=="Insurance":
        method=st.radio("**Select the Method**",["Aggregated Analysis","Map Analysis"])
        
        if method=="Map Analysis":
            
                st.markdown("## :violet[Overall State Data - Insurance Amount]")
                mycursor.execute(f"select states,sum(Amount) as Insurance_Amount from map_insurance where years= {Year} and quarter = {Quarter} group by states order by states")
                df1 = pd.DataFrame(mycursor.fetchall(),columns= ['State','Insurance_Amount'])
                df2 = pd.read_csv('C:/Users/Karthck/Documents/phonepe/state_names.csv')
                df1.State= df2
                

                fig = px.choropleth(df1,geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                        featureidkey='properties.ST_NM',
                        locations='State',
                        color='Insurance_Amount',
                        color_continuous_scale='earth')

                fig.update_geos(fitbounds="locations", visible=False)
                st.plotly_chart(fig,use_container_width=True)
                
            # Overall State Data - INSURANCE COUNT - INDIA MAP
            
                
                st.markdown("## :violet[Overall State Data - INSURANCE Count]")
                mycursor.execute(f"select States, sum(Count) as Total_Count from map_insurance where years = {Year} and quarter = {Quarter} group by states order by states")
                df1 = pd.DataFrame(mycursor.fetchall(),columns= ['State', 'Total_Count'])
                df2 = pd.read_csv('C:/Users/Karthck/Documents/phonepe/state_names.csv')
                df1.Total_Count = df1.Total_Count.astype(int)
                df1.State = df2

                fig = px.choropleth(df1,geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                        featureidkey='properties.ST_NM',
                        locations='State',
                        color='Total_Count',
                        color_continuous_scale='plasma')

                fig.update_geos(fitbounds="locations", visible=False)
                st.plotly_chart(fig,use_container_width=True)
        
        elif method=="Aggregated Analysis":
            # BAR CHART - INSURANCE AMOUNT
            st.subheader("Insurance State Wise")
            mycursor.execute(f"select States,Count,Amount from agg_insurance where years = {Year} and quarter = {Quarter} group by states order by states")
            df1 = pd.DataFrame(mycursor.fetchall(), columns=['State','Insurance_Count','Insurance_Amount'])
            fig = px.bar(df1,
                        title="States",
                        x="State",
                        y="Insurance_Count",
                        orientation='v',
                        color='Insurance_Amount',
                        color_continuous_scale=px.colors.sequential.Viridis)
            st.plotly_chart(fig,use_container_width=True)
        
    elif Type=="Transaction":
        method=st.radio("**Select the Method**",["Aggregated Analysis","Map Analysis"])
        
        if method=="Map Analysis":
            
                st.markdown("## :violet[Overall State Data - Transactions Amount]")
                mycursor.execute(f"select states,sum(Transaction_Amount) as Total_Amount from map_transaction where years= {Year} and quarter = {Quarter} group by states order by states")
                df1 = pd.DataFrame(mycursor.fetchall(),columns= ['State','Total_Amount'])
                df2 = pd.read_csv('C:/Users/Karthck/Documents/phonepe/state_names.csv')
                df1.State= df2
                

                fig = px.choropleth(df1,geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                        featureidkey='properties.ST_NM',
                        locations='State',
                        color='Total_Amount',
                        color_continuous_scale='magma')

                fig.update_geos(fitbounds="locations", visible=False)
                st.plotly_chart(fig,use_container_width=True)
                
            # Overall State Data - TRANSACTIONS COUNT - INDIA MAP
            
                
                st.markdown("## :violet[Overall State Data - Transactions Count]")
                mycursor.execute(f"select states, sum(Transaction_Count) as Total_Count from map_transaction where years = {Year} and quarter = {Quarter} group by states order by states")
                df1 = pd.DataFrame(mycursor.fetchall(),columns= ['State', 'Total_Count'])
                df2 = pd.read_csv('C:/Users/Karthck/Documents/phonepe/state_names.csv')
                df1.Total_Count = df1.Total_Count.astype(int)
                df1.State = df2

                fig = px.choropleth(df1,geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                        featureidkey='properties.ST_NM',
                        locations='State',
                        color='Total_Count',
                        color_continuous_scale='agsunset')

                fig.update_geos(fitbounds="locations", visible=False)
                st.plotly_chart(fig,use_container_width=True)
        
        elif method=="Aggregated Analysis":
            # BAR CHART - TOP PAYMENT TYPE
            st.subheader(":violet[Top Payment Type]")
            mycursor.execute(f"select Transaction_type, sum(Transaction_count) as Total_Transactions, sum(Transaction_amount) as Total_amount from agg_transaction where years= {Year} and quarter = {Quarter} group by Transaction_type order by Transaction_type")
            df = pd.DataFrame(mycursor.fetchall(), columns=['Transaction_type', 'Total_Transactions','Total_amount'])

            fig = px.bar(df,
                        title='Transaction Types vs Total_Transactions',
                        x="Total_Transactions",
                        y="Transaction_type",
                        orientation='h',
                        color='Total_amount',
                        color_continuous_scale=px.colors.sequential.Viridis)
            st.plotly_chart(fig,use_container_width=True)
            
            # BAR CHART TRANSACTION TYPE           
            st.subheader(":violet[Select any State for Payment Type Analysis]")
            selected_state = st.selectbox("",
                                ('Andaman and Nicobar Islands', 'Andhra Pradesh',
                                    'Arunachal Pradesh', 'Assam', 'Bihar', 'Chandigarh',
                                    'Chhattisgarh', 'Dadra and Nagar Haveli and Daman and Diu',
                                    'Delhi', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh',
                                    'Jammu and Kashmir', 'Jharkhand', 'Karnataka', 'Kerala', 'Ladakh',
                                    'Lakshadweep', 'Madhya Pradesh', 'Maharashtra', 'Manipur',
                                    'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Puducherry',
                                    'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana',
                                    'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal'),index=30)

            mycursor.execute(f"select States,Transaction_type,Transaction_count ,Transaction_amount from agg_transaction where years = {Year} and quarter = {Quarter} and States = '{selected_state}' group by Transaction_type order by Transaction_type")
            
            df1 = pd.DataFrame(mycursor.fetchall(), columns=['State','Transaction_type','Transaction_count','Transaction_amount'])
            fig = px.bar(df1,
                        title=selected_state,
                        x="Transaction_type",
                        y="Transaction_count",
                        orientation='v',
                        color='Transaction_amount',
                        color_continuous_scale=px.colors.sequential.Agsunset)
            st.plotly_chart(fig,use_container_width=True)
            
            # BAR CHART TRANSACTION TYPE           
            st.subheader(":violet[Select any State for district wise analysis]")
            mycursor.execute(f"select States,District_Names,Transaction_count ,Transaction_amount from map_transaction where years = {Year} and quarter = {Quarter} and States = '{selected_state}' group by States,District_Names order by States,District_Names")
            
            df1 = pd.DataFrame(mycursor.fetchall(), columns=['State','District','Transaction_count','Transaction_amount'])
            fig = px.bar(df1,
                        title=selected_state,
                        x="District",
                        y="Transaction_count",
                        orientation='v',
                        color='Transaction_amount',
                        color_continuous_scale=px.colors.sequential.Agsunset)
            st.plotly_chart(fig,use_container_width=True)
            
        
    elif Type=="Users":
        method=st.radio("**Select the Method**",["Aggregated Analysis","Map Analysis"])
        
        if method=="Map Analysis":
            # Overall State Data - TOTAL APPOPENS - INDIA MAP
            st.markdown("## :violet[Overall State Data - User App opening frequency]")
            mycursor.execute(f"select states, sum(Registered_Users) as Total_Users, sum(Apps_Open) as Total_App_opens from map_user where years = {Year} and quarter = {Quarter} group by states order by states")
            df1 = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Total_Users','Total_App_opens'])
            df2 = pd.read_csv('C:/Users/Karthck/Documents/phonepe/state_names.csv')
            df1.Total_App_opens = df1.Total_App_opens.astype(float)
            df1.State = df2
            
            fig = px.choropleth(df1,geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                    featureidkey='properties.ST_NM',
                    locations='State',
                    color='Total_App_opens',
                    color_continuous_scale='sunset')

            fig.update_geos(fitbounds="locations", visible=False)
            st.plotly_chart(fig,use_container_width=True)
        
        elif method=="Aggregated Analysis":
            # BAR CHART Brand - State wise 
            st.markdown("## :violet[Select any State to explore more]")
            selected_state = st.selectbox("",
                                ('Andaman and Nicobar Islands', 'Andhra Pradesh',
                                    'Arunachal Pradesh', 'Assam', 'Bihar', 'Chandigarh',
                                    'Chhattisgarh', 'Dadra and Nagar Haveli and Daman and Diu',
                                    'Delhi', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh',
                                    'Jammu and Kashmir', 'Jharkhand', 'Karnataka', 'Kerala', 'Ladakh',
                                    'Lakshadweep', 'Madhya Pradesh', 'Maharashtra', 'Manipur',
                                    'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Puducherry',
                                    'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana',
                                    'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal'),index=30)
            
            mycursor.execute(f"select States,Brand,Count,Percentage from agg_user where years = {Year} and quarter = {Quarter} and states = '{selected_state}' group by Brand order by Brand")
            
            df = pd.DataFrame(mycursor.fetchall(), columns=['State','Brand','Count','Percentage'])
            
            fig = px.bar(df,
                        title=selected_state,
                        x="Brand",
                        y="Count",
                        orientation='v',
                        color='Percentage',
                        color_continuous_scale=px.colors.sequential.Agsunset)
            st.plotly_chart(fig,use_container_width=True)
            
            
# Top Charts
elif select=="Top Charts":
    st.markdown("## :violet[Top Charts]")
    Type = st.sidebar.selectbox("**Type**", ("Transactions","Insurance","Users"))
    Year = st.slider("**Year**", min_value=2018, max_value=2023)
    Quarter = st.slider("**Quarter**", min_value=1, max_value=4)

#TOP CHARTS- INSURANCE    
    if Type=="Insurance":
        st.header("INSURANCE")
        col1,col2,= st.columns([2,2],gap="medium")
        col3,col4=st.columns([2,2],gap="small")
        
        with col1:
            st.markdown("### :violet[State]")
            mycursor.execute(f"select states, sum(Count) as Total_Transactions_Count, sum(Amount) as Total_Amount from agg_insurance where years = {Year} and quarter = {Quarter} group by states order by states desc limit 10")
            df = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Count','Total_Amount'])
            fig = px.pie(df, values='Total_Amount',
                                names='State',
                                title='Top 10',
                                color_discrete_sequence=px.colors.sequential.Plasma,
                                hover_data=['Count'],
                                labels={'Count':'Count'})
            st.plotly_chart(fig,use_container_width=True)
            
        with col2:
            st.markdown("### :violet[District]")
            mycursor.execute(f"select District_Names , sum(Transaction_Count) as Total_Count, sum(Transaction_Amount) as Total_Amount from top_insurance_districts where years = {Year} and quarter = {Quarter} group by District_Names order by District_Names desc limit 10")
            df = pd.DataFrame(mycursor.fetchall(), columns=['District_Names', 'Transactions_Count','Total_Amount'])

            fig = px.pie(df, values='Total_Amount',
                                names='District_Names',
                                title='Top 10',
                                color_discrete_sequence=px.colors.sequential.Plasma,
                                hover_data=['Transactions_Count'],
                                labels={'Transactions_Count':'Transactions_Count'})
            #fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)
        
        with col3:
            st.markdown("### :violet[Pincode]")
            mycursor.execute(f"select Pincodes, sum(Transaction_Count) as Total_Transactions_Count, sum(Transaction_Amount) as Total_Amount from top_insurance_pincode where years = {Year} and quarter = {Quarter} group by Pincodes order by Pincodes desc limit 10")
            df = pd.DataFrame(mycursor.fetchall(), columns=['Pincode', 'Transactions_Count','Total_Amount'])
            fig = px.pie(df, values='Total_Amount',
                                names='Pincode',
                                title='Top 10',
                                color_discrete_sequence=px.colors.sequential.Plasma,
                                hover_data=['Transactions_Count'],
                                labels={'Transactions_Count':'Transactions_Count'})
            #fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)


# Top Charts - TRANSACTIONS    
    elif Type == "Transactions":
        st.header("TRANSACTIONS")
        col1,col2= st.columns([2,2],gap="small")
        col3,col4= st.columns([2,2],gap="small")
        
        with col1:
            st.markdown(":violet[State]")
            mycursor.execute(f"select states,Transaction_type,Transaction_count,Transaction_amount from agg_transaction where years = {Year} and quarter = {Quarter} group by states order by Transaction_amount desc limit 10")
            df = pd.DataFrame(mycursor.fetchall(), columns=['State','Transaction_Type','Transactions_Count','Transaction_Amount'])
            fig = px.pie(df, values='Transaction_Amount',
                            names='State',
                            title='Top 10',
                            color_discrete_sequence=px.colors.sequential.Agsunset,
                            hover_data=['Transactions_Count'],
                            labels={'Transactions_Count':'Transactions_Count'})

            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)
            
        with col2:
            st.markdown("### :violet[District]")
            mycursor.execute(f"select District_Names , sum(Transaction_Count) as Total_Count, sum(Transaction_Amount) as Total_Amount from map_transaction where years = {Year} and quarter = {Quarter} group by District_Names order by Total_Amount desc limit 10")
            df = pd.DataFrame(mycursor.fetchall(), columns=['District_Names', 'Transactions_Count','Total_Amount'])

            fig = px.pie(df, values='Total_Amount',
                            names='District_Names',
                            title='Top 10',
                            color_discrete_sequence=px.colors.sequential.Agsunset,
                            hover_data=['Transactions_Count'],
                            labels={'Transactions_Count':'Transactions_Count'})

            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)
            
        
        with col3:
            st.markdown("### :violet[Pincode]")
            mycursor.execute(f"select Pincodes, sum(Transaction_Count) as Total_Transactions_Count, sum(Transaction_Amount) as Total from top_transaction_pincode where years = {Year} and quarter = {Quarter} group by Pincodes order by Total desc limit 10")
            df = pd.DataFrame(mycursor.fetchall(), columns=['Pincodes', 'Transactions_Count','Total_Amount'])
            fig = px.pie(df, values='Total_Amount',
                            names='Pincodes',
                            title='Top 10',
                            color_discrete_sequence=px.colors.sequential.Agsunset,
                            hover_data=['Transactions_Count'],
                            labels={'Transactions_Count':'Transactions_Count'})

            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)
    
    
    # Top Charts - Users
    
    elif Type=="Users":
        st.header("USERS")
        col1,col2= st.columns([3,3],gap="small")
        col3,col4 = st.columns([3,3],gap="small")
        with col1:
            st.markdown("### :violet[Brands]")
            mycursor.execute(f"select Brand, sum(Count) as Total_Count, avg(Percentage)*100 as Avg_Percentage from agg_user where years = {Year} and quarter = {Quarter} group by brand order by Total_Count desc limit 10")
            df = pd.DataFrame(mycursor.fetchall(), columns=['Brand', 'Total_Users','Avg_Percentage'])
            fig = px.bar(df,
                                title='Top 10',
                                x="Total_Users",
                                y="Brand",
                                orientation='h',
                                color='Avg_Percentage',
                                color_continuous_scale=px.colors.sequential.Inferno)
            st.plotly_chart(fig,use_container_width=True)   
            
    
        with col2:
            st.markdown("### :violet[District]")
            mycursor.execute(f"select District_Names, sum(Registered_Users) as Total_Users, sum(Apps_Open) as Total_Appopens from map_user where years = {Year} and quarter = {Quarter} group by District_Names order by Total_Appopens desc limit 10")
            df = pd.DataFrame(mycursor.fetchall(), columns=['District', 'Total_Users','Total_Appopens'])
            df.Total_Users = df.Total_Users.astype(float)
            fig = px.bar(df,
                            title='Top 10',
                            x="Total_Users",
                            y="District",
                            orientation='h',
                            color='Total_Appopens',
                            color_continuous_scale=px.colors.sequential.Inferno)
            st.plotly_chart(fig,use_container_width=True)
            
        with col3:
            st.markdown("### :violet[Pincode]")
            mycursor.execute(f"select Pincodes, sum(Registered_Users) as Total_Users from top_user_pincode where years = {Year} and quarter = {Quarter} group by Pincodes order by Total_Users desc limit 10")
            df = pd.DataFrame(mycursor.fetchall(), columns=['Pincode', 'Total_Users'])
            fig = px.pie(df,
                            values='Total_Users',
                            names='Pincode',
                            title='Top 10',
                            color_discrete_sequence=px.colors.sequential.Inferno,
                            hover_data=['Total_Users'])
            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)
        
        with col4:
            st.markdown("### :violet[State]")
            mycursor.execute(f"select States, sum(Registered_users) as Total_Users, sum(Apps_Open) as Total_Appopens from map_user where years = {Year} and quarter = {Quarter} group by states order by Total_Users desc limit 10")
            df = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Total_Users','Total_Appopens'])
            fig = px.pie(df, values='Total_Users',
                                names='State',
                                title='Top 10',
                                color_discrete_sequence=px.colors.sequential.Inferno,
                                hover_data=['Total_Appopens'],
                                labels={'Total_Appopens':'Total_Appopens'})
            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)