from django.urls import path

from .views import TemplateView, RegisterView, TemplateDetailView,UsersView, UserDetail
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [ 

    path('template/', TemplateView.as_view(), name='templates'),
    path('template/<template_id>/', TemplateDetailView.as_view(), name='template-details'),
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login-auth/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view()),
    path('user-profile/<user_id>/', UserDetail.as_view(), name='user-details'),
    path('users/', UsersView.as_view(), name='users-all'),
    ]

