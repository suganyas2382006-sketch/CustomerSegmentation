import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.cluster import KMeans

st.title("Customer Segmentation Dashboard")

df = pd.read_csv("customers.csv")

X = df[["AnnualIncome", "SpendingScore"]]

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df["Cluster"] = kmeans.fit_predict(X)

st.subheader("Customer Dataset")
st.dataframe(df)

st.subheader("Customer Segments")

fig = px.scatter(
    df,
    x="AnnualIncome",
    y="SpendingScore",
    color="Cluster",
    hover_data=["CustomerID","Age","Gender"]
)

st.plotly_chart(fig)

st.subheader("Cluster Summary")

summary = df.groupby("Cluster")[["AnnualIncome","SpendingScore"]].mean()
st.dataframe(summary)

st.success("Customer segmentation completed using K-Means Clustering")