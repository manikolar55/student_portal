from django.db import models

from app.utils import generate_random_int_with_max_length


# Create your models here.


class Students(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    number = models.IntegerField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    student_id = models.IntegerField(null=False, blank=False)
    joined_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}, {self.email}'

    class Meta:
        db_table = "student"

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        while True:
            student_id = generate_random_int_with_max_length()
            try:
                Students.objects.get(student_id=student_id)
            except Students.DoesNotExist:
                self.student_id = student_id
                break
        super(Students, self).save(force_insert, force_update, using, update_fields)


class Subject(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "subject"


class Semester(models.Model):
    semester_id = models.IntegerField(null=False, blank=False)
    section = models.ForeignKey("app.Section", on_delete=models.CASCADE, related_name="semester_section")

    def __str__(self):
        return f'<{self.semester_id}> <{self.section}>'

    class Meta:
        db_table = "semester"


class Section(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="section_subject")

    def __str__(self):
        return f'<{self.name}> <{self.subject}>'

    class Meta:
        db_table = "section"


class Degree(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name="degree_semester")

    def __str__(self):
        return f'{self.name} {self.semester}'

    class Meta:
        db_table = "degree"


class Profile(models.Model):
    student = models.OneToOneField(Students, on_delete=models.CASCADE, related_name="profile_student")
    degree = models.OneToOneField(Degree, on_delete=models.CASCADE, related_name="profile_degree")

    def __str__(self):
        return f'{self.student} {self.degree}'

    class Meta:
        db_table = "profile"


class Room(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    max_length = models.IntegerField(default=60)
