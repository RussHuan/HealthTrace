from flask import Blueprint, request, jsonify
from models import db
from models.user import User
from utils.response import success_response, error_response
from datetime import datetime, timedelta

class Judge():
    @staticmethod
    def judge_diet_calories(i: float):
        if i < 1800:
            return "请增加饮食"
        elif i > 2700:
            return "请减少饮食"
        else:
            return "饮食习惯良好"
        
    @staticmethod
    def judge_exercise(ave_duration: float):
        if ave_duration < 10:
            return "请增加锻炼时长"
        else:
            return "运动习惯良好"
        
    @staticmethod
    def judge_sleep(ave_sleep: float):
        if ave_sleep < 8:
            return "请增加睡眠时长"
        else:
            return "睡眠充足"
        
        
advice_bp = Blueprint('advice', __name__, url_prefix='/advice')     
   
# 使用上面的函数，根据用户习惯返回建议

@advice_bp.route('/get', methods=['GET'])
def get_advice():
    """根据用户记录返回健康建议"""
    user_id = request.args.get('user_id', type=int)
    if not user_id:
        return error_response(400, "缺少用户ID")
    user = User.query.get(user_id)
    if not user:
        return error_response(404, "用户不存在")

    # 这里假设有相关模型和方法可以获取用户的饮食、锻炼、睡眠平均值
    from models.diet import DietRecord
    from models.exercise import ExerciseRecord
    from models.sleep import SleepRecord
    from sqlalchemy import func

    # 获取最近30天的平均饮食摄入、锻炼时长、睡眠时长
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)

    diet_avg = db.session.query(func.avg(DietRecord.calories)).filter(
        DietRecord.user_id == user_id,
        DietRecord.date >= start_date,
        DietRecord.date <= end_date
    ).scalar() or 0

    exercise_avg = db.session.query(func.avg(ExerciseRecord.duration)).filter(
        ExerciseRecord.user_id == user_id,
        ExerciseRecord.date >= start_date,
        ExerciseRecord.date <= end_date
    ).scalar() or 0

    sleep_avg = db.session.query(func.avg(SleepRecord.duration)).filter(
        SleepRecord.user_id == user_id,
        SleepRecord.date >= start_date,
        SleepRecord.date <= end_date
    ).scalar() or 0

    advice = {
        "diet": Judge.judge_diet_calories(diet_avg),
        "exercise": Judge.judge_exercise(exercise_avg),
        "sleep": Judge.judge_sleep(sleep_avg)
    }
    return success_response({
        "diet_avg": diet_avg,
        "exercise_avg": exercise_avg,
        "sleep_avg": sleep_avg,
        "advice": advice
    })
