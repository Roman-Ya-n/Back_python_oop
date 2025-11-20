import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'seriaa.settings')
django.setup()

from main.repositories.team_repository import TeamRepository
from main.repositories.coach_repository import CoachRepository

team_repo = TeamRepository()
coach_repo = CoachRepository()

# ✅ Create
# barca = team_repo.create(team_name="MU", points=20, wins=5, draws=3, loses=2)

# # ✅ Read
all_coaches = coach_repo.get_all()
for coach in all_coaches:
    print(coach.coach_id)

# print(all_coaches)


# ✅ Search
# coach = coach_repo.get_by_id(8)
# print(coach)

# ✅ Update
# team_repo.update(barca.team_id, points=15)

# ✅ Delete
# coach_repo.delete(3)
