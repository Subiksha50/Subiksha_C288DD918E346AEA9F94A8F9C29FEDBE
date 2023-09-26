class Student:
  
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    # Sort the student list based on CGPA in descending order
    sorted_students = sorted(student_list,key=lambda student:student.cgpa,reverse=True)
  
    return sorted_students

# Test the function with a list of student objects
students = [
        Student("Logeshwaran", "2205084", 3.9),
        Student("Saran", "2205102", 3.5),
        Student("Naveen", "2205090", 3.4),
        Student("Mohanprasath", "2205089", 3.7),
]

sorted_students = sort_students(students)

for student in sorted_students:
 print("name:{},RollNumber:{},CGPA{}".format(student.name,student.roll_number,student.cgpa))