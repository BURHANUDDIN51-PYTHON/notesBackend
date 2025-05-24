from django.shortcuts import render
from notesapp.models import Note, Category
from notesapp.serializers import NoteSerializer, CategorySerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Q
from rest_framework import status

# Create your views here.

# View of searching a note
@api_view(['GET'])
def search_notes(request):
    try:
        query = request.query_params.get('search', '')
        if not query:
            return Response(
                {'error': 'Search query is required'}, 
                status=status.HTTP_400_BAD_REQUEST
            )     
        
        notes = Note.objects.filter(Q(title__icontains=query.strip('/')) | Q(body__icontains=query.strip('/')))
        print(notes)
        serializer = NoteSerializer(notes, many=True)
        return Response(
            serializer.data, 
            status=status.HTTP_200_OK
        )
        
    except Exception as e:
        return Response(
            {'error': str(e)}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

# Creating a note or viewing all notes
@api_view(["GET", "POST"])
def notes(request):
    if request.method == "GET":
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# Getting the detail of a singel note    
@api_view(['GET', 'PUT', 'DELETE'])
def note_detail(request, slug):
    try: 
        note = Note.objects.get(slug=slug)
    except: 
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    # Doing three different things based on the type of request
    if request.method == "GET":
        serializer = NoteSerializer(note)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = NoteSerializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET'])
def categories(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add_category(request):
    if request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
@api_view(['DELETE'])
def delete_category(request, id):
    if request.method == 'DELETE':
        try:
            category = Category.objects.get(id=id)
            category.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(status=status.HTTP_400_BAD_REQUEST)