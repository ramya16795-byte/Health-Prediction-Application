import re
from datetime import datetime
from tkinter import messagebox, END


def validate_details(self):
    self.name = self.fullname_entry.get().strip()
    self.dob = self.dob_entry.get().strip()
    self.email = self.email_entry.get().strip()
    self.glucose = self.glucose_entry.get().strip()
    self.haemoglobin = self.haemoglobin_entry.get().strip()
    self.cholesterol = self.cholesterol_entry.get().strip()
    self.remarks = self.remarks_text.get("1.0", END).strip()

    if self.name == "":
        messagebox.showerror("Error", "Full Name is required")
        return False

    if not self.name.replace(" ", "").isalpha():
        messagebox.showerror(
            "Error",
            "Name should contain only letters"
        )
        return False

    try:
        dob_date = datetime.strptime(
            self.dob,
            "%d/%m/%Y"
        )

        if dob_date > datetime.now():
            messagebox.showerror(
                "Error",
                "DOB cannot be future date"
            )
            return False

    except ValueError:
        messagebox.showerror(
            "Error",
            "DOB format should be DD/MM/YYYY"
        )
        return False

    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    if not re.match(email_pattern, self.email):
        messagebox.showerror(
            "Error",
            "Invalid email address"
        )
        return False

    try:
        float(self.glucose)
        float(self.haemoglobin)
        float(self.cholesterol)

    except ValueError:
        messagebox.showerror(
            "Error",
            "Blood values must be numeric"
        )
        return False

    return True
