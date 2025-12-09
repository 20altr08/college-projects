from datetime import date, time
from project.models import Fixtures, Team, Results
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

uk_league_names = [ "",
    "Southern Counties League",
    "Northern Premier Division",
    "West Midlands Football League",
    "Devon & Cornwall Championship",
    "East Sussex Senior League",
    "Greater London Premier"
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
    league = random.choice(uk_league_names)

    if league == "":
        league = "Normal Matches"

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
            league_name=league,
        )

        db.session.add(fixture)

        db.session.commit()

        team1_score = random.randint(0, 50)
        team2_score = random.randint(0, 50)

        repeater = random.randint(1,3)

        if repeater == 1:
            result = Results(
                fixture_id=fixture.id,
                team1_score=team1_score,
                team2_score=team2_score
            )
            db.session.add(result)
            db.session.commit()

            print(
                f"Created fixture: {team1.name} vs {team2.name} "
                f"at {fixture.venue} - {team1_score} - {team2_score}")
        else:
            print(f"Created fixture: {team1.name} vs {team2.name} "
                  f"at {fixture.venue}")

for i in range(5):
    creating_fixtures()