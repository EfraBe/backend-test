from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import PageUser, Course, Lesson, Question
from .serializers import *


class Login(APIView):
    
    def post(self, request):
        try:
            email = request.data['email']
            user_data = PageUser.objects.get(email=email)

            data = LoginSerializer(user_data).data

            if data['password'] == request.data['password']:
                response = PageUserSerializer(user_data).data
                return Response(response)
            else:
                return Response({'response': 'Bad password'}, status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            print(e)
            return Response({'response': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)


class Courses(APIView):
    def get(sef, request):
        courses = Course.objects.all()
        response = CourseSerializer(courses, many=True).data

        return Response(response)

    
    def post(self, request):

        student_id = request.data['student_id']

        user_type = PageUser.objects.get(id=student_id)
        user_type = PageUserSerializer(user_type).data['usertype']
        
        if user_type == 'teacher':
            course = CourseSerializer(data=request.data)

            if course.is_valid():
                course.save()
                return Response(course.data, status=status.HTTP_201_CREATED)
            else:
                return Response(course.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'response': 'Only teachers can create courses.'}, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request):

        student_id = request.data['student_id']

        user_type = PageUser.objects.get(id=student_id)
        user_type = PageUserSerializer(user_type).data['usertype']
        
        if user_type == 'teacher':
            rcourse = Course.objects.get(id=request.data['id'])
            rcourse = CourseSerializer(rcourse, data=reques.data)
            if rcourse.is_valid():
                return Response(rcourse.data, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(course.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'response': 'Only teachers can edit courses.'}, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, pk):
        student_id = request.data['student_id']

        user_type = PageUser.objects.get(id=student_id)
        user_type = PageUserSerializer(user_type).data['usertype']
        
        if user_type == 'teacher':
            course = Course.objects.get(id=pk).delete()

            return Response({'response': 'success'}, status=status.HTTP_200_OK)
        else:
            return Response({'response': 'Only teachers can delete courses.'}, status=status.HTTP_400_BAD_REQUEST)



class Lessons(APIView):
    def get(sef, request):
        lessons = Lesson.objects.all()
        response = LessonSerializer(lessons, many=True).data

        return Response(response)


    def put(self, request):
        lesson = Lesson.objects.get(id=request.data['id'])
        lesson = LessonSerializer(lesson, data=reques.data)
        if lesson.is_valid():
            return Response(lesson.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(lesson.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def post(self, request):
        lesson = LessonSerializer(data=request.data)

        if lesson.is_valid():
            lesson.save()
            return Response(lesson.data, status=status.HTTP_201_CREATED)
        else:
            return Response(lesson.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request):
        lesson = Lesson.objects.get(id=pk).delete()

        return Response({'response': 'success'}, status=status.HTTP_200_OK)


class Questions(APIView):
    def get(self, request):
        questions = Question.objects.all()
        response = QuestionSerializer(questions, many=true).data
        return response


    def put(self, request):
        question = Question.objects.get(id=request.data['id'])
        question = QuestionSerializer(question, data=reques.data)
        if question.is_valid():
            return Response(question.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(question.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def post(self, request):
        question = QuestionSerializer(data=request.data)

        if question.is_valid():
            question.save()
            return Response(question.data, status=status.HTTP_201_CREATED)
        else:
            return Response(question.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request):
        question = Question.objects.get(id=pk).delete()

        return Response({'response': 'success'}, status=status.HTTP_200_OK)