from .models import Todo
from rest_framework import viewsets
from .serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Todo.objects.all().order_by('-id')
    serializer_class = TodoSerializer
