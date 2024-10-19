import tkinter as tk
from tkinter import messagebox

class CustomerViewGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer Information")
        self.root.geometry("500x400")

        upper_frame = tk.Frame(root)
        upper_frame.pack(pady=20)

        self.name_label = tk.Label(upper_frame, text="Enter Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        self.name_entry = tk.Entry(upper_frame)
        self.name_entry.grid(row=0, column=1)

        self.address_label = tk.Label(upper_frame, text="Enter Address:")
        self.address_label.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.address_entry = tk.Entry(upper_frame)
        self.address_entry.grid(row=1, column=1)

        self.phone_label = tk.Label(upper_frame, text="Enter Phone number:")
        self.phone_label.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.phone_entry = tk.Entry(upper_frame)
        self.phone_entry.grid(row=2, column=1)

        self.customer_number_label = tk.Label(upper_frame, text="Enter Customer number:")
        self.customer_number_label.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        self.customer_number_entry = tk.Entry(upper_frame)
        self.customer_number_entry.grid(row=3, column=1)

        lower_frame = tk.Frame(root)
        lower_frame.pack(pady=20)

        self.mailing_list_label = tk.Label(lower_frame, text="Select Mailing List Option:", bg='lightblue')
        self.mailing_list_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        self.mailing_list_var = tk.StringVar(value="No")
        self.yes_checkbox = tk.Radiobutton(lower_frame, text="Yes", variable=self.mailing_list_var, value="Yes")
        self.yes_checkbox.grid(row=0, column=1, padx=10, pady=10)
        self.no_checkbox = tk.Radiobutton(lower_frame, text="No", variable=self.mailing_list_var, value="No")
        self.no_checkbox.grid(row=0, column=2, padx=10, pady=10)

        self.display_button = tk.Button(lower_frame, text="Display", command=self.display_customer_info)
        self.display_button.grid(row=1, column=0, columnspan=3, pady=10)

    def display_customer_info(self):
        name = self.name_entry.get()
        address = self.address_entry.get()
        phone_number = self.phone_entry.get()
        customer_number = self.customer_number_entry.get()
        mailing_list = self.mailing_list_var.get()

        messagebox.showinfo("Customer Information", f"Person name: {name}\nAddress: {address}\nPhone number: {phone_number}\nCustomer number: {customer_number}\nMailing List: {mailing_list}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CustomerViewGUI(root)
    root.mainloop()
