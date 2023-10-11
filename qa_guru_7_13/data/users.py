import dataclasses
from datetime import date
from enum import Enum


class Gender(Enum):
    male = 'Male'
    female = 'Female'
    other = 'Other'


class Hobbies(Enum):
    sports = 'Sports'
    reading = 'Reading'
    music = 'Music'


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: Gender
    user_number: str
    date_of_birth: date
    subject: str
    hobby: Hobbies
    upload_picture: str
    current_address: str
    state: str
    city: str


student = User(
    'Daniil',
    'Zverev',
   'test@gmail.ru',
    Gender.male.value,
    '1234567890',
    date(1998, 5, 4),
    'Maths',
    Hobbies.sports.value,
    'test_picture.jpg',
    'orehovo-zuevo, parcov, 15',
    'NCR',
    'Noida',
)