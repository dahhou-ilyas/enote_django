from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Note
from .serialazer import NoteSerializer





@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
        ]
    
    return Response(routes)

@api_view(['GET'])
def getNotes(request):
    notes=Note.objects.all().order_by('-updated')
    serializerNote=NoteSerializer(notes,many=True)
    return Response(serializerNote.data)

@api_view(['GET'])
def getNote(request ,pk):
    notes=Note.objects.get(id=pk)
    serializerNote=NoteSerializer(notes,many=False)
    return Response(serializerNote.data)


# @api_view(['POST'])
# def createNote(request):
    
#     print(request.method)
#     data=request.data
#     notes=Note.objects.create(
#         body=data['body']
#     )
    
#     serializerNote=NoteSerializer(notes,many=False)
#     return Response(serializerNote.data)

# @api_view(['POST'])
# def createNote(request):
#     data = request.data
#     note = Note.objects.create(
#         body=data['body']
#     )
#     serializer = NoteSerializer(note, many=False)
#     return Response(serializer.data)



@api_view(['PUT'])
def updateNote(request,pk):
    data=request.data
    print(data)
    note =Note.objects.get(id=pk)
    
    serializer=NoteSerializer(instance=note,data=data)

    
    if serializer.is_valid():
        serializer.save()
    
    
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteNote(request,pk):
    
    note=Note.objects.get(id=pk)
    note.delete()
    
    
    return Response('note was deleted')
    
@api_view(['POST'])  
def test(request):
    data = request.data
    note = Note.objects.create(
        body=data['body']
    )
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)

@api_view(['GET'])  
def test2(request):
    print("eeeeee")
    return Response('eeeeeeee')