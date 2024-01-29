from django.contrib import admin
from django.urls import path,include
from reviews.views import ProductViewset,ImageViewSet#,MyTokenObtainPairView
from auth.views import MyTokenObtainPairView
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    # TokenObtainPairView,
    TokenRefreshView
)


router = DefaultRouter()
router.register(r'product',ProductViewset,basename='Product')
router.register(r'image',ImageViewSet,basename='Image')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('token/',MyTokenObtainPairView.as_view(),name="token_obtain_pair"),
    # path('token/refresh/',TokenRefreshView.as_view(),name="token_refresh"),
    path('', include(router.urls)),
    path('pizzeria/', include("stores.urls")),
    path('auth/', include('auth.urls'))
]

if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
