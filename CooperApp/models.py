from django.db import models

# Create your models here.


class Agency():

    types = ["Government",
             "Multinational",
             "Commercial",
             "Educational",
             "Private",
             "Unknown", ]

    def __init__(self,
                 name,
                 abbrev,
                 countr_code,
                 type_type, ):
        self.name = name
        self.abbrev = abbrev
        self.countr_code = countr_code
        self.type = type_type


class Rocket():
    def __init__(self,
                 name,
                 configuration,
                 family_name,
                 agency,
                 image,):
        self.name = name
        self.configuration = configuration
        self.family_name = family_name
        self.agency = agency
        self.image = image 


class Mission():
    def __init__(self,
                 name,
                 description,
                 tipe,
                 type_name,
                 payload,
                 agency, ):
        self.name = name
        self.description = description
        self.agency = agency
        self.type = tipe
        self.type_name = type_name
        self.payload = payload


class RocketLaunch():
    status_types = ["Green",
                    "Red",
                    "Success",
                    "Failed", ]

    def __init__(self,
                 id_api,
                 agencies,
                 mission,
                 rocket,
                 date_start,
                 date_end,
                 location_name,
                 location_map,
                 status, ):
        self.id_api = id_api
        self.agencies = agencies
        self.mission = mission
        self.rocket = rocket
        self.date_start = date_start
        self.date_end = date_end
        self.location_name = location_name
        self.location_map = location_map
        self.status = status
