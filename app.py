import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Personal Finance Analytics", layout="wide")

st.title(" Personal Finance Analytics Dashboard")

st.sidebar.header("Enter Your Financial Details")

income = st.sidebar.number_input(
    "Monthly Income (₹)",
    min_value=0.0,
    value=50000.0
)

food = st.sidebar.number_input("Food Expense (₹)", min_value=0.0)
shopping = st.sidebar.number_input("Shopping Expense (₹)", min_value=0.0)
bills = st.sidebar.number_input("Bills (₹)", min_value=0.0)
travel = st.sidebar.number_input("Travel Expense (₹)", min_value=0.0)
entertainment = st.sidebar.number_input("Entertainment (₹)", min_value=0.0)

total_expense = food + shopping + bills + travel + entertainment
savings = income - total_expense

col1, col2, col3 = st.columns(3)

col1.metric("Income", f"₹{income:,.0f}")
col2.metric("Expenses", f"₹{total_expense:,.0f}")
col3.metric("Savings", f"₹{savings:,.0f}")

if income > 0:
    savings_rate = (savings / income) * 100

    st.subheader("Savings Analysis")
    st.write(f"Savings Rate: **{savings_rate:.2f}%**")

    if savings_rate >= 30:
        st.success("Excellent savings habit!")
    elif savings_rate >= 15:
        st.warning("Average savings. Try increasing it.")
    else:
        st.error("Low savings. Consider reducing expenses.")

    expense_df = pd.DataFrame({
        "Category": [
            "Food",
            "Shopping",
            "Bills",
            "Travel",
            "Entertainment"
        ],
        "Amount": [
            food,
            shopping,
            bills,
            travel,
            entertainment
        ]
    })

    st.subheader("Expense Breakdown")

    fig = px.pie(
        expense_df,
        names="Category",
        values="Amount",
        title="Expense Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Expense Table")
    st.dataframe(expense_df)