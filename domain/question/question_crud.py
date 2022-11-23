from models import Question
from sqlalchemy.orm import Session


def get_question_list(db: Session): # Question 모델의 모든 항목이 출력으로 리턴
    question_list = db.query(Question)\
        .order_by(Question.create_date.desc())\
        .all()
    return question_list


def get_question(db: Session, question_id: int):
    question = db.query(Question).get(question_id)
    return question
