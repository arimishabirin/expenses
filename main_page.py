import streamlit as st
import pandas as pd
from plotly import graph_objects as go
import plotly.express as px
st.set_page_config(layout="wide")

#%%
data = pd.read_csv('monthly.csv', encoding='unicode_escape')


#%%
total = (
    data.groupby(['Sub Category','Category'])
    .agg({'Cost':'sum'})
    .sort_values('Cost' , ascending = True)
    .reset_index()
)

total_subcat= (
    data.groupby(['Sub Category'])
    .agg({'Cost':'sum'})
    .sort_values('Cost' , ascending = False)
    .reset_index()
)

#%%
monhtly_spending_chart=go.Figure()

for sub_cat in total['Sub Category'].unique():
    # st.write(sub_cat)
    sub_cat_table = total.query("`Sub Category` == @sub_cat")
    # st.write(sub_cat_table)
    monhtly_spending_chart.add_trace(go.Bar(
            y=sub_cat_table['Category'],
            x=sub_cat_table['Cost'],
            orientation='h',
            name = sub_cat

        )
)
    
monhtly_spending_chart.update_layout(
    title=dict(text='Monhtly Spending'),
    xaxis_tickfont_size=14,
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    )
)

salary = 3925.20
total_spending = data['Cost'].sum()

col1 , col2 = st.columns([2,2])

with col1:
    st.metric('Salary' , salary , border = True)

with col2:
    st.metric('Extra' , round(salary - total_spending,2), border = True)

st.dataframe(total_subcat, hide_index=True)
st.plotly_chart(monhtly_spending_chart)