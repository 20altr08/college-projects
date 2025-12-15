from project import create_app, db
from project.models import Team, Fixtures
import os
import re
from datetime import date, time
app = create_app()


def create_teams_from_logos():

    """
    Scans the 'static/assets' folder for PNG files and creates Team entries in the database.

    Returns:
        dict: Dictionary with 'created', 'skipped', and 'errors' counts
    """

    # Set folder path to 'project/static/assets'
    folder_path = os.path.join('project', 'static', 'assets')

    results = {
        'created': 0,
        'skipped': 0,
        'errors': []
    }

    # Check if folder exists
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' does not exist")
        return results

    # Get all PNG files in the folder
    png_files = [f for f in os.listdir(folder_path)
                 if f.lower().endswith('.png')]

    if not png_files:
        print(f"No PNG files found in '{folder_path}'")
        return results

    print(f"Found {len(png_files)} PNG file(s)")

    for filename in png_files:
        try:
            # Remove .png extension to get team name
            team_name = filename[:-4]  # Remove last 4 characters (.png)
            team_name = re.findall('[A-Z][^A-Z]*', team_name)
            team_name = " ".join(team_name)
            # Check if team already exists
            existing_team = Team.query.filter_by(name=team_name).first()

            if existing_team:
                print(f"Skipped: Team '{team_name}' already exists")
                results['skipped'] += 1
                continue

            # Create new team entry
            new_team = Team(
                name=team_name,
                logo=filename  # Store the full filename with extension
            )

            db.session.add(new_team)
            print(f"Created: Team '{team_name}' with logo '{filename}'")
            results['created'] += 1

        except Exception as e:
            error_msg = f"Error processing '{filename}': {str(e)}"
            print(error_msg)
            results['errors'].append(error_msg)

    # Commit all changes to database
    try:
        db.session.commit()
        print(f"\nSuccessfully committed {results['created']} team(s) to database")
    except Exception as e:
        db.session.rollback()
        print(f"Error committing to database: {str(e)}")
        results['errors'].append(f"Database commit error: {str(e)}")

    return results



if __name__ == '__main__':
    with app.app_context():
        # Create tables if they don't exist
        db.drop_all()
        db.create_all()
        print("Tables created/verified\n")

        # Populate teams from PNG files
        results = create_teams_from_logos()

        print(f"\n=== Summary ===")
        print(f"Teams created: {results['created']}")
        print(f"Teams skipped: {results['skipped']}")
        print(f"Errors: {len(results['errors'])}")
