import streamlit as st
import pandas as pd
import plotly.express as px

# Page title
st.title("Sales & Revenue Analysis Dashboard")

# Load data
df = pd.read_csv("sales_data.csv")

# KPIs
total_revenue = df["Revenue"].sum()
total_quantity = df["Quantity"].sum()
total_orders = len(df)

col1, col2, col3 = st.columns(3)

col1.metric("Total Revenue", f"₹{total_revenue}")
col2.metric("Total Quantity", total_quantity)
col3.metric("Total Orders", total_orders)

st.divider()

# Revenue Trend
st.subheader("Revenue Trend")

trend = df.groupby("Date")["Revenue"].sum().reset_index()

fig1 = px.line(
    trend,
    x="Date",
    y="Revenue",
    title="Revenue Trend"
)

st.plotly_chart(fig1)

# Revenue by Product
st.subheader("Revenue by Product")

fig2 = px.bar(
    df.groupby("Product")["Revenue"].sum().reset_index(),
    x="Product",
    y="Revenue",
    title="Revenue by Product"
)

st.plotly_chart(fig2)

# Revenue by Region
st.subheader("Revenue by Region")

fig3 = px.pie(
    df,
    names="Region",
    values="Revenue",
    title="Revenue by Region"
)

st.plotly_chart(fig3)

# Revenue by Category
st.subheader("Revenue by Category")

fig4 = px.bar(
    df.groupby("Category")["Revenue"].sum().reset_index(),
    x="Category",
    y="Revenue",
    title="Revenue by Category"
)

st.plotly_chart(fig4)