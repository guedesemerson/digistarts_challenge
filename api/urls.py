from django.contrib import admin
from rest_framework import permissions
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Digistarts Challenge",
        default_version='v1',
        description="Builded by Emerson Guedes de Oliveira",
        contact=openapi.Contact(email="guedes.emerson@hotmail.com"),
        license=openapi.License(name="Todos os direitos reservados"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),

)

urlpatterns = [
    path('number/', include('number.urls')),
    path('admin', admin.site.urls),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]