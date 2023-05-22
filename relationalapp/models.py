from django.db import models


INCIDENTS = [
    'absence',
    'accident',
    'conduct report',
    'school issue',
    'home issue', 
]

STD_STATUS = [
    'registered',
    'active',
    'suspendet',
    'tobedeleted',
    'former',
]


class Student(models.Model):
    st_name = models.CharField(max_length=200)
    st_middlename = models.CharField(max_length=200)
    st_lastname = models.CharField(max_length=200)
    st_garde = models.CharField(max_length=50)
    st_group = models.CharField(max_length=50)
    st_code = models.CharField(max_length=100, default=0)
    st_clave = models.CharField(max_length=200, default='')
    st_bday = models.DateField(blank=True, null=True)
    st_status = models.CharField(max_length=50)


class Incident(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    incident = models.CharField(max_length=100)
    descp = models.TextField()
    day_incident = models.DateTimeField(auto_created=True)


class Assistence(models.Model):
    # Model to save assistances of the student during all course
    '''
    assisten is a json array saved as string comprending next structured
    {
        'take_assistance':DATETIME(dd/mm/yyy hh:mm:ss),
        'place':'gate/classroom'
    }

    '''
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    assisten = models.TextField(blank=True, null=True)


class Teacher(models.Model):
    tr_name = models.CharField(max_length=200)
    tr_middlename = models.CharField(max_length=200)
    tr_lastname = models.CharField(max_length=200)
    tr_garde = models.CharField(max_length=50)
    tr_group = models.CharField(max_length=50)
    tr_code = models.CharField(max_length=100)
    tr_clave = models.CharField(max_length=200)
    tr_bday = models.DateField(blank=True, null=True)


class Course(models.Model):
    title = models.CharField(max_length=200)
    descp = models.TextField()
    start = models.TimeField()
    end = models.TimeField()
    status = models.BooleanField(default=True)
    grade = models.CharField(max_length=10)
    periodicity = models.CharField(max_length=200)

class CourseTeacher(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class CourseStudent(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class School(models.Model):
    sc_name = models.CharField(max_length=255)
    logo = models.CharField(max_length=200)
    calendar = models.CharField(max_length=100)
    starting_code = models.CharField(max_length=100)
    curr_code = models.CharField(max_length=100)

class Product(models.Model):
    pd_name = models.CharField(max_length=200)
    pd_price = models.FloatField(default=0.0)
    pd_discount = models.FloatField(default=0.0)

class Service(models.Model):
    sr_name = models.CharField(max_length=255)
    sr_price = models.FloatField(default=0.0)
    sr_discount = models.FloatField(default=0.0)
    sr_surcharge = models.FloatField(default=0.0)

class Payment(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, blank=True, null=True, on_delete=models.CASCADE)
    payed = models.BooleanField(default=False)
    total_amount = models.FloatField(default=0.0)
    date_payed = models.DateTimeField()

class PaymentHistory(models.Model):
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    pay_date = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField(default=0.0)

class SchoolCalendar(models.Model):
    title = models.CharField(max_length=255)
    date_event = models.DateField(auto_now_add=True)
    descp = models.TextField() 
