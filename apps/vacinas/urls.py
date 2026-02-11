from rest_framework.routers import SimpleRouter

from apps.vacinas.views import RegistroVacinaViewSet, VacinaViewSet


router = SimpleRouter()
router.register("unidades", VacinaViewSet, basename="vacinas")
router.register("registros", RegistroVacinaViewSet, basename="registros")

urlpatterns = router.urls
