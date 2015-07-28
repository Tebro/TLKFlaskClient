__author__ = 'richard'
from .config import config
from .helpers import _url_request, _get_request, _parse_person_json, _parse_light_persons_list

def get_persons():
    persons = []
    persons_json = _get_request("persons")
    for person_json in persons_json:
        persons.append(_parse_person_json(person_json))

    return persons

def get_light_persons():
    return _parse_light_persons_list(_get_request("persons"))

def get_person(pk):
    return _parse_person_json(
        _url_request("%s%s" % (config['backend']['url'], "persons/%s/" % pk))
    )

def get_light_person(pk):
    person_json = _url_request("%s%s" % (config['backend']['url'], "persons/%s/" % pk))
    return {
        "firstname": person_json["firstname"],
        "lastname": person_json["lastname"],
        "email": person_json["email"],
        "pk": person_json["pk"],
        "url": person_json["url"]
    }