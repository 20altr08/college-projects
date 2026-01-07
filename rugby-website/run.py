from sqlalchemy.testing.plugin.plugin_base import fixtures
from project.models import Team
from project import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
    