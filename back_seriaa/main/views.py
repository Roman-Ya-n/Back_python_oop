# main/views.py
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import (
    Team, Coach, Stadium, Calendar, 
    History, Match, PlayerDetailed, PlayerTechnical
)
from .serializers import (
    TeamBaseSerializer, TeamDetailSerializer, TeamCreateSerializer,
    CoachBaseSerializer, CoachDetailSerializer, CoachCreateSerializer,
    StadiumBaseSerializer, StadiumDetailSerializer, StadiumCreateSerializer,
    CalendarBaseSerializer, CalendarDetailSerializer, CalendarCreateSerializer,
    HistoryBaseSerializer, HistoryDetailSerializer, HistoryCreateSerializer,
    MatchBaseSerializer, MatchDetailSerializer, MatchCreateSerializer,
    PlayerDetailedBaseSerializer, PlayerDetailedDetailSerializer, PlayerDetailedCreateSerializer,
    PlayerTechnicalBaseSerializer, PlayerTechnicalDetailSerializer, PlayerTechnicalCreateSerializer
)
from .repositories import (
    TeamRepository, CoachRepository, StadiumRepository,
    CalendarRepository, HistoryRepository, MatchRepository,
    PlayerDetailedRepository, PlayerTechnicalRepository
)


class TeamViewSet(viewsets.ModelViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.repository = TeamRepository()
    
    def get_serializer_class(self):
        if self.action == 'list':
            return TeamBaseSerializer
        elif self.action == 'retrieve':
            return TeamDetailSerializer
        elif self.action == 'create':
            return TeamCreateSerializer
        return TeamBaseSerializer
    
class CoachViewSet(viewsets.ModelViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.repository = CoachRepository()
    
    def get_serializer_class(self):
        if self.action == 'list':
            return CoachBaseSerializer
        elif self.action == 'retrieve':
            return CoachDetailSerializer
        elif self.action == 'create':
            return CoachCreateSerializer
        return CoachBaseSerializer

class StadiumViewSet(viewsets.ModelViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.repository = StadiumRepository()
    
    def get_serializer_class(self):
        if self.action == 'list':
            return StadiumBaseSerializer
        elif self.action == 'retrieve':
            return StadiumDetailSerializer
        elif self.action == 'create':
            return StadiumCreateSerializer
        return StadiumBaseSerializer
    
class CalendarViewSet(viewsets.ModelViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.repository = CalendarRepository()
    
    def get_serializer_class(self):
        if self.action == 'list':
            return CalendarBaseSerializer
        elif self.action == 'retrieve':
            return CalendarDetailSerializer
        elif self.action == 'create':
            return CalendarCreateSerializer
        return CalendarBaseSerializer
    
class HistoryViewSet(viewsets.ModelViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.repository = HistoryRepository()
    
    def get_serializer_class(self):
        if self.action == 'list':
            return HistoryBaseSerializer
        elif self.action == 'retrieve':
            return HistoryDetailSerializer
        elif self.action == 'create':
            return HistoryCreateSerializer
        return HistoryBaseSerializer

class MatchViewSet(viewsets.ModelViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.repository = MatchRepository()
    
    def get_serializer_class(self):
        if self.action == 'list':
            return MatchBaseSerializer
        elif self.action == 'retrieve':
            return MatchDetailSerializer
        elif self.action == 'create':
            return MatchCreateSerializer
        return MatchBaseSerializer
    
class PlayerDetailedViewSet(viewsets.ModelViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.repository = PlayerDetailedRepository()
    
    def get_serializer_class(self):
        if self.action == 'list':
            return PlayerDetailedBaseSerializer
        elif self.action == 'retrieve':
            return PlayerDetailedDetailSerializer
        elif self.action == 'create':
            return PlayerDetailedCreateSerializer
        return PlayerDetailedBaseSerializer 
    
class PlayerTechnicalViewSet(viewsets.ModelViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.repository = PlayerTechnicalRepository()
    
    def get_serializer_class(self):
        if self.action == 'list':
            return PlayerTechnicalBaseSerializer
        elif self.action == 'retrieve':
            return PlayerTechnicalDetailSerializer
        elif self.action == 'create':
            return PlayerTechnicalCreateSerializer
        return PlayerTechnicalBaseSerializer

class ReportViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['get'])
    def team_stats(self, request):
        # Агрегація даних через репозиторії
        team_repo = TeamRepository()
        player_repo = PlayerTechnicalRepository()
        
        report = {
            "total_teams": team_repo.get_team_count(),
            "top_scoring_teams": team_repo.get_top_teams_by_points(5),
            "player_stats": player_repo.get_top_scorers(10)
        }
        return Response(report)