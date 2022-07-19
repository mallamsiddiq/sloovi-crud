from django.contrib import admin
from django.urls import include, path
from api import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

#from newsite import blog


# handler404 = views.error_404

schema_view = get_schema_view(
   openapi.Info(
      title="a test API to perform CRUD operations on templates",
      default_version='v1',
      description="""An API built to register users, 
      provide login endpoint to get authentication token to access templates and view personal user details, 
      play around with this apis found each endpoin below""",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="mallamsiddiq@gmail.com"),
      license=openapi.License(name="Sloovi License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger-no/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', include('api.urls')),
]