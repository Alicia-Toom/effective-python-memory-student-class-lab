from typing import List
from pympler import asizeof

class Person:
    __slots__ = ('name')

    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name

class Student(Person):
    def __init__(self, name: str):
        super().__init__(name)

class Teacher(Person):
    def __init__(self, name: str):
        super().__init__(name)

class Subject():
    __slots__ = ('name')

    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name

class Room():
    __slots__ = ('room_number')

    def __init__(self, room_number: str):
        self.room_number = room_number

    def __str__(self):
        return self.room_number

class Schedule():
    __slots__ = ('schedule')

    def __init__(self, ):
        self.schedule = {}

    def add_to_schedule(self, date: str, room: Room, subject: Subject, teacher: Teacher, students: List[Student]):
        # Use custom class instead of dict to store the "schedule item" ?
        self.schedule[date] = { "room": room, "subject": subject, "teacher": teacher, "students": students }

    def print(self):
        for date, scheduled_class in self.schedule.items():
            print(f"Date: {date}, Room: {scheduled_class['room']}, Subject: {scheduled_class['subject']}, Teacher: {scheduled_class['teacher']}, Students: {','.join(str(student) for student in scheduled_class['students'])}")

if __name__ == "__main__":
    room: Room = Room("Computer Lab")
    subject: Subject = Subject("Python Programming 101")
    student: Student = Student("Alicia")
    teacher: Teacher = Teacher("Mrs Code")

    schedule: Schedule = Schedule()
    schedule.add_to_schedule("2022-09-21 09:00", room, subject, teacher, [student])
    schedule.print()

    print(asizeof.asizeof(schedule))
    # 2016 with dict
    # 40 with slots