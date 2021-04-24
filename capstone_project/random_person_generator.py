"""
Contains the logic for randomly creating

"""

import re
from random import choice
from random import randint
from pathlib import Path

path = Path(__file__).parent.absolute()
male_path = str(path) + "/data/dist.male.first"
female_path = str(path) + "/data/dist.female.first"
surname_path = str(path) + "/data/dist.all.last"


def male_first_name():
    """
    Reads in the dat file containing male
    names, parses it, and returns a random
    male name.
    :return: A random male first name
    """
    male_names = []
    with open(male_path, 'r') as male:
        for x in male:
            res = ''.join(re.findall('[a-zA-Z]+', x))
            male_names.append(res)
        random_male = choice(male_names)
        return random_male.capitalize()


def female_first_name():
    """
    Reads in the dat file containing female
    names, parses it, and returns a random
    female name.
    :return: A random female first name
    """
    female_names = []
    with open(female_path, 'r') as female:
        for x in female:
            res = ''.join(re.findall('[a-zA-Z]+', x))
            female_names.append(res)
        random_female = choice(female_names)
        return random_female.capitalize()


def surname():
    """
    Reads in the dat file containing surnames,
    parses it, and returns a random surname.
    :return: A random surname
    """
    surnames = []
    with open(surname_path, 'r') as surname:
        for x in surname:
            res = ''.join(re.findall('[a-zA-Z]+', x))
            surnames.append(res)
        random_surname = choice(surnames)
        return random_surname.capitalize()


def generate_random_name():
    """
    Generate a random name
    :return: a random name, consisting of male or female first name and a surname
    """
    first_name = choice([male_first_name(), female_first_name()])
    return first_name + ' ' + surname()


def random_age(min=1, max=100):
    """
    Returns a random age from 1-100. :min: and
    :max: must be between 1-100 or a ValueError
    exception will be raised.
    :min: minimum age
    :max: maximum age
    :return: random int between min and max
    """
    if (min < 1) or (max > 100):
        raise ValueError('Enter in min greater than 0 and a max less than one hundred')
    else:
        return randint(a=min, b=max)


def random_email_service():
    """
    Returns a random email service
    :return: random email service
    """
    providers = ['aol', 'gmail', 'outlook', 'yahoo', 'icloud', 'yandex']
    return choice(providers)


def generate_random_phone_digit(includeZero=True):
    """
    :return: a random phone digit as int
    """
    minimum = 0 if includeZero else 1
    maximum = 9
    return randint(minimum, maximum)


def random_phone_number():
    """
    Returns a random phone number, 10 digits and 2 dashes
    :return: a random phone number as string
    """
    length = 12
    phone_number = ''
    for x in range(length):
        if x == 0:
            phone_number += str(generate_random_phone_digit(includeZero=False))
        elif x == 3 or x == 7:
            phone_number += '-'
        else:
            phone_number += str(generate_random_phone_digit())
    return phone_number


def create_occupation(age):
    """
    Returns an occupation.
    Persons under the age of 4 have 'NA' job, persons under 18 years are 'student's,
    all others will be given a random job.
    :return: an occupation as string
    """
    occupancies = ["cook", "actor", "programmer", "doctor", "dentist", "uber driver", "photographer", "astronaut"]
    if age < 0:
        raise ValueError('age cannot be below 0')
    elif age < 4:
        return 'NA'
    elif age < 18:
        return 'student'
    else:
        return choice(occupancies)


def create_person():
    sex = choice(['male', 'female'])
    first_name = male_first_name() if sex is 'male' else female_first_name()
    last_name = surname()
    email = first_name.lower() + '.' + last_name.lower() + '@' + random_email_service() + '.com'
    age = random_age()
    job = create_occupation(age)
    phone = random_phone_number()
    person = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'sex': sex,
        'age': age,
        'job': job,
        'phone': phone
    }
    return person


if __name__ == '__main__':
    person = create_person()
    print(person)
