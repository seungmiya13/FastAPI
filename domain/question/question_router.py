from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from domain.question import question_schema, question_crud


router = APIRouter(
    prefix="/api/question",
)


@router.get("/list", response_model=list[question_schema.Question])
def question_list(db: Session = Depends(get_db)):
    # db 세션을 생성하고 해당 세션을 이용하여 질문 목록을 조회하여 리턴하는 함수
    _question_list = question_crud.get_question_list(db)
    return _question_list


@router.get("/detail/{question_id}", response_model=question_schema.Question)
def question_detail(question_id: int, db: Session = Depends(get_db)):
    # URL을 통해 얻은 question_id 값으로 질문 상세 내역을 조회하여 Question 스키마로 리턴하는 함수
    question = question_crud.get_question(db, question_id=question_id)
    return question
