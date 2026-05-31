from tkinter import ttk
from database import create_database
from CRUD_Operations import *
from prediction import *

class Login:
    def __init__(self, root):
        self.selected_id = None
        self.glucose = None
        self.email = None
        self.dob = None
        self.name = None
        self.root = root
        self.root.title("Health Prediction Application")
        root.state("zoomed")
        self.root.configure(bg="#ecf0f1")

        Label(self.root,
              text="Health Prediction Application",
              bg="#ecf0f1",
              font=("Arial", 20, "bold")).pack(padx=10, pady=10)

        self.main_frame = Frame(self.root, bg="#ecf0f1")
        self.main_frame.pack(padx=10,pady=10,anchor="center")

        Label(self.main_frame, text="Full Name:", bg="#ecf0f1",
              font=("Arial", 12)).grid(row=0, column=0, padx=5,pady=5,sticky="w")

        self.fullname_entry = Entry(self.main_frame, font=("Arial", 12), width=40)
        self.fullname_entry.grid(row=0, column=2, columnspan=2, padx=5, pady=5)

        Label(self.main_frame, text="Date Of Birth:", bg="#ecf0f1",
              font=("Arial", 12)).grid(row=1, column=0, padx=5,pady=5,sticky="w")

        self.dob_entry = Entry(self.main_frame, font=("Arial", 12), width=40)
        self.dob_entry.grid(row=1, column=2, columnspan=2, padx=5, pady=5)

        Label(self.main_frame, text="Email Address:", bg="#ecf0f1",
              font=("Arial", 12)).grid(row=2, column=0, padx=5,pady=5,sticky="w")

        self.email_entry = Entry(self.main_frame, font=("Arial", 12), width=40)
        self.email_entry.grid(row=2, column=2, columnspan=2, padx=5, pady=5)

        Label(self.main_frame, text="Glucose:", bg="#ecf0f1",
              font=("Arial", 12)).grid(row=3, column=0, padx=5, pady=5,sticky="w")

        self.glucose_entry = Entry(self.main_frame, font=("Arial", 12), width=40)
        self.glucose_entry.grid(row=3, column=2, columnspan=2, padx=5, pady=5)

        Label(self.main_frame, text="Haemoglobin:", bg="#ecf0f1",
              font=("Arial", 12)).grid(row=4, column=0, padx=5, pady=5,sticky="w")

        self.haemoglobin_entry = Entry(self.main_frame, font=("Arial", 12), width=40)
        self.haemoglobin_entry.grid(row=4, column=2, columnspan=2, padx=5, pady=5)

        Label(self.main_frame, text="Cholesterol:", bg="#ecf0f1",
              font=("Arial", 12)).grid(row=5, column=0, padx=5,pady=5,sticky="w")

        self.cholesterol_entry = Entry(self.main_frame, font=("Arial", 12), width=40)
        self.cholesterol_entry.grid(row=5, column=2, columnspan=2, padx=5, pady=5)

        Label(self.main_frame, text="Remarks:", bg="#ecf0f1",
              font=("Arial", 12)).grid(row=6, column=0, padx=5,pady=5,sticky="w")

        self.remarks_text = Text(
            self.main_frame,
            font=("Arial", 12),
            width=40,
            height=4
        )
        self.remarks_text.grid(row=6, column=2, columnspan=2, padx=5, pady=5)

        Button(self.main_frame, text="Predict", font=("Arial", 12, "bold"),
               bg="#27ae60", fg="white", width=20,command=lambda: predict(self)).grid(row=7, column=0, columnspan=4, pady=10)

        Button(self.main_frame, text="Save", font=("Arial", 12, "bold"), bg="#2c3e50",
               fg="white", width=20,command=lambda: save_details(self)).grid(row=8, column=0, pady=5)

        Button(self.main_frame, text="Clear", font=("Arial", 12, "bold"), bg="#2c3e50",
               fg="white", width=20,command=lambda: clear_fields(self)).grid(row=8, column=1, pady=5)

        Button(self.main_frame, text="Update", font=("Arial", 12, "bold"), bg="#2c3e50",
               fg="white", width=20,command=lambda: update_data(self)).grid(row=8, column=2, pady=5)

        Button(self.main_frame, text="Delete", font=("Arial", 12, "bold"), bg="#2c3e50",
               fg="white", width=20,command=lambda: delete_data(self)).grid(row=8, column=3, pady=5)

        table_frame = Frame(self.root)
        table_frame.pack(fill="both", expand=True)

        y_scroll = Scrollbar(table_frame, orient="vertical")
        y_scroll.pack(side="right", fill="y")

        x_scroll = Scrollbar(table_frame, orient="horizontal")
        x_scroll.pack(side="top", fill="x")

        self.patient_table = ttk.Treeview(
            table_frame,
            columns=(
                "ID",
                "Name",
                "DOB",
                "Email",
                "Glucose",
                "Haemoglobin",
                "Cholesterol",
                "Remarks"
            ),
            show="headings",
            height=5,
            yscrollcommand=y_scroll.set,
            xscrollcommand=x_scroll.set
        )

        self.patient_table.pack(fill="both", expand=True)

        y_scroll.config(command=self.patient_table.yview)
        x_scroll.config(command=self.patient_table.xview)

        self.patient_table.heading("ID", text="ID")
        self.patient_table.heading("Name", text="Name")
        self.patient_table.heading("DOB", text="DOB")
        self.patient_table.heading("Email", text="Email")
        self.patient_table.heading("Glucose", text="Glucose")
        self.patient_table.heading("Haemoglobin", text="Haemoglobin")
        self.patient_table.heading("Cholesterol", text="Cholesterol")
        self.patient_table.heading("Remarks", text="Remarks")

        self.patient_table.pack(fill="both", expand=True, padx=20, pady=20)
        self.patient_table.bind("<ButtonRelease-1>",self.get_cursor)
        create_database()
        view_data(self)

    def get_cursor(self, event=""):

        cursor_row = self.patient_table.focus()

        contents = self.patient_table.item(cursor_row)

        row = contents["values"]

        if row:
            self.fullname_entry.delete(0, END)
            self.fullname_entry.insert(0, row[1])

            self.dob_entry.delete(0, END)
            self.dob_entry.insert(0, row[2])

            self.email_entry.delete(0, END)
            self.email_entry.insert(0, row[3])

            self.glucose_entry.delete(0, END)
            self.glucose_entry.insert(0, row[4])

            self.haemoglobin_entry.delete(0, END)
            self.haemoglobin_entry.insert(0, row[5])

            self.cholesterol_entry.delete(0, END)
            self.cholesterol_entry.insert(0, row[6])

            self.remarks_text.delete("1.0", END)
            self.remarks_text.insert("1.0", row[7])

            self.selected_id = row[0]


if __name__ == "__main__":
    root = Tk()
    Login(root)
    root.mainloop()