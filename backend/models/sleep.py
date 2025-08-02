from models import db
from datetime import datetime, timedelta

class Sleep(db.Model):
    __tablename__ = 'sleep_records'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    sleep_time = db.Column(db.DateTime, nullable=False)  # 入睡时间
    wake_time = db.Column(db.DateTime, nullable=False)   # 起床时间
    duration_hours = db.Column(db.Float, nullable=False) # 睡眠时长（小时）
    quality_rating = db.Column(db.Integer)  # 睡眠质量评分 1-10
    notes = db.Column(db.Text)  # 备注
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # 关联用户
    user = db.relationship('User', backref=db.backref('sleep_records'))
    
    def calculate_duration(self):
        """计算睡眠时长"""
        if self.sleep_time and self.wake_time:
            duration = self.wake_time - self.sleep_time
            # 如果起床时间小于入睡时间，说明跨天了
            if duration.total_seconds() < 0:
                duration += timedelta(days=1)
            self.duration_hours = duration.total_seconds() / 3600
            return self.duration_hours
        return 0
    
    def to_dict(self):
        """转换为字典格式"""
        return {
            "id": self.id,
            "user_id": self.user_id,
            "sleep_time": self.sleep_time.isoformat() if self.sleep_time else None,
            "wake_time": self.wake_time.isoformat() if self.wake_time else None,
            "duration_hours": round(self.duration_hours, 2) if self.duration_hours else 0,
            "quality_rating": self.quality_rating,
            "notes": self.notes,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }
    