import pandas as pd
from datetime import datetime
import os
import matplotlib.pyplot as plt


file_name = "expenses.xlsx"


if not os.path.exists(file_name):
    df = pd.DataFrame(columns=["Date", "Amount", "Category", "Note"])
    df.to_excel(file_name, index=False)
else:
    df = pd.read_excel(file_name)


try:
    amount = float(input("Enter amount spent (₹): "))
except ValueError:
    print("❌ Invalid amount. Please enter a number.")
    exit()

category = input("Enter category (Food, Travel, etc.): ").title()
note = input("Optional note: ")


new_entry = {
    "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "Amount": amount,
    "Category": category,
    "Note": note
}
df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
df.to_excel(file_name, index=False)
print("✅ Expense saved to Excel!")


category_data = df.groupby("Category")["Amount"].sum()


plt.figure(figsize=(8, 6))
category_data.plot(kind="bar", color="skyblue")
plt.title("Spending by Category")
plt.xlabel("Category")
plt.ylabel("Total Amount (₹)")
plt.tight_layout()
plt.savefig("chart.png")
plt.show()
print("📊 Chart saved as 'chart.png'")
