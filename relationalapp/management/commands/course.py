from django.core.management.base import BaseCommand, CommandError
from relationalapp.models import (
    School, 
    Course, 
    Teacher, 
    CourseTeacher, 
    CourseStudent,
    Student
    )
import random
import string
from datetime import datetime


class Command(BaseCommand):
    help = "Closes the specified poll for voting"
    def __init__(self):
        self.characters = ''

    def add_school(self):
        sch,_ = School.objects.get_or_create(
            sc_name = 'K College',
            logo = 'default',
            calendar = '190',
            starting_code = '189',
            curr_code = '189',
        )
        sch.save()
        return True
    
    def addcourses(self):
        for i in range(1,20):
            periodicity  = random.choice(['daily', 'weekly', 'monthly'])
            strings = ["13:00", "14:00", "09:00", ]
            starts  = random.choice(strings)
            endsstr = ["08:00", "13:30", "10:00",]
            ends  = random.choice(endsstr)
            course = Course(
                title = f'course {random.choice(range(1,10))}',
                descp = 'description of the course',
                start = starts,
                end = ends,
                status = random.choice([1,0]),
                grade = random.choice(range(1,6)),
                periodicity = periodicity
            )
            course.save()

    def assign_courses(self):
        tch = Teacher.objects.all()
        for t in tch:
            relation_t_c = CourseTeacher(
                teacher = t,
                course = Course.objects.order_by('?').first()
            )
            relation_t_c.save()
        std = Student.objects.all()
        for st in std:
            relate_s_c = CourseStudent(
                student = st,
                course = Course.objects.order_by('?').first()
            )
            relate_s_c.save()

    def handle(self, *args, **options):
        self.add_school()
        self.addcourses()
        self.assign_courses()
        print('action processed succcesfully')
