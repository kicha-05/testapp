from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework import viewsets, views, permissions
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from django.conf import settings



class TestView(views.APIView):

    def get(self, request):
        return Response("deployed successfully")
