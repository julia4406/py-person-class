class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons = []
    for human in people:
        person = Person(name=human["name"], age=human["age"])

        # set attributes "husband" and "wife" as string-value
        if human.get("wife"):
            person.wife = human["wife"]
        if human.get("husband"):
            person.husband = human.get("husband")
        persons.append(person)

    for person in persons:
        # set link on wife(husband) object
        if hasattr(person, "wife"):
            person.wife = person.people.get(person.wife)
        elif hasattr(person, "husband"):
            person.husband = person.people.get(person.husband)

    return persons
