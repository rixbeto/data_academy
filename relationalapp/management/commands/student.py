from django.core.management.base import BaseCommand, CommandError
from relationalapp.models import (Student)
import random
import string

class Command(BaseCommand):
    help = "Closes the specified poll for voting"
    def __init__(self):
        self.characters = ''
    def aleatore(self):
        length = 10
        names = []
        for x in range(0,1000):
            names = []
            for r in range(1, 7):
                self.characters = ''
                names = []
                for i in range(0,5):
                    self.characters = string.ascii_letters 
                    random_string = ''.join(random.choice(self.characters) for _ in range(length))
                    names.append(random_string)
                status = random.choice([True, False])
                grade = r
                group = '1'
                student = Student(
                    st_name = names[0],
                    st_middlename = names[1],
                    st_lastname = names[2],
                    st_garde = grade,
                    st_group = group,
                    st_code = names[3],
                    st_clave = names[4],
                    st_status = status
                )
                student.save()

        return student
    
    def handle(self, *args, **options):
        name = self.aleatore()
        print('Students added succcesfully')
