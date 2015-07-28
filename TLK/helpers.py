from .config import config
import requests


#Helper functions
def _get_request(endpoint):
    url, auth = _get_url_and_auth()
    r = requests.get("%s%s/" % (url, endpoint), auth=auth)
    return r.json()

def _url_request(url):
    _, auth = _get_url_and_auth()
    r = requests.get(url, auth=auth)
    return r.json()

def _get_url_and_auth():
    return config['backend']['url'], config['backend']['auth']

def _parse_person_json(person_json):
    members = _parse_person_nested_json(person_json['members'])
    boards = _parse_person_nested_json(person_json["boards"])
    committees = _parse_person_nested_json(person_json["committees"])
    officials = _parse_person_nested_json(person_json["officials"])
    merits = _parse_person_nested_json(person_json["merits"])
    return {
        "url": str(person_json["url"]),
        "pk": str(person_json["pk"]),
        "firstname": str(person_json["firstname"]),
        "lastname": str(person_json["lastname"]),
        "email": str(person_json["email"]),
        "members": members,
        "boards": boards,
        "committees": committees,
        "officials": officials,
        "merits": merits
    }

def _parse_person_nested_json(members_json):
    members = []
    for member_url in members_json:
        member_json = _url_request(member_url)
        member_type_json = _url_request(member_json["type"])
        members.append({
            "pk": str(member_json["pk"]),
            "year": str(member_json["year"]),
            "type": {
                "url": member_type_json["url"],
                "name": member_type_json["name"],
            }
        })

    return members

def _parse_light_persons_list(persons_json):
    persons = []
    for person_json in persons_json:
        persons.append({
            "pk": person_json['pk'],
            "firstname": person_json['firstname'],
            "lastname": person_json['lastname'],
            "url": person_json['url'],
            "email": person_json['email'],
        })

    return persons