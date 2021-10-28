import Index 
import sys
import random
import os


courses = ['History', 'Math', 'Physics', 'CompSci']

random_course = random.choice(courses)

ind = Index.find_index(courses,random_course)
print(ind)
#print(sys.path)
#print(os.__file__)