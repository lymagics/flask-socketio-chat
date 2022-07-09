from flask import session
from flask_socketio import join_room, leave_room

from . import sio, db
from .models import User, Room, Message


@sio.on("connect", namespace="/chat")
def handle_connect():
    """SocketIO on connect event."""
    username = User.query.get(session.get("user")).username
    room = Room.query.get(session.get("room")).room_name
    join_room(room)
    sio.emit("status", {"msg": f"{username} has connected."}, namespace="/chat", to=room)


@sio.on("send_message", namespace="/chat")
def handle_message(data):
    """SocketIO on message sent event.
    
    :param data: data sent from user.
    """
    room = Room.query.get(session.get("room"))
    user = User.query.get(session.get("user"))
    msg = Message(text=data.get("msg"), author=user, room=room)
    db.session.add(msg)
    db.session.commit()
    
    data = {
        "username": data.get("username"),
        "msg": data.get("msg"),
        "timestamp": msg.get_timestamp()
    }
    sio.emit("new_message", data, namespace="/chat", to=room.room_name)
    
    
@sio.on("disconnect", namespace="/chat")
def handle_disconnect():
    """SocketIO on disconnect event."""
    username = User.query.get(session.get("user")).username
    room = Room.query.get(session.get("room")).room_name
    leave_room(room)
    sio.emit("status", {"msg": f"{username} has left."}, namespace="/chat", to=room)
    