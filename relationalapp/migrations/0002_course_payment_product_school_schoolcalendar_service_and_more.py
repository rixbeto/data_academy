# Generated by Django 4.0 on 2023-05-21 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('relationalapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('descp', models.TextField()),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('status', models.BooleanField(default=True)),
                ('periodicity', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payed', models.BooleanField(default=False)),
                ('total_amount', models.FloatField(default=0.0)),
                ('date_payed', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pd_name', models.CharField(max_length=200)),
                ('pd_price', models.FloatField(default=0.0)),
                ('pd_discount', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sc_name', models.CharField(max_length=255)),
                ('logo', models.CharField(max_length=200)),
                ('calendar', models.CharField(max_length=100)),
                ('starting_code', models.CharField(max_length=100)),
                ('curr_code', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SchoolCalendar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('date_event', models.DateField(auto_now_add=True)),
                ('descp', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sr_name', models.CharField(max_length=255)),
                ('sr_price', models.FloatField(default=0.0)),
                ('sr_discount', models.FloatField(default=0.0)),
                ('sr_surcharge', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tr_name', models.CharField(max_length=200)),
                ('tr_middlename', models.CharField(max_length=200)),
                ('tr_lastname', models.CharField(max_length=200)),
                ('tr_garde', models.CharField(max_length=50)),
                ('tr_group', models.CharField(max_length=50)),
                ('tr_code', models.CharField(max_length=100)),
                ('tr_clave', models.CharField(max_length=200)),
                ('tr_bday', models.DateField()),
                ('tr_status', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='st_bday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='st_clave',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='student',
            name='st_code',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='st_garde',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='st_group',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='st_status',
            field=models.CharField(default='registed', max_length=50),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='PaymentHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_date', models.DateTimeField(auto_now_add=True)),
                ('amount', models.FloatField(default=0.0)),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relationalapp.payment')),
            ],
        ),
        migrations.AddField(
            model_name='payment',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='relationalapp.product'),
        ),
        migrations.AddField(
            model_name='payment',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='relationalapp.service'),
        ),
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_incident', models.DateTimeField(auto_created=True)),
                ('incident', models.CharField(max_length=100)),
                ('descp', models.TextField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relationalapp.student')),
            ],
        ),
        migrations.CreateModel(
            name='CourseTeacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relationalapp.course')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relationalapp.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='CourseStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relationalapp.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relationalapp.student')),
            ],
        ),
        migrations.CreateModel(
            name='Assistence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assisten', models.TextField(blank=True, null=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relationalapp.student')),
            ],
        ),
    ]
