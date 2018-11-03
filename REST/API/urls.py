from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'people', PeopleViewSet)
router.register(r'users', UserViewSet)
router.register(r'question', QuestionViewSet )
router.register(r'answer', AnswerViewSet)


# Wire up our API using automatic URL routing.

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),   
]
