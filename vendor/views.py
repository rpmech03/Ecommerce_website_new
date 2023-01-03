from django.shortcuts import render
from vendor.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from django.db.models import Q


class VendorDetailsView(APIView):
    def get(self, request, pk):
        try:
            queryset = Vendor.objects.get(pk=pk)
            # queryset.incrementViews()
            serializer = VendorSerializer(queryset)
            return Response({
            'status' : True,
            'message' : 'vendors fetched with GET',
            'data': serializer.data
            })
        except Exception as e:
            print(e)

            return Response({
                'status' : False,
                'message' : 'something went wrong',
                'data': serializer.data
            })

class VendorView(APIView):

    def get(self, request):
        queryset =Vendor.objects.all()
        serializer = VendorSerializer(queryset, many =True)
        if request.GET.get('search'):
            search = request.GET.get('search')
            queryset = queryset.filter(
                Q(name__icontains = search) |
                Q(shop_documents__icontains = search) |
                Q(email__icontains = search) 
                # Q(animal_color__animal_color__icontains = search) 
            )

       

        return Response({
            'status' : True,
            'message' : 'vendors fetched with GET',
            'data': serializer.data
        })

    def post(self, request):
        return Response({
            'status' : True,
            'message' : 'vendors fetched with POST',
        })

    def put(self, request):
        return Response({
            'status' : True,
            'message' : 'vendors fetched with PUT',
        })

    def patch(self, request):
        return Response({
            'status' : True,
            'message' : 'animals fetched with PATCH',
        })