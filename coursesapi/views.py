from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import logging


from .serializers import PageUserSerializer, LoginSerializer
from .models import PageUser
from .services import LoginService


class PageUserViewSet(viewsets.ModelViewSet):
    queryset = PageUser.objects.all().order_by('fullname')
    serializer_class = PageUserSerializer


class LoginViewSet(viewsets.ModelViewSet):
    queryset = PageUser.objects.all()
    serializer_class = PageUserSerializer