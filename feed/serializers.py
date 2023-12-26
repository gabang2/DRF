from rest_framework import serializers


class FeedSerializer(serializers.Serializer):
    title = serializers.CharField()
    content = serializers.TextField()
