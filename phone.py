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

#map_insurance
path4="C:/Users/Karthck/Documents/phonepe/pulse/data/map/insurance/hover/country/india/state/"
map_insur_hover_st_list=os.listdir(path4)

data4={"States":[],"Years":[],"Quarter":[],"District Name":[],"Type":[],"Count":[],"Amount":[]}

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
                data4["District Name"].append(Name)
                data4["Type"].append(Type)
                data4["Count"].append(Count)
                data4["Amount"].append(Amount)
                data4["States"].append(state)
                data4["Years"].append(year)
                data4["Quarter"].append(int(file.strip(".json")))

map_insur_hover=pd.DataFrame(data4)

#map_transaction
path5="C:/Users/Karthck/Documents/phonepe/pulse/data/map/transaction/hover/country/india/state/"
map_trans_hover_st_list=os.listdir(path5)

data5={"States":[],"Years":[],"Quarter":[],"District Name":[],"Type":[],"Transaction_Count":[],"Transaction_Amount":[]}

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
                data5["District Name"].append(Name)
                data5["Type"].append(Type)
                data5["Transaction_Count"].append(Count)
                data5["Transaction_Amount"].append(Amount)
                data5["States"].append(state)
                data5["Years"].append(year)
                data5["Quarter"].append(int(file.strip(".json")))

map_trans_hover=pd.DataFrame(data5)

#map_user
path6="C:/Users/Karthck/Documents/phonepe/pulse/data/map/user/hover/country/india/state/"
map_user_hover_st_list=os.listdir(path6)

data6={"States":[],"Years":[],"Quarter":[],"District Name":[],"Registered Users":[],"Apps Open":[]}

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
                data6["District Name"].append(Name)
                data6["Registered Users"].append(user)
                data6["Apps Open"].append(apps)
                data6["States"].append(state)
                data6["Years"].append(year)
                data6["Quarter"].append(int(file.strip(".json")))

map_user_hover=pd.DataFrame(data6)

#top insurance_districts
path7d="C:/Users/Karthck/Documents/phonepe/pulse/data/top/insurance/country/india/state/"
top_insur_st_list=os.listdir(path7d)

data7d={"States":[],"Years":[],"Quarter":[],"Entity Name":[],"Type":[],"Transaction_Count":[],"Transaction_Amount":[]}

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
                data7d["Entity Name"].append(Name)
                data7d["Type"].append(Type)
                data7d["Transaction_Count"].append(Count)
                data7d["Transaction_Amount"].append(Amount)
                data7d["States"].append(state)
                data7d["Years"].append(year)
                data7d["Quarter"].append(int(file.strip(".json")))

top_insurance_districts=pd.DataFrame(data7d)

#top insurance_pincode
path7="C:/Users/Karthck/Documents/phonepe/pulse/data/top/insurance/country/india/state/"
top_insur_hover_st_list=os.listdir(path7)

data7={"States":[],"Years":[],"Quarter":[],"Entity Name":[],"Type":[],"Transaction_Count":[],"Transaction_Amount":[]}

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
                data7["Entity Name"].append(Name)
                data7["Type"].append(Type)
                data7["Transaction_Count"].append(Count)
                data7["Transaction_Amount"].append(Amount)
                data7["States"].append(state)
                data7["Years"].append(year)
                data7["Quarter"].append(int(file.strip(".json")))

top_insurance_pincode=pd.DataFrame(data7)

#top transaction districts
path8d="C:/Users/Karthck/Documents/phonepe/pulse/data/top/transaction/country/india/state/"
top_insur_st_list=os.listdir(path8d)

data8d={"States":[],"Years":[],"Quarter":[],"Entity Name":[],"Type":[],"Transaction_Count":[],"Transaction_Amount":[]}

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
                data8d["Entity Name"].append(Name)
                data8d["Type"].append(Type)
                data8d["Transaction_Count"].append(Count)
                data8d["Transaction_Amount"].append(Amount)
                data8d["States"].append(state)
                data8d["Years"].append(year)
                data8d["Quarter"].append(int(file.strip(".json")))
                
top_transaction_districts=pd.DataFrame(data8d)

#top transaction pincode
path8="C:/Users/Karthck/Documents/phonepe/pulse/data/top/transaction/country/india/state/"
top_insur_hover_st_list=os.listdir(path8)

data8={"States":[],"Years":[],"Quarter":[],"Entity Name":[],"Type":[],"Transaction_Count":[],"Transaction_Amount":[]}

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
                data8["Entity Name"].append(Name)
                data8["Type"].append(Type)
                data8["Transaction_Count"].append(Count)
                data8["Transaction_Amount"].append(Amount)
                data8["States"].append(state)
                data8["Years"].append(year)
                data8["Quarter"].append(int(file.strip(".json")))
                
top_transaction_pincode=pd.DataFrame(data8)

#top user districts
path9d="C:/Users/Karthck/Documents/phonepe/pulse/data/top/user/country/india/state/"
top_user_list=os.listdir(path9d)

data9d={"States":[],"Years":[],"Quarter":[],"Names":[],"Registered Users":[]}

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
                data9d["Names"].append(Name)
                data9d["Registered Users"].append(user)
                data9d["States"].append(state)
                data9d["Years"].append(year)
                data9d["Quarter"].append(int(file.strip(".json")))
                
top_user_districts=pd.DataFrame(data9d)

#top user pincodes
path9="C:/Users/Karthck/Documents/phonepe/pulse/data/top/user/country/india/state/"
top_user_st_list=os.listdir(path9)

data9={"States":[],"Years":[],"Quarter":[],"Names":[],"Registered Users":[]}

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
                data9["Names"].append(Name)
                data9["Registered Users"].append(user)
                data9["States"].append(state)
                data9["Years"].append(year)
                data9["Quarter"].append(int(file.strip(".json")))
                
top_user_pincode=pd.DataFrame(data9)

#connection to sql
mydb =mysql.connect(host="localhost",
                user="root",
                password="",
                database="phonepe_pulse"
                )
mycursor = mydb.cursor(buffered=True)

#mycursor.execute("CREATE DATABASE phonepe_pulse")

#creating table for agg_transaction

mycursor.execute("drop table if exists agg_transaction")
mydb.commit()

mycursor.execute("create table agg_transaction (State varchar(100), Year int, Quarter int, Transaction_type varchar(100), Transaction_count int, Transaction_amount double)")

for i,row in agg_transaction.iterrows():
    query= "INSERT INTO agg_transaction VALUES (%s,%s,%s,%s,%s,%s)"
    mycursor.execute(query, tuple(row))
    mydb.commit()
    
#creating table for agg_insurance

mycursor.execute("drop table if exists agg_insurance")
mydb.commit()

mycursor.execute('''create table agg_insurance (State varchar(100), Years int, Quarter int, Name varchar(100),
                Type varchar(10),Count int, Amount double)''')

for i,row in agg_insurance.iterrows():
    query1="INSERT INTO agg_insurance values (%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(query1,tuple(row))
    mydb.commit()
    
#creating table for agg_user

mycursor.execute("drop table if exists agg_user")
mydb.commit()

mycursor.execute('''create table agg_user (State varchar(100), Years int, Quarter int, Brand varchar(100),
                Count int, Percentage double)''')

for i,row in agg_user.iterrows():
    query2="INSERT INTO agg_user values (%s,%s,%s,%s,%s,%s)"
    mycursor.execute(query2,tuple(row))
    mydb.commit()
    
#creating table for map_insurance

mycursor.execute("drop table if exists map_insurance")
mydb.commit()

mycursor.execute('''create table map_insurance (States varchar(100), Years int, Quarter int, District_Names varchar(100),
                Types varchar(10),Count int, Amount double)''')

for i,row in map_insur_hover.iterrows():
    query3="INSERT INTO map_insurance values (%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(query3,tuple(row))
    mydb.commit()
    
#creating table for map_transaction

mycursor.execute("drop table if exists map_transaction")
mydb.commit()

mycursor.execute('''create table map_transaction (State varchar(100), Year int, Quarter int, District_Name varchar(100),
                Type varchar(10),Transaction_Count int, Transaction_Amount double)''')

for i,row in map_trans_hover.iterrows():
    query4= "INSERT INTO map_transaction VALUES (%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(query4, tuple(row))
    mydb.commit()
    
#creating table for map_user

mycursor.execute("drop table if exists map_user")
mydb.commit()

mycursor.execute('''create table map_user (States varchar(100), Years int, Quarter int, District_Names varchar(100),
                Registered_Users double, Apps_Open double)''')

for i,row in map_user_hover.iterrows():
    query5="INSERT INTO map_user values (%s,%s,%s,%s,%s,%s)"
    mycursor.execute(query5,tuple(row))
    mydb.commit()
    
#creating table for top_insurance_districts

mycursor.execute("drop table if exists top_insurance_districts")
mydb.commit()

mycursor.execute('''create table top_insurance_districts (State varchar(100), Year int, Quarter int, Entity_Name varchar(100),
                Type varchar(10),Transaction_Count int, Transaction_Amount double)''')

for i,row in top_insurance_districts.iterrows():
    query6= "INSERT INTO top_insurance_districts VALUES (%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(query6, tuple(row))
    mydb.commit()
    
#creating table for top_insurance_Pincode

mycursor.execute("drop table if exists top_insurance_pincode")
mydb.commit()

mycursor.execute('''create table top_insurance_pincode (State varchar(100), Year int, Quarter int, Entity_Name varchar(100),
                Type varchar(10),Transaction_Count int, Transaction_Amount double)''')

for i,row in top_insurance_pincode.iterrows():
    query7= "INSERT INTO top_insurance_pincode VALUES (%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(query7, tuple(row))
    mydb.commit()
    
#creating table for top_transaction_Districts

mycursor.execute("drop table if exists top_transaction_districts")
mydb.commit()

mycursor.execute('''create table top_transaction_districts (State varchar(100), Year int, Quarter int, Entity_Name varchar(100),
                Type varchar(10),Transaction_Count int, Transaction_Amount double)''')

for i,row in top_transaction_districts.iterrows():
    query8= "INSERT INTO top_transaction_districts VALUES (%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(query8, tuple(row))
    mydb.commit()
    
#creating table for top_transaction_Pincode

mycursor.execute("drop table if exists top_transaction_pincode")
mydb.commit()

mycursor.execute('''create table top_transaction_pincode (State varchar(100), Year int, Quarter int, Entity_Name varchar(100),
                Type varchar(10),Transaction_Count int, Transaction_Amount double)''')

for i,row in top_transaction_pincode.iterrows():
    query9= "INSERT INTO top_transaction_pincode VALUES (%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(query9, tuple(row))
    mydb.commit()
    
#creating table for top_user_districts

mycursor.execute("drop table if exists top_user_districts")
mydb.commit()

mycursor.execute('''create table top_user_districts (State varchar(100), Years int, Quarter int, Names varchar(100),
                Registered_Users double)''')

for i,row in top_user_districts.iterrows():
    query10="INSERT INTO top_user_districts values (%s,%s,%s,%s,%s)"
    mycursor.execute(query10,tuple(row))
    mydb.commit()
    
#creating table for top_user_pincode

mycursor.execute("drop table if exists top_user_pincode")
mydb.commit()

mycursor.execute('''create table top_user_pincode (State varchar(100), Years int, Quarter int, Names varchar(100),
                Registered_Users double)''')

try:
        for i,row in top_user_pincode.iterrows():
            query11="INSERT INTO top_user_pincode values (%s,%s,%s,%s,%s)"
            mycursor.execute(query11,tuple(row))
            mydb.commit()
except:
    pass        

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
                mycursor.execute(f"select states, sum(Count) as Total_Count from map_insurance where years = {Year} and quarter = {Quarter} group by states order by states")
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
                        x="Insurance_Amount",
                        y="Insurance_Count",
                        orientation='v',
                        color='State',
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
                        x="Transaction_type",
                        y="Total_Transactions",
                        orientation='v',
                        color='Total_amount',
                        color_continuous_scale=px.colors.sequential.Turbo)
            st.plotly_chart(fig,use_container_width=False)
            
            # BAR CHART TRANSACTION TYPE           
            st.subheader(":violet[Select any State for Payment Type Analysis]")
            selected_state = st.selectbox("",
                                ('andaman-&-nicobar-islands','andhra-pradesh','arunachal-pradesh','assam','bihar',
                                'chandigarh','chhattisgarh','dadra-&-nagar-haveli-&-daman-&-diu','delhi','goa','gujarat','haryana',
                                'himachal-pradesh','jammu-&-kashmir','jharkhand','karnataka','kerala','ladakh','lakshadweep',
                                'madhya-pradesh','maharashtra','manipur','meghalaya','mizoram',
                                'nagaland','odisha','puducherry','punjab','rajasthan','sikkim',
                                'tamil-nadu','telangana','tripura','uttar-pradesh','uttarakhand','west-bengal'),index=30)

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
            mycursor.execute(f"select States,District_Name,Transaction_count ,Transaction_amount from map_transaction where years = {Year} and quarter = {Quarter} and States = '{selected_state}' group by States,District_Name order by States,District_Name")
            
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
                                ('andaman-&-nicobar-islands','andhra-pradesh','arunachal-pradesh','assam','bihar',
                                'chandigarh','chhattisgarh','dadra-&-nagar-haveli-&-daman-&-diu','delhi','goa','gujarat','haryana',
                                'himachal-pradesh','jammu-&-kashmir','jharkhand','karnataka','kerala','ladakh','lakshadweep',
                                'madhya-pradesh','maharashtra','manipur','meghalaya','mizoram',
                                'nagaland','odisha','puducherry','punjab','rajasthan','sikkim',
                                'tamil-nadu','telangana','tripura','uttar-pradesh','uttarakhand','west-bengal'),index=30)
            
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
            mycursor.execute(f"select District_Name , sum(Transaction_Count) as Total_Count, sum(Transaction_Amount) as Total_Amount from top_insurance_districts where years = {Year} and quarter = {Quarter} group by District_Name order by District_Name desc limit 10")
            df = pd.DataFrame(mycursor.fetchall(), columns=['District_Name', 'Transactions_Count','Total_Amount'])

            fig = px.pie(df, values='Total_Amount',
                                names='District_Name',
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
            mycursor.execute(f"select District_Name , sum(Transaction_Count) as Total_Count, sum(Transaction_Amount) as Total_Amount from map_transaction where years = {Year} and quarter = {Quarter} group by District_Name order by Total_Amount desc limit 10")
            df = pd.DataFrame(mycursor.fetchall(), columns=['District_Name', 'Transactions_Count','Total_Amount'])

            fig = px.pie(df, values='Total_Amount',
                            names='District_Name',
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