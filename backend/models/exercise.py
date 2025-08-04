from models import db
from datetime import datetime, timedelta

class Exercise(db.Model):
    __tablename__ = 'exercise_records'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    duration_mimutes = db.Column(db.Float, nullable=False)
    type = db.Column(db.String(64))
    calories = db.Column(db.Float, nullable=False)
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    user = db.relationship('User', backref=db.backref('exercise_records'))

    def calculate_duration(self):
        """计算运动时长"""
        if self.start_time and self.end_time:
            duration = self.end_time - self.start_time
            if duration.total_seconds() < 0:
                duration += timedelta(days=1)
            self.duration_mimutes = duration.total_seconds() / 60
            return self.duration_mimutes
        return 0
    
    def to_dict(self):
        """转换为字典格式"""
        return {
            "id": self.id,
            "user_id": self.user_id,
            "start_time": self.start_time.isoformat() if self.start_time else None,
            "end_time": self.end_time.isoformat() if self.end_time else None,
            "duration_mimutes": round(self.duration_mimutes, 2) if self.duration_mimutes else 0,
            "type": self.type,
            "calories": round(self.calories, 2) if self.calories else 0,
            "notes": self.notes,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }