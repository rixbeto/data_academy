from django.core.management.base import BaseCommand, CommandError
from relationalapp.models import (
    Student,
    Teacher,
    Course,
    CourseStudent,
    CourseTeacher
)
from django.db.models import Count
import random
import string

class Command(BaseCommand):
    help = "Closes the specified poll for voting"
    def __init__(self):
        self.characters = ''
    def students(self):
        num_students = Student.objects.count()
        students_assigned = CourseStudent.objects.filter(course__status=True).count()
        courses = CourseStudent.objects.values('course__title').distinct().aggregate(total_students=Count('course_id'))
        return (num_students, students_assigned, courses)
    
    def handle(self, *args, **options):
        name = self.students()
        print(name)
