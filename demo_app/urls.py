from django.urls import  path, include
from rest_framework import routers
from . import views
from . import api_views

router = routers.DefaultRouter()
router.register(r'model_b' , api_views.ModelBViewSet, basename='model_b')
router.register(r'model_c' , api_views.ModelCViewSet, basename='model_c')

urlpatterns = router.urls

urlpatterns+= [
    path("index/", views.index, name="index"),
    # path("model_b/create", views.ModelBView.as_view(), name="model_b-create"),
    # path("model")
]
