from app_instance import db, app
from sqlalchemy.dialects.mysql import VARCHAR, INTEGER

class Text(db.Model):
    __tablename__ = 'texts'
    id = db.Column("id", INTEGER, primary_key=True)
    text = db.Column("text", VARCHAR(255), nullable=False)
    
    def __init__(self, text=None):
        self.text = text

    def __repr__(self):
        return f'<Text {self.text}>'

with app.app_context():
    db.create_all()