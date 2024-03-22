from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from main.models import *
from main.serializers import *
from django.core.files.storage import default_storage

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
    
@csrf_exempt
def all_users(request,id=0):
    if request.method == 'GET':
        users = User.objects.all()
        user_serializer = UserSerializer(users, many=True)
        return JsonResponse(user_serializer.data, safe=False)
    
    
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    
    
    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        user = User.objects.get(user_id=user_data['id'])
        user_serializer = UserSerializer(user, data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    
    
    elif request.method == 'DELETE':
        user = User.objects.get(user_id=id)
        user.delete()
        return JsonResponse("Deleted Successfully", safe=False)
    
@csrf_exempt
def all_docs(request,id=0):
    if request.method == 'GET':
        docs = Article.objects.all()
        doc_serializer = ArticleSerializer(docs, many=True)
        return JsonResponse(doc_serializer.data, safe=False)
    
    
    elif request.method == 'POST':
        doc_data = JSONParser().parse(request)
        doc_serializer = ArticleSerializer(data=doc_data)
        if doc_serializer.is_valid():
            doc_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    
    
    elif request.method == 'PUT':
        doc_data = JSONParser().parse(request)
        doc = Article.objects.get(article_id=doc_data['article_id'])
        doc_serializer = ArticleSerializer(doc, data=doc_data)
        if doc_serializer.is_valid():
            doc_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    
    
    elif request.method == 'DELETE':
        doc = Article.objects.get(article_id=id)
        doc.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
def all_comments(request,id=0):
    if request.method == 'GET':
        comments = Comments.objects.all()
        comment_serializer = CommentsSerializer(comments, many=True)
        return JsonResponse(comment_serializer.data, safe=False)
    
    
    elif request.method == 'POST':
        comment_data = JSONParser().parse(request)
        comment_serializer = CommentsSerializer(data=comment_data)
        if comment_serializer.is_valid():
            comment_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    
    
    elif request.method == 'PUT':
        comment_data = JSONParser().parse(request)
        comment = Comments.objects.get(comment_id=comment_data['comment_id'])
        comment_serializer = CommentsSerializer(comment, data=comment_data)
        if comment_serializer.is_valid():
            comment_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    
    
    elif request.method == 'DELETE':
        comment = Comments.objects.get(comment_id=id)
        comment.delete()
        return JsonResponse("Deleted Successfully", safe=False)
    
@csrf_exempt
def all_likes(request,id=0):
    if request.method == 'GET':
        likes = Like.objects.all()
        like_serializer = LikeSerializer(likes, many=True)
        return JsonResponse(like_serializer.data, safe=False)
    
    
    elif request.method == 'POST':
        like_data = JSONParser().parse(request)
        like_serializer = LikeSerializer(data=like_data)
        if like_serializer.is_valid():
            like_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    
    
    elif request.method == 'PUT':
        like_data = JSONParser().parse(request)
        like = Like.objects.get(like_id=like_data['like_id'])
        like_serializer = LikeSerializer(like, data=like_data)
        if like_serializer.is_valid():
            like_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    
    
    elif request.method == 'DELETE':
        like = Like.objects.get(like_id=id)
        like.delete()
        return JsonResponse("Deleted Successfully", safe=False)
    
@csrf_exempt
def all_trackers(request,id=0):
    if request.method == 'GET':
        trackers = Tracker.objects.all()
        tracker_serializer = TrackerSerializer(trackers, many=True)
        return JsonResponse(tracker_serializer.data, safe=False)
    
    
    elif request.method == 'POST':
        tracker_data = JSONParser().parse(request)
        tracker_serializer = TrackerSerializer(data=tracker_data)
        if tracker_serializer.is_valid():
            tracker_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    
    
    elif request.method == 'PUT':
        tracker_data = JSONParser().parse(request)
        tracker = Tracker.objects.get(tracker_id=tracker_data['tracker_id'])
        tracker_serializer = TrackerSerializer(tracker, data=tracker_data)
        if tracker_serializer.is_valid():
            tracker_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    
    
    elif request.method == 'DELETE':
        tracker = Tracker.objects.get(tracker_id=id)
        tracker.delete()
        return JsonResponse("Deleted Successfully", safe=False)
    

@csrf_exempt
def login(request):
    if request.method == 'POST':
        user_data = JSONParser().parse(request)
        email = user_data['email']
        password = user_data['password']
        if checkUser(email, password):
            user_id = getUserId(email)
            return JsonResponse({'user_id': user_id}, safe=False)
        else:
            return JsonResponse("Login Failed", safe=False)
    else:
        return JsonResponse("Invalid request method", safe=False)



def checkUser(email, password):
    users = User.objects.all()
    for user in users:
        if user.email == email and user.password == password:
            return True
    return False

def getUserId(email):
    users = User.objects.all()
    for user in users:
        if user.email == email:
            return user.id


@csrf_exempt
def saveFile(request):
    if request.method == 'POST':
        file = request.FILES['file']
        file_name = default_storage.save(file.name, file)
        return JsonResponse(file_name, safe=False)
    else:
        return JsonResponse("Invalid request method", safe=False)
    


@csrf_exempt
def forgotPassword(request):
    if request.method == 'POST':
        user_data = JSONParser().parse(request)
        email = user_data['email']
        if checkEmailExists(email):
            return JsonResponse(1, safe=False)
        else:
            return JsonResponse(0, safe=False);
        

def checkEmailExists(email):
    users = User.objects.all()
    for user in users:
        if user.email == email:
            return True
    return False