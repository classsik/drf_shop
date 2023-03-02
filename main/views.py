from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import ProductSerializer, CategorySerializer, ManufacturerSerializer

from .models import Product, Category, Manufacturer


class CRUDProduct(APIView):
    @staticmethod
    def get(self, request, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            serializer = ProductSerializer(Product.objects.all(), many=True)
        else:
            try:
                serializer = ProductSerializer(Product.objects.get(pk=pk))
            except Product.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data)

    @staticmethod
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    @staticmethod
    def put(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(data=request.data, instance=product)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    @staticmethod
    def delete(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response(status=status.HTTP_200_OK)


class CRUDManufacturer(APIView):
    @staticmethod
    def get(self, request, **kwargs):
        pk = kwargs.get('pk', None)

        if not pk:
            serializer = ManufacturerSerializer(Manufacturer.objects.all(), many=True)
        else:
            try:
                serializer = ManufacturerSerializer(Manufacturer.objects.get(pk=pk))
            except Manufacturer.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data)

    @staticmethod
    def post(self, request):
        serializer = ManufacturerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    @staticmethod
    def put(self, request, pk):
        try:
            product = Manufacturer.objects.get(pk=pk)
        except Manufacturer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ManufacturerSerializer(data=request.data, instance=product)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    @staticmethod
    def delete(self, request, pk):
        try:
            product = Manufacturer.objects.get(pk=pk)
        except Manufacturer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response(status=status.HTTP_200_OK)


class CRUDCategory(APIView):
    @staticmethod
    def get(request, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            serializer = CategorySerializer(CategorySerializer.objects.all(), many=True)
        else:
            try:
                serializer = CategorySerializer(Category.objects.get(pk=pk))
            except Category.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data)

    @staticmethod
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    @staticmethod
    def put(self, request, pk):
        try:
            product = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CategorySerializer(data=request.data, instance=product)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    @staticmethod
    def delete(self, request, pk):
        try:
            product = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response(status=status.HTTP_200_OK)
