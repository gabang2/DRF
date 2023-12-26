from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


@api_view(['GET'])
@permission_classes([AllowAny])
def hello_rest_api(request):
    data = {'message': 'Hello, RestAPI'}
    return Response(data)
