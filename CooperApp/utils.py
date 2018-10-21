import requests
import json
from dateutil import parser
from CooperApp.models import *
def get_api_launches(start_date, end_date):
    """
    this functions need the dates format in Y-M-D
    """
    response = requests.get(
        'https://launchlibrary.net/1.4/launch/{}/{}'.format(start_date, end_date)).json()
    rocket_launchs = []
    for i in range(len(response["launches"])):
        agencies = []
        for a in range(len(response["launches"][i]["rocket"]["agencies"])):
            typ = Agency.types[response["launches"]
                               [i]["rocket"]["agencies"][a]["type"]]
            agency = Agency(
                response["launches"][i]["rocket"]["agencies"][a]["name"],
                response["launches"][i]["rocket"]["agencies"][a]["abbrev"],
                response["launches"][i]["rocket"]["agencies"][a]["countryCode"],
                typ,
            )
            agencies.append(agency)
        if len(agencies) == 0:
            agencies = "Unknown"
        rocket = Rocket(
            response["launches"][i]["rocket"]["name"],
            response["launches"][i]["rocket"]["configuration"],
            response["launches"][i]["rocket"]["familyname"],
            agencies,
            response["launches"][i]["rocket"]["imageURL"],
        )
        missions = []
        for mission in range(len(response["launches"][i]["missions"])):
            payloads = []
            for x in range(len(response["launches"][i]["missions"][mission]["payloads"])):
                payloads.append(
                    response["launches"][i]["missions"][mission]["payloads"][x]["name"])
            mission_obj = Mission(
                response["launches"][i]["missions"][mission]["name"],
                response["launches"][i]["missions"][mission]["description"],
                response["launches"][i]["missions"][mission]["type"],
                response["launches"][i]["missions"][mission]["typeName"],
                payloads,
                "agency",
            )
            missions.append(mission_obj)
        status = RocketLaunch.status_types[response["launches"][i]["status"] - 1]
        try:
            loc_name = response["launches"][i]["location"]["pads"][0]["name"]
            loc_map = response["launches"][i]["location"]["pads"][0]["mapURL"]
            start = parser.parse(response["launches"][i]["windowstart"])
            end = parser.parse(response["launches"][i]["windowend"])
        except Exception as e:
            loc_name = None
            loc_map = None
        rocket_launch = RocketLaunch(
            response["launches"][i]["id"],
            agencies,
            missions,
            rocket,
            start,
            end,
            loc_name,
            loc_map,
            status,
            )
        rocket_launchs.append(rocket_launch)
    return rocket_launchs 