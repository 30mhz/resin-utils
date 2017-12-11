from os import system
import operator
from resin import Resin
resin = Resin()

def get():
    applications = resin.models.application.get_all()
    return applications

def list():
    applications = get()
    applications_uuid = {}
    applications_names = {}
    for items in applications:
        applications_uuid[items["id"]] = items
        applications_names[items["app_name"]] = items["id"]
    applications_names = sorted(applications_names.items(), key=operator.itemgetter(0))
    return applications_uuid, applications_names
