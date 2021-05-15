
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from products.views import ProductList
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='home'),
    path('about/', views.about_page, name='about'),
    path('reg', views.reg_page),
    path('login', views.login_page),
    path('products/', ProductList.as_view(), name='products'),
    path('products/<int:pk>/', views.ProductDetail.as_view(), name='detail' ),
    path('bootstrap/', TemplateView.as_view(template_name='bootstrap/example.html')),
    path('search/', include('search.urls')),
    path('cart/', include('cart.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
