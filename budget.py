import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class BudgetTracker:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Budget Tracker")
        self.window.geometry("500x400")

        self.menu_frame = tk.Frame(self.window)
        self.menu_frame.pack(pady=10)

        self.expense_frame = tk.Frame(self.window)
        self.income_frame = tk.Frame(self.window)

        self.create_menu()

    def create_menu(self):
        tk.Label(self.menu_frame, text="Select an Option", font=("Arial", 16)).pack(pady=10)

        '''add_expense_image = Image.open("add_expense.png").resize((200, 150))
        aad_income_photo = ImageTk.PhotoImage(add_expense_image)'''
        tk.Button(self.menu_frame, text="Add Expense", font=("Arial", 12), command=self.show_expense).pack(pady=10)
        tk.Button(self.menu_frame, text="Add Income", font=("Arial", 12), command=self.show_income).pack(pady=10)
        tk.Button(self.menu_frame, text="Exit", font=("Arial", 12), command=self.window.destroy).pack(pady=10)

    def show_expense(self):
        self.menu_frame.pack_forget()
        self.expense_frame.pack(pady=10)

        tk.Label(self.expense_frame, text="Add Expense", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.expense_frame, text="Expense Name:", font=("Arial", 12)).pack(pady=10)
        self.expense_name_entry = tk.Entry(self.expense_frame, font=("Arial", 12))
        self.expense_name_entry.pack()

        tk.Label(self.expense_frame, text="Expense Amount:", font=("Arial", 12)).pack(pady=10)
        self.expense_amount_entry = tk.Entry(self.expense_frame, font=("Arial", 12))
        self.expense_amount_entry.pack()

        tk.Button(self.expense_frame, text="Add Expense", font=("Arial", 12), command=self.add_expense).pack(pady=10)
        tk.Button(self.expense_frame, text="Back", font=("Arial", 12), command=self.back_to_menu).pack(pady=10)

    def add_expense(self):
        name = self.expense_name_entry.get()
        amount = self.expense_amount_entry.get()

        if name and amount:
            messagebox.showinfo("Success", f"{name} added as an expense with an amount of {amount}.")
            self.expense_name_entry.delete(0, tk.END)
            self.expense_amount_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please fill out all fields.")

    def show_income(self):
        self.menu_frame.pack_forget()
        self.income_frame.pack(pady=10)

        tk.Label(self.income_frame, text="Add Income", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.income_frame, text="Income Name:", font=("Arial", 12)).pack(pady=10)
        self.income_name_entry = tk.Entry(self.income_frame, font=("Arial", 12))
        self.income_name_entry.pack()

        tk.Label(self.income_frame, text="Income Amount:", font=("Arial", 12)).pack(pady=10)
        self.income_amount_entry = tk.Entry(self.income_frame, font=("Arial", 12))
        self.income_amount_entry.pack()

        tk.Button(self.income_frame, text="Add Income", font=("Arial", 12), command=self.add_income).pack(pady=10)
        tk.Button(self.expense_frame, text="Back", font=("Arial", 12), command=self.back_to_menu).pack(pady=10)

       

    def add_income(self):
        name = self.income_name_entry.get()
        amount = self.income_amount_entry.get()
        
        

        if name and amount:
            messagebox.showinfo("Success", f"{name} added as an income with an amount of {amount}.")
            self.income_name_entry.delete(0, tk.END)
            self.income_amount_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please fill out all fields.")

        

    def back_to_menu(self):
        self.expense_frame.pack_forget()
        self.income_frame.pack_forget()
        self.create_menu()

       

if __name__ == '__main__':
    budget_tracker = BudgetTracker()
    budget_tracker.window.mainloop()


       