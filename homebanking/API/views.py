from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from Clientes.models import Cliente
from API.serializers import ClienteSerializer

class ClienteDetails(APIView):
    def get(self, request, pk):
        cliente = Cliente.objects.filter(pk=pk).first()
        serializer = ClienteSerializer(cliente)
        if cliente:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)