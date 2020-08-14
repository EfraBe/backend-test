from django.db import models

# Create your models here.
class PageUser(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=60)
    usertype = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=60)

    def __str__(self):
        return str(self.id) + '-' + self.fullname


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    description = models.TextField()
    nextcourseid = models.IntegerField(default=0)
    previouscourseid = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id) + '-' + self.name


class Lesson(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    description = models.TextField()
    nextlessonid = models.IntegerField()
    previouslessonid = models.IntegerField()
    approvalscore = models.IntegerField()
    couseid = models.IntegerField()

    def __str__(self):
        return str(self.id) + '-' + self.name


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    preview = models.TextField()
    question = models.TextField()
    questiontype = models.IntegerField(default=0)
    score = models.IntegerField()
    lessonid = models.IntegerField()
    def __str__(self):
        return str(self.id) + '-' +  self.preview


class QuestionType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    
    def __str__(self):
        return str(self.id) + '-' +  self.preview
