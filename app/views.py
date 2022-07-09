from flask import Blueprint, redirect, render_template, session, url_for

from . import db, events
from .decorators import login_required
from .forms import LoginForm
from .models import User, Room

main = Blueprint("main", __name__)


@main.route("/", methods=["GET", "POST"])
def index():
    """Index page route handler.
    
    :GET landing page: "main.index".
    :POST login user and redirect to "main.chat".
    """
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None:
            user = User(username=form.username.data)
            db.session.add(user)
            db.session.commit()
            
        room = Room.query.filter_by(room_name=form.room.data).first()
        if room is None:
            room = Room(room_name=form.room.data)
            db.session.add(room)
            db.session.commit()
            
        session["user"] = user.user_id 
        session["room"] = room.room_id
        return redirect(url_for("main.chat"))
    rooms = Room.query.all()
    return render_template("index.html", form=form, rooms=rooms)


@main.route("/chat")
@login_required
def chat():
    """Chat page route handler.
    
    :GET landing page: "main.chat".
    """
    username = User.query.get(session.get("user")).username
    
    room = Room.query.get(session.get("room"))
    messages = room.messages
    room_name = room.room_name
    return render_template("chat.html", username=username, messages=messages,
                           room_name=room_name)


@main.route("/home")
@login_required
def home():
    """Home page route handler with logout function.
    
    :GET reset session credentials and redirect to "main.index".
    """
    session["user"] = None 
    return redirect(url_for("main.index"))
