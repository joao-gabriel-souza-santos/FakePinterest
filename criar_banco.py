from fakePinterest import database, app
from fakePinterest.model import Usuario, Foto
with app.app_context():
    database.create_all()