from rest_framework import serializers

from .models import PageUser, Course, Lesson, Question

class PageUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageUser
        fields = '__all__'


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageUser
        fields = ('email', 'password')


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'