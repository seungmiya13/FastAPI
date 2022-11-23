from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from domain.answer import answer_router
from domain.question import question_router

app = FastAPI()

origins = [
    "http://127.0.0.1:5173",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
) # 프론트엔드에서 FastAPI 백엔드 서버로 호출하도록 FastAPI에 CORS 예외 URL을 등록


app.include_router(question_router.router) # question_router.py 파일의 router 객체를 등록
app.include_router(answer_router.router)
