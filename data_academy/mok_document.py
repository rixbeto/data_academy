
class MongoDocument():

    def __init__(self):
        self.student = {}
        self.course = {}
        self.teacher = {}
        self.payment = {}
        self.insident = {}
        self.assistantce = {}
        self.product = {}
        self.school = {}

    def define_student(self):

        self.student = {
                'name': '',
                'middle_name': '',
                'last_name': '',
                'group': '',
                'grade': '',
                'code': '',
                'clave': '',
                'bday': '',
                'status': '',
                'contacts': [
                    {
                        'type': 'emergency',
                        'contact_name': 'Mom',
                        'movil': '9999999',
                    }
                ],
                'courses': [
                    {
                        'course_id': '',
                        'course_name': '',
                        'teacher_id': '',
                        'teacher_name': '',
                        'schedule': {
                                'start': '', 'end': ''
                                }
                    }
                ]
        }
        return True
    
    def define_course(self):

        # Define document and relations (mix relation embebed and refered).

        self.course = {
            'name': '',
            'teacher_id': 0,
            'teacher_name': '',
            'active': True,
            'strat': 'dd/mm/yyyy',
            'end': 'dd/mm/yyyy',
            'periodicity': '',
            'grade': ''
        }

    def define_teacher(self):

        self.teacher = {
            'name': '',
            'middle_name': '',
            'last_name': '',
            'courses': [],
            'grade': '',
            'code': '',
            'bday': '',
            'status': '',
            'auth': {},
            'assistance': [],
            'reports': []
        }

    def define_school(self):

        # To define School onfo.

        self.school = {
            'name': 'K College',
            'logo': 'logo',
            'calendar': 190,
            'start_code': 100,
            'current_code': 100,
            'manifesto': 'In this institute ',
            'rules': ['rule 1', 'rule 2'],
            'info': {
                'adress':'Elm Street'
            }
        }

        return True
