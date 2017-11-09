#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
class Student:
   '所有学生的基类'
   stuCount = 0
 
   def __init__(self, stu_no,name, stu_class,male):
      self.stu_no = stu_no
      self.name = name
      self.stu_class = stu_class
      self.male = male
      Student.stuCount += 1
   
   def displayCountByClass(self):
     print "Total Student %d" % Student.stuCount
 
   def displayStudent(self):
      print "Stu_no:",self.stu_no, ",Name : ", self.name,  ",Stu_class:",self.stu_class,", Male: ", self.male
