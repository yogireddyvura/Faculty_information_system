import tkinter as tk
from tkinter import messagebox, simpledialog

class Faculty:
    def __init__(self, name, department, courses):
        self.name = name
        self.department = department
        self.courses = courses

    def __str__(self):
        courses_str = ', '.join(self.courses)
        return f"Name: {self.name}, Department: {self.department}, Courses: {courses_str}"

class FacultyInformationSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Faculty Information System")
        self.faculty_records = {}

        # Create UI components
        self.create_widgets()

    def create_widgets(self):
        # Labels
        tk.Label(self.root, text="Faculty Name:").grid(row=0, column=0)
        tk.Label(self.root, text="Department:").grid(row=1, column=0)
        tk.Label(self.root, text="Courses (comma-separated):").grid(row=2, column=0)

        # Entry fields
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1)

        self.department_entry = tk.Entry(self.root)
        self.department_entry.grid(row=1, column=1)

        self.courses_entry = tk.Entry(self.root)
        self.courses_entry.grid(row=2, column=1)

        # Buttons
        self.add_button = tk.Button(self.root, text="Add Faculty", command=self.add_faculty)
        self.add_button.grid(row=3, column=0)

        self.view_button = tk.Button(self.root, text="View Faculty", command=self.view_faculty)
        self.view_button.grid(row=3, column=1)

        self.update_button = tk.Button(self.root, text="Update Faculty", command=self.update_faculty)
        self.update_button.grid(row=4, column=0)

        self.delete_button = tk.Button(self.root, text="Delete Faculty", command=self.delete_faculty)
        self.delete_button.grid(row=4, column=1)

    def add_faculty(self):
        name = self.name_entry.get()
        department = self.department_entry.get()
        courses = self.courses_entry.get().split(',')
        courses = [course.strip() for course in courses]  # Clean up whitespace

        if not name or not department or not courses:
            messagebox.showerror("Input Error", "All fields are required.")
            return

        emp_id = len(self.faculty_records) + 1  # Simple ID generation
        self.faculty_records[emp_id] = Faculty(name, department, courses)
        messagebox.showinfo("Success", "Faculty added successfully!")
        self.clear_entries()

    def view_faculty(self):
        if not self.faculty_records:
            messagebox.showinfo("Faculty Records", "No faculty records found.")
            return
        
        records = "\n".join([f"ID: {emp_id}, {faculty}" for emp_id, faculty in self.faculty_records.items()])
        messagebox.showinfo("Faculty Records", records)

    def update_faculty(self):
        emp_id = simpledialog.askinteger("Update Faculty", "Enter Faculty ID to update:")
        if emp_id in self.faculty_records:
            name = simpledialog.askstring("Update Name", "Enter new Faculty Name:")
            department = simpledialog.askstring("Update Department", "Enter new Faculty Department:")
            courses = simpledialog.askstring("Update Courses", "Enter new Courses (comma-separated):")
            courses = [course.strip() for course in courses.split(',')]  # Clean up whitespace

            if name:
                self.faculty_records[emp_id].name = name
            if department:
                self.faculty_records[emp_id].department = department
            if courses:
                self.faculty_records[emp_id].courses = courses

            messagebox.showinfo("Success", "Faculty updated successfully!")
        else:
            messagebox.showerror("Error", "Faculty not found.")

    def delete_faculty(self):
        emp_id = simpledialog.askinteger("Delete Faculty", "Enter Faculty ID to delete:")
        if emp_id in self.faculty_records:
            del self.faculty_records[emp_id]
            messagebox.showinfo("Success", "Faculty deleted successfully!")
        else:
            messagebox.showerror("Error", "Faculty not found.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.department_entry.delete(0, tk.END)
        self.courses_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = FacultyInformationSystem(root)
    root.mainloop()