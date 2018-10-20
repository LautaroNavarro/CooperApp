from django.db import models

# Create your models here.


class Agency():

    types = {"1": "Government",
             "2": "Multinational",
             "3": "Commercial",
             "4": "Educational",
             "5": "Private",
             "6": "Unknown", }

    def __init__(self,
                 name,
                 abbrev,
                 countr_code,
                 type, ):
        self.name
        self.abbrev
        self.countr_code
        self.type


class Rocket():
    def __init__(self,
                 name,
                 configuration,
                 family_name,
                 Agency,
                 image,):
        self.name
        self.configuration
        self.family_name
        self.Agency
        self.image


class Mission():
    def __init__(self,
                 name,
                 description,
                 type,
                 type_name,
                 payload,
                 agency, ):
        self.name
        self.description
        self.agency
        self.type
        self.type_name
        self.payload


class RocketLaunch():

    status_types = {"1": "Green",
                    "2": "Red",
                    "3": "Success",
                    "4": "Failed", }

    def __init__(self,
                 id_api,
                 agency,
                 mission,
                 rocket,
                 date_start,
                 date_end,
                 location_name,
                 location_map,
                 status, ):
        self.id_api
        self.mission
        self.rocket
        self.date_start
        self.date_end
        self.location_name
        self.location_map
        self.status
