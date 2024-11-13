class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        # when obj created add link on it to the dict "people"
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons = []
    for human in people:
        person = Person(name=human["name"], age=human["age"])
        persons.append(person)
        # temporary set attributes "husband" and "wife" if they exist
        if "wife" in human.keys() and human["wife"] is not None:
            person.wife = human["wife"]     # set name as string
        elif "husband" in human.keys() and human["husband"] is not None:
            person.husband = human["husband"]       # set name as string

    for person in persons:
        # set link on wife(husband) object
        # for each object "person" who has this attributes
        if hasattr(person, "wife"):
            person.wife = person.people.get(person.wife)
        elif hasattr(person, "husband"):
            person.husband = person.people.get(person.husband)

    return persons
