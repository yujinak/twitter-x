from django.shortcuts import render

# from rest_framework import viewsets
# from .models import Tweet
# from .serialzers import TweetSerializer

# class TweetViewSet(viewsets.ModelViewSet):
#     queryset = Tweet.objects.all().order_by('-created_at')
#     serializer_class = TweetSerializer


def login(request):
    return render(request, 'login.html', {})