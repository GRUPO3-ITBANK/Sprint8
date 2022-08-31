from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from Clientes.models import Cliente
from Cuentas.models import Cuenta
from Prestamos.models import Prestamo
from Tarjetas.models import Tarjeta
from API.serializers import ClienteSerializer, CuentaSerializer, PrestamoSerializer, TarjetaSerializer

class ClienteList(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            if not (request.user.id_empleado_id == None) or request.user.is_staff: #si es empleado/staff... traigo todos
                serializer = ClienteSerializer(Cliente.objects.all(), many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                 serializer = ClienteSerializer(Cliente.objects.filter(pk=request.user.id_cliente.id).first())
            return Response(serializer.data, status=status.HTTP_200_OK)
        else: 
            return Response( status=status.HTTP_401_UNAUTHORIZED)


class CuentaList(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            if not (request.user.id_empleado_id == None) or request.user.is_staff: #si es empleado/staff... traigo todos
                serializer = CuentaSerializer(Cuenta.objects.all(), many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                serializer = CuentaSerializer(Cuenta.objects.filter(ID_cliente=request.user.id_cliente.id), many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else: 
            return Response( status=status.HTTP_401_UNAUTHORIZED)



class PrestamoDetails(APIView):
    def get(self, request,pk):
        if request.user.is_authenticated:
            if not (request.user.id_empleado_id == None) or request.user.is_staff: #si es empleado... filtro los prestamos por sucursal
                serializer = PrestamoSerializer(Prestamo.objects.filter(sucursal=pk), many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                serializer = PrestamoSerializer(Prestamo.objects.filter(ID_cliente=request.user.id_cliente.id), many=True) #si tan solo es un cliente filtro los prestamos por id de cliente
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response( status=status.HTTP_401_UNAUTHORIZED)

class PrestamoList(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            if not (request.user.id_empleado_id == None) or request.user.is_staff: #si es empleado... traigo todos
                serializer = PrestamoSerializer(Prestamo.objects.all(), many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                serializer = PrestamoSerializer(Prestamo.objects.filter(ID_cliente=request.user.id_cliente.id), many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        else: 
            return Response( status=status.HTTP_401_UNAUTHORIZED)


# class TarjetaDetails(APIView):
#     def get(self, request,pk):
#         if request.user.is_authenticated:
#             if not (request.user.id_empleado_id == None) or request.user.is_staff : #si es empleado... filtro por id de Usuario
#                 serializer = TarjetaSerializer(Tarjeta.objects.filter(ID_cliente=pk), many=True)
#                 return Response(serializer.data, status=status.HTTP_200_OK)
#             else:
#                 serializer = TarjetaSerializer(Tarjeta.objects.filter(ID_cliente=request.user.id_cliente.id), many=True) #si tan solo es un cliente filtro las tarjetas por id de cliente
#                 return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response( status=status.HTTP_401_UNAUTHORIZED)

class TarjetaList(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            if not (request.user.id_empleado_id == None) or request.user.is_staff: #si es empleado... traigo todas las tarjetas
                serializer = TarjetaSerializer(Tarjeta.objects.all(), many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                serializer = TarjetaSerializer(Tarjeta.objects.filter(ID_cliente=request.user.id_cliente.id), many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        else: 
            return Response( status=status.HTTP_401_UNAUTHORIZED)

    def post(self,request,format=None):
        serializer = TarjetaSerializer(data=request.data)
        if request.user.is_authenticated:
            if not (request.user.id_empleado_id == None): #Si es empleado
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response( status=status.HTTP_401_UNAUTHORIZED)
        return Response( status=status.HTTP_401_UNAUTHORIZED)






