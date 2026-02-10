from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register("", views.VeterinarioViewSet)

urlpatterns = router.urls
