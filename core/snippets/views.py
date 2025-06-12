from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import CodeSnippet, SnippetTracker
from .tasks import send_next_snippet_email

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_snippets(request):
    snippets = CodeSnippet.objects.filter(user=request.user).order_by('created_at')
    tracker, _ = SnippetTracker.objects.get_or_create(user=request.user)

    data = []
    for idx, snippet in enumerate(snippets):
        data.append({
            'id': snippet.id,
            'code': snippet.code,
            'created_at': snippet.created_at,
            'index': idx,
            'is_next_to_send': idx == ((tracker.last_sent_index + 1) % snippets.count())
        })

    return Response(data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_snippet(request, snippet_id):
    try:
        snippet = CodeSnippet.objects.get(id=snippet_id, user=request.user)
    except CodeSnippet.DoesNotExist:
        return Response({'error': 'Snippet not found'}, status=404)

    snippet.delete()
    return Response({'message': 'Snippet deleted successfully'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_snippet(request):
    code = request.data.get('code', '')
    if not code:
        return Response({'error': 'Code is required'}, status=400)

    snippet = CodeSnippet.objects.create(user=request.user, code=code)
    send_next_snippet_email.delay(request.user.id)
    return Response({'message': 'Snippet saved and email task triggered', 'snippet_id': snippet.id})
