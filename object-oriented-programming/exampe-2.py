class Student:
    def __init__(self,name ,grades):
      self.name = name
      self.grades = grades
    
    def average(self):
     return sum(self.grades) / len(self.grades)
 
 
s1 = Student("ali",(1,2,3,4,5,6,7,8,9,10))

print(s1.average())