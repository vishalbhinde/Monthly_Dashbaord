import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt

st.set_page_config(page_title="Lokyata Dashboard", page_icon="https://www.lokyata.com/favicon.png", layout="wide")

df = pd.read_csv('Lead_Loan_Summary.csv')

# ---- SIDEBAR ----
st.sidebar.header("Filter Client:")
Client = st.sidebar.multiselect(
    "Select required Client:",
    options=df["Client"].unique(),
    default= 'All US'
)


df_selection = df.query(
    "Client == @Client"
)



# st.title("Marketing Metrics")
st.markdown("<h1 style='text-align: center; color: #00BFFF;'>Marketing Metrics</h1>", unsafe_allow_html=True)
st.markdown("##")
st.markdown("""---""")   

Total_Looks = int(df_selection['Num Looks'].sum())
Total_Approved = int(df_selection['Num Approved'].sum())
Total_Funded = int(df_selection['Num Funded Loans'].sum())
Total_Fpd = int(df_selection['Num Fpd'].sum())

Num_Months = str(df_selection.shape[0])
Bad_FPD = str((df_selection['Fpd % Change'] > 0).sum())
Good_FPD = str((df_selection['Fpd % Change'] <= 0).sum())
Bad_CPF = str((df_selection['Cpf % Change'] > 0).sum())
Good_CPF = str((df_selection['Cpf % Change'] <= 0).sum())
Bad_Num_Approved = str((round((df_selection['Num Approved'].pct_change())*100, 2) < 0).sum())
Good_Num_Approved = str((round((df_selection['Num Approved'].pct_change())*100, 2) >= 0).sum())

left_column, middle_column, right_column, last_column = st.columns(4)
with left_column:
    st.subheader("Total Looks:")
    st.subheader(f"{Total_Looks}")
with middle_column:
    st.subheader("Total Approved:")
    st.subheader(f"{Total_Approved}")
with right_column:
    st.subheader("Total Funded:")
    st.subheader(f"{Total_Funded}")
with last_column:
    st.subheader("Total FPD:")
    st.subheader(f"{Total_Fpd}")
  

    
st.markdown("""---""") 

  
loans_approved = px.bar(
    df_selection,
    x="Month",
    y="Num Approved",
    orientation="v",
    title="<b>Leads Approved</b>",
    template="plotly_white",
    text_auto=True,
    
)

loans_approved.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)

loans_approved.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
    title_x=0.5,
    
)

loans_funded = px.bar(
    df_selection,
    x="Month",
    y="Num Funded Loans",
    orientation="v",
    title="<b>Loans Funded</b>",
    template="plotly_white",
    text_auto=True,
)

loans_funded.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)

loans_funded.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
    title_x=0.5,
)

left_column, right_column = st.columns(2)

left_column.plotly_chart(loans_approved)
right_column.plotly_chart(loans_funded)

st.markdown("""---""")   

fpd_rate = px.bar(
    df_selection,
    x="Month",
    y="Fpd Rate %",
    orientation="v",
    title="<b>FPD Rate % month on month (lesser is better) </b>",
    template="plotly_white",
    text_auto=True,
)

fpd_rate.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)

fpd_rate.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
    title_x=0.5,
    
)

Cpf = px.bar(
    df_selection,
    x="Month",
    y="Cpf",
    orientation="v",
    title="<b>CPF month on month (lesser is better)</b>",
    template="plotly_white",
    text_auto=True,
)

Cpf.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)

Cpf.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
    title_x=0.5,
)

left_column, right_column = st.columns(2)

left_column.plotly_chart(fpd_rate)
right_column.plotly_chart(Cpf)


st.markdown("""---""")  

# left_column, middle_column, right_column, last_column = st.columns(2)
# with left_column:
#     st.subheader("Number of Months:")
#     st.subheader(f"{Num_Months}")
# with middle_column:
#     st.subheader("Leads Approved:")
#     st.subheader(f"Good Months - {Good_Num_Approved}")
#     st.subheader(f"Bad Months - {Bad_Num_Approved}")
# with right_column:
#     st.subheader("FPD:")
#     st.subheader(f"Good Months - {Good_FPD}")
#     st.subheader(f"Bad Months - {Bad_FPD}")
# with last_column:
#     st.subheader("CPF:")
#     st.subheader(f"Good Months - {Good_CPF}")
#     st.subheader(f"Bad Months - {Bad_CPF}")

test1, left_column, test3, test4, right_column, test6 = st.columns(6)

with test1:
    st.subheader("")
with left_column:
    st.subheader("FPD:")
    st.subheader(f"Good Months - {Good_FPD}")
    st.subheader(f"Bad Months - {Bad_FPD}")
with test3:
    st.subheader("")
with test4:
    st.subheader("")
with right_column:
    st.subheader("CPF:")
    st.subheader(f"Good Months - {Good_CPF}")
    st.subheader(f"Bad Months - {Bad_CPF}")
with test6:
    st.subheader("")

st.markdown("""---""")  

fpd_change = px.bar(
    df_selection,
    x="Month",
    y="Fpd % Change",
    orientation="v",
    title="<b>Percentage change in FPD month on month (-ve is good)</b>",
    template="plotly_white",
    text_auto=True,
)

fpd_change.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)

fpd_change.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False)),
    yaxis=(dict(showgrid=False)),
    title_x=0.5,
)

cpf_change = px.bar(
    df_selection,
    x="Month",
    y="Cpf % Change",
    orientation="v",
    title="<b>Percentage change in CPF month on month (-ve is good)</b>",
    template="plotly_white",
    text_auto=True,
)

cpf_change.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)

cpf_change.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False)),
    yaxis=(dict(showgrid=False)),
    title_x=0.5,
)

left_column, right_column = st.columns(2)
left_column.plotly_chart(fpd_change)
right_column.plotly_chart(cpf_change)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
            
hide_st_style2 = """
            <style>
            
            footer {visibility: hidden;}
            
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
