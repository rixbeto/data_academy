from pymongo import MongoClient
from utils import Mok
import random
MONGO_URI = "mongodb+srv://albertoriospy:S4ruman.mongodb@cluster0.9h8rfte.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(MONGO_URI)
moking = Mok()
teachers = []
for _ in range(0,20):
    teacher = {
        'name': moking.random_string(length=10).capitalize(),
            'middle_name': moking.random_string(length=8).capitalize(),
            'last_name': moking.random_string(length=10).capitalize(),
            'courses': [],
            'grade': random.choice(range(0,6)),
            'code': moking.random_string(length=6).upper(),
            'bday': '',
            'status': random.choice([1, 0]),
            'auth': {},
            'assistance': [],
            'reports': []
        }
    teachers.append(teacher)

#print(teachers)
#client.academy.Teacher.insert_many(teachers)
courses = []
for _ in range(100):
    grade = random.choice(range(6))
    teacher = client.academy.Teacher.find_one({'grade': grade})
    course = {
        'name': f'Course {grade}',
        'teacher_id': teacher.get('_id'),
        'teacher_name': teacher.get('name'),
        'active': True,
        'strat': 'dd/mm/yyyy',
        'end': 'dd/mm/yyyy',
        'periodicity': moking.random_periodicity(),
        'grade': grade,
        'status': moking.random_bool()
    }
    courses.append(course)
#client.academy.Course.insert_many(courses)

students = []
for _ in range(100):
    grade = random.choice(range(1, 6))
    online_courses = client.academy.Course.find({'grade': grade})
    ol_courses = [
        {
            'course_id': c.get('_id'),
            'course_name': c.get('name'),
            'teacher_id': c.get('teacher_id'),
            'teacher_name': c.get('teacher_name'),
        } for c in online_courses
    ]
    student = {
        'name': moking.random_string(length=10),
        'middle_name': moking.random_string(length=10),
        'last_name': moking.random_string(length=10),
        'group': moking.random_string(length=1),
        'grade': grade,
        'code': moking.random_string(length=5),
        'clave': moking.random_string(length=10),
        'bday': 'dd/mm/yyyy',
        'status': moking.random_bool(),
        'contacts': [
            {
                'type': random.choice(['normal', 'emergency', 'notes']),
                'contact_name': random.choice(['Mom' ,'Dad', 'Aunt', 'Sister']),
                'movil': moking.random_string(length=10),
            } for _ in range(0, random.choice(range(4)))
            ],
        'courses': ol_courses[:3]

    }
    students.append(student)
print(students)
client.academy.Student.insert_many(students)
