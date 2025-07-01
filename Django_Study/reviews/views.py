from django.shortcuts import render
from rest_framework.exceptions import NotFound

from reviews.serializers import ReviewSerializer
from .models import Review
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
class Reviews(APIView):
    def get(self,request):
        reviews=Review.objects.all()
        serializer=ReviewSerializer(reviews,many=True)
        return Response(serializer.data)

class ReviewDetail(APIView):
    def get(self,request, review_id):
        try:
            review=Review.objects.get(pk=review_id)
        except:
            raise NotFound

        serializer=ReviewSerializer(review)
        return Response(serializer.data)