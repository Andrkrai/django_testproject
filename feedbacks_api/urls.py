# feedbacks_api/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'category', views.CategoriesViewset)
router.register(r'product', views.ProductViewset)
# router.register(r'feedback', views.FeedbackAPIView)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('feedback_list/', views.FeedbackAPIViewList.as_view()),
    path('feedback/', views.FeedbackAPIView.as_view()),
    path('feedback_edit/<int:pk>', views.FeedbackAPIViewEdit.as_view()),
]
