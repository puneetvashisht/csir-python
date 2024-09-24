from fastapi import FastAPI
from course import Course
app = FastAPI()

courses: Course = [{
    "id": 1,
    "title": "Python Programming",
    "instructor": "Dr. Samuel Johnson",
    "students": 300
}]

@app.get("/hello")
def hello_world():
    return {"message": f"Hello, World!"}

@app.get("/courses")
def get_courses():
    return courses

#fetch a single course

@app.get("/courses/{course_id}")
def get_course(course_id: int):
    for course in courses:
        if course["id"] == course_id:
            return course

@app.post("/courses")
def create_course(course: Course):
    courses.append(course)
    return course

@app.delete("/courses/{course_id}")
def delete_course(course_id: int):
   for course in courses:
        if course["id"] == course_id:
            courses.remove(course)
            return {"message": f"Course with id {course_id} deleted"}


@app.patch("/courses/{course_id}")

def update_course(course_id: int, updated_course: Course):
    global courses
    course = next((course for course in courses if course['id'] == course_id), None)
    if course is None:
        return {"error": f"Course with id {course_id} not found"}
    course.update(updated_course.dict(exclude_unset=True))
    return course