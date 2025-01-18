from fastapi import FastAPI, Body

app = FastAPI()

courses_db = [
    {"id": 1, "instructor": "Ramazan", "title": "Python", "category": "Programming"},
    {"id": 2, "instructor": "Ahmet", "title": "Java", "category": "Programming"},
    {"id": 3, "instructor": "Atlas", "title": "C#", "category": "Programming"},
    {"id": 4, "instructor": "Berivan", "title": "C++", "category": "Programming"},
    {"id": 5, "instructor": "Devrim", "title": "R", "category": "Programming"},
    {"id": 6, "instructor": "Gülistan", "title": "Shell", "category": "Programming"},
]

@app.get("/")
def hello_world():
    return {"message": "Hello World!"}

@app.get("/courses")
def get_courses():
    return courses_db

#Path Parameter
@app.get("/courses/{course_title}")
async def get_course(course_title: str):
    for course in courses_db:
        if course["title"].lower() == course_title:
            return course

#Çalışmaz.
@app.get("/courses/{course_id}")
async def get_course_id(course_id: int):
    for course in courses_db:
        if course["id"] == course_id:
            return course



@app.get("/courses/id/{course_id}")
async def get_course_id(course_id: int):
    for course in courses_db:
        if course["id"] == course_id:
            return course


@app.get("/courses/")
async def get_course_by_query(category: str):
    courses_to_return = []
    for course in courses_db:
        if course["category"].casefold() == category.casefold():
            courses_to_return.append(course)
    return courses_to_return

@app.get("/courses/{course_instructor}/")
async def get_instructor_category_by_query(course_instructor: str,category: str):
    courses_to_return = []
    for course in courses_db:
        if (course["instructor"].casefold() == course_instructor.casefold()
            and course["category"].casefold() == category.casefold()):
            courses_to_return.append(course)
        return courses_to_return


@app.post("/courses/{create_course}/")
async def create_course(new_course=Body()):
    courses_db.append(new_course)


@app.put("/courses/update_course")
async def update_course(update_course=Body()):
    for i in range(len(courses_db)):
        if courses_db[i]["id"] == update_course["id"]:
            courses_db[i] = update_course


@app.delete("/courses/delete/{course_id}")
async def delete_course(course_id: int):
    for i in range(len(courses_db)):
        if courses_db[i]["id"] == course_id:
            courses_db.pop(i)
            break