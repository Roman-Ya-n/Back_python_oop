# test_repositories.py

from repositories.team_repository import TeamRepository
from repositories.coach_repository import CoachRepository

team_repo = TeamRepository()
coach_repo = CoachRepository()

# ✅ Create
barca = team_repo.create(team_name="Barcelona", point=12, wins=4, draws=0, loses=1)

# ✅ Read
all_teams = team_repo.get_all()
print(all_teams)

# ✅ Search
coach = coach_repo.get_by_id(1)
print(coach)

# ✅ Update
team_repo.update(barca.team_id, point=15)

# ✅ Delete
coach_repo.delete(3)
