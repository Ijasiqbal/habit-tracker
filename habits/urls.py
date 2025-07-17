from django.urls import path
from .views import RegisterView, UserDetailView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from .views import HabitViewSet

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('me/', UserDetailView.as_view(), name='user_detail'),
]

router = DefaultRouter()
router.register(r'habits', HabitViewSet, basename='habit')

urlpatterns += router.urls 