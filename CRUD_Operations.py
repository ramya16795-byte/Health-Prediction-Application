import sqlite3
from validation import *

def save_details(self):
    if not validate_details(self):
        return

    if self.selected_id is None:
        conn = sqlite3.connect("patients.db")

        cursor = conn.cursor()

        cursor.execute("""
               INSERT INTO patients(
                   fullname,
                   dob,
                   email,
                   glucose,
                   haemoglobin,
                   cholesterol,
                   remarks
               )
               VALUES (?, ?, ?, ?, ?, ?, ?)
           """,
                   (
                       self.name,
                       self.dob,
                       self.email,
                       self.glucose,
                       self.haemoglobin,
                       self.cholesterol,
                       self.remarks
                   ))

        conn.commit()
        conn.close()

        messagebox.showinfo(
            "Success",
            "Patient record saved successfully"
        )
        clear_fields(self)
        view_data(self)
    else:
        messagebox.showinfo(
            "Error",
            "This record already inserted"
        )
        clear_fields(self)
        view_data(self)

def clear_fields(self):

    self.fullname_entry.delete(0, END)
    self.dob_entry.delete(0, END)
    self.email_entry.delete(0, END)
    self.glucose_entry.delete(0, END)
    self.haemoglobin_entry.delete(0, END)
    self.cholesterol_entry.delete(0, END)
    self.remarks_text.delete("1.0", END)

def view_data(self):

    self.patient_table.delete(*self.patient_table.get_children())

    conn = sqlite3.connect("patients.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM patients")

    rows = cursor.fetchall()

    conn.close()

    for row in rows:
        self.patient_table.insert("",END, values=row)

def update_data(self):

    if self.selected_id is None:
        messagebox.showerror(
            "Error",
            "Please select a record first"
        )
        return

    if not validate_details(self):
        return

    conn = sqlite3.connect("patients.db")
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE patients
        SET
            fullname=?,
            dob=?,
            email=?,
            glucose=?,
            haemoglobin=?,
            cholesterol=?,
            remarks=?
        WHERE id=?
    """,
    (
        self.name,
        self.dob,
        self.email,
        self.glucose,
        self.haemoglobin,
        self.cholesterol,
        self.remarks,
        self.selected_id
    ))

    conn.commit()
    conn.close()

    messagebox.showinfo(
        "Success",
        "Record updated successfully"
    )

    view_data(self)
    clear_fields(self)
    self.selected_id = None

def delete_data(self):

    if self.selected_id is None:
        messagebox.showerror(
            "Error",
            "Please select a record first"
        )
        return

    answer = messagebox.askyesno(
        "Confirm Delete",
        "Are you sure you want to delete this record?"
    )

    if not answer:
        return

    conn = sqlite3.connect("patients.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM patients WHERE id=?",
        (self.selected_id,)
    )

    conn.commit()
    conn.close()

    messagebox.showinfo(
        "Success",
        "Record deleted successfully"
    )

    view_data(self)
    clear_fields(self)
    self.selected_id = None