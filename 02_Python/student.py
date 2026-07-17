# ## FOUR PILLARS OF OBJECT ORIENTED PROGRAMMING

# - Encapsulation
# - Inheritance
# - Polymorphism
# - Abstraction
# ## #1 Encapsulation

# - Binding data with Methods.

# class Student():
#     def __init__(self,name,roll,course,email,marks):
#         self.name = name
#         self.roll = roll
#         self.course = course
#         self.email = email
#         self._marks = marks

#     def show_profile(self):
#         print("-------Student Profile-------")
#         print(f"{self.name}")
#         print(f"{self.roll}")
#         print(f"{self.course}")
#         print(f"{self.email}")
#         print(f"{self.marks}")

#     def get_marks(self):
#         return self._marks
    
#     def set_marks(self,new_marks):
#         if (new_marks>=0) & (new_marks<=100):
#             self.marks = new_marks
#         else:
#             return "Invalid Marks"


# s1 = Student("Abdullah","BAI-24F-020","BSAI","abdullah@gmail.com",550)

# print(s1.name)

# print(s1.show_profile())
# s1.set_marks(97)
# # Accessing a public attribute outside the class
# s1.get_marks()
# ## Access Modifiers

# - Public
# - Private
# - Protective

class Student():
    def __init__(self,name,roll,course,email,marks):
        # Instance Variables
        # Public Access
        self.name = name
        self.roll = roll
        self.course = course
        self.email = email

        # Protected Instance Variable
        self._marks = marks

    def show_profile(self):
        print("-------Student Profile-------")
        print(f"{self.name}")
        print(f"{self.roll}")
        print(f"{self.course}")
        print(f"{self.email}")
        print(f"{self._marks}")

    def get_marks(self):
        return self._marks
    
    def set_marks(self,new_marks):
        if (new_marks>=0) & (new_marks<=100):
            self._marks = new_marks
        else:
            return "Invalid Marks"


# s2 = Student("Ayub","BAI-24F-014","BSAI","abdullah@gmail.com",94)

# # Accessing a protected atttibute outside the class
# s2._marks