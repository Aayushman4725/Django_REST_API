from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Blog
from api.serializers import BlogSerializer
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def blog_list(request):
    blog = Blog.objects.all()

    serializer = BlogSerializer(blog, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def blog_detail(request,pk):
   try:
        blog = Blog.objects.get(pk=pk)
   except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

   serializer = BlogSerializer(blog)
   return Response(serializer.data)

@api_view(['POST'])
def blog_post(request):
  
    serializer = BlogSerializer(data= request.data)

    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['PUT'])
def blog_update(request,pk):
    
    blog = Blog.objects.get(pk=pk)
    serializer = BlogSerializer(blog, data= request.data)

    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['DELETE'])
def blog_delete(request,pk):
    
    blog = Blog.objects.get(pk=pk)
    
    blog.delete()
   
    return Response(status=status.HTTP_204_NO_CONTENT)
