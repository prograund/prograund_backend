from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from main.models import *
from main.serializers import *

# Create your views here.

@csrf_exempt
def all_posts(request,id=0):
    if request.method == 'GET':
        posts = Post.objects.all()
        post_serializer = PostSerializer(posts, many=True)
        return JsonResponse(post_serializer.data, safe=False)
    
    
    elif request.method == 'POST':
        post_data = JSONParser().parse(request)
        post_serializer = PostSerializer(data=post_data)
        if post_serializer.is_valid():
            post_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    
    
    elif request.method == 'PUT':
        post_data = JSONParser().parse(request)
        post = Post.objects.get(post_id=post_data['post_id'])
        post_serializer = PostSerializer(post, data=post_data)
        if post_serializer.is_valid():
            post_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    
    
    elif request.method == 'DELETE':
        post = Post.objects.get(post_id=id)
        post.delete()
        return JsonResponse("Deleted Successfully", safe=False)
    