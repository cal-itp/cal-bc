from django.db import models
from django.utils.translation import gettext as _
from cal_bc.projects.models.model_version import ModelVersion


class Project(models.Model):
    class District(models.IntegerChoices):
        ONE = 1, _("District 1 - Eureka")
        TWO = 2, _("District 2 - Redding")
        THREE = 3, _("District 3 - Marysville / Sacramento")
        FOUR = 4, _("District 4 - Bay Area / Oakland")
        FIVE = 5, _("District 5 - Central Coast")
        SIX = 6, _("District 6 - Fresno / Bakersfield")
        SEVEN = 7, _("District 7 - Los Angeles / Ventura")
        EIGHT = 8, _("District 8 - San Bernardino / Riverside")
        NINE = 9, _("District 9 - Bishop")
        TEN = 10, _("District 10 - Stockton")
        ELEVEN = 11, _("District 11 - San Diego")
        TWELVE = 12, _("District 12 - Orange County")

    class HighwayCapacityType(models.TextChoices):
        GENERAL_HIGHWAY = "    General Highway", _("General Highway")
        HOV_LANE_ADDITION = "    HOV Lane Addition", _("HOV Lane Addition")
        HOT_LANE_ADDITION = "    HOT Lane Addition", _("HOT Lane Addition")
        PASSING_LANE = "    Passing Lane", _("Passing Lane")
        INTERSECTION = "    Intersection", _("Intersection")
        TRUCK_ONLY_LANE = "    Truck Only Lane", _("Truck Only Lane")
        BYPASS = "    Bypass", _("Bypass")
        QUEUING = "    Queuing", _("Queuing")
        PAVEMENT = "    Pavement", _("Pavement")

    class RailTransitCapacityType(models.TextChoices):
        PASSENGER_RAIL = "    Passenger Rail", _("Passenger Rail")
        LIGHT_RAIL = "    Light-Rail (LRT)", _("Light Rail (LRT)")
        HIGHWAY_RAIL_GRADE_CROSSING = (
            "    Highway-Rail Grade Crossing",
            _("Highway-Rail Grade Crossing"),
        )

    class HighwayOperationalType(models.TextChoices):
        AUXILIARY_LANE = "    Auxiliary Lane", _("Auxiliary Lane")
        FREEWAY_CONNECTOR = "    Freeway Connector", _("Freeway Connector")
        HOV_CONNECTOR = "    HOV Connector", _("HOV Connector")
        HOV_DROP_RAMP = "    HOV Drop Ramp", _("HOV Drop Ramp")
        OFF_RAMP_WIDENING = "    Off-Ramp Widening", _("Off-Ramp Widening")
        ON_RAMP_WIDENING = "    On-Ramp Widening", _("On-Ramp Widening")
        HOT_LANE_CONVERSION = "    Hot Lane Conversion", _("Hot Lane Conversion")

    class TransportationManagmentSystemsType(models.TextChoices):
        RAMP_METERING = "    Ramp Metering", _("Ramp Metering")
        RAMP_METERING_SIGNAL_COORDINATION = (
            "    Ramp Metering Signal Coordination",
            _("Ramp Metering Signal Coordination"),
        )
        INCIDENT_MANAGEMENT = "    Incident Management", _("Incident Management")
        TRAVELER_INFORMATION = "    Traveler Information", _("Traveler Information")
        ARTERIAL_SIGNAL_MANAGEMENT = (
            "    Arterial Signal Management",
            _("Arterial Signal Management"),
        )
        TRANSIT_VEHICLE_LOCATION = (
            "    Transit Vehicle Location (AVL)",
            _("Transit Vehicle Location (AVL)"),
        )
        TRANSIT_VEHICLE_SIGNAL_PRIORITY = (
            "    Transit Vehicle Signal Priority",
            _("Transit Vehicle Signal Priority"),
        )
        BUS_RAPID_TRANSIT = "    Bus Rapid Transit (BRT)", _("Bus Rapid Transit (BRT)")

    TYPE_CHOICES = {
        _("Highway Capacity Expansion"): HighwayCapacityType,
        _("Rail or Transit Capacity Expansion"): RailTransitCapacityType,
        _("Highway Operational Improvement"): HighwayOperationalType,
        _(
            "Transportation Management Systems (TMS)"
        ): TransportationManagmentSystemsType,
    }

    class Location(models.IntegerChoices):
        SO_CAL = 1, _("Southern California")
        NO_CAL = 2, _("Northern California")
        RURAL = 3, _("Rural")

    class DataDirection(models.IntegerChoices):
        ONE_WAY = 1, _("One-Way")
        TWO_WAY = 2, _("Two-Way")

    name = models.CharField()
    district = models.IntegerField(choices=District, null=True)
    type = models.CharField(choices=TYPE_CHOICES, null=True)
    location = models.IntegerField(choices=Location, null=True)
    construction_period_length = models.IntegerField(null=True)
    data_direction = models.IntegerField(
        choices=DataDirection, default=DataDirection.TWO_WAY
    )
    peak_periods_length = models.IntegerField(default=5)
    model_version = models.ForeignKey(
        ModelVersion, null=False, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
