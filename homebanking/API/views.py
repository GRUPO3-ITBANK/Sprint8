from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from Clientes.models import Cliente
from Cuentas.models import Cuenta
from Prestamos.models import Prestamo
from API.serializers import ClienteSerializer, CuentaSerializer, PrestamoSerializer

class ClienteDetails(APIView):
    # def get(self, request, pk):
    #     cliente = Cliente.objects.filter(pk=pk).first()
    #     serializer = ClienteSerializer(cliente)
    #     if cliente:
    #         if request.user.is_authenticated and (request.user.id_cliente.id ==pk):
    #             return Response(serializer.data, status=status.HTTP_200_OK)
    #         else:
    #             return Response( status=status.HTTP_401_UNAUTHORIZED)
    #     return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    def get(self, request):
        if request.user.is_authenticated:
            serializer = ClienteSerializer(Cliente.objects.filter(pk=request.user.id_cliente.id).first())
            return Response(serializer.data, status=status.HTTP_200_OK)
        else: 
            return Response( status=status.HTTP_401_UNAUTHORIZED)

class CuentaDetails(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            serializer = CuentaSerializer(Cuenta.objects.filter(ID_cliente=request.user.id_cliente.id), many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else: 
            return Response( status=status.HTTP_401_UNAUTHORIZED)

class PrestamoDetails(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            serializer = PrestamoSerializer(Prestamo.objects.filter(ID_cliente=request.user.id_cliente.id), many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else: 
            return Response( status=status.HTTP_401_UNAUTHORIZED)


