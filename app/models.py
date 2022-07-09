from datetime import datetime

from . import db 


class User(db.Model):
    """SQLALchemy model to represent users table.
    
    :param user_id: unique user identifier.
    :param username: user nick name.
    """
    __tablename__ = "users"
    
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    
    messages = db.relationship("Message", backref="author", cascade="all,delete", lazy="dynamic")
    
    def __repr__(self):
        return f"<User {self.username}>"
    
    
class Room(db.Model):
    """SQLALchemy model to represent rooms table.
    
    :param room_id: unique room identifier.
    :param room_name: room name.
    """
    __tablename__ = "rooms"
    
    room_id = db.Column(db.Integer, primary_key=True)
    room_name = db.Column(db.String(64), nullable=False, unique=True)
    
    messages = db.relationship("Message", backref="room", cascade="all,delete", lazy="dynamic")
    
    def __repr__(self):
        return f"<Room {self.room_name}>"
    
    
class Message(db.Model):
    """SQLALchemy model to represent messages table.
    
    :param message_id: unique user identifier.
    :param text: message body.
    :param timestamp: date and time message was sent.
    :param author_id: message publisher id.
    :param room_id: room where message was published.
    """
    __tablename__ = "messages"
    
    message_id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    room_id = db.Column(db.Integer, db.ForeignKey("rooms.room_id"))
    
    def get_timestamp(self):
        """Convert message timestamp to string repr."""
        return self.timestamp.strftime("%m.%d.%Y, %H:%M")
    
    def __repr__(self):
        return f"<Message {self.message_id}>"
    