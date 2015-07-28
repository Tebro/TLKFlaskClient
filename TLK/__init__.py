__author__ = 'richard'
import requests, yaml, os
from .config import config


#Helper functions
def tlk_get_request(endpoint):
    url, auth = get_url_and_auth()
    r = requests.get("%s%s/" % (url, endpoint), auth=auth)
    return r.json()

def tlk_url_request(url):
    _, auth = get_url_and_auth()
    r = requests.get(url, auth=auth)
    return r.json()

def get_person_merits(person):
    merits = []
    for merit in person["merits"]:
        merit_json = tlk_url_request(str(merit))
        merit_type_json = tlk_url_request(str(merit_json["type"]))
        merits.append(str(merit_type_json["name"]))

    return merits

def get_url_and_auth():
    return config['backend']['url'], config['backend']['auth']

def get_persons():
    persons = []
    persons_json = tlk_get_request("persons")
    for person_json in persons_json:
        person = {}
        person['url'] = str(person_json["url"])
        person['firstname'] = str(person_json["firstname"])
        person['lastname'] = str(person_json["lastname"])

        person['merits'] = get_person_merits(person_json)
        persons.append(person)

    return persons