import streamlit as st
import pandas as pd
import os
from datetime import datetime
import matplotlib.pyplot as plt

st.set_page_config(page_title="Expense Tracker", layout="centered")

st.title("💼 Automated Expense Tracker")

# File
file_name = "expenses.xlsx"

# Create file if not exists
if not os.path.exists(file_name):
    df = pd.DataFrame(columns=["Date", "Amount", "Category", "Note"])
    df.to_excel(file_name, index=False)

# Load existing data
df = pd.read_excel(file_name)

# Sidebar: Input Form
st.sidebar.header(" Add New Expense")

with st.sidebar.form("expense_form"):
    amount = st.number_input("Amount Spent (₹)", min_value=0.0, step=1.0)
    category = st.selectbox("Category", ["Food", "Transport", "Entertainment", "Education", "Other"])
    note = st.text_input("Optional Note")
    submitted = st.form_submit_button("Add Expense")

if submitted:
    new_entry = {
        "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Amount": amount,
        "Category": category,
        "Note": note
    }
    df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
    df.to_excel(file_name, index=False)
    st.success("✅ Expense added successfully!")

# Show Data Table
st.subheader(" Expense History")
st.dataframe(df, use_container_width=True)

# Bar Chart
st.subheader(" Spending by Category")

if not df.empty:
    category_data = df.groupby("Category")["Amount"].sum()
    fig, ax = plt.subplots()
    category_data.plot(kind="bar", color="skyblue", ax=ax)
    ax.set_xlabel("Category")
    ax.set_ylabel("Total Spent (₹)")
    ax.set_title("Category-wise Spending")
    st.pyplot(fig)
else:
    st.info("No expenses added yet.")
