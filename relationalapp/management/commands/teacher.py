from django.core.management.base import BaseCommand, CommandError
from relationalapp.models import (Teacher)
import random
import string

class Command(BaseCommand):
    help = "Closes the specified poll for voting"
    def __init__(self):
        self.characters = ''
    def aleatore(self):
        length = 10
        names = []
        for x in range(0,2):
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
                student = Teacher(
                    tr_name = names[0],
                    tr_middlename = names[1],
                    tr_lastname = names[2],
                    tr_garde = grade,
                    tr_group = group,
                    tr_code = names[3],
                    tr_clave = names[4]
                )
                student.save()

        return student
    
    def handle(self, *args, **options):
        name = self.aleatore()
        print('Students added succcesfully')
