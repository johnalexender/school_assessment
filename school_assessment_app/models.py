from django.db import models

class School(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Class(models.Model):
    class_name = models.CharField(max_length=255)

    def __str__(self):
        return self.class_name

class Student(models.Model):
    full_name = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name

class Subject(models.Model):
    subject_name = models.CharField(max_length=255)
    subject_score = models.IntegerField()

    def __str__(self):
        return self.subject_name

class AssessmentAreas(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Answers(models.Model):
    answer_text = models.TextField()

    def __str__(self):
        return self.answer_text

class Awards(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Summary(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    assessment_area = models.ForeignKey(AssessmentAreas, on_delete=models.CASCADE)
    award = models.ForeignKey(Awards, on_delete=models.CASCADE)
    answers = models.ForeignKey(Answers, on_delete=models.CASCADE)

    sydney_participant = models.CharField(max_length=255)
    sydney_percentile = models.FloatField()
    correct_answer_percentage_per_class = models.FloatField()
    correct_answer = models.CharField(max_length=255)
    student_score = models.IntegerField()
    participant = models.CharField(max_length=255)
    year_level_name = models.CharField(max_length=255)
    category_id = models.IntegerField()
    correct_answer_id = models.IntegerField()

    def __str__(self):
        return f'{self.student} Summary'
