__author__ = 'richard'
import requests, yaml, os
from .config import config


#Helper functions
def _get_request(endpoint):
    url, auth = get_url_and_auth()
    r = requests.get("%s%s/" % (url, endpoint), auth=auth)
    return r.json()

def _url_request(url):
    _, auth = get_url_and_auth()
    r = requests.get(url, auth=auth)
    return r.json()

def get_person_merits(person):
    merits = []
    for merit in person["merits"]:
        merit_json = _url_request(str(merit))
        merit_type_json = _url_request(str(merit_json["type"]))
        merit_obj = {
            "url": str(merit_json['url']),
            "year": str(merit_json['year']),
            'type': {
                "url": str(merit_type_json['url']),
                "name": str(merit_type_json['name'])
            }
        }
        merits.append(merit_obj)

    return merits

def get_url_and_auth():
    return config['backend']['url'], config['backend']['auth']

def get_persons():
    persons = []
    persons_json = _get_request("persons")
    for person_json in persons_json:
        person = {}
        person['url'] = str(person_json["url"])
        person['firstname'] = str(person_json["firstname"])
        person['lastname'] = str(person_json["lastname"])
        person['email'] = str(person_json['email'])
        person['merits'] = get_person_merits(person_json)
        persons.append(person)

    return persons

def get_person(id):
    person_json = _url_request(id)
    return {
        "url": person_json["url"],
        "firstname": person_json["firstname"],
        "lastname": person_json["lastname"],
        "email": person_json["email"],
    }