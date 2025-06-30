from django.shortcuts import render
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Feed
from .serializers import FeedSerializer

# from django.http import HttpResponse
#
# def show_feed(request):
# 	return HttpResponse("show feed")
#
# def one_feed(request, feed_id, feed_content):
# 	return HttpResponse(f"feed id: {feed_id}, {feed_content}")
#
# def all_feed(request):
# 	return HttpResponse("all feed")

class Feeds(APIView):
	def get(self, request):
		feeds = Feed.objects.all()

		serializer = FeedSerializer(feeds, many=True)
		return Response(serializer.data)

class FeedDetail(APIView):
	def get_object(self, feed_id):
		try:
			return Feed.objects.get(id=feed_id)
		except Feed.DoesNotExist:
			raise NotFound()

	def get(self, request, feed_id):
		feed = self.get_object(feed_id)

		serializer = FeedSerializer(feed)
		print(serializer)

		return Response(serializer.data)