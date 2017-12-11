from os import system
import operator
from resin import Resin
resin = Resin()

def getBuildDetails(APP_ID, COMMIT):
    all_builds = resin.models.build.get_all_by_application(APP_ID)
    builds_on_Hash = {}
    for items in all_builds:
       builds_on_Hash[items["commit_hash"]] = items
    return builds_on_Hash[COMMIT]