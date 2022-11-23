import datetime

from pydantic import BaseModel # pydantic : FastAPI의 입출력 스펙을 정의하고 그 값을 검증하기 위해 사용하는 라이브러리


class Question(BaseModel):
    id: int
    subject: str
    content: str
    create_date: datetime.datetime

    class Config:
        orm_mode = True
