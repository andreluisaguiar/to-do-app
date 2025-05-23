from app import create_app
from flask_migrate import upgrade

app = create_app()

# Use o contexto do app para garantir que o banco está acessível
with app.app_context():
    upgrade()