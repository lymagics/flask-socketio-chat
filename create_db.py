from app.models import db, User, Room, Message
from manage import app

app_ctx = app.app_context()
app_ctx.push()

db.create_all()

app_ctx.pop()
