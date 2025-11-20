from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from main import views

router = DefaultRouter()
router.register(r'teams', views.TeamViewSet)
router.register(r'coach', views.CoachViewSet)
router.register(r'stadium', views.StadiumViewSet)
router.register(r'calendar', views.CalendarViewSet)
router.register(r'history', views.HistoryViewSet)
router.register(r'match', views.MatchViewSet)
router.register(r'player-detailed', views.PlayerDetailedViewSet)
router.register(r'player-technical', views.PlayerTechnicalViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
