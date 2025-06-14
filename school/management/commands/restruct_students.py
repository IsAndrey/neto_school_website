from django.core.management.base import BaseCommand
from school.models import Student, Teacher


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):

        for student in Student.objects.all():
            if student.teacher != 0:
                try:
                    student.teachers.add(Teacher.objects.get(pk__exact=student.teacher))
                except Exception as e:
                    print(f'Ошибка при обработке {student} - {e}')
        Student.objects.update(teacher=0)
