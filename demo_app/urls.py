from django.urls import  path, include
from rest_framework import routers
from . import views
from . import api_views

router = routers.DefaultRouter()
router.register(r'model_b1' , api_views.ModelB1ViewSet, basename='model_b1')
router.register(r'model_b2' , api_views.ModelB2ViewSet, basename='model_b2')
router.register(r'model_c1' , api_views.ModelC1ViewSet, basename='model_c1')
router.register(r'model_c2' , api_views.ModelC2ViewSet, basename='model_c2')
router.register(r'model_d' , api_views.ModelDViewSet, basename='model_d')
router.register(r'model_a' , api_views.ModelAViewSet, basename="model_a")
router.register(r'model_b' , api_views.ModelBViewSet, basename="model_b")
router.register(r'model_c' , api_views.ModelCViewSet, basename="model_c")
# router.register(r'model_c' , api_views.ModelCViewSet, basename='model_c')

urlpatterns = router.urls

urlpatterns+= [
    path("index/", views.create_product, name="index"),
    path("products/", views.list_product, name="product-list")
    # path("model_b/create", views.ModelBView.as_view(), name="model_b-create"),
    # path("model")
]
