from fpdf import FPDF
from datetime import datetime

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Automated Expense Tracker Using Python & Excel", ln=True, align="C")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Generated on {datetime.now().strftime('%Y-%m-%d')}", align="C")

# Create PDF
pdf = PDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_font("Arial", size=11)

# Clean text content (no emojis)
lines = [
    "Built by: Ayushman Mukherjee",
    "Date: July 2025",
    "Country: India",
    "Aspiring Degree: BSc in Business Informatics (Hungary)",
    "GitHub Link: [https://github.com/ayush585]",
    "Linkedin Link: [https://www.linkedin.com/in/ayushman-mukherjee-437a49314/]",
    "",
    "Project Objective:",
    "To build a simple, efficient tool that helps users log their daily expenses, categorize them,",
    "and visualize their spending patterns using bar charts - all automated using Python and Excel.",
    "",
    "Tools & Technologies Used:",
    "- Python 3",
    "- pandas - data handling",
    "- openpyxl - Excel support",
    "- matplotlib - chart generation",
    "- Excel (.xlsx) files",
    "",
    "Key Features:",
    "- User enters amount, category & note via terminal",
    "- Auto-creates 'expenses.xlsx' if not present",
    "- Generates 'chart.png' bar graph of total category spend",
    "- Shows total & average spend in terminal",
    "",
    "Skills Demonstrated:",
    "- Real-world data entry automation",
    "- Excel file handling using Python",
    "- Data visualization",
    "- GitHub project creation",
    "",
    "Reflection:",
    "\"As a 15-year-old preparing for Business Informatics, this project helped me understand automation,",
    "data handling, and how to make my work visual and useful.\""
]


# Add lines to PDF
for line in lines:
    pdf.multi_cell(0, 10, line)

# Save
pdf.output("summary.pdf")
print("✅ summary.pdf generated successfully!")
