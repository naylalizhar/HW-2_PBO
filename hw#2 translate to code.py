# Menentukan kelas pengguna
class User:
    def __init__(self, user_id, name, email, password):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password

    def login(self):
        pass  # For login

    def logout(self):
        pass  # For logout


# Tentukan kelas siswa
class Student(User):
    def __init__(self, user_id, name, email, password):
        super().__init__(user_id, name, email, password)
        self.enrollment_id = None
        self.courses = []
        self.grades = []
        self.absences = []

    def enroll_in_course(self, course):
        pass  # mendaftar suatu kursus
    def view_grades(self):
        pass  # Melihat nilai
    def record_absence(self):
        pass  # pencatatan ketidakhadiran
    def view_courses(self):
        pass  # melihat kursus yang terdaftar

class Professor(User):
    def __init__(self, user_id, name, email, password):
        super().__init__(user_id, name, email, password)
        self.faculty_id = None
        self.courses_taught = []

    def upload_grades(self, course, grades):
        pass  
    def manage_course_materials(self, course):
        pass 
    def monitor_attendance(self, course):
        pass  

class Admin(User):
    def __init__(self, user_id, name, email, password):
        super().__init__(user_id, name, email, password)
        self.admin_id = None

    def manage_user_accounts(self):
        pass  
    def generate_reports(self):
        pass   
    def oversee_system_operations(self):
        pass  

class Operator(User):
    def __init__(self, user_id, name, email, password):
        super().__init__(user_id, name, email, password)
        self.operator_id = None

    def provide_technical_support(self):
        pass  
    def maintain_system(self):
        pass  


# Define Course Class
class Course:
    def __init__(self, course_id, name, description):
        self.course_id = course_id
        self.name = name
        self.description = description
        self.students_enrolled = []
        self.course_materials = []

    def add_student(self, student):
        pass 
    def remove_student(self, student):
        pass  
    def update_course_material(self, material):
        pass 

# Define Grade Class
class Grade:
    def __init__(self, student_id, course_id, letter_grade, numeric_score):
        self.student_id = student_id
        self.course_id = course_id
        self.letter_grade = letter_grade
        self.numeric_score = numeric_score

    def update_grade(self):
        pass  # Implementation for updating a grade


# Define Attendance Class
class Attendance:
    def __init__(self, student_id, course_id, dates_absent):
        self.student_id = student_id
        self.course_id = course_id
        self.dates_absent = dates_absent

    def record_absence(self):
        pass  # Implementation for recording absence

    def calculate_attendance_rate(self):
        pass  # Implementation for calculating attendance rate
