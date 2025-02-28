import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Sales Dashboard", layout="wide")

st.title("📊 Sales Dashboard")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    sample_data = {
        "Date": ["2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04", "2024-01-05", "2024-01-06", "2024-01-07"],
        "Category": ["Electronics", "Furniture", "Clothing", "Electronics", "Furniture", "Clothing", "Electronics"],
        "Product": ["Laptop", "Chair", "T-shirt", "Phone", "Table", "Jacket", "Tablet"],
        "Quantity": [5, 10, 20, 8, 3, 7, 4],
        "Revenue": [5000, 1500, 800, 4000, 900, 2100, 1600],
    }
    df = pd.DataFrame(sample_data)

st.subheader("📄 Data Preview")
st.write(df.head())

st.subheader("📊 Key Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"${df['Revenue'].sum():,.2f}")
col2.metric("Total Products Sold", f"{df['Quantity'].sum()}")
col3.metric("Unique Products", f"{df['Product'].nunique()}")

st.subheader("📈 Revenue by Category")
fig, ax = plt.subplots()
category_revenue = df.groupby("Category")['Revenue'].sum()
category_revenue.plot(kind='bar', colormap='viridis', ax=ax)
plt.ylabel("Revenue")
st.pyplot(fig)

st.subheader("📊 Sales by Product")
fig, ax = plt.subplots()
product_quantity = df.groupby("Product")['Quantity'].sum()
product_quantity.plot(kind='pie', autopct='%1.1f%%', colormap='Set2', ax=ax)
ax.set_ylabel('')
st.pyplot(fig)

st.subheader("🔍 Filter by Category")
categories = df["Category"].unique()
selected_category = st.selectbox("Select Category", categories)
filtered_data = df[df["Category"] == selected_category]
st.write(filtered_data)

st.subheader("⬇️ Download Data")
st.download_button("Download CSV", df.to_csv(index=False), "data.csv", "text/csv")