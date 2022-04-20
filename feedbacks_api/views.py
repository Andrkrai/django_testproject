from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .serializers import CategorySerializer, ProductSerializer, FeedbackSerializer
from catalog.models import Category, Product
from feedbacks.models import Feedback
from rest_framework.views import APIView
from rest_framework.response import Response


class CategoriesViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['category']


class FeedbackAPIView(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

# class FeedbackAPIView(APIView):
#     def get(self, request):
#         queryset = Feedback.objects.all()
#         serializer = FeedbackSerializer(queryset, many=True)
#         return Response({"feedbacks": serializer.data})
#
#     def post(self, request):
#         feedback = request.data.get('feedbacks')
#         serializer = FeedbackSerializer(data=feedback)
#         if serializer.is_valid(raise_exception=True):
#             feedback_saved = serializer.save()
#         return Response({"success": "Feedback '{}' created successfully".format(feedback_saved.title)})
