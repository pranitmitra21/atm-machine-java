import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import csv
import os

# Expense Tracker Application
class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        # Initialize expense list
        self.expenses = []
        self.filename = "expenses.csv"

        # Load existing expenses from file
        self.load_expenses()

        # UI Elements
        self.create_ui()

    def create_ui(self):
        # Title
        tk.Label(self.root, text="Expense Tracker", font=("Arial", 18, "bold")).pack(pady=10)

        # Input fields
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        tk.Label(frame, text="Date (YYYY-MM-DD):").grid(row=0, column=0, padx=5, pady=5)
        self.date_entry = tk.Entry(frame, width=15)
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame, text="Category:").grid(row=1, column=0, padx=5, pady=5)
        self.category_entry = tk.Entry(frame, width=15)
        self.category_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame, text="Amount:").grid(row=2, column=0, padx=5, pady=5)
        self.amount_entry = tk.Entry(frame, width=15)
        self.amount_entry.grid(row=2, column=1, padx=5, pady=5)

        # Buttons
        tk.Button(frame, text="Add Expense", command=self.add_expense).grid(row=3, column=0, columnspan=2, pady=10)

        # Expense list
        columns = ("Date", "Category", "Amount")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings", height=10)
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150, anchor="center")
        self.tree.pack(pady=10)

        # Populate with existing data
        self.update_treeview()

        # Total amount
        self.total_label = tk.Label(self.root, text=f"Total Expenses: ₹{self.calculate_total()}", font=("Arial", 12))
        self.total_label.pack(pady=10)

    def add_expense(self):
        # Get user input
        date = self.date_entry.get().strip()
        category = self.category_entry.get().strip()
        try:
            amount = float(self.amount_entry.get().strip())
        except ValueError:
            messagebox.showerror("Invalid Input", "Amount must be a number.")
            return

        if not date or not category:
            messagebox.showerror("Invalid Input", "All fields are required.")
            return

        # Add to expenses list
        self.expenses.append([date, category, amount])
        self.save_expenses()

        # Update UI
        self.update_treeview()
        self.date_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)

        self.total_label.config(text=f"Total Expenses: ₹{self.calculate_total()}")
        messagebox.showinfo("Success", "Expense added successfully!")

    def calculate_total(self):
        return sum(expense[2] for expense in self.expenses)

    def update_treeview(self):
        # Clear existing data in the treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Add all expenses to the treeview
        for expense in self.expenses:
            self.tree.insert("", tk.END, values=expense)

    def save_expenses(self):
        # Save expenses to a CSV file
        with open(self.filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(self.expenses)

    def load_expenses(self):
        # Load expenses from the CSV file
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                reader = csv.reader(file)
                self.expenses = [[row[0], row[1], float(row[2])] for row in reader]

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.mainloop()
