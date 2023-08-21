from typing import List

class Student:
    def __init__(self, name:str,grades:List[int] = None):
      self.name = name
      self.grades = grades or []
      
    def take_exam(self,result:int):
        self.grades.append(result)
    
s1 = Student("ali")
s2 = Student("moussa")

s1.take_exam(100)

print(s1.grades)
print(s2.grades)