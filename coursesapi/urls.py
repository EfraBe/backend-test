from django.urls import include, path
from rest_framework import routers
from . import views
from .apiviews import Login, Courses, Lessons, Questions

router = routers.DefaultRouter()
router.register(r'pageuser', views.PageUserViewSet)
# router.register(r'login', views.PageUserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('login/', Login.as_view(), name='login'),
    path('course/', Courses.as_view(), name='course'),
    path('course/<int:pk>/', Courses.as_view(), name='course'),
    path('lesson/', Lessons.as_view(), name='lesson'),
    path('question/', Questions.as_view(), name='question'),
]