# filepath: /home/whydude230/work/ctf/2025/Defensys/web/TheFinder/finder/management/commands/seed_db.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.apps import apps
import os
from finder.models import AcademicDivision, Department, Employee, Course

from faker import Faker

class Command(BaseCommand):
    help = 'Seed the database with initial data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding database...')
        self.delete_all_data()
        self.create_or_replace_school_admin()
        self.create_database()
        self.stdout.write('Database seeding completed.')

    def create_or_replace_school_admin(self):
        username = 'school_admin'
        password = os.getenv('SCHOOL_ADMIN_PASSWORD', 'default_password')
        email = 'school_admin@example.com'

        try:
            user = User.objects.get(username=username)
            user.delete()
            self.stdout.write(f"Deleted existing user: {username}")
        except User.DoesNotExist:
            self.stdout.write(f"No existing user found with username: {username}")

        school_admin = User(username=username, password=password, email=email)
        school_admin.save()
        self.stdout.write(f"Created new user: {username}")

    def delete_all_data(self):
        models = apps.get_models()
        for model in models:
            if model._meta.app_label == 'admin':
                continue  # Skip the admin models
            model.objects.all().delete()
            self.stdout.write(f"Deleted all data from {model.__name__}")

    def create_database(self):
        deparetement_data = [
                            {"name": "Computer Science", "description": "Computer Science Department"},
                             {"name": "Mathematics", "description": "Mathematics Department"},
                             {"name": "Physics", "description": "Physics Department"},
                             {"name": "Chemistry", "description": "Chemistry Department"},
                             {"name": "Economics", "description": "Economics Department"},
                             {"name": "Humanities", "description": "Humanities Department"},
                             {"name": "Commerce", "description": "Commerce Department"},
                        ]
        
        courses_data = [{"name":"web programing", "description": "web programing course","academicdivisions":{"Software Development", "Data Science", "Cyber Security"}},
                        {"name":"database management", "description": "database management course","academicdivisions":{"Software Development", "Data Science", "Data Management"}},
                        {"name":"operating systems", "description": "operating systems course","academicdivisions":{"Software Development", "Cyber Security"}},
                        {"name":"computer networks", "description": "computer networks course", "academicdivisions":{"Cyber Security"}},
                        {"name":"software engineering", "description": "software engineering course","academicdivisions":{"Software Development"}}, 
                        {"name":"discrete mathematics", "description": "discrete mathematics course","academicdivisions":{"Mathematics"}} ,
                        {"name":"algebra 1", "description": "algebra 1 course","academicdivisions":{"Mathematics","Cyber Security"}} ,
                        {"name":"analysis 1", "description": "analysis 1 course","academicdivisions":{"Mathematics"}} ,
                        {"name":"algorithms", "description":"algotithms course","academicdivisions":{"Software Development", "Data Science", "Cyber Security"}}, 
                        {"name":"cloud computing", "description":"cloud computing course","academicdivisions":{"Data Science", "Cyber Security"}}, 
                        {"name":"general history", "description":"history course","academicdivisions":{"History"}},
                        {"name": "comtabilite", "description":"comtabilite course","academicdivisions":{"Commerce"}},]
        
        academicdivision_data = [
            {"name": "Data Science", "description": "Data Science Division", "department": "Computer Science"},
            {"name": "Cyber Security", "description": "Cyber Security Division", "department": "Computer Science"},
            {"name": "Artificial Intelligence", "description": "Artificial Intelligence Division", "department": "Computer Science"},
            {"name": "Data Management", "description": "Data Management Division", "department": "Computer Science"},
            {"name": "Software Development", "description": "Software Development Division", "department": "Computer Science"},
            {"name": "Commerce", "description": "Commerce Division", "department": "Commerce"},
            {"name": "Mathematics", "description": "Mathematics Division", "department": "Mathematics"},
            {"name": "Philosophy", "description": "Philosophy Division", "department": "Humanities"},
            {"name": "History", "description": "History Division", "department": "Humanities"},
            {"name": "Geography", "description": "Geography Division", "department": "Humanities"},
        ]

        for data in deparetement_data:
            department = Department.objects.create(name=data['name'], description=data['description'])
            self.stdout.write(f"Created Department: {department.name}")

        for data in academicdivision_data:
            department = Department.objects.get(name=data['department'])
            academic_division = AcademicDivision.objects.create(
            name=data['name'],
            description=data['description'],
            department=department
            )
            self.stdout.write(f"Created Academic Division: {academic_division.name}")

        for data in courses_data:
            course = Course.objects.create(
                name=data['name'],
                description=data['description']
            )
            for division_name in data['academicdivisions']:
                academic_division = AcademicDivision.objects.get(name=division_name)
                academic_division.course.add(course)
                self.stdout.write(f"Created Course: {course.name}")
        
        fake = Faker()
        
        for _ in range(9):
            employee = Employee.objects.create(
                name=fake.name(),
                is_admin=False,
                description=fake.job(),
            )
            employee.department.add(Department.objects.order_by('?').first())
            employee.save()
        
        school_admin_employee = Employee.objects.create(
            name="school_admin",
            description="school_admin",
            is_admin=False,
            user=User.objects.get(username="school_admin")
        )
        school_admin_employee.department.add(Department.objects.get(name="Computer Science"))
        school_admin_employee.save()
        