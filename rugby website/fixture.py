from datetime import date, time
from project.models import Fixtures, Team
from project import db, create_app
import random

app = create_app()

devon_rugby_towns = [
    "Exeter",
    "Tiverton",
    "Okehampton",
    "Brixham",
    "Torquay",
    "Barnstaple",
    "Cullompton",
    "Crediton",
    "Dartmouth",
    "Exmouth",
    "Honiton",
    "Ivybridge",
    "Newton Abbot",
    "Paignton",
    "Plymouth",
    "South Molton",
    "Teignmouth",
    "Topsham"
]

home_away = ['away', 'home']

def creating_fixtures():
    # Load team list once

    venue = random.choice(devon_rugby_towns)
    away = random.choice(home_away)
    random_time = time(
        hour=random.randint(8, 20),
        minute=random.choice([0, 15, 30, 45])  # quarter hours
    )

    with app.app_context():
        teams = Team.query.all()

    with app.app_context():

        # Pick two DIFFERENT random teams
        team1, team2 = random.sample(teams, 2)

        # team2 = random.choice(teams)
        #
        # while team2.id == team1.id:
        #     team2 = random.choice(teams)

        # Create fixture
        fixture = Fixtures(
            venue=venue,
            date=date(2024, 12, 1),
            time=random_time,
            team1_id=team1.id,
            team2_id=team2.id,
            away=away
        )

        db.session.add(fixture)
        db.session.commit()

        print(f"Created fixture: {team1.name} vs {team2.name} at {fixture.venue}: {fixture.date} ({fixture.time})")

for i in range(5):
    creating_fixtures()