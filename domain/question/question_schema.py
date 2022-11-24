import datetime

from pydantic import BaseModel, validator
# pydantic : FastAPI의 입출력 스펙을 정의하고 그 값을 검증하기 위해 사용하는 라이브러리

from domain.answer.answer_schema import Answer


class Question(BaseModel):
    id: int
    subject: str
    content: str
    create_date: datetime.datetime
    answers: list[Answer] = []

    class Config:
        orm_mode = True

class QuestionCreate(BaseModel):
    subject: str
    content: str\

    @validator('subject', 'content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v
