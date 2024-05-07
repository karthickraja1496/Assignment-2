#git clone https://github.com/PhonePe/pulse.git

import os
import json
import mysql.connector as mysql
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px


#connection to sql
mydb =mysql.connect(host="localhost",
                user="root",
                password="",
                database="phonepe"
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
                df2 = pd.read_csv('D:/Documents/phonepe/state_names.csv')
                df1.State= df2
                

                fig = px.choropleth(df1,geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                        featureidkey='properties.ST_NM',
                        locations='State',
                        color='Insurance_Amount',
                        color_continuous_scale='earth')

                fig.update_geos(fitbounds="locations", visible=False)
                st.plotly_chart(fig,use_container_width=False)
                
            # Overall State Data - INSURANCE COUNT - INDIA MAP
            
                
                st.markdown("## :violet[Overall State Data - INSURANCE Count]")
                mycursor.execute(f"select States, sum(Count) as Total_Count from map_insurance where years = {Year} and quarter = {Quarter} group by states order by states")
                df1 = pd.DataFrame(mycursor.fetchall(),columns= ['State', 'Total_Count'])
                df2 = pd.read_csv('D:/Documents/phonepe/state_names.csv')
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
            st.plotly_chart(fig,use_container_width=False)
        
    elif Type=="Transaction":
        method=st.radio("**Select the Method**",["Aggregated Analysis","Map Analysis"])
        
        if method=="Map Analysis":
            
                st.markdown("## :violet[Overall State Data - Transactions Amount]")
                mycursor.execute(f"select States,sum(Transaction_Amount) as Total_Amount from map_transaction where years= {Year} and quarter = {Quarter} group by States order by States")
                df1 = pd.DataFrame(mycursor.fetchall(),columns= ['State','Total_Amount'])
                df2 = pd.read_csv('D:/Documents/phonepe/state_names.csv')
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
                mycursor.execute(f"select States, sum(Transaction_Count) as Total_Count from map_transaction where years = {Year} and quarter = {Quarter} group by States order by States")
                df1 = pd.DataFrame(mycursor.fetchall(),columns= ['State', 'Total_Count'])
                df2 = pd.read_csv('D:/Documents/phonepe/state_names.csv')
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
            st.plotly_chart(fig,use_container_width=False)
            
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
            df2 = pd.read_csv('D:/Documents/phonepe/state_names.csv')
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
            st.plotly_chart(fig,use_container_width=False)
            
            
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
            df = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Total_Transactions_Count','Total_Amount'])
            fig = px.pie(df, values='Total_Amount',
                                names='State',
                                title='Top 10',
                                color_discrete_sequence=px.colors.sequential.Plasma,
                                hover_data=['Total_Transactions_Count'],
                                labels={'Count':'Count'})
            st.plotly_chart(fig,use_container_width=True)
            
        with col2:
            st.markdown("### :violet[District]")
            mycursor.execute(f"select District_Names , sum(Transaction_Count) as Total_Count, sum(Transaction_Amount) as Total_Amount from top_insurance_districts where years = {Year} and quarter = {Quarter} group by District_Names order by District_Names desc limit 10")
            df = pd.DataFrame(mycursor.fetchall(), columns=['District_Names', 'Total_Count','Total_Amount'])

            fig = px.pie(df, values='Total_Amount',
                                names='District_Names',
                                title='Top 10',
                                color_discrete_sequence=px.colors.sequential.Plasma,
                                hover_data=['Total_Count'],
                                labels={'Transactions_Count':'Transactions_Count'})
            #fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)
        
        with col3:
            st.markdown("### :violet[Pincode]")
            mycursor.execute(f"select Pincodes, sum(Transaction_Count) as Total_Transactions_Count, sum(Transaction_Amount) as Total_Amount from top_insurance_pincode where years = {Year} and quarter = {Quarter} group by Pincodes order by Pincodes desc limit 10")
            df = pd.DataFrame(mycursor.fetchall(), columns=['Pincode', 'Total_Transactions_Count','Total_Amount'])
            fig = px.pie(df, values='Total_Amount',
                                names='Pincode',
                                title='Top 10',
                                color_discrete_sequence=px.colors.sequential.Plasma,
                                hover_data=['Total_Transactions_Count'],
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
            df = pd.DataFrame(mycursor.fetchall(), columns=['District_Names', 'Total_Count','Total_Amount'])

            fig = px.pie(df, values='Total_Amount',
                            names='District_Names',
                            title='Top 10',
                            color_discrete_sequence=px.colors.sequential.Agsunset,
                            hover_data=['Total_Count'],
                            labels={'Transaction_Count':'Transaction_Count'})

            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)
            
        
        with col3:
            st.markdown("### :violet[Pincode]")
            mycursor.execute(f"select Pincodes, sum(Transaction_Count) as Total_Transactions_Count, sum(Transaction_Amount) as Total from top_transaction_pincode where years = {Year} and quarter = {Quarter} group by Pincodes order by Total desc limit 10")
            df = pd.DataFrame(mycursor.fetchall(), columns=['Pincodes', 'Total_Transactions_Count','Total_Amount'])
            fig = px.pie(df, values='Total_Amount',
                            names='Pincodes',
                            title='Top 10',
                            color_discrete_sequence=px.colors.sequential.Agsunset,
                            hover_data=['Total_Transactions_Count'],
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