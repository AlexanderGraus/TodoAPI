from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import TodoSerializer, UserSerializer
from django.contrib.auth.models import User
from .models import Todo
from .permissions import EsDuenioOSoloLectura
# Create your views here.

class TodoView(viewsets.ModelViewSet): #U: la clase ModelViewSet implementa automaticamente las operaciones CRUD
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        EsDuenioOSoloLectura
    ]

    def perform_create(self,serializer):
        serializer.save(user = self.request.user)

class UserViewSet(viewsets.ReadOnlyModelViewSet): #U: al ser ReadOnly solo permite ver y no editar
    queryset = User.objects.all()
    serializer_class = UserSerializer