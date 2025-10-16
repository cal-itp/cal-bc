from django.db import models
from django.utils.translation import gettext as _


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
        GENERAL_HIGHWAY = "general_highway", _("General Highway")
        HOV_LANE_ADDITION = "hov_lane_addition", _("HOV Lane Addition")
        HOT_LANE_ADDITION = "hot_lane_addition", _("HOT Lane Addition")
        PASSING_LANE = "passing_lane", _("Passing Lane")
        INTERSECTION = "intersection", _("Intersection")
        TRUCK_ONLY_LANE = "truck_only_lane", _("Truck Only Lane")
        BYPASS = "bypass", _("Bypass")
        QUEUING = "queuing", _("Queuing")
        PAVEMENT = "pavement", _("Pavement")

    class RailTransitCapacityType(models.TextChoices):
        PASSENGER_RAIL = "passenger_rail", _("Passenger Rail")
        LIGHT_RAIL = "light_rail", _("Light Rail (LRT)")
        HIGHWAY_RAIL_GRADE_CROSSING = (
            "highway_rail_grade_crossing",
            _("Highway-Rail Grade Crossing"),
        )

    class HighwayOperationalType(models.TextChoices):
        AUXILIARY_LANE = "auxiliary_lane", _("Auxiliary Lane")
        FREEWAY_CONNECTOR = "freeway_connector", _("Freeway Connector")
        HOV_CONNECTOR = "hov_connector", _("HOV Connector")
        HOV_DROP_RAMP = "hov_drop_ramp", _("HOV Drop Ramp")
        OFF_RAMP_WIDENING = "off_ramp_widening", _("Off-Ramp Widening")
        ON_RAMP_WIDENING = "on_ramp_widening", _("On-Ramp Widening")
        HOT_LANE_CONVERSION = "hot_lane_conversion", _("Hot Lane Conversion")

    class TransportationManagmentSystemsType(models.TextChoices):
        RAMP_METERING = "ramp_metering", _("Ramp Metering")
        RAMP_METERING_SIGNAL_COORDINATION = (
            "ramp_metering_signal_coordination",
            _("Ramp Metering Signal Coordination"),
        )
        INCIDENT_MANAGEMENT = "incident_management", _("Incident Management")
        TRAVELER_INFORMATION = "traveler_information", _("Traveler Information")
        ARTERIAL_SIGNAL_MANAGEMENT = (
            "arterial_signal_management",
            _("Arterial Signal Management"),
        )
        TRANSIT_VEHICLE_LOCATION = (
            "transit_vehicle_location",
            _("Transit Vehicle Location (AVL)"),
        )
        TRANSIT_VEHICLE_SIGNAL_PRIORITY = (
            "transit_vehicle_signal_priority",
            _("Transit Vehicle Signal Priority"),
        )
        BUS_RAPID_TRANSIT = "bus_rapid_transit", _("Bus Rapid Transit (BRT)")

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

    def __str__(self):
        return self.name
