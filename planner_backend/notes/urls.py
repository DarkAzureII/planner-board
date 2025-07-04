from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'notes', views.NoteViewSet)
router.register(r'connections', views.ConnectionViewSet)

urlpatterns = router.urls