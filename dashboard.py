import streamlit as st
import pandas as pd
import plotly.express as px

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Internship Analytics", layout="wide")
st.title("INTERNSHIP PROJECT ANALYTICS DASHBOARD")

df = pd.read_csv('data.csv')
df['Date'] = pd.to_datetime(df['Date'])

col1, col2 = st.columns(2)
with col1:
    dept = st.multiselect("Select Department", df['Department'].unique(), default=df['Department'].unique())
with col2:
    status = st.multiselect("Select Status", df['Status'].unique(), default=df['Status'].unique())

df_filtered = df[df['Department'].isin(dept) & df['Status'].isin(status)]

col1, col2 = st.columns(2)
with col1:
    st.subheader("Hours Trend Over Time")
    fig_line = px.line(df_filtered, x='Date', y='Hours', markers=True)
    st.plotly_chart(fig_line, use_container_width=True)

with col2:
    st.subheader("Total Hours by Department")
    dept_hours = df_filtered.groupby('Department')['Hours'].sum().reset_index()
    fig_bar = px.bar(dept_hours, x='Department', y='Hours', text='Hours', color='Department')
    fig_bar.update_traces(texttemplate='%{text}h', textposition='outside')
    st.plotly_chart(fig_bar, use_container_width=True)

col3, col4 = st.columns(2)
with col3:
    st.subheader("Team Size vs Hours Spent")
    fig_scatter = px.scatter(df_filtered, x='TeamSize', y='Hours', color='Status', size='Hours', hover_data=['Date'])
    st.plotly_chart(fig_scatter, use_container_width=True)

with col4:
    st.subheader("Project Status Distribution")
    status_count = df_filtered['Status'].value_counts().reset_index()
    fig_pie = px.pie(status_count, values='count', names='Status', hole=0.3)
    fig_pie.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig_pie, use_container_width=True)
