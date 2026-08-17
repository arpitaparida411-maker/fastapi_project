from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Student(BaseModel):
    name: str = Field(min_length=2)
    age: int = Field(ge=1, le=100)
    email: str


@app.get("/")
async def home():
    return {"message": "FastAPI is working!"}


@app.post("/students")
async def create_student(student: Student):
    return {
        "message": "Student created successfully",
        "student": student
    }


@app.get("/students/{student_id}")
async def get_student(student_id: int):
    return {
        "student_id": student_id,
        "message": "Student found"
    }