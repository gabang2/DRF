from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend

from feed.models import Feed
from feed.paginations import CustomPagination
from feed.serializers import FeedSerializer


class FeedListView(APIView):

    # 인증, 인가
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    # 쓰로틀링(Throttling) # 클라이언트의 요청 횟수 제한
    # throttle_classes = [UserRateThrottle]

    # 페이지네이션(pagination)
    # pagination_class = CustomPagination

    # 필터(Filtering) : 데이터 검색, 정렬, 필터링에 도움을 주는 기능
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['title', 'content']

    def get(self, request):
        feeds = Feed.objects.all()
        serializer = FeedSerializer(feeds, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FeedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
