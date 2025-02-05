import tkinter as tk
from tkinter import messagebox
import csv
import os

master = tk.Tk()
master.title("MARKSHEET")
master.geometry("700x500")
master.configure(bg="lavender")



e1 = tk.Entry(master)  
e2 = tk.Entry(master)  
e3 = tk.Entry(master)  
e4 = tk.Entry(master)  
e5 = tk.Entry(master)  
e6 = tk.Entry(master)  
e7 = tk.Entry(master)  
e8 = tk.Entry(master)  


valid_grades = ['A', 'B', 'C', 'D', 'E', 'F']
sub_cred = {
    'CSET 101': 5,
    'CSET 102': 3,
    'EMAT 101': 4,
    'CSET 103': 2
}

def csv1(data):
    filename = "student_records.csv"
    file_exists = os.path.isfile(filename)
    
    try:
        with open(filename, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=data.keys())
        
            if not file_exists:
                writer.writeheader()
            
            writer.writerow(data)
        return True
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save record: {str(e)}")
        return False

def errorbox():
  
   
    if not e1.get().strip():
        messagebox.showerror("Error", "Please enter student name")
        return False
    if not e1.get().isalpha():
        messagebox.showerror("Error", "Please add only alphabets")
    
  
    if not e2.get().strip():
        messagebox.showerror("Error", "Please enter enrollment number")
        return False
        
   
    if not e3.get().strip():
        messagebox.showerror("Error", "Please enter batch")
        return False
    if not e3.get().isnumeric():
        messagebox.showerror("Error","Add only numbers")
    if not e8.get().strip():
        messagebox.showerror("Error", "Please enter group")
        return False
        
  
    for grade_entry, subject in [(e4, 'CSET 101'), (e5, 'CSET 102'), 
                               (e6, 'EMAT 101'), (e7, 'CSET 103')]:
        grade = grade_entry.get().strip().upper()
        if not grade:
            messagebox.showerror("Error", f"Please enter grade for {subject}")
            return False
        if grade not in valid_grades:
            messagebox.showerror("Error", 
                f"Invalid grade for {subject}: {grade}\nValid grades are: {', '.join(valid_grades)}")
            return False
            
    return True

def calc(grade, credits):
   
    grades = {
        'A': 10,
        'B': 9,
        'C': 8,
        'D': 7,
        'E': 6,
        'F': 0
    }
    return grades[grade.upper()] * credits

def display():
    if not errorbox():
        return

    tot = 0
    total = sum(sub_cred.values())
    failed_subjects = []
    subject_points = {}

  
    subjects = {
        'CSET 101': (e4, 3),
        'CSET 102': (e5, 4),
        'EMAT 101': (e6, 5),
        'CSET 103': (e7, 6)
    }

    for subject, (entry, row) in subjects.items():
        grade = entry.get().upper()
        points = calc(grade , sub_cred[subject])
        subject_points[subject] = points
        
        if grade == 'F':
            failed_subjects.append(subject)
        
        tk.Label(master, text=str(points)).grid(row=row, column=4)
        tot += points

   
    sgpa = tot/total
    
   
    tk.Label(master, text=str(tot)).grid(row=7, column=4)
    tk.Label(master, text=f"{sgpa:.2f}").grid(row=8, column=4)

    
    record = {
        'Name': e1.get().strip(),
        'Enrollment_No': e2.get().strip(),
        'Batch': e3.get().strip(),
        'Group': e8.get().strip(),
        'CSET_101_Grade': e4.get().upper(),
        'CSET_101_Points': subject_points['CSET 101'],
        'CSET_102_Grade': e5.get().upper(),
        'CSET_102_Points': subject_points['CSET 102'],
        'EMAT_101_Grade': e6.get().upper(),
        'EMAT_101_Points': subject_points['EMAT 101'],
        'CSET_103_Grade': e7.get().upper(),
        'CSET_103_Points': subject_points['CSET 103'],
        'Total_Points': tot,
        'SGPA': f"{sgpa:.2f}"
    }

    if csv1(record):
        messagebox.showinfo("Success", "Record saved successfully!")
    
  
    if failed_subjects:
        messagebox.showwarning("Failed Subjects", 
            f"Student has failed in: {', '.join(failed_subjects)}\nSGPA: {sgpa:.2f}")
    elif sgpa < 6.0:
        messagebox.showwarning("Low SGPA", 
            f"Student has low performance with SGPA: {sgpa:.2f}")
    elif sgpa >= 9.0:
        messagebox.showinfo("Excellent Performance", 
            f"Student has achieved excellent SGPA: {sgpa:.2f}")


tk.Label(master, text="Name").grid(row=0, column=0)
tk.Label(master, text="Enroll.No").grid(row=0, column=3)
tk.Label(master, text="Batch").grid(row=1, column=0)
tk.Label(master, text="Group").grid(row=1, column=3)

tk.Label(master, text="Srl.No").grid(row=2, column=0)
for i in range(4):
    tk.Label(master, text=str(i+1)).grid(row=i+3, column=0)


subjects = [("Subject", 2), ("CSET 101", 3), ("CSET 102", 4), 
           ("EMAT 101", 5), ("CSET 103", 6)]
for subject, row in subjects:
    tk.Label(master, text=subject).grid(row=row, column=1)


tk.Label(master, text="Grade").grid(row=2, column=2)
e4.grid(row=3, column=2)
e5.grid(row=4, column=2)
e6.grid(row=5, column=2)
e7.grid(row=6, column=2)


tk.Label(master, text="Sub Credit").grid(row=2, column=3)
credits = [(5, 3), (3, 4), (4, 5), (2, 6)]
for credit, row in credits:
    tk.Label(master, text=str(credit)).grid(row=row, column=3)

tk.Label(master, text="Credit obtained").grid(row=2, column=4)


e1.grid(row=0, column=1)
e2.grid(row=0, column=4)
e3.grid(row=1, column=1)
e8.grid(row=1, column=4)


button_frame = tk.Frame(master, bg="lavender")
button_frame.grid(row=8, column=1, columnspan=2)

submit_btn = tk.Button(button_frame, text="Submit", bg="green", fg="white", command=display)
submit_btn.pack(side=tk.LEFT, padx=5)




tk.Label(master, text="Total credit", bg="lavender").grid(row=7, column=3)
tk.Label(master, text="SGPA", bg="lavender").grid(row=8, column=3)



master.mainloop()
