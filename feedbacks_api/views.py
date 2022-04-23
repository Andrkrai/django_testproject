from rest_framework import viewsets
from .serializers import CategorySerializer, ProductSerializer, FeedbackSerializer
from catalog.models import Category, Product
from feedbacks.models import Feedback
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import get_object_or_404
from rest_framework.throttling import SimpleRateThrottle, ScopedRateThrottle


class CategoriesViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['category']


# class FeedbackAPIView(viewsets.ModelViewSet):
#     queryset = Feedback.objects.all()
#     serializer_class = FeedbackSerializer

class FeedbackAPIViewList(APIView):
    def get(self, request):
        queryset = Feedback.objects.all()
        serializer = FeedbackSerializer(queryset, many=True)
        return Response({"feedbacks": serializer.data})


class FeedbackAPIView(APIView):
    class Per5MinutesRateThrottle(ScopedRateThrottle, SimpleRateThrottle):
        def parse_rate(self, rate):
            """
            Throttling by 5 minutes
            """
            if rate is None:
                return None, None
            num, period = rate.split('/')
            num_requests = int(num)
            duration = {'m': 300}[period[0]]
            return num_requests, duration

    throttle_classes = [Per5MinutesRateThrottle]
    throttle_scope = 'feedbackAPIViewAdd'

    def post(self, request):
        feedback = request.data.get('feedback')
        serializer = FeedbackSerializer(data=feedback)
        if serializer.is_valid(raise_exception=True):
            feedback_saved = serializer.save()
        return Response({"success": "Feedback '{}' '{}' created successfully".format(feedback_saved.full_name,
                                                                                     feedback_saved.product)})


class FeedbackAPIViewEdit(APIView):
    def put(self, request, pk):
        saved_feedback = get_object_or_404(Feedback.objects.all(), pk=pk)
        data = request.data.get('feedback')
        serializer = FeedbackSerializer(instance=saved_feedback, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            feedback_saved = serializer.save()
        return Response({"success": "Feedback '{}' updated successfully".format(feedback_saved.full_name,
                                                                                feedback_saved.product)})

    def delete(self, request, pk):
        feedback = get_object_or_404(Feedback.objects.all(), pk=pk)
        feedback.delete()
        return Response({"success": "Feedback with id '{}' has been deleted.".format(pk)}, status=204)
