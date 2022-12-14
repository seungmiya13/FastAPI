import datetime

from pydantic import BaseModel, validator


class AnswerCreate(BaseModel):
    content: str

    @validator('content')
    def not_empty(cls, v):  # 답변에 빈 문자열을 허용하지 않도록 설정
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v


class Answer(BaseModel):
    id: int
    content: str
    create_date: datetime.datetime

    class Config:
        orm_mode = True  # 조회한 모델의 속성을 스키마에 매핑
