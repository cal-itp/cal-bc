import ipywidgets as widgets
from ipywidgets import Widget
from ipywidgets import interactive
from IPython.display import display, Markdown
from parameters import parameters
params = parameters()

<<<<<<< HEAD
from widgets_helper import (highway_speed_and_volume_input_nobuild_title, highway_speed_and_volume_input_nobuild_subtitle, highway_speed_and_volume_input_info, highway_speed_and_volume_input_build_title, highway_speed_and_volume_input_build_subtitle
)

import projectinfo_widgets
project_inputs = projectinfo_widgets.create_project_info_widgets()

from widgets_helper import info_button_popup, create_section, create_section_with_subsections
=======
from widgets_helper import (highway_speed_and_volume_input_title, highway_speed_and_volume_input_subtitle, highway_speed_and_volume_input_info
)

import projectinfo_widgets 

from widgets_helper import info_button_popup, create_section
>>>>>>> 3ce506f0b22b27317d6525ffa8fe8b5e58771617

common_layout = widgets.Layout(
    width='450px', 
    background_color='#CCFFCC',  # Background color for all widgets
    padding='2px',
    border='2px solid gray'  # Border color and thickness
)


<<<<<<< HEAD
#Defining functions from Project Info for easy calculations
ProjLoc = projectinfo_widgets.projloc_widget.value
ProjType = projectinfo_widgets.subcategory_dropdown.value
Construct = projectinfo_widgets.construct_widget.value
NumDirections = projectinfo_widgets.one_two_way_widget.value
PeakLngthNB = projectinfo_widgets.peak_period_widget.value
RoadTypeNB = projectinfo_widgets.roadway_type_no_build_widget.value
RoadTypeB = projectinfo_widgets.roadway_type_build_widget.value
GenLanesNB = projectinfo_widgets.general_traffic_lanes_no_build_widget.value
GenLanesB = projectinfo_widgets.general_traffic_lanes_build_widget.value
HOVLanesNB = projectinfo_widgets.hov_hot_lanes_no_build_widget.value
HOVLanesB = projectinfo_widgets.hov_hot_lanes_build_widget.value
HOVRest = projectinfo_widgets.HOVRest_widget.value
Exclusive = projectinfo_widgets.Exclusive_widget.value
FFSpeedNB = projectinfo_widgets.free_flow_speed_no_build_widget.value
FFSpeedB = projectinfo_widgets.free_flow_speed_build_widget.value
RampFFSpdNB = projectinfo_widgets.ramp_design_speed_no_build_widget.value
RampFFSpdB = projectinfo_widgets.ramp_design_speed_build_widget.value
SegmentNB = projectinfo_widgets.highway_segment_no_build_widget.value
SegmentB = projectinfo_widgets.highway_segment_build_widget.value
ImpactedNB = projectinfo_widgets.impacted_length_no_build_widget.value
ImpactedB = projectinfo_widgets.impacted_length_build_widget.value
ADT0 = projectinfo_widgets.ADT_current_widget.value
ADT1NB = projectinfo_widgets.adt_base_year_no_build_widget.value
ADT1B = projectinfo_widgets.adt_base_year_build_widget.value
ADT20NB = projectinfo_widgets.ADT_20NB_widget.value
ADT20B = projectinfo_widgets.adt_20_year_build_widget.value
HOVvolNB = projectinfo_widgets.HOV_lane_nobuild_widget.value
HOVvolB = projectinfo_widgets.HOV_lane_build_widget.value
PerWeaveNB = projectinfo_widgets.percent_traffic_weave_no_build_widget.value
PerWeaveB = projectinfo_widgets.percent_traffic_weave_build_widget.value
PerIndHOV = projectinfo_widgets.percent_induced_trip_widget.value
PerTruckNB = projectinfo_widgets.percent_trucks_nobuild_widget.value
PerTruckB = projectinfo_widgets.percent_trucks_build_widget.value
TruckSpeed = projectinfo_widgets.truck_speed_widget.value
RampVolP = projectinfo_widgets.hourly_ramp_volume_peak_widget.value
RampVolNP = projectinfo_widgets.hourly_ramp_volume_nonpeak_widget.value
MeterStrat = projectinfo_widgets.metering_strategy_widget.value
ArrRate1 = projectinfo_widgets.arrival_rate_base_year_no_build_widget.value
ArrRate20 = projectinfo_widgets.arrival_rate_base_year_build_widget.value
DepRate1 = projectinfo_widgets.departure_rate_forecast_year_no_build_widget.value
DepRate20 = projectinfo_widgets.departure_rate_forecast_year_build_widget.value
IRI1NB = projectinfo_widgets.iri_base_year_no_build_widget.value
IRI1B = projectinfo_widgets.iri_base_year_build_widget.value
IRI20NB = projectinfo_widgets.iri_forecast_year_no_build_widget.value
IRI20B = projectinfo_widgets.iri_forecast_year_build_widget.value
AVONonNB = projectinfo_widgets.AVO_traffic_NP_no_build_widget.value
AVONonB = projectinfo_widgets.AVO_traffic_NP_build_widget.value
AVOPeakNB = projectinfo_widgets.AVO_traffic_P_no_build_widget.value
AVOPeakB = projectinfo_widgets.AVO_traffic_P_build_widget.value
AVOHovNB = projectinfo_widgets.AVOHovNB_widget.value
AVOHovB = projectinfo_widgets.AVOHovB_widget.value
GateTime1 = projectinfo_widgets.GateTime1_widget.value
GateTime20 = projectinfo_widgets.GateTime20_widget.value
NumTrain1 = projectinfo_widgets.NumTrain1_widget.value
NumTrain20 = projectinfo_widgets.NumTrain20_widget.value
TPerPeak = projectinfo_widgets.TPerPeak_widget.value
TPerHwy = projectinfo_widgets.TPerHwy_widget.value
TAPT1B = projectinfo_widgets.TAPT1B_widget.value
TAPT1NB = projectinfo_widgets.TAPT1NB_widget.value
TAPT20NB =  projectinfo_widgets.TAPT20NB_widget.value
TAPT20B = projectinfo_widgets.TAPT20B_widget.value
PerPeakADT = params.per_peak_adt
TMSLookup = params.TMSLookup
TMSAdj = params.tms_adj
roadway_capacity = params.roadway_capacity
roadway_capacity_non_HOV = params.roadway_capacity_non_HOV
MaxVC = params.MaxVC
AnnualFactor = params.AnnualFactor
SpeedWeaveAdj = params.SpeedWeaveAdj 
SpeedPavAdj = params.SpeedPavAdj
IdleSpeed = params.IdleSpeed




def create_new_widgets():
    
    
##################################################################################  No Build Scenario ##################################################################################
################################################## Year 1 ##################################################
############################### Peak Period ###############################

    # Create the HOV Volume widget to display the calculated value
    HOV_Vol_year1peak_nobuild_modelcalc_widget = widgets.IntText(
        value=0,
        description="HOV Volume(Calculated by Model):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Create the HOV Volume Peak Period widget for user-modified value
    HOV_Vol_year1peak_nobuild_userchanged_widget = widgets.Text(
        value='',
        description="HOV Volume (Changed by User):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Create the PHV1NB widget based on the formula
    PHV1NB_widget = widgets.IntText(
        value=HOV_Vol_year1peak_nobuild_modelcalc_widget.value,
        description="HOV Volume (Used for Proj Evaluation):",
        disabled=True,
=======

def create_new_widgets():
    #HOV Volume 
    def update_HOV_Volume(change):
        # Access the necessary widget values from projectinfo_widgets
        HOVvolNB = projectinfo_widgets.HOV_lane_nobuild_widget.value
        PeakLngthNB = projectinfo_widgets.peak_period_widget.value
        PerWeaveNB = projectinfo_widgets.percent_traffic_weave_no_build_widget.value
        subcategory_value = projectinfo_widgets.subcategory_dropdown.value

        # Formula for HOV volume model calculated widget
        if subcategory_value == "Hwy-Rail Grade Crossing":
            HOV_Volume_Peak_Model = 0
        else:
            # Check for HOVConn (HOV Connector) or HOVDrop (HOV Drop Ramp)
            if subcategory_value == "HOV Connector" or subcategory_value == "HOV Drop Ramp":
                HOV_Volume_Peak_Model = HOVvolNB * PeakLngthNB * (1 - PerWeaveNB)
            else:
                HOV_Volume_Peak_Model = HOVvolNB * PeakLngthNB  # Default case if no HOVConn or HOVDrop
        
        # Update the HOV Volume Peak Period widget dynamically
        HOV_Vol_peak_modelcalc_widget.value = round(HOV_Volume_Peak_Model, 0)

    # Create the HOV Volume widget to display the calculated value
    HOV_Vol_peak_modelcalc_widget = widgets.IntText(
        value=0,  # Set initial value to 0, or any other valid integer
        description="HOV Volume Peak Period (Calculated by Model):",
        disabled=True,  # Allow the user to modify the value
        layout=common_layout,  
        style={'description_width': 'initial'}
    )
    
    # Create the HOV Volume Peak Period widget for user-modified value
    HOV_Vol_peak_userchanged_widget = widgets.IntText(
        value=0,  # Initially set to 0 or a valid integer value
        description="HOV Volume Peak Period (Changed by User):",
        disabled=False,  
        layout=common_layout,  
        style={'description_width': 'initial'}
    )

    # Attach observers to the relevant widgets to update the HOV Volume widget dynamically
    projectinfo_widgets.subcategory_dropdown.observe(update_HOV_Volume, names='value')
    projectinfo_widgets.HOV_lane_nobuild_widget.observe(update_HOV_Volume, names='value')
    projectinfo_widgets.peak_period_widget.observe(update_HOV_Volume, names='value')
    projectinfo_widgets.percent_traffic_weave_no_build_widget.observe(update_HOV_Volume, names='value')


    # Create the PHV1NB widget based on the formula
    def calculate_phv1nb(change):
        # Access the user-modified value directly from the widget
        if isinstance(HOV_Vol_peak_userchanged_widget.value, (int, float)) and HOV_Vol_peak_userchanged_widget.value >= 0:
            PHV1NB = HOV_Vol_peak_userchanged_widget.value  # Use the user-modified value if valid
        else:
            PHV1NB = HOV_Vol_peak_modelcalc_widget.value  # Use the model value if the user value is invalid

        # Update the value of PHV1NB widget
        PHV1NB_widget.value = PHV1NB

    # Create the PHV1NB widget to display the result
    PHV1NB_widget = widgets.IntText(
        value=HOV_Vol_peak_modelcalc_widget.value,  # Set initially to the calculated value
        description="HOV Volume (Used for Proj Evaluation):",
        disabled=True,  # Make it read-only 
>>>>>>> 3ce506f0b22b27317d6525ffa8fe8b5e58771617
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    PHV1NB_explaination_widget = widgets.Text(
<<<<<<< HEAD
        value=None,
        description="Reasons for Change:",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Function to update HOV Volume dynamically
    def update_HOV_Year1Peak_nobuild_Volume(change):
        if ProjType == "Hwy-Rail Grade Crossing":
            HOV_Volume_Year1Peak_nobuild_Model = 0
        else:
            if ProjType == "HOV Connector" or ProjType == "HOV Drop Ramp":
                HOV_Volume_Year1Peak_nobuild_Model = HOVvolNB * PeakLngthNB * (1 - PerWeaveNB)
            else:
                HOV_Volume_Year1Peak_nobuild_Model = HOVvolNB * PeakLngthNB

        HOV_Vol_year1peak_nobuild_modelcalc_widget.value = round(HOV_Volume_Year1Peak_nobuild_Model, 0)

    # Function to calculate PHV1NB
    def calculate_phv1nb(change):
        try:
            val = float(HOV_Vol_year1peak_nobuild_userchanged_widget.value)
            if val >= 0:
                PHV1NB = val
            else:
                PHV1NB = HOV_Vol_year1peak_nobuild_modelcalc_widget.value
        except:
            PHV1NB = HOV_Vol_year1peak_nobuild_modelcalc_widget.value

        PHV1NB_widget.value = PHV1NB

    # Link the PHV1NB widget update to changes in user-modified value
    HOV_Vol_year1peak_nobuild_userchanged_widget.observe(calculate_phv1nb, names='value')

    # Combine all widgets into a horizontal layout
    HOV_vol_year1peak_nobuild_widgets = widgets.HBox([
        HOV_Vol_year1peak_nobuild_modelcalc_widget,
        HOV_Vol_year1peak_nobuild_userchanged_widget,
        PHV1NB_explaination_widget
    ])

    # Attach observers to update dynamically
    projectinfo_widgets.subcategory_dropdown.observe(update_HOV_Year1Peak_nobuild_Volume, names='value')
    projectinfo_widgets.HOV_lane_nobuild_widget.observe(update_HOV_Year1Peak_nobuild_Volume, names='value')
    projectinfo_widgets.peak_period_widget.observe(update_HOV_Year1Peak_nobuild_Volume, names='value')
    projectinfo_widgets.percent_traffic_weave_no_build_widget.observe(update_HOV_Year1Peak_nobuild_Volume, names='value')
    HOV_Vol_year1peak_nobuild_modelcalc_widget.observe(calculate_phv1nb, names='value')
    HOV_Vol_year1peak_nobuild_userchanged_widget.observe(calculate_phv1nb, names='value')

    
    ###################################################################    
 
  
    # Create the Non-HOV Volume widget to display the calculated value
    Non_HOV_Vol_year1peak_nobuild_modelcalc_widget = widgets.IntText(
        value=0,
        description="Non-HOV Volume (Calculated by Model):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Create the Non-HOV Volume Peak Period widget for user-modified value
    Non_HOV_Vol_year1peak_nobuild_userchanged_widget = widgets.Text(
        value='',
        description="Non-HOV Volume (Changed by User):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    PNV1NB_widget = widgets.IntText(
        value=Non_HOV_Vol_year1peak_nobuild_modelcalc_widget.value,
        description="Non-HOV Volume (Used for Proj Evaluation):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    PNV1NB_explanation_widget = widgets.Text(
        value=None,
        description="Reasons for Change:",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Non-HOV Volume Widget update function
    def update_Non_HOV_Year1Peak_nobuild_Volume(change):
        if ProjType == "Hwy-Rail Grade Crossing":
            Non_HOV_Volume_Year1Peak_nobuild_Model = 0
        else:
            if ProjType in ["Auxiliary Lane", "Off-Ramp Widening"]:
                traffic_factor = PerWeaveNB
            else:
                traffic_factor = PerTruckNB

            TMS_value = TMSAdj.get(TMSLookup, {}).get("VolumeWithout", 1)

            Non_HOV_Volume_Year1Peak_nobuild_Model = (
                (PerPeakADT * ADT1NB) * (1 - traffic_factor) * TMS_value - HOVvolNB * PeakLngthNB
            )

        Non_HOV_Vol_year1peak_nobuild_modelcalc_widget.value = round(Non_HOV_Volume_Year1Peak_nobuild_Model, 0)

    # Attach observers to update dynamically
    projectinfo_widgets.adt_base_year_no_build_widget.observe(update_Non_HOV_Year1Peak_nobuild_Volume, names='value')
    projectinfo_widgets.percent_traffic_weave_no_build_widget.observe(update_Non_HOV_Year1Peak_nobuild_Volume, names='value')
    projectinfo_widgets.percent_trucks_nobuild_widget.observe(update_Non_HOV_Year1Peak_nobuild_Volume, names='value')
    projectinfo_widgets.HOV_lane_nobuild_widget.observe(update_Non_HOV_Year1Peak_nobuild_Volume, names='value')
    projectinfo_widgets.peak_period_widget.observe(update_Non_HOV_Year1Peak_nobuild_Volume, names='value')
    projectinfo_widgets.subcategory_dropdown.observe(update_Non_HOV_Year1Peak_nobuild_Volume, names='value')

    # Update PNV1NB when user changes the input
    def calculate_pnv1nb(change):
        try:
            val = float(Non_HOV_Vol_year1peak_nobuild_userchanged_widget.value)
            if val >= 0:
                PNV1NB = val
            else:
                PNV1NB = Non_HOV_Vol_year1peak_nobuild_modelcalc_widget.value
        except:
            PNV1NB = Non_HOV_Vol_year1peak_nobuild_modelcalc_widget.value

        PNV1NB_widget.value = PNV1NB

    Non_HOV_Vol_year1peak_nobuild_userchanged_widget.observe(calculate_pnv1nb, names='value')

    # Combine for layout
    Non_HOV_vol_year1peak_nobuild_widgets = widgets.HBox([
        Non_HOV_Vol_year1peak_nobuild_modelcalc_widget,
        Non_HOV_Vol_year1peak_nobuild_userchanged_widget,
        PNV1NB_explanation_widget
    ])
     
    
    ###################################################################    
    # Weaving Volume (Calculated by Model)
    weaving_volume_year1peak_nobuild_modelcalc_widget = widgets.IntText(
        value=0,
        description="Weaving Volume (Calculated by Model):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Weaving Volume (User-modified value)
    weaving_volume_year1peak_nobuild_userchanged_widget = widgets.Text(
        value='',
        description="Weaving Volume (Changed by User):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Weaving Volume (Used for Project Evaluation)
    PWV1NB_widget = widgets.IntText(
        value=weaving_volume_year1peak_nobuild_modelcalc_widget.value,
        description="Weaving Volume (Used for Proj Evaluation):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Explanation widget for user-modified values
    PWV1NB_explanation_widget = widgets.Text(
        value=None,
        description="Reasons for Change:",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Update Weaving Volume Calculation
    def update_weaving_year1peak_nobuild_volume(change):
        if TMSLookup in TMSAdj:
            TMS_value = TMSAdj[TMSLookup]["VolumeWithout"]
        else:
            TMS_value = 1

        Weaving_Volume_Model = 0

        if ProjType in ["Auxiliary Lane", "Off-Ramp Widening"]:
            Weaving_Volume_Model += (PerPeakADT * ADT1NB) * (PerWeaveNB - PerTruckNB) * TMS_value

        if ProjType == "Auxiliary Lane":
            Weaving_Volume_Model += RampVolP * PeakLngthNB

        if ProjType in ["HOV Connector", "HOV Drop Ramp"]:
            Weaving_Volume_Model += PerWeaveNB * HOVvolNB * PeakLngthNB

        weaving_volume_year1peak_nobuild_modelcalc_widget.value = round(Weaving_Volume_Model, 0)

    # Observers
    projectinfo_widgets.adt_base_year_no_build_widget.observe(update_weaving_year1peak_nobuild_volume, names='value')
    projectinfo_widgets.percent_traffic_weave_no_build_widget.observe(update_weaving_year1peak_nobuild_volume, names='value')
    projectinfo_widgets.percent_trucks_nobuild_widget.observe(update_weaving_year1peak_nobuild_volume, names='value')
    projectinfo_widgets.hourly_ramp_volume_peak_widget.observe(update_weaving_year1peak_nobuild_volume, names='value')
    projectinfo_widgets.peak_period_widget.observe(update_weaving_year1peak_nobuild_volume, names='value')
    projectinfo_widgets.HOV_lane_nobuild_widget.observe(update_weaving_year1peak_nobuild_volume, names='value')
    projectinfo_widgets.subcategory_dropdown.observe(update_weaving_year1peak_nobuild_volume, names='value')

    # Update PWV1NB when user modifies input
    def calculate_pwv1nb(change):
        try:
            val = float(weaving_volume_year1peak_nobuild_userchanged_widget.value)
            if val >= 0:
                PWV1NB = val
            else:
                PWV1NB = weaving_volume_year1peak_nobuild_modelcalc_widget.value
        except:
            PWV1NB = weaving_volume_year1peak_nobuild_modelcalc_widget.value

        PWV1NB_widget.value = PWV1NB

    weaving_volume_year1peak_nobuild_userchanged_widget.observe(calculate_pwv1nb, names='value')

    # Display layout
    Weaving_Volume_year1peak_nobuild_widgets = widgets.HBox([
        weaving_volume_year1peak_nobuild_modelcalc_widget,
        weaving_volume_year1peak_nobuild_userchanged_widget,
        PWV1NB_explanation_widget
    ])

    
    ###################################################################    
    # Truck Volume (Calculated by Model)
    truck_volume_year1peak_nobuild_modelcalc_widget = widgets.IntText(
        value=0,
        description="Truck Volume (Calculated by Model):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Truck Volume (User-modified value)
    truck_volume_year1peak_nobuild_userchanged_widget = widgets.Text(
        value='',
        description="Truck Volume (Changed by User):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Truck Volume (Used for Project Evaluation)
    PTV1NB_widget = widgets.IntText(
        value=truck_volume_year1peak_nobuild_modelcalc_widget.value,
        description="Truck Volume (Used for Proj Evaluation):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Explanation widget for user-modified values
    PTV1NB_explanation_widget = widgets.Text(
        value=None,
        description="Reasons for Change:",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Update Truck Volume Calculation based on widget values
    def update_truck_volume_year1peak_nobuild(change):
        if TMSLookup in TMSAdj:
            TMS_value = TMSAdj[TMSLookup]["VolumeWithout"]
        else:
            TMS_value = 1

        if ProjType == "Hwy-Rail Grade Crossing":
            Truck_Volume_Model = 0
        else:
            Truck_Volume_Model = (PerPeakADT * ADT1NB) * PerTruckNB * TMS_value

        truck_volume_year1peak_nobuild_modelcalc_widget.value = round(Truck_Volume_Model, 0)

    # Observers for calculation
    projectinfo_widgets.adt_base_year_no_build_widget.observe(update_truck_volume_year1peak_nobuild, names='value')
    projectinfo_widgets.percent_trucks_nobuild_widget.observe(update_truck_volume_year1peak_nobuild, names='value')
    projectinfo_widgets.subcategory_dropdown.observe(update_truck_volume_year1peak_nobuild, names='value')

    # Update PTV1NB when user modifies the input
    def calculate_ptv1nb(change):
        try:
            val = float(truck_volume_year1peak_nobuild_userchanged_widget.value)
            if val >= 0:
                PTV1NB = val
            else:
                PTV1NB = truck_volume_year1peak_nobuild_modelcalc_widget.value
        except:
            PTV1NB = truck_volume_year1peak_nobuild_modelcalc_widget.value

        PTV1NB_widget.value = PTV1NB

    truck_volume_year1peak_nobuild_userchanged_widget.observe(calculate_ptv1nb, names='value')

    # Layout for display
    Truck_Volume_year1peak_nobuild_widgets = widgets.HBox([
        truck_volume_year1peak_nobuild_modelcalc_widget,
        truck_volume_year1peak_nobuild_userchanged_widget,
        PTV1NB_explanation_widget
    ])

    
    ###################################################################     
    # Non-HOV Speed widgets 
    nonhov_speed_year1peak_nobuild_modelcalc_widget = widgets.IntText(
        value=0,
        description="Non-HOV Speed (Calculated by Model):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    nonhov_speed_year1peak_nobuild_userchanged_widget = widgets.Text(
        value='',
        description="Non-HOV Speed (Changed by User):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    PNS1NB_widget = widgets.IntText(
        value=nonhov_speed_year1peak_nobuild_modelcalc_widget.value,
        description="Non-HOV Speed (Used for Proj Evaluation):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    PNS1NB_explanation_widget = widgets.Text(
        value=None,
        description="Reasons for Change:",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    def update_nonhov_speed_year1peak_nobuild(change=None):
        traffic_volumes = [
            PHV1NB_widget.value,
            PNV1NB_widget.value,
            PWV1NB_widget.value,
            PTV1NB_widget.value
        ]

        sum_all = sum(traffic_volumes)
        sum_hov_zero = sum_all
        sum_hov_nonzero = sum(traffic_volumes[1:])

        if sum_all == 0:
            nonhov_speed = 55
        else:
            if ProjType == "Queuing":
                try:
                    part1 = (
                        PeakLngthNB / DepRate1 / 2
                        * (ArrRate1 - DepRate1)
                        * (DepRate1 - ADT1NB * (1 - PerPeakADT) / (24 - PeakLngthNB))
                        / (ArrRate1 - ADT1NB * (1 - PerPeakADT) / (24 - PeakLngthNB))
                    )
                except ZeroDivisionError:
                    part1 = float("inf")

                nonhov_speed = ImpactedNB / (max(part1, 0) + ImpactedNB / FFSpeedNB)
            else:
                flow_sum = sum_hov_nonzero if HOVLanesNB != 0 else sum_hov_zero

                capacity_params = roadway_capacity_non_HOV["Non-HOV Lanes"]["No Build"]
                GenAlphaNB = capacity_params["GenAlphaNB"]
                GenBetaNB = capacity_params["GenBetaNB"]
                GenLaneCapNB = capacity_params["GenLaneCapNB"]

                volume_term = flow_sum / (GenLanesNB * GenLaneCapNB * PeakLngthNB)
                delay_speed = FFSpeedNB / (IRI1NB * (1 + GenAlphaNB * min(volume_term, MaxVC) ** GenBetaNB))
                base_speed = delay_speed * TMSAdj[TMSLookup][1]

                if ProjType == "Passing":
                    nonhov_speed = (TruckSpeed + FFSpeedNB) / 2
                else:
                    nonhov_speed = min(base_speed, FFSpeedNB)

        if ProjType == "Freeway Connector":
            nonhov_speed *= SpeedWeaveAdj.get(PerWeaveNB, {"Freeway": 1.0})["Freeway"]

        if ProjType in ["HOV Connector", "HOV Drop Ramp"]:
            nonhov_speed *= SpeedWeaveAdj.get(PerWeaveNB, {"HOV": 1.0})["HOV"]

        closest_iri_key = min(SpeedPavAdj.keys(), key=lambda x: abs(x - IRI1NB))
        nonhov_speed *= SpeedPavAdj[closest_iri_key]["Auto"]

        nonhov_speed_year1peak_nobuild_modelcalc_widget.value = round(nonhov_speed, 1)

    update_nonhov_speed_year1peak_nobuild()

    PHV1NB_widget.observe(update_nonhov_speed_year1peak_nobuild, names='value')
    PNV1NB_widget.observe(update_nonhov_speed_year1peak_nobuild, names='value')
    PWV1NB_widget.observe(update_nonhov_speed_year1peak_nobuild, names='value')
    PTV1NB_widget.observe(update_nonhov_speed_year1peak_nobuild, names='value')
    projectinfo_widgets.subcategory_dropdown.observe(update_nonhov_speed_year1peak_nobuild, names='value')
    projectinfo_widgets.peak_period_widget.observe(update_nonhov_speed_year1peak_nobuild, names='value')
    projectinfo_widgets.departure_rate_forecast_year_no_build_widget.observe(update_nonhov_speed_year1peak_nobuild, names='value')
    projectinfo_widgets.arrival_rate_base_year_no_build_widget.observe(update_nonhov_speed_year1peak_nobuild, names='value')
    projectinfo_widgets.adt_base_year_no_build_widget.observe(update_nonhov_speed_year1peak_nobuild, names='value')
    projectinfo_widgets.free_flow_speed_no_build_widget.observe(update_nonhov_speed_year1peak_nobuild, names='value')
    projectinfo_widgets.impacted_length_no_build_widget.observe(update_nonhov_speed_year1peak_nobuild, names='value')
    projectinfo_widgets.general_traffic_lanes_no_build_widget.observe(update_nonhov_speed_year1peak_nobuild, names='value')
    projectinfo_widgets.hov_hot_lanes_no_build_widget.observe(update_nonhov_speed_year1peak_nobuild, names='value')
    projectinfo_widgets.percent_traffic_weave_no_build_widget.observe(update_nonhov_speed_year1peak_nobuild, names='value')
    projectinfo_widgets.iri_base_year_no_build_widget.observe(update_nonhov_speed_year1peak_nobuild, names='value')
    projectinfo_widgets.truck_speed_widget.observe(update_nonhov_speed_year1peak_nobuild, names='value')

    def calculate_pns1nb(change):
        try:
            val = float(nonhov_speed_year1peak_nobuild_userchanged_widget.value)
            updated_speed = max(val, 5)
        except:
            updated_speed = max(nonhov_speed_year1peak_nobuild_modelcalc_widget.value, 5)

        PNS1NB_widget.value = updated_speed

    nonhov_speed_year1peak_nobuild_userchanged_widget.observe(calculate_pns1nb, names='value')

    NonHOV_speed_year1peak_nobuild_widgets = widgets.HBox([
        nonhov_speed_year1peak_nobuild_modelcalc_widget,
        nonhov_speed_year1peak_nobuild_userchanged_widget,
        PNS1NB_explanation_widget
    ])


    ###################################################################     
    # HOV Speed widgets 
    hov_speed_year1peak_nobuild_modelcalc_widget = widgets.IntText(
        value=0,
        description="HOV Speed (Calculated by Model):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    hov_speed_year1peak_nobuild_userchanged_widget = widgets.Text(
        value='',
        description="HOV Speed (Changed by User):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    PHS1NB_widget = widgets.IntText(
        value=hov_speed_year1peak_nobuild_modelcalc_widget.value,
        description="HOV Speed (Used for Proj Evaluation):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    PHS1NB_explanation_widget = widgets.Text(
        value=None,
        description="Reasons for Change:",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    def update_hov_speed_year1peak_nobuild(change=None):
        hov_capacity_params = roadway_capacity["HOV Lanes"]
        HOVAlpha = hov_capacity_params["HOVAlpha"]
        HOVBeta = hov_capacity_params["HOVBeta"]
        HOVLaneCap = hov_capacity_params["HOVLaneCap"]

        PHV1NB = PHV1NB_widget.value

        if PHV1NB == 0:
            hov_speed = 55

        elif HOVLanesNB == 0:
            hov_speed = PNS1NB_widget.value

        elif ProjType == "Queuing":
            try:
                queue_denom = (
                    PeakLngthNB / DepRate1 / 2
                    * (ArrRate1 - DepRate1)
                    * (DepRate1 - ADT1NB * (1 - PerPeakADT) / (24 - PeakLngthNB))
                    / (ArrRate1 - ADT1NB * (1 - PerPeakADT) / (24 - PeakLngthNB))
                )
            except ZeroDivisionError:
                queue_denom = float("inf")

            hov_speed = ImpactedNB / (max(queue_denom, 0) + ImpactedNB / FFSpeedNB)

        else:
            try:
                volume_term = PHV1NB / (HOVLanesNB * HOVLaneCap * PeakLngthNB)
                delay_speed = FFSpeedNB / (1 + HOVAlpha * min(volume_term, MaxVC) ** HOVBeta)
            except ZeroDivisionError:
                delay_speed = 0

            closest_iri_key = min(SpeedPavAdj.keys(), key=lambda x: abs(x - IRI1NB))
            pavement_adj = SpeedPavAdj[closest_iri_key]["Auto"]

            hov_speed = delay_speed * pavement_adj

        hov_speed_year1peak_nobuild_modelcalc_widget.value = round(hov_speed, 1)

    update_hov_speed_year1peak_nobuild()

    # Adding Observers
    PHV1NB_widget.observe(update_hov_speed_year1peak_nobuild, names='value')
    PNS1NB_widget.observe(update_hov_speed_year1peak_nobuild, names='value')
    projectinfo_widgets.subcategory_dropdown.observe(update_hov_speed_year1peak_nobuild, names='value')
    projectinfo_widgets.impacted_length_no_build_widget.observe(update_hov_speed_year1peak_nobuild, names='value')
    projectinfo_widgets.peak_period_widget.observe(update_hov_speed_year1peak_nobuild, names='value')
    projectinfo_widgets.departure_rate_forecast_year_no_build_widget.observe(update_hov_speed_year1peak_nobuild, names='value')
    projectinfo_widgets.arrival_rate_base_year_no_build_widget.observe(update_hov_speed_year1peak_nobuild, names='value')
    projectinfo_widgets.adt_base_year_no_build_widget.observe(update_hov_speed_year1peak_nobuild, names='value')
    projectinfo_widgets.percent_induced_trip_widget.observe(update_hov_speed_year1peak_nobuild, names='value')
    projectinfo_widgets.hov_hot_lanes_no_build_widget.observe(update_hov_speed_year1peak_nobuild, names='value')
    projectinfo_widgets.free_flow_speed_no_build_widget.observe(update_hov_speed_year1peak_nobuild, names='value')
    projectinfo_widgets.iri_base_year_no_build_widget.observe(update_hov_speed_year1peak_nobuild, names='value')

    def calculate_phs1nb(change):
        try:
            val = float(hov_speed_year1peak_nobuild_userchanged_widget.value)
            updated_HOV_speed = max(val, 5)
        except:
            updated_HOV_speed = max(hov_speed_year1peak_nobuild_modelcalc_widget.value, 5)

        PHS1NB_widget.value = updated_HOV_speed

    hov_speed_year1peak_nobuild_userchanged_widget.observe(calculate_phs1nb, names='value')

    HOV_Speed_year1peak_nobuild_widgets = widgets.HBox([
        hov_speed_year1peak_nobuild_modelcalc_widget,
        hov_speed_year1peak_nobuild_userchanged_widget,
        PHS1NB_explanation_widget
    ])


    ###################################################################    
    # Weaving Speed widgets 
    weave_speed_year1peak_nobuild_modelcalc_widget = widgets.IntText(
        value=0,
        description="Weaving Speed (Calculated by Model):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    weave_speed_year1peak_nobuild_userchanged_widget = widgets.Text(
        value='',
        description="Weaving Speed (Changed by User):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    PWS1NB_widget = widgets.IntText(
        value=weave_speed_year1peak_nobuild_modelcalc_widget.value,
        description="Weaving Speed (Used for Proj Evaluation):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    PWS1NB_explanation_widget = widgets.Text(
        value=None,
        description="Reasons for Change:",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    def update_weaving_speed_year1peak_nobuild(change=None):
        PWV1NB = PWV1NB_widget.value
        PNS1NB = PNS1NB_widget.value
        PTV1NB = PTV1NB_widget.value
        Pavement = ProjType == "Pavement"

        if PWV1NB == 0:
            weaving_speed = 55
        else:
            if ProjType in ["Auxiliary Lane", "Off-Ramp Widening"]:
                try:
                    base_speed = 1.1 * (
                        FFSpeedNB - (FFSpeedNB - 42) * (
                            0.321 +
                            0.0039 * exp((PWV1NB + PTV1NB) / NumDirections / PeakLngthNB / 1000) -
                            0.002 * (
                                1083 if ProjType == "Off-Ramp Widening" else SegmentNB * 5280
                            ) * RampFFSpdNB / 1000
                        )
                    )

                    tms_factor = TMSAdj.get(TMSLookup, 1)

                    pavement_factor = SpeedPavAdj[
                        max([k for k in sorted(SpeedPavAdj.keys()) if k <= IRI1NB], default=0)
                    ]["Auto"] if Pavement else 1

                    weaving_speed = max(5, min(PNS1NB, base_speed) * tms_factor * pavement_factor)

                except ZeroDivisionError:
                    print("Error calculating weaving speed due to division by zero.")
                    weaving_speed = 55
                except Exception as e:
                    print(f"Error calculating weaving speed: {e}")
                    weaving_speed = 55
            else:
                weaving_speed = PNS1NB

        weave_speed_year1peak_nobuild_modelcalc_widget.value = round(weaving_speed, 1)

    update_weaving_speed_year1peak_nobuild()

    # Observers
    PWV1NB_widget.observe(update_weaving_speed_year1peak_nobuild, names='value')
    PNS1NB_widget.observe(update_weaving_speed_year1peak_nobuild, names='value')
    PTV1NB_widget.observe(update_weaving_speed_year1peak_nobuild, names='value')
    projectinfo_widgets.subcategory_dropdown.observe(update_weaving_speed_year1peak_nobuild, names='value')
    projectinfo_widgets.impacted_length_no_build_widget.observe(update_weaving_speed_year1peak_nobuild, names='value')
    projectinfo_widgets.peak_period_widget.observe(update_weaving_speed_year1peak_nobuild, names='value')
    projectinfo_widgets.departure_rate_forecast_year_no_build_widget.observe(update_weaving_speed_year1peak_nobuild, names='value')
    projectinfo_widgets.arrival_rate_base_year_no_build_widget.observe(update_weaving_speed_year1peak_nobuild, names='value')
    projectinfo_widgets.adt_base_year_no_build_widget.observe(update_weaving_speed_year1peak_nobuild, names='value')
    projectinfo_widgets.percent_induced_trip_widget.observe(update_weaving_speed_year1peak_nobuild, names='value')
    projectinfo_widgets.hov_hot_lanes_no_build_widget.observe(update_weaving_speed_year1peak_nobuild, names='value')
    projectinfo_widgets.free_flow_speed_no_build_widget.observe(update_weaving_speed_year1peak_nobuild, names='value')
    projectinfo_widgets.iri_base_year_no_build_widget.observe(update_weaving_speed_year1peak_nobuild, names='value')

    def calculate_pws1nb(change):
        try:
            val = float(weave_speed_year1peak_nobuild_userchanged_widget.value)
            updated_weave_speed = max(val, 5)
        except:
            updated_weave_speed = max(weave_speed_year1peak_nobuild_modelcalc_widget.value, 5)

        PWS1NB_widget.value = updated_weave_speed

    weave_speed_year1peak_nobuild_userchanged_widget.observe(calculate_pws1nb, names='value')

    Weave_Speed_year1peak_nobuild_widgets = widgets.HBox([
        weave_speed_year1peak_nobuild_modelcalc_widget,
        weave_speed_year1peak_nobuild_userchanged_widget,
        PWS1NB_explanation_widget
    ])

    
    ###################################################################    
    # Truck Speed widgets 
    truck_speed_year1peak_nobuild_modelcalc_widget = widgets.IntText(
        value=0,
        description="Truck Speed (Calculated by Model):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    truck_speed_year1peak_nobuild_userchanged_widget = widgets.Text(
        value='',
        description="Truck Speed (Changed by User):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    PTS1NB_widget = widgets.IntText(
        value=truck_speed_year1peak_nobuild_modelcalc_widget.value,
        description="Truck Speed (Used for Proj Evaluation):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    PTS1NB_explanation_widget = widgets.Text(
        value=None,
        description="Reasons for Change:",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    def update_truck_speed_year1peak_nobuild(change=None):
        PTV1NB = PTV1NB_widget.value
        PWS1NB = PWS1NB_widget.value
        PNS1NB = PNS1NB_widget.value
        Pavement = ProjType == "Pavement"

        if PTV1NB == 0:
            truck_speed = 55
        else:
            base_speed = PWS1NB if ProjType in ["Auxiliary Lane", "Off-Ramp Widening"] else PNS1NB

            if Pavement:
                iri_keys = [k for k in SpeedPavAdj if k <= IRI1NB]
                closest_iri = max(iri_keys) if iri_keys else 0

                pavement_divisor = SpeedPavAdj[closest_iri]["Truck"]
                adjusted_speed = min(TruckSpeed, base_speed / pavement_divisor)
                pavement_multiplier = SpeedPavAdj[closest_iri]["Truck"]
                truck_speed = adjusted_speed * pavement_multiplier
            else:
                truck_speed = min(TruckSpeed, base_speed)

        truck_speed_year1peak_nobuild_modelcalc_widget.value = round(truck_speed, 1)

    update_truck_speed_year1peak_nobuild()  # Initial truck speed calculation

    # Adding Observers for the widgets to trigger truck speed calculation when the user changes values
    PTV1NB_widget.observe(update_truck_speed_year1peak_nobuild, names='value')
    PWS1NB_widget.observe(update_truck_speed_year1peak_nobuild, names='value')
    PNS1NB_widget.observe(update_truck_speed_year1peak_nobuild, names='value')
    projectinfo_widgets.truck_speed_widget.observe(update_truck_speed_year1peak_nobuild, names='value')
    projectinfo_widgets.subcategory_dropdown.observe(update_truck_speed_year1peak_nobuild, names='value')
    projectinfo_widgets.iri_base_year_no_build_widget.observe(update_truck_speed_year1peak_nobuild, names='value')

    def calculate_pts1nb(change):
        try:
            val = float(truck_speed_year1peak_nobuild_userchanged_widget.value)
            updated_truck_speed = max(val, 5)
        except:
            updated_truck_speed = max(truck_speed_year1peak_nobuild_modelcalc_widget.value, 5)

        PTS1NB_widget.value = updated_truck_speed

    truck_speed_year1peak_nobuild_userchanged_widget.observe(calculate_pts1nb, names='value')

    Truck_Speed_year1peak_nobuild_widgets = widgets.HBox([
        truck_speed_year1peak_nobuild_modelcalc_widget,
        truck_speed_year1peak_nobuild_userchanged_widget,
        PTS1NB_explanation_widget
    ])

    
###################################################################################################################################################################
############################### Peak Period ###############################
    
    # Create the Non-Peak period Non-HOV Volume widget to display the calculated value
    Non_HOV_Vol_year1nonpeak_modelcalc_widget = widgets.IntText(
        value=0,  # Set initial value to 0, or any other valid integer
        description="Non-HOV Volume (Calculated by Model):",
        disabled=True,  # Make it read-only so the user cannot modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Create the Non-HOV Volume Peak Period widget for user-modified value
    Non_HOV_Vol_year1nonpeak_userchanged_widget = widgets.Text(
        value='',  # Initially set to 0 or a valid integer value
        description="Non-HOV Volume (Changed by User):",
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )
    
    NNV1NB_widget = widgets.IntText(
        value=Non_HOV_Vol_year1nonpeak_modelcalc_widget.value,  # Set initially to the calculated value
        description="Non-HOV Volume (Used for Proj Evaluation):",
        disabled=True,  # Make it read-only
        layout=common_layout,
        style={'description_width': 'initial'}
    )
    
    NNV1NB_explanation_widget = widgets.Text(
        value=None,  # Allow users to enter a text explanation
        description="Reasons for Change:",  # Label for the input field
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,  # Optional layout style, if needed
        style={'description_width': 'initial'}  # Optional style for description width
    )
    
    # Non-HOV Volume Widget update function
    def update_NonHOV_year1nonpeak_Volume(change):
        # Apply formula directly based on ProjType
        if ProjType == "Hwy-Rail Grade Crossing":
            try:
                result = (
                    ((ArrRate1 * GateTime1) / 60)
                    / (1 - (ArrRate1 / DepRate1))
                    * (NumTrain1 / AnnualFactor)
                    * (1 - PerTruckNB)
                )
            except ZeroDivisionError:
                result = 0
        else:
            traffic_factor = PerWeaveNB if (ProjType == "Auxiliary Lane" or ProjType == "Off-Ramp Widening") else PerTruckNB
            result = (1 - PerPeakADT) * ADT1NB * (1 - traffic_factor)

        # Update the output widget
        Non_HOV_Vol_year1peak_nobuild_modelcalc_widget.value = round(result, 0)
    
    projectinfo_widgets.subcategory_dropdown.observe(update_NonHOV_year1nonpeak_Volume, names='value')
    projectinfo_widgets.HOV_lane_nobuild_widget.observe(update_NonHOV_year1nonpeak_Volume, names='value')
    projectinfo_widgets.arrival_rate_base_year_no_build_widget.observe(update_NonHOV_year1nonpeak_Volume, names='value')
    projectinfo_widgets.GateTime1_widget.observe(update_NonHOV_year1nonpeak_Volume, names = 'value')
    projectinfo_widgets.departure_rate_forecast_year_no_build_widget.observe(update_NonHOV_year1nonpeak_Volume, names = 'value')
    projectinfo_widgets.NumTrain1_widget.observe(update_NonHOV_year1nonpeak_Volume, names = 'value')
    projectinfo_widgets.percent_trucks_nobuild_widget.observe(update_NonHOV_year1nonpeak_Volume, names = 'value')
    projectinfo_widgets.adt_base_year_no_build_widget.observe(update_NonHOV_year1nonpeak_Volume, names = 'value')
    projectinfo_widgets.percent_traffic_weave_no_build_widget.observe(update_NonHOV_year1nonpeak_Volume, names = 'value')
    projectinfo_widgets.percent_trucks_nobuild_widget.observe(update_NonHOV_year1nonpeak_Volume, names = 'value')
    
    # Function to calculate PHV1NB
    def calculate_nnv1nb(change):
        # Access the user-modified value directly from the widget
        if isinstance(Non_HOV_Vol_year1nonpeak_userchanged_widget.value, (int, float)) and Non_HOV_Vol_year1nonpeak_userchanged_widget.value >= 0:
            NNV1NB = Non_HOV_Vol_year1nonpeak_userchanged_widget.value  # Use the user-modified value if valid
        else:
            NNV1NB = Non_HOV_Vol_year1nonpeak_modelcalc_widget.value  # Use the model value if the user value is invalid

        # Update the value of PHV1NB widget
        NNV1NB_widget.value = NNV1NB

    # Link the PHV1NB widget update to changes in HOV_Vol_peak_userchanged_widget
    Non_HOV_Vol_year1nonpeak_userchanged_widget.observe(calculate_nnv1nb, names='value')  

    # Combine all widgets into a horizontal layout for HOV Volume
    Non_HOV_vol_year1nonpeak_widgets = widgets.HBox([Non_HOV_Vol_year1nonpeak_modelcalc_widget, Non_HOV_Vol_year1nonpeak_userchanged_widget, NNV1NB_explanation_widget])
    
    ###################################################################    
    
    # Weaving Volume (Calculated by Model)
    weaving_volume_year1nonpeak_modelcalc_widget = widgets.IntText(
        value=0,  # Set initial value to 0 or any other valid integer
        description="Weaving Volume (Calculated by Model):",
        disabled=True,  # Make it read-only so the user cannot modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Weaving Volume (User-modified value)
    weaving_volume_year1nonpeak_userchanged_widget = widgets.Text(
        value='',  # Initially set to 0 or a valid integer value
        description="Weaving Volume (Changed by User):",
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Weaving Volume (Used for Project Evaluation)
    NWV1NB_widget = widgets.IntText(
        value=weaving_volume_year1nonpeak_modelcalc_widget.value,  # Set initially to the calculated value
        description="Weaving Volume (Used for Proj Evaluation):",
        disabled=True,  # Make it read-only
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Explanation widget for user-modified values
    NWV1NB_explanation_widget = widgets.Text(
        value=None,  # Allow users to enter a text explanation
        description="Reasons for Change:",  # Label for the input field
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,  # Optional layout style, if needed
        style={'description_width': 'initial'}  # Optional style for description width
    )
    
    # Update Weaving Volume Calculation based on widget values
    def update_year1nonpeak_weaving_volume(change):
        # Initialize the Weaving Volume Non-Peak as 0
        Weaving_Volume_Year1NonPeak = 0

        # Apply the first condition: Check if project type is "Auxiliary Lane" or "Off-Ramp"
        if ProjType == "Auxiliary Lane" or ProjType == "Off-Ramp Widening":
            # Calculate the first part of the formula
            Weaving_Volume_Year1NonPeak += ((1 - PerPeakADT) * ADT1NB) * (PerWeaveNB - PerTruckNB)

        # Apply the second condition: Check if project type is "Auxiliary Lane"
        if ProjType == "Auxiliary Lane":
            # Calculate the second part of the formula
            Weaving_Volume_Year1NonPeak += RampVolNP * (24 - PeakLngthNB)

        # Update the weaving volume based on the calculated value
        return Weaving_Volume_Year1NonPeak
    
            
    # Link the update function to changes in relevant widgets
    projectinfo_widgets.adt_base_year_no_build_widget.observe(update_year1nonpeak_weaving_volume, names='value')
    projectinfo_widgets.percent_traffic_weave_no_build_widget.observe(update_year1nonpeak_weaving_volume, names='value')
    projectinfo_widgets.percent_trucks_nobuild_widget.observe(update_year1nonpeak_weaving_volume, names='value')
    projectinfo_widgets.hourly_ramp_volume_nonpeak_widget.observe(update_year1nonpeak_weaving_volume, names='value')
    projectinfo_widgets.peak_period_widget.observe(update_year1nonpeak_weaving_volume, names='value')
    
    # Function to calculate PHV1NB
    def calculate_nwv1nb(change):
        # Access the user-modified value directly from the widget
        if isinstance(weaving_volume_year1nonpeak_userchanged_widget.value, (int, float)) and weaving_volume_year1nonpeak_userchanged_widget.value >= 0:
            NWV1NB = weaving_volume_year1nonpeak_userchanged_widget.value  # Use the user-modified value if valid
        else:
            NWV1NB = weaving_volume_year1nonpeak_modelcalc_widget.value  # Use the model value if the user value is invalid

        # Update the value of PHV1NB widget
        NWV1NB_widget.value = NWV1NB

    # Link the PHV1NB widget update to changes in HOV_Vol_peak_userchanged_widget
    weaving_volume_year1nonpeak_userchanged_widget.observe(calculate_nwv1nb, names='value')  

    # Combine all widgets into a horizontal layout for HOV Volume
    Weaving_volume_year1nonpeak_widgets = widgets.HBox([weaving_volume_year1nonpeak_modelcalc_widget, weaving_volume_year1nonpeak_userchanged_widget, NWV1NB_explanation_widget])
    
    ###################################################################    
    # Truck Non Peak Volume (Calculated by Model)
    truck_volume_year1nonpeak_modelcalc_widget = widgets.IntText(
        value=0,  # Set initial value to 0 or any other valid integer
        description="Truck Volume (Calculated by Model):",
        disabled=True,  # Make it read-only so the user cannot modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Truck Volume (User-modified value)
    truck_volume_year1nonpeak_userchanged_widget = widgets.Text(
        value='',  # Initially set to 0 or a valid integer value
        description="Truck Volume (Changed by User):",
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Truck Volume (Used for Project Evaluation)
    NTV1NB_widget = widgets.IntText(
        value=truck_volume_year1nonpeak_modelcalc_widget.value,  # Set initially to the calculated value
        description="Truck Volume (Used for Proj Evaluation):",
        disabled=True,  # Make it read-only
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Explanation widget for user-modified values
    NTV1NB_explanation_widget = widgets.Text(
        value=None,  # Allow users to enter a text explanation
        description="Reasons for Change:",  # Label for the input field
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,  # Optional layout style, if needed
        style={'description_width': 'initial'}  # Optional style for description width
    )
    
    def update_truck_volume_year1nonpeak(change):
        # Initialize Truck Volume Model as 0
        Truck_Volume_Model_year1nonpeak = 0

        # Check for "Hwy-Rail Grade Crossing" condition
        if ProjType == "Hwy-Rail Grade Crossing":
            # Calculate the truck volume for Hwy-Rail Grade Crossing
            Truck_Volume_Model_year1nonpeak = (ArrRate1 * GateTime1 / 60) / (1 - ArrRate1 / DepRate1) * NumTrain1 / AnnualFactor * PerTruckNB
        else:
            # Apply the second formula for other types of projects
            Truck_Volume_Model_year1nonpeak = ((1 - PerPeakADT) * ADT1NB) * PerTruckNB

        # Update the Truck Volume widget dynamically (ensure correct widget is updated)
        truck_volume_year1nonpeak_modelcalc_widget.value = round(Truck_Volume_Model_year1nonpeak, 0)  # Correct widget name

        # Optionally, return the calculated value
        return Truck_Volume_Model_year1nonpeak
    
    projectinfo_widgets.subcategory_dropdown.observe(update_truck_volume_year1nonpeak, names='value')
    projectinfo_widgets.arrival_rate_base_year_no_build_widget.observe(update_truck_volume_year1nonpeak, names='value')
    projectinfo_widgets.GateTime1_widget.observe(update_truck_volume_year1nonpeak, names = 'value')
    projectinfo_widgets.departure_rate_forecast_year_no_build_widget.observe(update_truck_volume_year1nonpeak, names = 'value')
    projectinfo_widgets.NumTrain1_widget.observe(update_truck_volume_year1nonpeak, names = 'value')
    projectinfo_widgets.percent_trucks_nobuild_widget.observe(update_truck_volume_year1nonpeak, names = 'value')
    projectinfo_widgets.adt_base_year_no_build_widget.observe(update_truck_volume_year1nonpeak, names = 'value')
    projectinfo_widgets.percent_trucks_nobuild_widget.observe(update_truck_volume_year1nonpeak, names = 'value')
    
    # Function to calculate NTV1NB
    def calculate_ntv1nb(change):
        # Access the user-modified value directly from the widget
        if isinstance(truck_volume_year1nonpeak_userchanged_widget.value, (int, float)) and truck_volume_year1nonpeak_userchanged_widget.value >= 0:
            NTV1NB = truck_volume_year1nonpeak_userchanged_widget.value  # Use the user-modified value if valid
        else:
            NTV1NB = truck_volume_year1nonpeak_modelcalc_widget.value  # Use the model value if the user value is invalid

        # Update the value of PHV1NB widget
        NTV1NB_widget.value = NTV1NB

    # Link the PHV1NB widget update to changes in HOV_Vol_peak_userchanged_widget
    truck_volume_year1nonpeak_userchanged_widget.observe(calculate_ntv1nb, names='value')  

    # Combine all widgets into a horizontal layout for HOV Volume
    Truck_volume_year1nonpeak_widgets = widgets.HBox([truck_volume_year1nonpeak_modelcalc_widget, truck_volume_year1nonpeak_userchanged_widget, NTV1NB_explanation_widget])
    
    
    ###################################################################    
    #Non-HOV Speed widgets 
    nonhov_speed_year1nonpeak_modelcalc_widget = widgets.IntText(
        value=0,  # Set initial value to 0 or any other valid integer
        description="Non-HOV Speed (Calculated by Model):",
        disabled=True,  # Make it read-only so the user cannot modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )
    
    nonhov_speed_year1nonpeak_userchanged_widget = widgets.Text(
        value='',  # Initially set to 0 or a valid integer value
        description="Non-HOV Speed (Changed by User):",
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )
    
    # Non-HOV Speed Volume (Used for Project Evaluation)
    NNS1NB_widget = widgets.IntText(
        value=nonhov_speed_year1nonpeak_modelcalc_widget.value,  # Set initially to the calculated value
        description="Non-HOV Speed (Used for Proj Evaluation):",
        disabled=True,  # Make it read-only
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Explanation widget for user-modified values
    NNS1NB_explanation_widget = widgets.Text(
        value=None,  # Allow users to enter a text explanation
        description="Reasons for Change:",  # Label for the input field
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,  # Optional layout style, if needed
        style={'description_width': 'initial'}  # Optional style for description width
    )    
    
    
    def update_nonhov_year1nonpeak_speed(change=None):
        
        capacity_params = roadway_capacity_non_HOV["Non-HOV Lanes"]["No Build"]
        GenAlphaNB = capacity_params["GenAlphaNB"]
        GenBetaNB = capacity_params["GenBetaNB"]
        GenLaneCapNB = capacity_params["GenLaneCapNB"]
        
        # Step 1: Special condition: Hwy-Rail Grade Crossing
        if ProjType == "Hwy-Rail Grade Crossing":
            speed = IdleSpeed

        else:
            # Step 2: Total volume from widgets
            total_volume = NNV1NB_widget.value + NWV1NB_widget.value + NTV1NB_widget.value

            if total_volume == 0:
                speed = 55
            else:
                # Step 3: BPR calculation
                demand = total_volume
                capacity = (GenLanesNB + HOVLanesNB) * GenLaneCapNB * (24 - PeakLngthNB)
                vc_ratio = min(demand / capacity, MaxVC)

                speed_bpr = FFSpeedNB / (1 + GenAlphaNB * (vc_ratio ** GenBetaNB))

                # Step 4: Passing adjustment
                if ProjType == "Passing":
                    speed = min(speed_bpr, (TruckSpeed + FFSpeedNB) / 2)
                else:
                    speed = min(speed_bpr, FFSpeedNB)

        # Step 5: Speed adjustments

        # Freeway Connector adjustment
        if ProjType == "Freeway Connector":
            closest_key = min(SpeedWeaveAdj.keys(), key=lambda k: abs(k - PerWeaveNB))
            adj = SpeedWeaveAdj.get(closest_key, {}).get("Freeway", 1)
            speed *= adj

        # HOV Connector / HOV Drop Ramp adjustment
        if ProjType in ["HOV Connector", "HOV Drop Ramp"]:
            closest_key = min(SpeedWeaveAdj.keys(), key=lambda k: abs(k - PerWeaveNB))
            adj = SpeedWeaveAdj.get(closest_key, {}).get("HOV", 1)
            speed *= adj

        # Pavement condition adjustment
        if ProjType == "Pavement":
            iri_key = min(SpeedPavAdj.keys(), key=lambda k: abs(k - IRI1NB))  # Closest IRI
            adj = SpeedPavAdj.get(iri_key, {}).get("Auto", 1)
            speed *= adj

        # Step 6: Update the widget
        nonhov_speed_year1nonpeak_modelcalc_widget.value = round(speed, 1)

        return speed
    
    update_nonhov_year1nonpeak_speed()
    
    # Link the update function to changes in relevant widgets
    NNV1NB_widget.observe(update_nonhov_year1nonpeak_speed, names='value')
    NWV1NB_widget.observe(update_nonhov_year1nonpeak_speed, names='value')
    NTV1NB_widget.observe(update_nonhov_year1nonpeak_speed, names='value')
    projectinfo_widgets.subcategory_dropdown.observe(update_nonhov_year1nonpeak_speed, names='value')  
    projectinfo_widgets.percent_traffic_weave_no_build_widget.observe(update_nonhov_year1nonpeak_speed, names='value')  
    projectinfo_widgets.iri_base_year_no_build_widget.observe(update_nonhov_year1nonpeak_speed, names='value')  
    projectinfo_widgets.free_flow_speed_no_build_widget.observe(update_nonhov_year1nonpeak_speed, names='value')
    projectinfo_widgets.general_traffic_lanes_no_build_widget.observe(update_nonhov_year1nonpeak_speed, names='value')
    projectinfo_widgets.hov_hot_lanes_no_build_widget.observe(update_nonhov_year1nonpeak_speed, names='value')
    projectinfo_widgets.peak_period_widget.observe(update_nonhov_year1nonpeak_speed, names='value')
    projectinfo_widgets.truck_speed_widget.observe(update_nonhov_year1nonpeak_speed, names='value')
    
        # Function to calculate NNS1NB
    def calculate_nns1nb(change):
        # Access the user-modified value directly from the widget
        if isinstance(nonhov_speed_year1nonpeak_userchanged_widget.value, (int, float)) and nonhov_speed_year1nonpeak_userchanged_widget.value >= 0:
            NNS1NB= max(nonhov_speed_year1nonpeak_userchanged_widget.value, 5)  # Ensure the speed is at least 5
        else:
            NNS1NB = max(nonhov_speed_year1nonpeak_modelcalc_widget.value, 5)  # Use the model value if the user value is invalid
            
        # Update the value of NNS1NB widget
        NNS1NB_widget.value = NNS1NB

    # Link the PHV1NB widget update to changes in HOV_Vol_peak_userchanged_widget
    nonhov_speed_year1nonpeak_userchanged_widget.observe(calculate_nns1nb, names='value')  

    # Combine all widgets into a horizontal layout for HOV Volume
    NonHOV_speed_year1nonpeak_widgets = widgets.HBox([nonhov_speed_year1nonpeak_modelcalc_widget, nonhov_speed_year1nonpeak_userchanged_widget, NNS1NB_explanation_widget])
    
    ###################################################################    
    
    # Weaving Non Peak Speed widgets 
    weave_speed_year1nonpeak_modelcalc_widget = widgets.IntText(
        value=0,  # Set initial value to 0 or any other valid integer
        description="Weaving Speed (Calculated by Model):",
        disabled=True,  # Make it read-only so the user cannot modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    weave_speed_year1nonpeak_userchanged_widget = widgets.Text(
        value='',  # Initially set to 0 or a valid integer value
        description="Weaving Speed (Changed by User):",
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Non-HOV Speed Volume (Used for Project Evaluation)
    NWS1NB_widget = widgets.IntText(
        value=weave_speed_year1nonpeak_modelcalc_widget.value,  # Set initially to the calculated value
        description="Weaving Speed (Used for Proj Evaluation):",
        disabled=True,  # Make it read-only
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Explanation widget for user-modified values
    NWS1NB_explanation_widget = widgets.Text(
        value=None,  # Allow users to enter a text explanation
        description="Reasons for Change:",  # Label for the input field
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,  # Optional layout style, if needed
        style={'description_width': 'initial'}  # Optional style for description width
    ) 
    
    def update_year1nonpeak_weave_speed(change=None):
        try:
            # Retrieve relevant widget values
            NWV1NB = NWV1NB_widget.value
            NNS1NB = NNS1NB_widget.value
            NTV1NB = NTV1NB_widget.value
            # Apply the formula
            if NWV1NB == 0:
                Year1NonPeakWeaveSpeed = 55
            else:
                if ProjType == "Auxiliary Lane" or ProjType == "Off-Ramp Widening":
                    exponent_part = math.exp((NWV1NB + NTV1NB) / NumDirections / (24 - PeakLngthNB) / 1000)
                    part1 = FFSpeedNB - (FFSpeedNB - 42) * (0.321 + 0.0039 * exponent_part - 0.002 * (1083 if ProjType == "Off-Ramp Widening" else SegmentNB * 5280) * RampFFSpdNB / 1000)
                    adjusted_speed = 1.1 * part1

                    # If ProjType is Pavement, apply pavement adjustment using SpeedPavAdj
                    if ProjType == "Pavement":
                        # Lookup SpeedPavAdj for the provided IRI1NB value
                        speed_adj = SpeedPavAdj.get(IRI1NB, {"Auto": 1.0})  # Default to Auto: 1.0 if no match
                        auto_speed_factor = speed_adj["Auto"]  # Assuming we are interested in the "Auto" value for adjustment
                        adjusted_speed *= auto_speed_factor

                    Year1NonPeakWeaveSpeed = max(5, min(NNS1NB, adjusted_speed))
                else:
                    Year1NonPeakWeaveSpeed = NNS1NB

            # Update the widget with the result
            weave_speed_year1nonpeak_modelcalc_widget.value = round(Year1NonPeakWeaveSpeed, 2)

        except Exception:
            weave_speed_year1nonpeak_modelcalc_widget.value = 0
            
    update_year1nonpeak_weave_speed()
    
    # Link the update function to changes in relevant widgets
    NNV1NB_widget.observe(update_year1nonpeak_weave_speed, names='value')
    NNS1NB_widget.observe(update_year1nonpeak_weave_speed, names='value')
    NTV1NB_widget.observe(update_year1nonpeak_weave_speed, names='value')
    projectinfo_widgets.one_two_way_widget.observe(update_year1nonpeak_weave_speed, names='value')
    projectinfo_widgets.subcategory_dropdown.observe(update_year1nonpeak_weave_speed, names='value')   
    projectinfo_widgets.free_flow_speed_no_build_widget.observe(update_year1nonpeak_weave_speed, names='value')
    projectinfo_widgets.ramp_design_speed_no_build_widget.observe(update_year1nonpeak_weave_speed, names='value')
    projectinfo_widgets.hov_hot_lanes_no_build_widget.observe(update_year1nonpeak_weave_speed, names='value')
    projectinfo_widgets.highway_segment_no_build_widget.observe(update_year1nonpeak_weave_speed, names='value')
    projectinfo_widgets.peak_period_widget.observe(update_year1nonpeak_weave_speed, names='value')
    projectinfo_widgets.iri_base_year_no_build_widget.observe(update_year1nonpeak_weave_speed, names='value')
 
    # Function to calculate NNS1NB
    def calculate_nws1nb(change):
        # Access the user-modified value directly from the widget
        if isinstance(weave_speed_year1nonpeak_userchanged_widget.value, (int, float)) and weave_speed_year1nonpeak_userchanged_widget.value >= 0:
            NWS1NB= max(weave_speed_year1nonpeak_userchanged_widget.value, 5)  # Ensure the speed is at least 5
        else:
            NWS1NB = max(weave_speed_year1nonpeak_modelcalc_widget.value, 5)  # Use the model value if the user value is invalid
            
        # Update the value of NNS1NB widget
        NWS1NB_widget.value = NWS1NB

    # Link the PHV1NB widget update to changes in HOV_Vol_peak_userchanged_widget
    weave_speed_year1nonpeak_userchanged_widget.observe(calculate_nws1nb, names='value')  

    # Combine all widgets into a horizontal layout for HOV Volume
    Weave_speed_year1nonpeak_widgets = widgets.HBox([weave_speed_year1nonpeak_modelcalc_widget, weave_speed_year1nonpeak_userchanged_widget, NWS1NB_explanation_widget])

    ###################################################################
    # Truck Non Peak Speed widgets 
    truck_speed_year1nonpeak_modelcalc_widget = widgets.IntText(
        value=0,  # Set initial value to 0 or any other valid integer
        description="Truck Speed (Calculated by Model):",
        disabled=True,  # Make it read-only so the user cannot modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    truck_speed_year1nonpeak_userchanged_widget = widgets.Text(
        value='',  # Initially set to 0 or a valid integer value
        description="Truck Speed (Changed by User):",
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Truck Speed Volume (Used for Project Evaluation)
    NTS1NB_widget = widgets.IntText(
        value=truck_speed_year1nonpeak_modelcalc_widget.value,  # Set initially to the calculated value
        description="Truck Speed (Used for Proj Evaluation):",
        disabled=True,  # Make it read-only
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Explanation widget for user-modified values
    NTS1NB_explanation_widget = widgets.Text(
        value=None,  # Allow users to enter a text explanation
        description="Reasons for Change:",  # Label for the input field
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,  # Optional layout style, if needed
        style={'description_width': 'initial'}  # Optional style for description width
    )  
    
    def update_year1nonpeak_truck_speed(change=None):
        # Retrieve relevant widget values
        NTV1NB = NTV1NB_widget.value
        NWS1NB = NWS1NB_widget.value
        NNS1NB = NNS1NB_widget.value
        Pavement = ProjType == "Pavement"

        if ProjType == "Hwy-Rail Grade Crossing":
            truck_speed = IdleSpeed
        elif NTV1NB == 0:
            truck_speed = 55
        else:
            # Use NWS1NB if it's Auxiliary or Off-Ramp, otherwise use NNS1NB
            base_speed = NWS1NB if ProjType in ["Auxiliary Lane", "Off-Ramp Widening"] else NNS1NB

            if Pavement:
                # Get the closest IRI key <= IRI1NB
                iri_keys = [k for k in SpeedPavAdj if k <= IRI1NB]
                closest_iri = max(iri_keys) if iri_keys else 0

                divisor = SpeedPavAdj[closest_iri]["Truck"]
                adjusted_speed = min(TruckSpeed, base_speed / divisor)
                multiplier = SpeedPavAdj[closest_iri]["Truck"]
                truck_speed = adjusted_speed * multiplier
            else:
                truck_speed = min(TruckSpeed, base_speed)

        # Update the non-peak truck speed model calculation widget
        truck_speed_year1nonpeak_modelcalc_widget.value = round(truck_speed, 1)

    # Initial call
    update_year1nonpeak_truck_speed()
    
    
    # Adding Observers to trigger truck speed calculation
    NTV1NB_widget.observe(update_year1nonpeak_truck_speed, names='value')
    NWS1NB_widget.observe(update_year1nonpeak_truck_speed, names='value')
    NNS1NB_widget.observe(update_year1nonpeak_truck_speed, names='value')
    projectinfo_widgets.truck_speed_widget.observe(update_year1nonpeak_truck_speed, names='value')
    projectinfo_widgets.subcategory_dropdown.observe(update_year1nonpeak_truck_speed, names='value')
    projectinfo_widgets.iri_base_year_no_build_widget.observe(update_year1nonpeak_truck_speed, names='value')
        
    def calculate_nts1nb(change):
        # Access the user-modified value directly from the widget
        if isinstance(truck_speed_year1nonpeak_userchanged_widget.value, (int, float)) and truck_speed_year1nonpeak_userchanged_widget.value >= 0:
            updated_year1nonpeaktruck_speed = max(truck_speed_year1nonpeak_userchanged_widget.value, 5)  # Ensure the speed is at least 5
        else:
            updated_year1nonpeaktruck_speed = max(truck_speed_year1nonpeak_modelcalc_widget.value, 5)  # Use the model value if the user value is invalid

        # Update the value of PHS1NB widget
        NTS1NB_widget.value = updated_year1nonpeaktruck_speed
        
    # Link the function to the user input widget change
    truck_speed_year1nonpeak_modelcalc_widget.observe(calculate_nts1nb, names='value')
    
    # Combine all the Non HOV Speed widgets into a horizontal layout for display
    Truck_speed_year1nonpeak_widgets = widgets.HBox([truck_speed_year1nonpeak_modelcalc_widget, truck_speed_year1nonpeak_userchanged_widget, NTS1NB_explanation_widget])     
    
    
######################################################################################################################################################################
################################################## Year 20 ##################################################
############################### Peak Period ###############################
   
    # Create the HOV Volume widget to display the calculated value
    HOV_Vol_year20peak_modelcalc_widget = widgets.IntText(
        value=0,  # Set initial value to 0, or any other valid integer
        description="HOV Volume(Calculated by Model):",
        disabled=True,  # Make it read-only so the user cannot modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Create the HOV Volume Peak Period widget for user-modified value
    HOV_Vol_year20peak_userchanged_widget = widgets.Text(
        value='',  # Initially set to 0 or a valid integer value
        description="HOV Volume (Changed by User):",
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Create the PHV1NB widget based on the formula
    PHV20NB_widget = widgets.IntText(
        value=HOV_Vol_year20peak_modelcalc_widget.value,  # Set initially to the calculated value
        description="HOV Volume (Used for Proj Evaluation):",
        disabled=True,  # Make it read-only 
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    PHV20NB_explaination_widget = widgets.Text(
=======
>>>>>>> 3ce506f0b22b27317d6525ffa8fe8b5e58771617
        value=None,  
        description="Reasons for Change:",  # Label for the input field
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,  # Optional layout style, if needed
        style={'description_width': 'initial'}  # Optional style for description width
    )
<<<<<<< HEAD

    # Function to update HOV Volume dynamically
    # Function to update HOV Volume dynamically
    def update_HOV_Year20Peak_Volume(change):
        try:
            # Check if project type is "Hwy-Rail Grade Crossing"
            if ProjType == "Hwy-Rail Grade Crossing":
                HOV_Volume_Year20Peak_Model = 0

            # Check if project type is "Queuing"
            elif ProjType == "Queuing":
                numerator = PeakLngthNB * (DepRate1 - ADT1NB * (1 - PerPeakADT) / (24 - PeakLngthNB))
                denominator = (ADT1NB / ADT20NB * DepRate20 - ADT1NB * (1 - PerPeakADT) / (24 - PeakLngthNB))
                HOV_Volume_Year20Peak_Model = numerator / denominator if denominator != 0 else 0

            # Default case for other project types
            else:
                hov_factor = (1 - PerWeaveNB) if ProjType in ["HOV Connector", "HOV Drop Ramp"] else 1
                HOV_Volume_Year20Peak_Model = PeakLngthNB * HOVvolNB * hov_factor

            # Update the widget with the result
            hov_volume_year20peak_modelcalc_widget.value = round(HOV_Volume_Year20Peak_Model, 2)

        except Exception:
            hov_volume_year20peak_modelcalc_widget.value = 0
            
    # Attach observers to the relevant widgets to update the HOV Volume widget dynamically
    projectinfo_widgets.subcategory_dropdown.observe(update_HOV_Year20Peak_Volume, names='value')
    projectinfo_widgets.HOV_lane_nobuild_widget.observe(update_HOV_Year20Peak_Volume, names='value')
    projectinfo_widgets.peak_period_widget.observe(update_HOV_Year20Peak_Volume, names='value')
    projectinfo_widgets.percent_traffic_weave_no_build_widget.observe(update_HOV_Year20Peak_Volume, names='value')
    projectinfo_widgets.departure_rate_forecast_year_no_build_widget.observe(update_HOV_Year20Peak_Volume, names='value')
    projectinfo_widgets.adt_base_year_no_build_widget.observe(update_HOV_Year20Peak_Volume, names='value')
    projectinfo_widgets.ADT_20NB_widget.observe(update_HOV_Year20Peak_Volume, names='value')
    projectinfo_widgets.departure_rate_forecast_year_build_widget.observe(update_HOV_Year20Peak_Volume, names='value')
    

    # Function to calculate PHV1NB
    def calculate_phv20nb(change):
        # Access the user-modified value directly from the widget
        if isinstance(HOV_Vol_year20peak_userchanged_widget.value, (int, float)) and HOV_Vol_year20peak_userchanged_widget.value >= 0:
            PHV20NB = HOV_Vol_year20peak_userchanged_widget.value  # Use the user-modified value if valid
        else:
            PHV20NB = HOV_Vol_year20peak_modelcalc_widget.value  # Use the model value if the user value is invalid

        # Update the value of PHV1NB widget
        PHV20NB_widget.value = PHV20NB
        

    # Link the PHV1NB widget update to changes in HOV_Vol_peak_userchanged_widget
    HOV_Vol_year20peak_userchanged_widget.observe(calculate_phv20nb, names='value')  

    # Combine all widgets into a horizontal layout for HOV Volume
    HOV_vol_year20peak_widgets = widgets.HBox([HOV_Vol_year20peak_modelcalc_widget, HOV_Vol_year20peak_userchanged_widget, PHV20NB_explaination_widget])


    
    
    ###################################################################    
  
    # Create the Non-HOV Volume widget to display the calculated value
    Non_HOV_Vol_year20peak_modelcalc_widget = widgets.IntText(
        value=0,  # Set initial value to 0, or any other valid integer
        description="Non-HOV Volume (Calculated by Model):",
        disabled=True,  # Make it read-only so the user cannot modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Create the Non-HOV Volume Peak Period widget for user-modified value
    Non_HOV_Vol_year20peak_userchanged_widget = widgets.Text(
        value='',  # Initially set to 0 or a valid integer value
        description="Non-HOV Volume(Changed by User):",
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )
    
    PNV20NB_widget = widgets.IntText(
        value=Non_HOV_Vol_year20peak_modelcalc_widget.value,  # Set initially to the calculated value
        description="Non-HOV Volume (Used for Proj Evaluation):",
        disabled=True,  # Make it read-only
        layout=common_layout,
        style={'description_width': 'initial'}
    )
    
    PNV20NB_explanation_widget = widgets.Text(
        value=None,  # Allow users to enter a text explanation
        description="Reasons for Change:",  # Label for the input field
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,  # Optional layout style, if needed
        style={'description_width': 'initial'}  # Optional style for description width
    )
    

    # Non-HOV Volume Widget update function
    def update_Non_HOV_Year20Peak_Volume(change):
        try:
            # Check if project type is "Hwy-Rail Grade Crossing"
            if ProjType == "Hwy-Rail Grade Crossing":
                Non_HOV_Volume_Year20Peak = 0

            # Check if project type is "Queuing"
            elif ProjType == "Queuing":
                numerator = PeakLngthNB * (DepRate1 - ADT1NB * (1 - PerPeakADT) / (24 - PeakLngthNB))
                denominator = (ADT1NB / ADT20NB * DepRate20 - ADT1NB * (1 - PerPeakADT) / (24 - PeakLngthNB))
                Non_HOV_Volume_Year20Peak = (numerator / denominator if denominator != 0 else 0) * DepRate20

            # Default case for other project types
            else:
                non_hov_factor = (1 - PerWeaveNB) if ProjType in ["Auxiliary Lane", "Off-Ramp Widening"] else (1 - PerTruckNB)
                Non_HOV_Volume_Year20Peak = PerPeakADT * ADT20NB * non_hov_factor
                if ProjType == "Queuing":
                    Non_HOV_Volume_Year20Peak -= (HOVvolNB / DepRate20)

                # Replace the vlookup with dictionary lookup in TMSAdj
                if TMSLookup in TMSAdj:
                    tms_values = TMSAdj[TMSLookup]
                    Non_HOV_Volume_Year20Peak *= tms_values["VolumeWith"]  # Using VolumeWith as per the formula

            # Final adjustment for the formula
            if ProjType != "Queuing":
                Non_HOV_Volume_Year20Peak -= (HOVvolNB * PeakLngthNB)

            # Update the widget with the result
            Non_HOV_Vol_year20peak_modelcalc_widget.value = round(Non_HOV_Volume_Year20Peak, 2)

        except Exception:
            # In case of error, set default value to 0
            Non_HOV_Vol_year20peak_modelcalc_widget.value = 0


    projectinfo_widgets.subcategory_dropdown.observe(update_Non_HOV_Year20Peak_Volume, names='value')
    projectinfo_widgets.HOV_lane_nobuild_widget.observe(update_Non_HOV_Year20Peak_Volume, names='value')
    projectinfo_widgets.peak_period_widget.observe(update_Non_HOV_Year20Peak_Volume, names='value')
    projectinfo_widgets.percent_traffic_weave_no_build_widget.observe(update_Non_HOV_Year20Peak_Volume, names='value')
    projectinfo_widgets.departure_rate_forecast_year_no_build_widget.observe(update_Non_HOV_Year20Peak_Volume, names='value')
    projectinfo_widgets.adt_base_year_no_build_widget.observe(update_Non_HOV_Year20Peak_Volume, names='value')
    projectinfo_widgets.ADT_20NB_widget.observe(update_Non_HOV_Year20Peak_Volume, names='value')
    projectinfo_widgets.departure_rate_forecast_year_build_widget.observe(update_Non_HOV_Year20Peak_Volume, names='value')


       
    # Non-HOV PNV1NB update function (similar to PHV20NB)
    def calculate_pnv20nb(change):
        # Access the user-modified value directly from the widget
        if isinstance(Non_HOV_Vol_year20peak_userchanged_widget.value, (int, float)) and Non_HOV_Vol_year20peak_userchanged_widget.value >= 0:
            PNV20NB = Non_HOV_Vol_year20peak_userchanged_widget.value  # Use the user-modified value if valid
        else:
            PNV20NB = Non_HOV_Vol_year20peak_modelcalc_widget.value  # Use the model value if the user value is invalid

        # Update the value of PNV1NB widget
        PNV20NB_widget.value = PNV20NB

    # Link the PNV1NB widget update to changes in Non-HOV Volume Peak User widget
    Non_HOV_Vol_year20peak_modelcalc_widget.observe(calculate_pnv20nb, names='value')
    Non_HOV_Vol_year20peak_userchanged_widget.observe(calculate_pnv20nb, names='value')    

    # Combine all the Non-HOV volume widgets into a horizontal layout for display
    Non_HOV_vol_year20peak_widgets = widgets.HBox([Non_HOV_Vol_year20peak_modelcalc_widget, Non_HOV_Vol_year20peak_userchanged_widget, PNV20NB_explanation_widget])
    
    ###################################################################
       
    # Weaving Volume (Calculated by Model)
    weaving_volume_year20peak_modelcalc_widget = widgets.IntText(
        value=0,  # Set initial value to 0 or any other valid integer
        description="Weaving Volume (Calculated by Model):",
        disabled=True,  # Make it read-only so the user cannot modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Weaving Volume (User-modified value)
    weaving_volume_year20peak_userchanged_widget = widgets.Text(
        value='',  # Initially set to 0 or a valid integer value
        description="Weaving Volume (Changed by User):",
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Weaving Volume (Used for Project Evaluation)
    PWV20NB_widget = widgets.IntText(
        value=weaving_volume_year20peak_modelcalc_widget.value,  # Set initially to the calculated value
        description="Weaving Volume (Used for Proj Evaluation):",
        disabled=True,  # Make it read-only
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Explanation widget for user-modified values
    PWV20NB_explanation_widget = widgets.Text(
        value=None,  # Allow users to enter a text explanation
        description="Reasons for Change:",  # Label for the input field
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,  # Optional layout style, if needed
        style={'description_width': 'initial'}  # Optional style for description width
    )
    
    # Update Weaving Volume Calculation based on widget values
    def update_weaving_year20peak_volume(change):
        # Look up the TMS adjustment factor
        TMS_value = TMSAdj.get(TMSLookup, {}).get("VolumeWithout", 1)

        # Initialize total weaving volume model for year 20 peak
        Weaving_Volume_Model_20peak = 0

        # First condition
        if ProjType in ["Auxiliary Lane", "Off-Ramp Widening"]:
            Weaving_Volume_Model_20peak += (PerPeakADT * ADT20NB) * (PerWeaveNB - PerTruckNB) * TMS_value

        # Second condition:
        if ProjType == "Auxiliary Lane":
            Weaving_Volume_Model_20peak += RampVolP * PeakLngthNB

        # Third condition: IF(OR(HOVConn,HOVDrop), ...)
        if ProjType in ["HOV Connector", "HOV Drop Ramp"]:
            Weaving_Volume_Model_20peak += PerWeaveNB * HOVvolNB * PeakLngthNB

        # Update the widget with the calculated value
        weaving_volume_year20peak_modelcalc_widget.value = round(Weaving_Volume_Model_20peak, 0)
        
    # Link the update function to changes in relevant widgets
    projectinfo_widgets.ADT_20NB_widget.observe(update_weaving_year20peak_volume, names='value')
    projectinfo_widgets.percent_traffic_weave_no_build_widget.observe(update_weaving_year20peak_volume, names='value')
    projectinfo_widgets.percent_traffic_weave_build_widget.observe(update_weaving_year20peak_volume, names='value')
    projectinfo_widgets.percent_trucks_nobuild_widget.observe(update_weaving_year20peak_volume, names='value')
    projectinfo_widgets.hourly_ramp_volume_peak_widget.observe(update_weaving_year20peak_volume, names='value')
    projectinfo_widgets.peak_period_widget.observe(update_weaving_year20peak_volume, names='value')
    projectinfo_widgets.HOV_lane_nobuild_widget.observe(update_weaving_year20peak_volume, names='value')
    projectinfo_widgets.subcategory_dropdown.observe(update_weaving_year20peak_volume, names='value') 
        
 # Non-HOV PNV1NB update function (similar to PHV20NB)
    def calculate_pwv20nb(change):
        # Access the user-modified value directly from the widget
        if isinstance(weaving_volume_year20peak_userchanged_widget.value, (int, float)) and weaving_volume_year20peak_userchanged_widget.value >= 0:
            PWV20NB = weaving_volume_year20peak_userchanged_widget.value  # Use the user-modified value if valid
        else:
            PWV20NB = weaving_volume_year20peak_modelcalc_widget.value  # Use the model value if the user value is invalid

        # Update the value of PNV1NB widget
        PWV20NB_widget.value = PWV20NB

    # Link the PNV1NB widget update to changes in Non-HOV Volume Peak User widget
    weaving_volume_year20peak_modelcalc_widget.observe(calculate_pwv20nb, names='value')
    weaving_volume_year20peak_userchanged_widget.observe(calculate_pwv20nb, names='value')    

    # Combine all the Non-HOV volume widgets into a horizontal layout for display
    Weaving_Volume_year20peak_widgets = widgets.HBox([weaving_volume_year20peak_modelcalc_widget, weaving_volume_year20peak_userchanged_widget, PWV20NB_explanation_widget])
        

    ###################################################################
    # Truck Volume (Calculated by Model)
    truck_volume_year20peak_modelcalc_widget = widgets.IntText(
        value=0,  # Set initial value to 0 or any other valid integer
        description="Truck Volume (Calculated by Model):",
        disabled=True,  # Make it read-only so the user cannot modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Truck Volume (User-modified value)
    truck_volume_year20peak_userchanged_widget = widgets.Text(
        value='',  # Initially set to 0 or a valid integer value
        description="Truck Volume (Changed by User):",
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Truck Volume (Used for Project Evaluation)
    PTV20NB_widget = widgets.IntText(
        value=truck_volume_year20peak_modelcalc_widget.value,  # Set initially to the calculated value
        description="Truck Volume (Used for Proj Evaluation):",
        disabled=True,  # Make it read-only
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Explanation widget for user-modified values
    PTV20NB_explanation_widget = widgets.Text(
        value=None,  # Allow users to enter a text explanation
        description="Reasons for Change:",  # Label for the input field
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,  # Optional layout style, if needed
        style={'description_width': 'initial'}  # Optional style for description width
    )
    
    # Update Truck Volume Calculation based on widget values
    def update_truck_peakyear20_volume(change):
        # Look up the TMS volume adjustment factor
        TMS_value = TMSAdj.get(TMSLookup, {}).get("VolumeWithout", 1)

        # Check if it's a Highway Rail Grade Crossing project
        if ProjType == "Hwy-Rail Grade Crossing":
            truck_volume = 0
        else:
            if ProjType == "Queuing":
                try:
                    numerator = PeakLngthNB * (DepRate1 - ADT1NB * (1 - PerPeakADT) / (24 - PeakLngthNB))
                    denominator = ((ADT1NB / ADT20NB) * DepRate20 - ADT1NB * (1 - PerPeakADT) / (24 - PeakLngthNB))
                    base_volume = (numerator / denominator) * DepRate20
                except ZeroDivisionError:
                    base_volume = 0  # Prevent crash from division by zero
            else:
                base_volume = PerPeakADT * ADT20NB

            truck_volume = base_volume * PerTruckNB * TMS_value

        # Update the widget with the calculated truck volume
        truck_volume_year20peak_modelcalc_widget.value = round(truck_volume, 0)
        
    projectinfo_widgets.adt_base_year_no_build_widget.observe(update_truck_peakyear20_volume, names='value')
    projectinfo_widgets.ADT_20NB_widget.observe(update_truck_peakyear20_volume, names='value')
    projectinfo_widgets.percent_trucks_nobuild_widget.observe(update_truck_peakyear20_volume, names='value')
    projectinfo_widgets.peak_period_widget.observe(update_truck_peakyear20_volume, names='value')
    projectinfo_widgets.departure_rate_forecast_year_no_build_widget.observe(update_truck_peakyear20_volume, names='value')
    projectinfo_widgets.departure_rate_forecast_year_build_widget.observe(update_truck_peakyear20_volume, names='value')
    projectinfo_widgets.subcategory_dropdown.observe(update_truck_peakyear20_volume, names='value') 
    
 # Non-HOV PNV1NB update function (similar to PHV20NB)
    def calculate_ptv20nb(change):
        # Access the user-modified value directly from the widget
        if isinstance(truck_volume_year20peak_userchanged_widget.value, (int, float)) and truck_volume_year20peak_userchanged_widget.value >= 0:
            PTV20NB = truck_volume_year20peak_userchanged_widget.value  # Use the user-modified value if valid
        else:
            PTV20NB = truck_volume_year20peak_modelcalc_widget.value  # Use the model value if the user value is invalid

        # Update the value of PNV1NB widget
        PTV20NB_widget.value = PTV20NB

    # Link the PNV1NB widget update to changes in Non-HOV Volume Peak User widget
    truck_volume_year20peak_modelcalc_widget.observe(calculate_ptv20nb, names='value')
    truck_volume_year20peak_userchanged_widget.observe(calculate_ptv20nb, names='value')    

    # Combine all the Non-HOV volume widgets into a horizontal layout for display
    Truck_Volume_year20peak_widgets = widgets.HBox([truck_volume_year20peak_modelcalc_widget, truck_volume_year20peak_userchanged_widget, PTV20NB_explanation_widget])
    
    ###################################################################
    # Non-HOV Speed widgets 
    nonhov_speed_year20peak_modelcalc_widget = widgets.IntText(
        value=0,  # Set initial value to 0 or any other valid integer
        description="Non-HOV Speed (Calculated by Model):",
        disabled=True,  # Make it read-only so the user cannot modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    nonhov_speed_year20peak_userchanged_widget = widgets.Text(
        value='',  # Initially set to 0 or a valid integer value
        description="Non-HOV Speed (Changed by User):",
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Non-HOV Speed Volume (Used for Project Evaluation)
    PNS20NB_widget = widgets.IntText(
        value=nonhov_speed_year20peak_modelcalc_widget.value,  # Set initially to the calculated value
        description="Non-HOV Speed (Used for Proj Evaluation):",
        disabled=True,  # Make it read-only
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Explanation widget for user-modified values
    PNS20NB_explanation_widget = widgets.Text(
        value=None,  # Allow users to enter a text explanation
        description="Reasons for Change:",  # Label for the input field
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,  # Optional layout style, if needed
        style={'description_width': 'initial'}  # Optional style for description width
    )    
    
    def update_nonhov_year20peak_speed(change=None):
        # Accessing the relevant traffic volume widgets (PHV20NB, PNV20NB, PWV20NB, PTV20NB)
        traffic_volumes = [
            PHV20NB_widget.value,  
            PNV20NB_widget.value,  
            PWV20NB_widget.value,  
            PTV20NB_widget.value   
        ]

        sum_all = sum(traffic_volumes)

        # Step 1: Formula for Non-HOV Speed calculation
        if sum_all == 0:
            nonhov_speed = 55  # If total volume is zero, use default value
        else:
            if ProjType == "Queuing":
                # Special case for queuing calculation
                try:
                    part1 = (
                        PeakLngthNB / DepRate20 / 2
                        * (ArrRate20 - DepRate20)
                        * (DepRate1 - ADT1NB * (1 - PerPeakADT) / (24 - PeakLngthNB))
                        / (ArrRate1 - ADT1NB * (1 - PerPeakADT) / (24 - PeakLngthNB))
                    )
                except ZeroDivisionError:
                    part1 = float("inf")

                nonhov_speed = ImpactedNB / (max(part1, 0) + ImpactedNB / FFSpeedNB)
            else:
                # Normal speed calculation using "No Build" parameters from the formula
                flow_sum = sum(traffic_volumes[1:]) if HOVLanesNB != 0 else sum(traffic_volumes)

                # Access the "No Build" parameters from the roadway_capacity_non_HOV dictionary
                capacity_params = roadway_capacity_non_HOV["Non-HOV Lanes"]["No Build"]
                GenAlphaNB = capacity_params["GenAlphaNB"]
                GenBetaNB = capacity_params["GenBetaNB"]
                GenLaneCapNB = capacity_params["GenLaneCapNB"]

                # Apply the speed calculation formula
                volume_term = flow_sum / (GenLanesNB * GenLaneCapNB * PeakLngthNB)
                delay_speed = FFSpeedNB / (IRI20NB * (1 + GenAlphaNB * min(volume_term, MaxVC) ** GenBetaNB))
                base_speed = delay_speed * TMSAdj[TMSLookup][1]

                if ProjType == "Passing":
                    nonhov_speed = (TruckSpeed + FFSpeedNB) / 2
                else:
                    nonhov_speed = min(base_speed, FFSpeedNB)

        # === Apply adjustments based on project type ===

        # Adjust for Freeway Connector using SpeedWeaveAdj
        if ProjType == "Freeway Connector":
            nonhov_speed *= SpeedWeaveAdj.get(PerWeaveNB, {"Freeway": 1.0})["Freeway"]

        # Adjust for HOV Connector / Drop Ramp using SpeedWeaveAdj
        if ProjType in ["HOV Connector", "HOV Drop Ramp"]:
            nonhov_speed *= SpeedWeaveAdj.get(PerWeaveNB, {"HOV": 1.0})["HOV"]

        # Apply pavement condition adjustments using SpeedPavAdj
        closest_iri_key = min(SpeedPavAdj.keys(), key=lambda x: abs(x - IRI20NB))
        nonhov_speed *= SpeedPavAdj[closest_iri_key]["Auto"]

        # Update the widget with the final calculated speed value
        nonhov_speed_year20peak_modelcalc_widget.value = round(nonhov_speed, 1)

    # Trigger the calculation once or observe widget changes
    update_nonhov_year20peak_speed()  # To calculate initially


    # Link the update function to changes in relevant widgets
    PHV20NB_widget.observe(update_nonhov_year20peak_speed, names='value')
    PNV20NB_widget.observe(update_nonhov_year20peak_speed, names='value')
    PWV20NB_widget.observe(update_nonhov_year20peak_speed, names='value')
    PTV20NB_widget.observe(update_nonhov_year20peak_speed, names='value')
    projectinfo_widgets.subcategory_dropdown.observe(update_nonhov_year20peak_speed, names='value')  # ProjType
    projectinfo_widgets.peak_period_widget.observe(update_nonhov_year20peak_speed, names='value')     # PeakLngthNB
    projectinfo_widgets.departure_rate_forecast_year_build_widget.observe(update_nonhov_year20peak_speed, names='value')  # DepRate20
    projectinfo_widgets.departure_rate_forecast_year_no_build_widget.observe(update_nonhov_year20peak_speed, names='value')  # DepRate1
    projectinfo_widgets.arrival_rate_base_year_build_widget.observe(update_nonhov_year20peak_speed, names='value')  # ArrRate20
    projectinfo_widgets.arrival_rate_base_year_no_build_widget.observe(update_nonhov_year20peak_speed, names='value')  # ArrRate1
    projectinfo_widgets.adt_base_year_no_build_widget.observe(update_nonhov_year20peak_speed, names='value')  # ADT1NB
    projectinfo_widgets.free_flow_speed_no_build_widget.observe(update_nonhov_year20peak_speed, names='value')  # FFSpeedNB
    projectinfo_widgets.impacted_length_no_build_widget.observe(update_nonhov_year20peak_speed, names='value')  # ImpactedNB
    projectinfo_widgets.general_traffic_lanes_no_build_widget.observe(update_nonhov_year20peak_speed, names='value')  # GenLanesNB
    projectinfo_widgets.hov_hot_lanes_no_build_widget.observe(update_nonhov_year20peak_speed, names='value')  # HOVLanesNB
    projectinfo_widgets.percent_traffic_weave_no_build_widget.observe(update_nonhov_year20peak_speed, names='value')  # PerWeaveNB
    projectinfo_widgets.iri_forecast_year_no_build_widget.observe(update_nonhov_year20peak_speed, names='value')  # IRI20NB
    
    def calculate_pns20nb(change):
        # Access the user-modified value directly from the widget
        if isinstance(nonhov_speed_year20peak_userchanged_widget.value, (int, float)) and nonhov_speed_year20peak_userchanged_widget.value >= 0:
            updated_NonHOV_year20peak_speed = max(nonhov_speed_year20peak_userchanged_widget.value, 5)  # Ensure the speed is at least 5
        else:
            updated_NonHOV_year20peak_speed = max(nonhov_speed_year20peak_modelcalc_widget.value, 5)  # Use the model value if the user value is invalid

        # Update the value of PNS20NB widget
        PNS20NB_widget.value = updated_NonHOV_year20peak_speed


    nonhov_speed_year20peak_userchanged_widget.observe(calculate_pns20nb, names='value')

    # Combine into layout
    NonHOV_Year20Peak_Speed_widgets = widgets.HBox([nonhov_speed_year20peak_modelcalc_widget, nonhov_speed_year20peak_userchanged_widget, PNS20NB_explanation_widget])
    
    ###################################################################        
     # HOV Speed widgets for Year 20
    hov_speed_year20peak_modelcalc_widget = widgets.IntText(
        value=0,
        description="HOV Speed (Calculated by Model):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    hov_speed_year20peak_userchanged_widget = widgets.Text(
        value='',
        description="HOV Speed (Changed by User):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    PHS20NB_widget = widgets.IntText(
        value=hov_speed_year20peak_modelcalc_widget.value,
        description="HOV Speed (Used for Proj Evaluation):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    PHS20NB_explanation_widget = widgets.Text(
        value=None,
        description="Reasons for Change:",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )


    def update_hov_year20peak_speed(change=None):
        # Grab HOV capacity parameters
        hov_capacity_params = roadway_capacity["HOV Lanes"]
        HOVAlpha = hov_capacity_params["HOVAlpha"]
        HOVBeta = hov_capacity_params["HOVBeta"]
        HOVLaneCap = hov_capacity_params["HOVLaneCap"]

        PHV20NB = PHV20NB_widget.value

        if PHV20NB == 0:
            hov_speed = 55

        elif HOVLanesNB == 0:
            hov_speed = PNS20NB_widget.value

        elif ProjType == "Queuing":
            try:
                queue_denom = (
                    PeakLngthNB / DepRate20 / 2
                    * (ArrRate20 - DepRate20)
                    * (DepRate1 - ADT1NB * (1 - PerPeakADT) / (24 - PeakLngthNB))
                    / (ArrRate1 - ADT1NB * (1 - PerPeakADT) / (24 - PeakLngthNB))
                )
            except ZeroDivisionError:
                queue_denom = float("inf")

            hov_speed = ImpactedNB / (max(queue_denom, 0) + ImpactedNB / FFSpeedNB)

        else:
            try:
                volume_term = PHV20NB / (HOVLanesNB * HOVLaneCap * PeakLngthNB)
                base_speed = FFSpeedNB / (1 + HOVAlpha * min(volume_term, MaxVC) ** HOVBeta)
            except ZeroDivisionError:
                base_speed = 0

            closest_iri_key = min(SpeedPavAdj.keys(), key=lambda x: abs(x - IRI20NB))
            pavement_adj = SpeedPavAdj[closest_iri_key]["Auto"]

            hov_speed = base_speed * pavement_adj

        hov_speed_year20peak_modelcalc_widget.value = round(hov_speed, 1)

    update_hov_year20peak_speed()
    
    # === Observers to trigger speed update ===
    PHV20NB_widget.observe(update_hov_year20peak_speed, names='value')
    PNS20NB_widget.observe(update_hov_year20peak_speed, names='value')
    projectinfo_widgets.subcategory_dropdown.observe(update_hov_year20peak_speed, names='value')
    projectinfo_widgets.impacted_length_no_build_widget.observe(update_hov_year20peak_speed, names='value')
    projectinfo_widgets.peak_period_widget.observe(update_hov_year20peak_speed, names='value')
    projectinfo_widgets.departure_rate_forecast_year_build_widget.observe(update_hov_year20peak_speed, names='value')
    projectinfo_widgets.arrival_rate_base_year_build_widget.observe(update_hov_year20peak_speed, names='value')
    projectinfo_widgets.departure_rate_forecast_year_no_build_widget.observe(update_hov_year20peak_speed, names='value')
    projectinfo_widgets.arrival_rate_base_year_no_build_widget.observe(update_hov_year20peak_speed, names='value')
    projectinfo_widgets.adt_base_year_no_build_widget.observe(update_hov_year20peak_speed, names='value')
    projectinfo_widgets.percent_induced_trip_widget.observe(update_hov_year20peak_speed, names='value')
    projectinfo_widgets.hov_hot_lanes_no_build_widget.observe(update_hov_year20peak_speed, names='value')
    projectinfo_widgets.free_flow_speed_no_build_widget.observe(update_hov_year20peak_speed, names='value')
    projectinfo_widgets.iri_forecast_year_no_build_widget.observe(update_hov_year20peak_speed, names='value')


    def calculate_phs20nb(change):
        # Access the user-modified value directly from the widget
        if isinstance(hov_speed_year20peak_userchanged_widget.value, (int, float)) and hov_speed_year20peak_userchanged_widget.value >= 0:
            updated_HOV_year20peak_speed = max(hov_speed_year20peak_userchanged_widget.value, 5)  # Ensure the speed is at least 5
        else:
            updated_HOV_year20peak_speed = max(hov_speed_year20peak_modelcalc_widget.value, 5)  # Use the model value if the user value is invalid

        # Update the value of PNS20NB widget
        PHS20NB_widget.value = updated_HOV_year20peak_speed


    hov_speed_year20peak_userchanged_widget.observe(calculate_phs20nb, names='value')

    # Combine into layout
    HOV_Year20Peak_Speed_widgets = widgets.HBox([hov_speed_year20peak_modelcalc_widget, hov_speed_year20peak_userchanged_widget, PHS20NB_explanation_widget])
    
    ###################################################################    
    # Weaving Speed widgets 
    weave_speed_year20peak_modelcalc_widget = widgets.IntText(
        value=0,  # Set initial value to 0 or any other valid integer
        description="Weaving Speed (Calculated by Model):",
        disabled=True,  # Make it read-only so the user cannot modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    weave_speed_year20peak_userchanged_widget = widgets.Text(
        value='',  # Initially set to 0 or a valid integer value
        description="Weaving Speed (Changed by User):",
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Non-HOV Speed Volume (Used for Project Evaluation)
    PWS20NB_widget = widgets.IntText(
        value=weave_speed_year20peak_modelcalc_widget.value,  # Set initially to the calculated value
        description="Weaving Speed (Used for Proj Evaluation):",
        disabled=True,  # Make it read-only
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Explanation widget for user-modified values
    PWS20NB_explanation_widget = widgets.Text(
        value=None,  # Allow users to enter a text explanation
        description="Reasons for Change:",  # Label for the input field
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,  # Optional layout style, if needed
        style={'description_width': 'initial'}  # Optional style for description width
    )

    def update_year20peak_weave_speed(change=None):
        try:
            # Retrieve relevant widget values
            PWV20NB = PWV20NB_widget.value
            PNS20NB = PNS20NB_widget.value
            PTV20NB = PTV20NB_widget.value

            # Check if the value of PWV20NB is 0
            if PWV20NB == 0:
                Year20PeakWeaveSpeed = 55
            else:
                # If ProjType is Auxiliary Lane or Off-Ramp Widening, perform the calculation
                if ProjType == "Auxiliary Lane" or ProjType == "Off-Ramp Widening":
                    # Applying the formula for calculating adjusted speed
                    exponent_part = math.exp((PWV20NB + PTV20NB) / NumDirections / PeakLngthNB / 1000)
                    part1 = FFSpeedNB - (FFSpeedNB - 42) * (0.321 + 0.0039 * exponent_part - 0.002 * (1083 if ProjType == "Off-Ramp Widening" else SegmentNB * 5280) * RampFFSpdNB / 1000)
                    adjusted_speed = 1.1 * part1

                    # If ProjType is Pavement, apply pavement adjustment using SpeedPavAdj
                    if ProjType == "Pavement":
                        # Perform the lookup in SpeedPavAdj for the given IRI20NB
                        closest_iri_key = min(SpeedPavAdj.keys(), key=lambda x: abs(x - IRI20NB))
                        speed_adj = SpeedPavAdj[closest_iri_key]["Auto"]  # Use "Auto" adjustment factor

                        # Adjust the speed based on the pavement condition
                        adjusted_speed *= speed_adj

                    # Apply the lookup adjustment for TMS
                    tms_adj = TMSAdj.get(TMSLookup, [1.0])[1]  # Default to 1 if no match in TMSAdj

                    # Final calculated speed considering the adjustments
                    Year20PeakWeaveSpeed = max(5, min(PNS20NB, adjusted_speed * tms_adj))

                else:
                    # If not Auxiliary Lane or Off-Ramp Widening, just use PNS20NB
                    Year20PeakWeaveSpeed = PNS20NB

            # Update the widget with the calculated result
            weave_speed_year20peak_modelcalc_widget.value = round(Year20PeakWeaveSpeed, 2)

        except Exception:
            # In case of any error, set the result to 0 without printing anything
            weave_speed_year20peak_modelcalc_widget.value = 0

    # Initial call to set the value based on the current widget state
    update_year20peak_weave_speed()

    # Add observers to trigger the function when relevant widget values change
    PWV20NB_widget.observe(update_year20peak_weave_speed, names='value')
    PNS20NB_widget.observe(update_year20peak_weave_speed, names='value')
    PTV20NB_widget.observe(update_year20peak_weave_speed, names='value')
    projectinfo_widgets.subcategory_dropdown.observe(update_year20peak_weave_speed, names='value')
    projectinfo_widgets.free_flow_speed_no_build_widget.observe(update_year20peak_weave_speed, names='value')
    projectinfo_widgets.ramp_design_speed_no_build_widget.observe(update_year20peak_weave_speed, names='value')
    projectinfo_widgets.hov_hot_lanes_no_build_widget.observe(update_year20peak_weave_speed, names='value')
    projectinfo_widgets.highway_segment_no_build_widget.observe(update_year20peak_weave_speed, names='value')
    projectinfo_widgets.iri_forecast_year_no_build_widget.observe(update_year20peak_weave_speed, names='value')

    def calculate_pws20nb(change):
        # Access the user-modified value directly from the widget
        if isinstance(weave_speed_year20peak_userchanged_widget.value, (int, float)) and weave_speed_year20peak_userchanged_widget.value >= 0:
            updated_Weave_year20peak_speed = max(weave_speed_year20peak_userchanged_widget.value, 5)  # Ensure the speed is at least 5
        else:
            updated_Weave_year20peak_speed = max(weave_speed_year20peak_modelcalc_widget.value, 5)  # Use the model value if the user value is invalid

        # Update the value of PWS20NB widget (project evaluation widget)
        PWS20NB_widget.value = updated_Weave_year20peak_speed

    # Link the function to the user input widget change
    weave_speed_year20peak_userchanged_widget.observe(calculate_pws20nb, names='value')

    # Combine into layout for display
    Weave_Year20Peak_Speed_widgets = widgets.HBox([weave_speed_year20peak_modelcalc_widget, weave_speed_year20peak_userchanged_widget, PWS20NB_explanation_widget])

    ###################################################################
    # Truck Speed widgets 
    truck_speed_year20peak_modelcalc_widget = widgets.IntText(
        value=0,  # Set initial value to 0 or any other valid integer
        description="Truck Speed (Calculated by Model):",
        disabled=True,  # Make it read-only so the user cannot modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    truck_speed_year20peak_userchanged_widget = widgets.Text(
        value='',  # Initially set to 0 or a valid integer value
        description="Truck Speed (Changed by User):",
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Non-HOV Speed Volume (Used for Project Evaluation)
    PTS20NB_widget = widgets.IntText(
        value=truck_speed_year20peak_modelcalc_widget.value,  # Set initially to the calculated value
        description="Truck Speed (Used for Proj Evaluation):",
        disabled=True,  # Make it read-only
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Explanation widget for user-modified values
    PTS20NB_explanation_widget = widgets.Text(
        value=None,  # Allow users to enter a text explanation
        description="Reasons for Change:",  # Label for the input field
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,  # Optional layout style, if needed
        style={'description_width': 'initial'}  # Optional style for description width
    )

    def update_year20peak_truck_speed(change=None):
        try:
            # Retrieve relevant widget values
            PTV20NB = PTV20NB_widget.value
            PWS20NB = PWS20NB_widget.value
            PNS20NB = PNS20NB_widget.value

            # Check if the value of PTV20NB is 0
            if PTV20NB == 0:
                Year20PeakTruckSpeed = 55
            else:
                # If ProjType is Auxiliary Lane or Off-Ramp Widening, perform the calculation
                if ProjType == "Auxiliary Lane" or ProjType == "Off-Ramp Widening":
                    # Formula for truck speed adjustment based on pavement and other factors
                    if ProjType == "Pavement":  # Check if the project type is Pavement
                        # Perform the lookup in SpeedPavAdj for the given IRI20NB
                        closest_iri_key = min(SpeedPavAdj.keys(), key=lambda x: abs(x - IRI20NB))
                        speed_adj_auto = SpeedPavAdj[closest_iri_key]["Auto"]
                        speed_adj_truck = SpeedPavAdj[closest_iri_key]["Truck"]
                    else:
                        speed_adj_auto = 1
                        speed_adj_truck = 1

                    adjusted_speed = min(TruckSpeed, PWS20NB if ProjType in ["Auxiliary Lane", "Off-Ramp Widening"] else PNS20NB) * speed_adj_truck

                    # Apply pavement adjustment if necessary
                    if ProjType == "Pavement":
                        adjusted_speed *= speed_adj_auto

                    # Final calculated truck speed
                    Year20PeakTruckSpeed = max(5, adjusted_speed)

                else:
                    # If not Auxiliary Lane or Off-Ramp Widening, just use PNS20NB
                    Year20PeakTruckSpeed = PNS20NB

            # Update the widget with the calculated result
            truck_speed_year20peak_modelcalc_widget.value = round(Year20PeakTruckSpeed, 2)

        except Exception:
            # In case of any error, set the result to 0 without printing anything
            truck_speed_year20peak_modelcalc_widget.value = 0

    # Initial call to set the value based on the current widget state
    update_year20peak_truck_speed()

    # Add observers to trigger the function when relevant widget values change
    PTV20NB_widget.observe(update_year20peak_truck_speed, names='value')
    PWS20NB_widget.observe(update_year20peak_truck_speed, names='value')
    PNS20NB_widget.observe(update_year20peak_truck_speed, names='value')
    projectinfo_widgets.subcategory_dropdown.observe(update_year20peak_truck_speed, names='value')
    projectinfo_widgets.free_flow_speed_no_build_widget.observe(update_year20peak_truck_speed, names='value')
    projectinfo_widgets.iri_forecast_year_no_build_widget.observe(update_year20peak_truck_speed, names='value')
    projectinfo_widgets.truck_speed_widget.observe(update_year20peak_truck_speed, names='value')

    def calculate_pts20nb(change):
        # Access the user-modified value directly from the widget
        if isinstance(truck_speed_year20peak_userchanged_widget.value, (int, float)) and truck_speed_year20peak_userchanged_widget.value >= 0:
            updated_Truck_year20peak_speed = max(truck_speed_year20peak_userchanged_widget.value, 5)  # Ensure the speed is at least 5
        else:
            updated_Truck_year20peak_speed = max(truck_speed_year20peak_modelcalc_widget.value, 5)  # Use the model value if the user value is invalid

        # Update the value of PTS20NB widget (project evaluation widget)
        PTS20NB_widget.value = updated_Truck_year20peak_speed

    # Link the function to the user input widget change
    truck_speed_year20peak_userchanged_widget.observe(calculate_pts20nb, names='value')

    # Combine into layout for display
    Truck_Year20Peak_Speed_widgets = widgets.HBox([truck_speed_year20peak_modelcalc_widget, truck_speed_year20peak_userchanged_widget, PTS20NB_explanation_widget])
    
######################################################################################################################################################################
############################### NonPeak Period ###############################

    # Non-HOV Volume Year 20 Non-Peak widgets
    non_hov_vol_year20nonpeak_modelcalc_widget = widgets.IntText(
        value=0,  # Set initial value to 0 or any other valid integer
        description="Non-HOV Volume (Calculated by Model):",
        disabled=True,  # Make it read-only so the user cannot modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    non_hov_vol_year20nonpeak_userchanged_widget = widgets.Text(
        value='',  # Initially set to 0 or a valid integer value
        description="Non-HOV Volume (Changed by User):",
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Non-HOV Speed Volume (Used for Project Evaluation)
    NNV20NB_widget = widgets.IntText(
        value=non_hov_vol_year20nonpeak_modelcalc_widget.value,  # Set initially to the calculated value
        description="Non-HOV Volume (Used for Project Evaluation):",
        disabled=True,  # Make it read-only
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Explanation widget for user-modified values
    NNV20NB_explanation_widget = widgets.Text(
        value=None,  # Allow users to enter a text explanation
        description="Reasons for Change:",  # Label for the input field
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,  # Optional layout style, if needed
        style={'description_width': 'initial'}  # Optional style for description width
    )

    def update_NonHOV_year20nonpeak_Volume(change=None):
        try:
            if ProjType == "Hwy-Rail Grade Crossing":
                # Formula for highway rail case
                NonHOV_year20nonpeak_Volume = (ArrRate20 * GateTime20 / 60) / (1 - ArrRate20 / DepRate20) * NumTrain20 / AnnualFactor * (1 - PerTruckNB)
            elif ProjType == "Queuing":
                # Formula for queuing case
                NonHOV_year20nonpeak_Volume = (ADT20NB - PeakLngthNB * (DepRate1 - ADT1NB * (1 - PerPeakADT) / (24 - PeakLngthNB)) /
                                              (ADT1NB / ADT20NB * DepRate20 - ADT1NB * (1 - PerPeakADT) / (24 - PeakLngthNB)) * DepRate20)
            else:
                # Formula for regular case
                NonHOV_year20nonpeak_Volume = (1 - PerPeakADT) * ADT20NB

            # Apply adjustment based on Auxiliary Lane or Off-Ramp Widening
            if ProjType == "Auxiliary Lane" or ProjType == "Off-Ramp Widening":
                NonHOV_year20nonpeak_Volume *= (1 - PerWeaveNB)
            else:
                NonHOV_year20nonpeak_Volume *= (1 - PerTruckNB)

            # Update the widget with the calculated result
            non_hov_vol_year20nonpeak_modelcalc_widget.value = round(NonHOV_year20nonpeak_Volume, 2)  # Variable: NonHOV_year20nonpeak_Volume

        except Exception:
            # In case of any error, set the result to 0 without printing anything
            non_hov_vol_year20nonpeak_modelcalc_widget.value = 0


    # Initial call to set the value based on the current widget state
    update_NonHOV_year20nonpeak_Volume()

    # Add observers to trigger the function when relevant widget values change
    projectinfo_widgets.subcategory_dropdown.observe(update_NonHOV_year20nonpeak_Volume, names='value')  # Variable: ProjType
    projectinfo_widgets.arrival_rate_base_year_no_build_widget.observe(update_NonHOV_year20nonpeak_Volume, names='value')  # Variable: ArrRate20
    projectinfo_widgets.GateTime20_widget.observe(update_NonHOV_year20nonpeak_Volume, names='value')  # Variable: GateTime20
    projectinfo_widgets.NumTrain20_widget.observe(update_NonHOV_year20nonpeak_Volume, names='value')  # Variable: NumTrain20
    projectinfo_widgets.percent_trucks_nobuild_widget.observe(update_NonHOV_year20nonpeak_Volume, names='value')  # Variable: PerTruckNB
    projectinfo_widgets.ADT_20NB_widget.observe(update_NonHOV_year20nonpeak_Volume, names='value')  # Variable: ADT20NB
    projectinfo_widgets.departure_rate_forecast_year_no_build_widget.observe(update_NonHOV_year20nonpeak_Volume, names='value')  # Variable: DepRate1
    projectinfo_widgets.adt_base_year_no_build_widget.observe(update_NonHOV_year20nonpeak_Volume, names='value')  # Variable: ADT1NB
    projectinfo_widgets.peak_period_widget.observe(update_NonHOV_year20nonpeak_Volume, names='value')  # Variable: PeakLngthNB
    projectinfo_widgets.percent_traffic_weave_no_build_widget.observe(update_NonHOV_year20nonpeak_Volume, names='value')  # Variable: PerWeaveNB
    projectinfo_widgets.departure_rate_forecast_year_build_widget.observe(update_NonHOV_year20nonpeak_Volume, names='value')  # Variable: DepRate20

    def calculate_nnv20nb(change):
        # Access the user-modified value directly from the widget
        if isinstance(non_hov_vol_year20nonpeak_userchanged_widget.value, (int, float)) and non_hov_vol_year20nonpeak_userchanged_widget.value >= 0:
            updated_NonHOV_year20nonpeak_vol = max(non_hov_vol_year20nonpeak_userchanged_widget.value, 0)  # Ensure volume is not negative
        else:
            updated_NonHOV_year20nonpeak_vol = max(non_hov_vol_year20nonpeak_modelcalc_widget.value, 0)  # Use the model value if the user value is invalid

        # Update the value of NonHOV_year20nonpeak widget (project evaluation widget)
        NNV20NB_widget.value = updated_NonHOV_year20nonpeak_vol  # Variable: NonHOV_year20nonpeak_modelcalc_widget

    # Link the function to the user input widget change
    non_hov_vol_year20nonpeak_userchanged_widget.observe(calculate_nnv20nb, names='value')  

    # Combine into layout for display
    Non_HOV_Vol_year20nonpeak_widgets = widgets.HBox([non_hov_vol_year20nonpeak_modelcalc_widget, non_hov_vol_year20nonpeak_userchanged_widget, NNV20NB_explanation_widget])

    ###################################################################
    # Weaving Volume Year 20 Non-Peak widgets
    weaving_vol_year20nonpeak_modelcalc_widget = widgets.IntText(
        value=0,  # Set initial value to 0 or any other valid integer
        description="Weaving Volume (Calculated by Model):",
        disabled=True,  # Make it read-only so the user cannot modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    weaving_vol_year20nonpeak_userchanged_widget = widgets.Text(
        value='',  # Initially set to 0 or a valid integer value
        description="Weaving Volume (Changed by User):",
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Weaving Speed Volume (Used for Project Evaluation)
    NWV20NB_widget = widgets.IntText(
        value=weaving_vol_year20nonpeak_modelcalc_widget.value,  # Set initially to the calculated value
        description="Weaving Volume (Used for Project Evaluation):",
        disabled=True,  # Make it read-only
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Explanation widget for user-modified values
    NWV20NB_explanation_widget = widgets.Text(
        value=None,  # Allow users to enter a text explanation
        description="Reasons for Change:",  # Label for the input field
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,  # Optional layout style, if needed
        style={'description_width': 'initial'}  # Optional style for description width
    )

    def update_year20nonpeak_weaving_volume(change=None):
        try:
            # Apply the formula as provided
            if ProjType == "Auxiliary Lane" or ProjType == "Off-Ramp Widening":
                Weaving_year20nonpeak_Volume = ((1 - PerPeakADT) * ADT20NB) * (PerWeaveNB - PerTruckNB)
            else:
                Weaving_year20nonpeak_Volume = 0

            # Apply additional adjustment for Auxiliary Lane
            if ProjType == "Auxiliary Lane":
                Weaving_year20nonpeak_Volume += RampVolNP * (24 - PeakLngthNB)

            # Update the widget with the calculated result
            weaving_vol_year20nonpeak_modelcalc_widget.value = round(Weaving_year20nonpeak_Volume, 2)  # Variable: Weaving_year20nonpeak_Volume

        except Exception:
            # In case of any error, set the result to 0 without printing anything
            weaving_vol_year20nonpeak_modelcalc_widget.value = 0

    # Initial call to set the value based on the current widget state
    update_year20nonpeak_weaving_volume()

    # Observers for weaving volume update — only required variables included
    projectinfo_widgets.subcategory_dropdown.observe(update_year20nonpeak_weaving_volume, names='value')  # ProjType
    projectinfo_widgets.ADT_20NB_widget.observe(update_year20nonpeak_weaving_volume, names='value')        # ADT20NB
    projectinfo_widgets.percent_trucks_nobuild_widget.observe(update_year20nonpeak_weaving_volume, names='value')  # PerTruckNB
    projectinfo_widgets.percent_traffic_weave_no_build_widget.observe(update_year20nonpeak_weaving_volume, names='value')  # PerWeaveNB
    projectinfo_widgets.hourly_ramp_volume_nonpeak_widget.observe(update_year20nonpeak_weaving_volume, names='value')  # RampVolNP
    projectinfo_widgets.peak_period_widget.observe(update_year20nonpeak_weaving_volume, names='value')  # PeakLngthNB


    def calculate_nwv20nb(change):
        # Access the user-modified value directly from the widget
        if isinstance(weaving_vol_year20nonpeak_userchanged_widget.value, (int, float)) and weaving_vol_year20nonpeak_userchanged_widget.value >= 0:
            updated_Weaving_year20nonpeak_vol = max(weaving_vol_year20nonpeak_userchanged_widget.value, 0)  # Ensure volume is not negative
        else:
            updated_Weaving_year20nonpeak_vol = max(weaving_vol_year20nonpeak_modelcalc_widget.value, 0)  # Use the model value if the user value is invalid

        # Update the value of Weaving_year20nonpeak widget (project evaluation widget)
        NWV20NB_widget.value = updated_Weaving_year20nonpeak_vol  # Variable: Weaving_year20nonpeak_modelcalc_widget

    # Link the function to the user input widget change
    weaving_vol_year20nonpeak_userchanged_widget.observe(calculate_nwv20nb, names='value')  

    # Combine into layout for display
    Weaving_Vol_year20nonpeak_widgets = widgets.HBox([weaving_vol_year20nonpeak_modelcalc_widget, weaving_vol_year20nonpeak_userchanged_widget, NWV20NB_explanation_widget])
    
    ###################################################################
    # Truck Volume Year 20 Non-Peak widgets
    Truck_Volume_year20nonpeak_modelcalc_widget = widgets.IntText(
        value=0,
        description="Truck Volume (Calculated by Model):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    Truck_Volume_year20nonpeak_userchanged_widget = widgets.Text(
        value='',
        description="Truck Volume (Changed by User):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Truck Volume Used for Evaluation
    NTV20NB_widget = widgets.IntText(
        value=Truck_Volume_year20nonpeak_modelcalc_widget.value,
        description="Truck Volume (Used for Project Evaluation):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Explanation widget for user-modified values
    NTV20NB_explanation_widget = widgets.Text(
        value=None,
        description="Reasons for Change:",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    def update_year20nonpeak_truck_volume(change=None):
        try:
            if ProjType == "Hwy-Rail Grade Crossing":
                Truck_Volume_year20nonpeak = ((ArrRate20 * GateTime20 / 60) / (1 - ArrRate20 / DepRate20)) * NumTrain20 / AnnualFactor * PerTruckNB
            elif ProjType == "Queuing":
                Truck_Volume_year20nonpeak = (
                    ADT20NB
                    - PeakLngthNB * (DepRate1 - ADT1NB * (1 - PerPeakADT) / (24 - PeakLngthNB))
                    / (ADT1NB / ADT20NB * DepRate20 - ADT1NB * (1 - PerPeakADT) / (24 - PeakLngthNB)) * DepRate20
                ) * PerTruckNB
            else:
                Truck_Volume_year20nonpeak = (1 - PerPeakADT) * ADT20NB * PerTruckNB

            Truck_Volume_year20nonpeak_modelcalc_widget.value = round(Truck_Volume_year20nonpeak, 2)

        except Exception:
            Truck_Volume_year20nonpeak_modelcalc_widget.value = 0

    # Initial calculation
    update_year20nonpeak_truck_volume()

    # Observers for Truck Volume — only required variables
    projectinfo_widgets.subcategory_dropdown.observe(update_year20nonpeak_truck_volume, names='value')
    projectinfo_widgets.arrival_rate_base_year_no_build_widget.observe(update_year20nonpeak_truck_volume, names='value')
    projectinfo_widgets.GateTime20_widget.observe(update_year20nonpeak_truck_volume, names='value')
    projectinfo_widgets.NumTrain20_widget.observe(update_year20nonpeak_truck_volume, names='value')
    projectinfo_widgets.ADT_20NB_widget.observe(update_year20nonpeak_truck_volume, names='value')
    projectinfo_widgets.adt_base_year_no_build_widget.observe(update_year20nonpeak_truck_volume, names='value')
    projectinfo_widgets.departure_rate_forecast_year_no_build_widget.observe(update_year20nonpeak_truck_volume, names='value')
    projectinfo_widgets.departure_rate_forecast_year_build_widget.observe(update_year20nonpeak_truck_volume, names='value')
    projectinfo_widgets.peak_period_widget.observe(update_year20nonpeak_truck_volume, names='value')
    projectinfo_widgets.percent_trucks_nobuild_widget.observe(update_year20nonpeak_truck_volume, names='value')

    def calculate_ntv20nb(change):
        try:
            user_input_Truck_Volume_year20nonpeak = float(Truck_Volume_year20nonpeak_userchanged_widget.value)
            if user_input_Truck_Volume_year20nonpeak >= 0:
                updated_Truck_Volume_year20nonpeak = user_input_Truck_Volume_year20nonpeak
            else:
                updated_Truck_Volume_year20nonpeak = Truck_Volume_year20nonpeak_modelcalc_widget.value
        except:
            updated_Truck_Volume_year20nonpeak = Truck_Volume_year20nonpeak_modelcalc_widget.value

        NTV20NB_widget.value = updated_Truck_Volume_year20nonpeak


    # Observer for user override
    Truck_Volume_year20nonpeak_userchanged_widget.observe(calculate_ntv20nb, names='value')

    # Combine into layout for display
    Truck_Volume_year20nonpeak_widgets = widgets.HBox([Truck_Volume_year20nonpeak_modelcalc_widget, Truck_Volume_year20nonpeak_userchanged_widget, NTV20NB_explanation_widget])

    ###################################################

    # Non-HOV Speed Year 20 Non-Peak widgets
    nonhov_speed_year20nonpeak_modelcalc_widget = widgets.IntText(
        value=0,
        description="Non-HOV Speed (Calculated by Model):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    nonhov_speed_year20nonpeak_userchanged_widget = widgets.Text(
        value='',
        description="Non-HOV Speed (Changed by User):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Evaluation Widget
    NNS20NB_widget = widgets.IntText(
        value=nonhov_speed_year20nonpeak_modelcalc_widget.value,
        description="Non-HOV Speed (Used for Proj Evaluation):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Explanation Widget
    NNS20NB_explanation_widget = widgets.Text(
        value=None,
        description="Reasons for Change:",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )
    
    def update_nonhov_year20nonpeak_speed(change=None):
        try:
            capacity_params = roadway_capacity_non_HOV["Non-HOV Lanes"]["No Build"]
            GenAlphaNB = capacity_params["GenAlphaNB"]
            GenBetaNB = capacity_params["GenBetaNB"]
            GenLaneCapNB = capacity_params["GenLaneCapNB"]

            # Hwy-Rail special case
            if ProjType == "Hwy-Rail Grade Crossing":
                speed = IdleSpeed

            else:
                # Total volume
                total_volume = NNV20NB_widget.value + NWV20NB_widget.value + NTV20NB_widget.value

                if total_volume == 0:
                    speed = 55
                else:
                    # Queuing check for adjustment
                    queuing_adjustment = 1
                    if ProjType == "Queuing":
                        numerator = DepRate1 - ADT1NB * (1 - PerPeakADT) / (24 - PeakLngthNB)
                        denominator = (ADT1NB / ADT20NB) * DepRate20 - ADT1NB * (1 - PerPeakADT) / (24 - PeakLngthNB)
                        queuing_adjustment = numerator / denominator if denominator != 0 else 1

                    hours = 24 - PeakLngthNB * queuing_adjustment
                    capacity = (GenLanesNB + HOVLanesNB) * GenLaneCapNB * hours

                    vc_ratio = min(total_volume / capacity, MaxVC) if capacity > 0 else MaxVC
                    speed_bpr = FFSpeedNB / (1 + GenAlphaNB * (vc_ratio ** GenBetaNB))

                    # Speed selection logic
                    if ProjType == "Passing":
                        speed = min(speed_bpr, (TruckSpeed + FFSpeedNB) / 2)
                    else:
                        speed = min(speed_bpr, FFSpeedNB)

            # Freeway Connector Adjustment
            if ProjType == "Freeway Connector":
                closest_key = min(SpeedWeaveAdj.keys(), key=lambda k: abs(k - PerWeaveNB))
                adj = SpeedWeaveAdj.get(closest_key, {}).get("Freeway", 1)
                speed *= adj

            # HOV Connector or Drop Ramp
            if ProjType in ["HOV Connector", "HOV Drop Ramp"]:
                closest_key = min(SpeedWeaveAdj.keys(), key=lambda k: abs(k - PerWeaveNB))
                adj = SpeedWeaveAdj.get(closest_key, {}).get("HOV", 1)
                speed *= adj

            # Pavement Adjustment
            if ProjType == "Pavement":
                iri_key = min(SpeedPavAdj.keys(), key=lambda k: abs(k - IRI20NB))
                adj = SpeedPavAdj.get(iri_key, {}).get("Auto", 1)
                speed *= adj

            # Final assignment to widget
            nonhov_speed_year20nonpeak_modelcalc_widget.value = round(speed, 1)

        except Exception:
            nonhov_speed_year20nonpeak_modelcalc_widget.value = 0
            
    update_nonhov_year20nonpeak_speed()
    
    # Observer triggers
    NNV20NB_widget.observe(update_nonhov_year20nonpeak_speed, names='value')  # NNV20NB
    NWV20NB_widget.observe(update_nonhov_year20nonpeak_speed, names='value')  # NWV20NB
    NTV20NB_widget.observe(update_nonhov_year20nonpeak_speed, names='value')  # NTV20NB
    projectinfo_widgets.subcategory_dropdown.observe(update_nonhov_year20nonpeak_speed, names='value')  # ProjType
    projectinfo_widgets.percent_traffic_weave_no_build_widget.observe(update_nonhov_year20nonpeak_speed, names='value')  # PerWeaveNB
    projectinfo_widgets.iri_forecast_year_no_build_widget.observe(update_nonhov_year20nonpeak_speed, names='value')  # IRI20NB
    projectinfo_widgets.free_flow_speed_no_build_widget.observe(update_nonhov_year20nonpeak_speed, names='value')  # FFSpeedNB
    projectinfo_widgets.general_traffic_lanes_no_build_widget.observe(update_nonhov_year20nonpeak_speed, names='value')  # GenLanesNB
    projectinfo_widgets.hov_hot_lanes_no_build_widget.observe(update_nonhov_year20nonpeak_speed, names='value')  # HOVLanesNB
    projectinfo_widgets.peak_period_widget.observe(update_nonhov_year20nonpeak_speed, names='value')  # PeakLngthNB
    projectinfo_widgets.truck_speed_widget.observe(update_nonhov_year20nonpeak_speed, names='value')  # TruckSpeed
    projectinfo_widgets.departure_rate_forecast_year_no_build_widget.observe(update_nonhov_year20nonpeak_speed, names='value')  # DepRate1
    projectinfo_widgets.adt_base_year_no_build_widget.observe(update_nonhov_year20nonpeak_speed, names='value')  # ADT1NB
    projectinfo_widgets.ADT_20NB_widget.observe(update_nonhov_year20nonpeak_speed, names='value')  # ADT20NB
    projectinfo_widgets.departure_rate_forecast_year_build_widget.observe(update_nonhov_year20nonpeak_speed, names='value')  # DepRate20

    def calculate_nns20nb(change):
        try:
            user_input = float(nonhov_speed_year20nonpeak_userchanged_widget.value)
        except:
            user_input = None

        if isinstance(user_input, (int, float)) and user_input >= 0:
            NNS20NB = max(user_input, 5)  # Minimum speed enforced
        else:
            NNS20NB = max(nonhov_speed_year20nonpeak_modelcalc_widget.value, 5)

        NNS20NB_widget.value = NNS20NB

    nonhov_speed_year20nonpeak_userchanged_widget.observe(calculate_nns20nb, names='value')
    
    NonHOV_speed_year20nonpeak_widgets = widgets.HBox([ nonhov_speed_year20nonpeak_modelcalc_widget, nonhov_speed_year20nonpeak_userchanged_widget, NNS20NB_explanation_widget])
    

    ###################################################
    # Weaving Speed Year 20 Non-Peak widgets
    weave_speed_year20nonpeak_modelcalc_widget = widgets.FloatText(
        value=0,
        description="Weaving Speed (Calculated by Model):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    weave_speed_year20nonpeak_userchanged_widget = widgets.Text(
        value='',
        description="Weaving Speed (Changed by User):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Weaving Speed for Evaluation
    NWS20NB_widget = widgets.FloatText(
        value=weave_speed_year20nonpeak_modelcalc_widget.value,
        description="Weaving Speed (Used for Proj Evaluation):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Explanation for user changes
    NWS20NB_explanation_widget = widgets.Text(
        value=None,
        description="Reasons for Change:",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )
    
    def update_year20nonpeak_weave_speed(change=None):
        try:
            if NWV20NB_widget.value == 0:
                speed = 55
            elif ProjType in ["Auxiliary Lane", "Off-Ramp Widening"]:
                base_speed = FFSpeedNB - (FFSpeedNB - 42) * (
                    0.321 + 0.0039 * math.exp(
                        (NWV20NB_widget.value + NTV20NB_widget.value) / NumDirections / (24 - PeakLngthNB)
                        / 1000
                    ) - 0.002 * ((1083 if ProjType == "Off-Ramp Widening" else SegmentNB * 5280) * RampFFSpdNB / 1000)
                )

                speed = min(NNS20NB_widget.value, 1.1 * base_speed)

                # Pavement adjustment
                if ProjType == "Pavement":
                    iri_key = min(SpeedPavAdj.keys(), key=lambda k: abs(k - IRI20NB))  # Closest IRI
                    speed *= SpeedPavAdj.get(iri_key, {}).get("Auto", 1)

                speed = max(speed, 5)  # Ensure a minimum speed of 5
            else:
                speed = NNS20NB_widget.value  # Fallback

            weave_speed_year20nonpeak_modelcalc_widget.value = round(speed, 1)

        except Exception:
            weave_speed_year20nonpeak_modelcalc_widget.value = 0
  
    update_year20nonpeak_weave_speed()
    
    # Trigger updates only based on used variables
    NWV20NB_widget.observe(update_year20nonpeak_weave_speed, names='value')  # NWV20NB
    NTV20NB_widget.observe(update_year20nonpeak_weave_speed, names='value')  # NTV20NB
    NNS20NB_widget.observe(update_year20nonpeak_weave_speed, names='value')  # NNS20NB
    projectinfo_widgets.subcategory_dropdown.observe(update_year20nonpeak_weave_speed, names='value')  # ProjType
    projectinfo_widgets.highway_segment_no_build_widget.observe(update_year20nonpeak_weave_speed, names='value')  # SegmentNB
    projectinfo_widgets.ramp_design_speed_no_build_widget.observe(update_year20nonpeak_weave_speed, names='value')  # RampFFSpdNB
    projectinfo_widgets.peak_period_widget.observe(update_year20nonpeak_weave_speed, names='value')  # PeakLngthNB
    projectinfo_widgets.iri_forecast_year_no_build_widget.observe(update_year20nonpeak_weave_speed, names='value')  # IRI20NB

    def calculate_nws20nb(change):
        try:
            if isinstance(weave_speed_year20nonpeak_userchanged_widget.value, (int, float)) and weave_speed_year20nonpeak_userchanged_widget.value >= 0:
                NWS20NB = max(float(weave_speed_year20nonpeak_userchanged_widget.value), 5)
            else:
                NWS20NB = max(weave_speed_year20nonpeak_modelcalc_widget.value, 5)

            NWS20NB_widget.value = NWS20NB
        except Exception:
            NWS20NB_widget.value = max(weave_speed_year20nonpeak_modelcalc_widget.value, 5)

    Weave_Speed_year20nonpeak_widgets = widgets.HBox([weave_speed_year20nonpeak_modelcalc_widget, weave_speed_year20nonpeak_userchanged_widget,  NWS20NB_explanation_widget])

  ###################################################   
    # Truck Speed Year 20 Non-Peak widgets
    truck_speed_year20nonpeak_modelcalc_widget = widgets.FloatText(
        value=0,
        description="Truck Speed (Calculated by Model):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    truck_speed_year20nonpeak_userchanged_widget = widgets.Text(
        value='',
        description="Truck Speed (Changed by User):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Truck Speed for Evaluation
    NTS20NB_widget = widgets.FloatText(
        value=truck_speed_year20nonpeak_modelcalc_widget.value,
        description="Truck Speed (Used for Proj Evaluation):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Explanation for user changes
    NTS20NB_explanation_widget = widgets.Text(
        value=None,
        description="Reasons for Change:",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )
    
    def update_year20nonpeak_truck_speed(change=None):
        try:
            if ProjType == "Hwy-Rail Grade Crossing":
                speed = IdleSpeed
            elif NTV20NB_widget.value == 0:
                speed = 55
            else:
                # Formula for truck speed calculation
                if ProjType in ["Auxiliary Lane", "Off-Ramp Widening"]:
                    base_speed = min(
                        TruckSpeed,
                        NTS20NB_widget.value if (ProjType == "Auxiliary Lane" or ProjType == "Off-Ramp Widening") else NNS20NB_widget.value
                    )

                    # Apply Pavement condition
                    if ProjType == "Pavement":
                        iri_key = min(SpeedPavAdj.keys(), key=lambda k: abs(k - IRI20NB))  # Closest IRI
                        speed = base_speed / SpeedPavAdj.get(iri_key, {}).get("Auto", 1)
                    else:
                        speed = base_speed

                    # Further adjustment based on Pavement (if applicable)
                    if ProjType == "Pavement":
                        speed *= SpeedPavAdj.get(IRI20NB, {}).get("Truck", 1)
                else:
                    speed = NNS20NB_widget.value  # Fallback if no special conditions

            truck_speed_year20nonpeak_modelcalc_widget.value = round(speed, 1)
        except Exception:
            truck_speed_year20nonpeak_modelcalc_widget.value = 0

    update_year20nonpeak_truck_speed()
            
    # Trigger updates only based on used variables
    NTV20NB_widget.observe(update_year20nonpeak_truck_speed, names='value')  # NTV20NB
    NNS20NB_widget.observe(update_year20nonpeak_truck_speed, names='value')  # NNS20NB
    NTS20NB_widget.observe(update_year20nonpeak_truck_speed, names='value')  # NTS20NB
    projectinfo_widgets.subcategory_dropdown.observe(update_year20nonpeak_truck_speed, names='value')  # ProjType
    projectinfo_widgets.highway_segment_no_build_widget.observe(update_year20nonpeak_truck_speed, names='value')  # SegmentNB
    projectinfo_widgets.ramp_design_speed_no_build_widget.observe(update_year20nonpeak_truck_speed, names='value')  # RampFFSpdNB
    projectinfo_widgets.iri_forecast_year_no_build_widget.observe(update_year20nonpeak_truck_speed, names='value')  # IRI20NB
    projectinfo_widgets.peak_period_widget.observe(update_year20nonpeak_truck_speed, names='value')  # PeakLngthNB

    def calculate_nts20nb(change):
        try:
            if isinstance(truck_speed_year20nonpeak_userchanged_widget.value, (int, float)) and truck_speed_year20nonpeak_userchanged_widget.value >= 0:
                NTS20NB = max(float(truck_speed_year20nonpeak_userchanged_widget.value), 5)
            else:
                NTS20NB = max(truck_speed_year20nonpeak_modelcalc_widget.value, 5)

            NTS20NB_widget.value = NTS20NB
        except Exception:
            NTS20NB_widget.value = max(truck_speed_year20nonpeak_modelcalc_widget.value, 5)

    truck_speed_year20nonpeak_userchanged_widget.observe(calculate_nts20nb, names='value')
    
    Truck_Speed_year20nonpeak_widgets = widgets.HBox([ truck_speed_year20nonpeak_modelcalc_widget, truck_speed_year20nonpeak_userchanged_widget,  NTS20NB_explanation_widget])

    


##########################################################################################################################################################################

    # HOV Volume Year 1 Peak Build Widgets
    HOV_vol_year1peak_build_modelcalc_widget = widgets.IntText(
        value=0,  # Set initial value to 0 or any other valid integer
        description="HOV Volume (Calculated by Model):",
        disabled=True,  # Make it read-only so the user cannot modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    HOV_vol_year1peak_build_userchanged_widget = widgets.Text(
        value='',  # Initially set to 0 or a valid integer value
        description="HOV Volume (Changed by User):",
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # HOV Volume (Used for Project Evaluation)
    PHV1B_widget = widgets.IntText(
        value=HOV_vol_year1peak_build_modelcalc_widget.value,  # Set initially to the calculated value
        description="HOV Volume (Used for Project Evaluation):",
        disabled=True,  # Make it read-only
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Explanation widget for user-modified values
    PHV1B_explanation_widget = widgets.Text(
        value=None,  # Allow users to enter a text explanation
        description="Reasons for Change:",  # Label for the input field
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,  # Optional layout style, if needed
        style={'description_width': 'initial'}  # Optional style for description width
    )

    # Function to calculate HOV Volume Year 1 Peak Build
    def update_HOV_Year1Peak_Build_Volume(change=None):
        try:
            if ProjType == "Hwy-Rail Grade Crossing":
                # For Hwy-Rail, HOV Volume is 0
                volume = 0
            else:
                # Formula for HOV Volume Year 1 Peak Build
                volume = HOVvolB * PeakLngthNB * (1 - PerWeaveNB if (ProjType == "HOV Connector" or ProjType == "HOV Drop Ramp") else 1)

            # Update the widget with the calculated result
            HOV_vol_year1peak_build_modelcalc_widget.value = round(volume, 2)
        except Exception:
            # In case of any error, set the result to 0 without printing anything
            HOV_vol_year1peak_build_modelcalc_widget.value = 0

    # Trigger updates based on used variables
    projectinfo_widgets.HOV_lane_build_widget.observe(update_HOV_Year1Peak_Build_Volume, names='value')  # HOVvolB
    projectinfo_widgets.subcategory_dropdown.observe(update_HOV_Year1Peak_Build_Volume, names='value')  # ProjType
    projectinfo_widgets.peak_period_widget.observe(update_HOV_Year1Peak_Build_Volume, names='value')  # PeakLngthNB
    projectinfo_widgets.percent_traffic_weave_no_build_widget.observe(update_HOV_Year1Peak_Build_Volume, names='value')  # PerWeaveNB

    # Function to calculate PHV1B (for user-modified values)
    def calculate_phv1b(change):
        try:
            if isinstance(HOV_vol_year1peak_build_userchanged_widget.value, (int, float)) and HOV_vol_year1peak_build_userchanged_widget.value >= 0:
                PHV1B = max(float(HOV_vol_year1peak_build_userchanged_widget.value), 0)
            else:
                PHV1B = max(HOV_vol_year1peak_build_modelcalc_widget.value, 0)

            PHV1B_widget.value = PHV1B
        except Exception:
            PHV1B_widget.value = max(HOV_vol_year1peak_build_modelcalc_widget.value, 0)

    # Link the function to the user input widget change
    HOV_vol_year1peak_build_userchanged_widget.observe(calculate_phv1b, names='value')

    # Combine all widgets into a horizontal layout for HOV Volume
    HOV_Vol_year1peak_build_widgets = widgets.HBox([HOV_vol_year1peak_build_modelcalc_widget,  HOV_vol_year1peak_build_userchanged_widget, PHV1B_explanation_widget])
    
    #########################################################################
    
    Non_HOV_vol_year1peak_build_modelcalc_widget = widgets.IntText(
        value=0,  # Set initial value to 0 or any other valid integer
        description="Non-HOV Volume (Calculated by Model):",
        disabled=True,  # Make it read-only so the user cannot modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    Non_HOV_vol_year1peak_build_userchanged_widget = widgets.Text(
        value='',  # Initially set to 0 or a valid integer value
        description="Non-HOV Volume (Changed by User):",
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Non-HOV Volume (Used for Project Evaluation)
    PNV1B_widget = widgets.IntText(
        value=Non_HOV_vol_year1peak_build_modelcalc_widget.value,  # Set initially to the calculated value
        description="Non-HOV Volume (Used for Project Evaluation):",
        disabled=True,  # Make it read-only
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Explanation widget for user-modified values
    PNV1B_explanation_widget = widgets.Text(
        value=None,  # Allow users to enter a text explanation
        description="Reasons for Change:",  # Label for the input field
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,  # Optional layout style, if needed
        style={'description_width': 'initial'}  # Optional style for description width
    )

    def update_Non_HOV_Year1Peak_Build_Volume(change=None):
        try:
            # If ProjType is "Hwy-Rail Grade Crossing", set volume to 0 directly
            if ProjType == "Hwy-Rail Grade Crossing":
                volume = 0
            else:
                # Retrieve the TMS adjustments for the given TMSLookup
                tms_adj_values = TMSAdj[TMSLookup]  # Directly access the dictionary for TMS adjustments

                # Non-HOV Volume Year 1 Peak Build formula:
                # The formula will depend on the ProjType (AuxLane, OffRamp, etc.)

                # Check for conditions where auxiliary lane or off-ramp widening applies
                if ProjType in ["Auxiliary Lane", "Off-Ramp Widening"]:
                    volume = (PerPeakADT * ADT1B) * (1 - PerWeaveB) * tms_adj_values["VolumeWith"]
                else:
                    # Default for other ProjTypes (including HOV Drop Ramp, etc.)
                    volume = (PerPeakADT * ADT1B) * (1 - PerTruckB) * tms_adj_values["VolumeWith"]

                # Subtract HOV volume and apply the other adjustments
                volume -= HOVvolB * PeakLngthNB
                volume -= (TPerPeak * TPerHwy * (TAPT1B - TAPT1NB)) / (AnnualFactor * AVOPeakNB)

            # Round and set the calculated volume value to the widget
            Non_HOV_vol_year1peak_build_modelcalc_widget.value = round(volume, 2)

        except Exception:
            # If there's an error in the calculation, set the value to 0 without printing anything
            Non_HOV_vol_year1peak_build_modelcalc_widget.value = 0

    update_Non_HOV_Year1Peak_Build_Volume()
    
    
    # Trigger updates based on used variables
    projectinfo_widgets.adt_base_year_build_widget.observe(update_Non_HOV_Year1Peak_Build_Volume, names='value')  # ADT1B
    projectinfo_widgets.HOV_lane_build_widget.observe(update_Non_HOV_Year1Peak_Build_Volume, names='value')  # HOVvolB
    projectinfo_widgets.peak_period_widget.observe(update_Non_HOV_Year1Peak_Build_Volume, names='value')  # PeakLngthNB
    projectinfo_widgets.TPerPeak_widget.observe(update_Non_HOV_Year1Peak_Build_Volume, names='value')  # TPerPeak
    projectinfo_widgets.TPerHwy_widget.observe(update_Non_HOV_Year1Peak_Build_Volume, names='value')  # TPerHwy
    projectinfo_widgets.TAPT1B_widget.observe(update_Non_HOV_Year1Peak_Build_Volume, names='value')  # TAPT1B
    projectinfo_widgets.TAPT1NB_widget.observe(update_Non_HOV_Year1Peak_Build_Volume, names='value')  # TAPT1NB
    projectinfo_widgets.AVO_traffic_P_no_build_widget.observe(update_Non_HOV_Year1Peak_Build_Volume, names='value')  # AVOPeakNB
    projectinfo_widgets.percent_trucks_build_widget.observe(update_Non_HOV_Year1Peak_Build_Volume, names='value') #PerTruckB
    projectinfo_widgets.percent_traffic_weave_build_widget.observe(update_Non_HOV_Year1Peak_Build_Volume, names='value') #PerWeaveB
    projectinfo_widgets.subcategory_dropdown.observe(update_Non_HOV_Year1Peak_Build_Volume, names='value') 
    

    # Function to calculate PNV1B (for user-modified values)
    def calculate_pnv1b(change):
        try:
            if isinstance(Non_HOV_vol_year1peak_build_userchanged_widget.value, (int, float)) and Non_HOV_vol_year1peak_build_userchanged_widget.value >= 0:
                PNV1B = max(float(Non_HOV_vol_year1peak_build_userchanged_widget.value), 0)
            else:
                PNV1B = max(Non_HOV_vol_year1peak_build_modelcalc_widget.value, 0)

            PNV1B_widget.value = PNV1B
        except Exception:
            PNV1B_widget.value = max(Non_HOV_vol_year1peak_build_modelcalc_widget.value, 0)

    # Link the function to the user input widget change
    Non_HOV_vol_year1peak_build_userchanged_widget.observe(calculate_pnv1b, names='value')

    # Combine all widgets into a horizontal layout for Non-HOV Volume
    Non_HOV_Vol_year1peak_build_widgets = widgets.HBox([Non_HOV_vol_year1peak_build_modelcalc_widget,  Non_HOV_vol_year1peak_build_userchanged_widget, PNV1B_explanation_widget])
    
    
    #########################################################################
# Weaving Volume Year 1 Peak Build Widgets

    weaving_vol_year1peak_build_modelcalc_widget = widgets.IntText(
        value=0,  # Set initial value to 0 or any other valid integer
        description="Weaving Volume (Calculated by Model):",
        disabled=True,  # Make it read-only so the user cannot modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    weaving_vol_year1peak_build_userchanged_widget = widgets.Text(
        value='',  # Initially set to 0 or a valid integer value
        description="Weaving Volume (Changed by User):",
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Weaving Volume (Used for Project Evaluation)
    PWV1B_widget = widgets.IntText(
        value=weaving_vol_year1peak_build_modelcalc_widget.value,  # Set initially to the calculated value
        description="Weaving Volume (Used for Project Evaluation):",
        disabled=True,  # Make it read-only
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Explanation widget for user-modified values
    PWV1B_explanation_widget = widgets.Text(
        value=None,  # Allow users to enter a text explanation
        description="Reasons for Change:",  # Label for the input field
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,  # Optional layout style, if needed
        style={'description_width': 'initial'}  # Optional style for description width
    )

    # Function to calculate Weaving Volume Year 1 Peak Build
    def update_weaving_year1peak_Build_volume(change=None):
        try:
            # If ProjType is "Hwy-Rail Grade Crossing", set volume to 0 directly
            if ProjType == "Hwy-Rail Grade Crossing":
                volume = 0
            else:
                # Retrieve the TMS adjustments for the given TMSLookup
                tms_adj_values = TMSAdj[TMSLookup]  # Directly access the dictionary for TMS adjustments

                # Weaving Volume Formula:
                # Weaving Volume calculation will depend on the ProjType (AuxLane, OffRamp, etc.)

                # Check for conditions where auxiliary lane or off-ramp might apply
                if ProjType in ["Auxiliary Lane", "Off-Ramp Widening"]:
                    # Formula: Volume = (PerPeakADT * ADT1B) * (PerWeaveB - PerTruckB) * VolumeWith adjustment
                    volume = (PerPeakADT * ADT1B) * (PerWeaveB - PerTruckB) * tms_adj_values["VolumeWith"]
                elif ProjType in ["HOV Connector", "HOV Drop Ramp"]:
                    # For HOV connectors, use HOVvolB and PeakLngthNB in the calculation
                    volume = PerWeaveNB * HOVvolB * PeakLngthNB
                else:
                    volume = 0  # Default to 0 if ProjType is not one of the specified types

                # If ProjType is "Auxiliary Lane", add RampVolP * PeakLngthNB to the volume
                if ProjType == "Auxiliary Lane":
                    volume += RampVolP * PeakLngthNB

                # If ProjType is "HOV Connector" or "HOV Drop Ramp", add PerWeaveNB * HOVvolB * PeakLngthNB to the volume
                if ProjType in ["HOV Connector", "HOV Drop Ramp"]:
                    volume += PerWeaveNB * HOVvolB * PeakLngthNB

            # Round and set the calculated volume value to the widget
            weaving_vol_year1peak_build_modelcalc_widget.value = round(volume, 2)

        except Exception:
            # If there's an error in the calculation, set the value to 0 without printing anything
            weaving_vol_year1peak_build_modelcalc_widget.value = 0


    # Trigger updates based on used variables

    projectinfo_widgets.adt_base_year_build_widget.observe(update_weaving_year1peak_Build_volume, names='value')  # ADT1B
    projectinfo_widgets.percent_traffic_weave_build_widget.observe(update_weaving_year1peak_Build_volume, names='value')  # PerWeaveB
    projectinfo_widgets.percent_trucks_build_widget.observe(update_weaving_year1peak_Build_volume, names='value')  # PerTruckB
    projectinfo_widgets.hourly_ramp_volume_peak_widget.observe(update_weaving_year1peak_Build_volume, names='value')  # RampVolP
    projectinfo_widgets.HOV_lane_build_widget.observe(update_weaving_year1peak_Build_volume, names='value')  # HOVvolB
    projectinfo_widgets.peak_period_widget.observe(update_weaving_year1peak_Build_volume, names='value')  # PeakLngthNB
    projectinfo_widgets.subcategory_dropdown.observe(update_weaving_year1peak_Build_volume, names='value')
    

    # Function to calculate PWV1B (for user-modified values)
    def calculate_pwv1b(change):
        try:
            if isinstance(weaving_vol_year1peak_build_userchanged_widget.value, (int, float)) and weaving_vol_year1peak_build_userchanged_widget.value >= 0:
                PWV1B = max(float(weaving_vol_year1peak_build_userchanged_widget.value), 0)
            else:
                PWV1B = max(weaving_vol_year1peak_build_modelcalc_widget.value, 0)

            PWV1B_widget.value = PWV1B
        except Exception:
            PWV1B_widget.value = max(weaving_vol_year1peak_build_modelcalc_widget.value, 0)

    # Link the function to the user input widget change
    weaving_vol_year1peak_build_userchanged_widget.observe(calculate_pwv1b, names='value')

    # Combine all widgets into a horizontal layout for Weaving Volume
    Weaving_Vol_year1peak_build_widgets = widgets.HBox([ weaving_vol_year1peak_build_modelcalc_widget, weaving_vol_year1peak_build_userchanged_widget, PWV1B_explanation_widget])
    
    
   #######################################################################
    
    # Widgets for Truck Volume Year 1 Peak Build

    truck_vol_year1peak_build_modelcalc_widget = widgets.IntText(
        value=0,
        description="Truck Volume (Calculated by Model):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    truck_vol_year1peak_build_userchanged_widget = widgets.Text(
        value='',
        description="Truck Volume (Changed by User):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    PTV1B_widget = widgets.IntText(
        value=truck_vol_year1peak_build_modelcalc_widget.value,
        description="Truck Volume (Used for Project Evaluation):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    PTV1B_explanation_widget = widgets.Text(
        value=None,
        description="Reasons for Change:",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )
    
    def update_truck_year1peak_Build_volume(change=None):
        try:
            if ProjType == "Hwy-Rail Grade Crossing":
                volume = 0
            else:
                tms_adj_values = TMSAdj[TMSLookup]  # Assumes TMSAdj and TMSLookup are defined
                volume = (PerPeakADT * ADT1B) * PerTruckB * tms_adj_values["VolumeWith"]

            truck_vol_year1peak_build_modelcalc_widget.value = round(volume, 2)
        except Exception:
            truck_vol_year1peak_build_modelcalc_widget.value = 0
            
            
    projectinfo_widgets.adt_base_year_build_widget.observe(update_truck_year1peak_Build_volume, names='value')  # ADT1B
    projectinfo_widgets.percent_trucks_build_widget.observe(update_truck_year1peak_Build_volume, names='value')  # PerTruckB
    projectinfo_widgets.subcategory_dropdown.observe(update_truck_year1peak_Build_volume, names='value')
    
    
    def calculate_ptv1b(change):
        try:
            if isinstance(truck_vol_year1peak_build_userchanged_widget.value, (int, float)) and float(truck_vol_year1peak_build_userchanged_widget.value) >= 0:
                PTV1B = max(float(truck_vol_year1peak_build_userchanged_widget.value), 0)
            else:
                PTV1B = max(truck_vol_year1peak_build_modelcalc_widget.value, 0)

            PTV1B_widget.value = round(PTV1B, 2)
        except Exception:
            PTV1B_widget.value = max(truck_vol_year1peak_build_modelcalc_widget.value, 0)

    # Watch user entry and update final PTV1B value
    truck_vol_year1peak_build_userchanged_widget.observe(calculate_ptv1b, names='value')
    
    Truck_Vol_year1peak_build_widgets = widgets.HBox([
        truck_vol_year1peak_build_modelcalc_widget,
        truck_vol_year1peak_build_userchanged_widget,
        PTV1B_explanation_widget
    ])




   #######################################################################
    # Non-HOV Speed (Calculated by Model)
    nonhov_speed_year1peak_build_modelcalc_widget = widgets.FloatText(
        value=0,  # Initial value
        description="Non-HOV Speed (Calculated by Model):",
        disabled=True,  # Read-only
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # User-changed Non-HOV Speed
    nonhov_speed_year1peak_build_userchanged_widget = widgets.Text(
        value='',  # User input allowed
        description="Non-HOV Speed (Changed by User):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Non-HOV Speed (Used for Project Evaluation)
    PNS1B_widget = widgets.FloatText(
        value=nonhov_speed_year1peak_build_modelcalc_widget.value,
        description="Non-HOV Speed (Used for Project Evaluation):",
        disabled=True,  # Read-only
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Explanation for changes
    PNS1B_explanation_widget = widgets.Text(
        value=None,
        description="Reasons for Change:",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    def update_nonhov_year1peak_Build_speed(change=None):
        try:
            # Inputs from widgets
            PHV1B = PHV1B_widget.value
            PNV1B = PNV1B_widget.value
            PWV1B = PWV1B_widget.value
            PTV1B = PTV1B_widget.value

            total_volume = PHV1B + PNV1B + PWV1B + PTV1B

            if total_volume == 0:
                NonHOVSpeed = 55
            else:
                # Capacity parameters
                GenAlphaB = roadway_capacity_non_HOV["Non-HOV Lanes"]["Build"]["GenAlphaB"]
                GenBetaB = roadway_capacity_non_HOV["Non-HOV Lanes"]["Build"]["GenBetaB"]
                GenLaneCapB = roadway_capacity_non_HOV["Non-HOV Lanes"]["Build"]["GenLaneCapB"]

                # Volume denominator
                if HOVLanesB == 0:
                    volume = total_volume
                else:
                    volume = PNV1B + PWV1B + PTV1B

                denominator = GenLanesB * GenLaneCapB * PeakLngthNB
                vc_ratio = min(volume / denominator if denominator else 0, MaxVC)

                # Base speed calculation
                speed_without_adj = FFSpeedB / (1 + GenAlphaB * vc_ratio**GenBetaB)

                # TMS adjustment
                tms_speed = TMSAdj.get(TMSLookup, {}).get("SpeedWith", 1.0)
                speed = speed_without_adj * tms_speed

                # Pavement adjustment
                if ProjType == "Pavement":
                    closest_iri = min(SpeedPavAdj.keys(), key=lambda x: abs(x - IRI1B))
                    speed *= SpeedPavAdj[closest_iri].get("Auto", 1)

                # Free connector adjustment
                if ProjType == "Freeway Connector":
                    closest_weave_key = min(SpeedWeaveAdj.keys(), key=lambda x: abs(x - PerWeaveB))
                    speed *= SpeedWeaveAdj[closest_weave_key].get("Freeway", 1)

                # HOV connector/drop adjustment
                if ProjType == "HOV Connector" or ProjType == "HOV Drop Ramp":
                    closest_weave_key = min(SpeedWeaveAdj.keys(), key=lambda x: abs(x - PerWeaveB))
                    speed *= SpeedWeaveAdj[closest_weave_key].get("HOV", 1)

                # Final speed, capped at FFSpeedB
                NonHOVSpeed = min(speed, FFSpeedB)

            # Update the widget with result
            nonhov_speed_year1peak_build_modelcalc_widget.value = round(NonHOVSpeed, 2)

        except Exception:
            nonhov_speed_year1peak_build_modelcalc_widget.value = 0
    
    update_nonhov_year1peak_Build_speed()
    
    
    PHV1B_widget.observe(update_nonhov_year1peak_Build_speed, names='value') 
    PNV1B_widget.observe(update_nonhov_year1peak_Build_speed, names='value')  
    PWV1B_widget.observe(update_nonhov_year1peak_Build_speed, names='value')  
    PTV1B_widget.observe(update_nonhov_year1peak_Build_speed, names='value') 
    projectinfo_widgets.iri_base_year_build_widget.observe(update_nonhov_year1peak_Build_speed, names='value') 
    projectinfo_widgets.percent_traffic_weave_build_widget.observe(update_nonhov_year1peak_Build_speed, names='value') 
    projectinfo_widgets.free_flow_speed_build_widget.observe(update_nonhov_year1peak_Build_speed, names='value') 
    projectinfo_widgets.peak_period_widget.observe(update_nonhov_year1peak_Build_speed, names='value') 
    projectinfo_widgets.hov_hot_lanes_build_widget.observe(update_nonhov_year1peak_Build_speed, names='value')
    projectinfo_widgets.subcategory_dropdown.observe(update_nonhov_year1peak_Build_speed, names='value')
    
    # Function to calculate PNS1B (for user-modified values)
    def calculate_pns1b(change):
        try:
            if isinstance(nonhov_speed_year1peak_build_userchanged_widget.value, (int, float)) and nonhov_speed_year1peak_build_userchanged_widget.value >= 0:
                PNS1B = max(float(nonhov_speed_year1peak_build_userchanged_widget.value), 5)
            else:
                PNS1B = max(nonhov_speed_year1peak_build_modelcalc_widget.value, 5)

            PNS1B_widget.value = round(PNS1B, 2)
        except Exception:
            PNS1B_widget.value = max(nonhov_speed_year1peak_build_modelcalc_widget.value, 5)


    # Link the function to user input widget change
    nonhov_speed_year1peak_build_userchanged_widget.observe(calculate_pns1b, names='value')

    # Combine widgets into layout for Non-HOV Speed Year 1 Peak Build
    NonHOV_Speed_Year1Peak_Build_Widgets = widgets.HBox([nonhov_speed_year1peak_build_modelcalc_widget,  nonhov_speed_year1peak_build_userchanged_widget, PNS1B_explanation_widget])

   #######################################################################

    # Widget for HOV Speed (Calculated by Model)
    hov_speed_year1peak_build_modelcalc_widget = widgets.FloatText(
        value=0,
        description="HOV Speed (Calculated by Model):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Widget for HOV Speed (Changed by User)
    hov_speed_year1peak_build_userchanged_widget = widgets.Text(
        value='',
        description="HOV Speed (Changed by User):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Widget for HOV Speed (Used for Project Evaluation)
    PHS1B_widget = widgets.FloatText(
        value=hov_speed_year1peak_build_modelcalc_widget.value,
        description="HOV Speed (Used for Project Evaluation):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Explanation widget for user-modified values
    PHS1B_explanation_widget = widgets.Text(
        value=None,
        description="Reasons for Change:",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Function to calculate HOV Speed for Year 1 Peak Build
    def update_hov_year1peak_Build_speed(change=None):
        try:
            # Access HOV capacity values from the pre-defined roadway_capacity dictionary
            hov_capacity = roadway_capacity["HOV Lanes"]
            HOVLaneCap = hov_capacity["HOVLaneCap"]
            HOVAlpha = hov_capacity["HOVAlpha"]
            HOVBeta = hov_capacity["HOVBeta"]

            # Define PHV1B, PNS1B, and Pavement from user-modified widget values
            PHV1B = PHV1B_widget.value  
            PNS1B = PNS1B_widget.value  
            Pavement = ProjType == "Pavement"  # Check if project type is Pavement

            # Compute the speed logic based on the Excel formula
            if PHV1B == 0:
                hov_build_peak_speed = 55
            elif HOVLanesB == 0:
                hov_build_peak_speed = PNS1B
            else:
                # Compute the vehicle to capacity ratio
                v_c_ratio = PHV1B / (HOVLanesB * HOVLaneCap * PeakLngthNB)
                # Ensure the ratio does not exceed MaxVC
                min_vc = min(v_c_ratio, MaxVC)
                # Calculate the base speed
                hov_build_peak_speed = FFSpeedB / (1 + HOVAlpha * (min_vc ** HOVBeta))

                # Apply pavement adjustment if applicable
                if Pavement:
                    closest_iri_key = min(SpeedPavAdj.keys(), key=lambda x: abs(x - IRI1B))
                    speed_adj = SpeedPavAdj[closest_iri_key]["Auto"]
                    hov_build_peak_speed *= speed_adj

            # Set the calculated speed in the output widget
            hov_speed_year1peak_build_modelcalc_widget.value = round(hov_build_peak_speed, 2)

        except Exception:
            hov_speed_year1peak_build_modelcalc_widget.value = 0
            
    update_hov_year1peak_Build_speed()

    # Trigger updates based on used variables
    # Observe changes in widgets and update HOV speed calculation
    PHV1B_widget.observe(update_hov_year1peak_Build_speed, names='value')  # PHV1B
    PNS1B_widget.observe(update_hov_year1peak_Build_speed, names='value')  # PNS1B
    projectinfo_widgets.subcategory_dropdown.observe(update_hov_year1peak_Build_speed, names='value')
    projectinfo_widgets.peak_period_widget.observe(update_hov_year1peak_Build_speed, names='value')  # PeakLngthNB
    projectinfo_widgets.iri_base_year_build_widget.observe(update_hov_year1peak_Build_speed, names='value')  # IRI1B
    projectinfo_widgets.free_flow_speed_build_widget.observe(update_hov_year1peak_Build_speed, names='value') # FFSpeedB

    # Function to calculate PHS1B (for user-modified values)
    def calculate_phs1b(change):
        try:
            if isinstance(hov_speed_year1peak_build_userchanged_widget.value, (int, float)) or (
                isinstance(hov_speed_year1peak_build_userchanged_widget.value, str) and
                hov_speed_year1peak_build_userchanged_widget.value.replace('.', '', 1).isdigit()
            ):
                PHS1B = max(float(hov_speed_year1peak_build_userchanged_widget.value), 5)
            else:
                PHS1B = max(hov_speed_year1peak_build_modelcalc_widget.value, 5)

            PHS1B_widget.value = round(PHS1B, 2)
        except Exception:
            PHS1B_widget.value = max(hov_speed_year1peak_build_modelcalc_widget.value, 5)


    # Link user override for PHS1B
    hov_speed_year1peak_build_userchanged_widget.observe(calculate_phs1b, names='value')

    # Combine all widgets into a horizontal layout for HOV Speed Year 1 Peak Build
    HOV_Speed_year1peak_build_widgets = widgets.HBox([
        hov_speed_year1peak_build_modelcalc_widget,
        hov_speed_year1peak_build_userchanged_widget,
        PHS1B_explanation_widget
    ])

   #######################################################################

    weaving_speed_year1peak_build_modelcalc_widget = widgets.FloatText(
        value=0,
        description="Weaving Speed (Calculated by Model):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    weaving_speed_year1peak_build_userchanged_widget = widgets.Text(
        value='',
        description="Weaving Speed (Changed by User):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    PWS1B_widget = widgets.FloatText(
        value=weaving_speed_year1peak_build_modelcalc_widget.value,
        description="Weaving Speed (Used for Project Evaluation):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    PWS1B_explanation_widget = widgets.Text(
        value=None,
        description="Reasons for Change:",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )
    
    def update_weave_year1peak_Build_speed(change=None):
        try:
            PWV1B = PWV1B_widget.value
            PTV1B = PTV1B_widget.value
            PNS1B = PNS1B_widget.value

            if PWV1B == 0:
                weave_speed = 55
            elif ProjType == "Auxiliary Lane":
                exp_component = math.exp((PWV1B + PTV1B) / NumDirections / PeakLngthNB / 1000)
                ramp_factor = 1083 if ProjType == "Off-Ramp Widening" else SegmentB * 5280
                ramp_effect = 0.002 * (ramp_factor * RampFFSpdB / 1000)

                base_speed = FFSpeedB - (FFSpeedB - 42) * (0.321 + 0.0039 * exp_component - ramp_effect)
                adjusted_speed = 1.1 * base_speed

                # Pavement Adjustment
                pavement_adj = 1
                if ProjType == "Pavement":
                    closest_iri_key = min(SpeedPavAdj.keys(), key=lambda x: abs(x - IRI1B))
                    pavement_adj = SpeedPavAdj[closest_iri_key]["Auto"]

                # TMS Adjustment
                tms_adj = TMSAdj.get(TMSLookup, {}).get("SpeedWith", 1)

                # Final Speed
                final_speed = adjusted_speed * tms_adj * pavement_adj
                weave_speed = max(5, min(PNS1B, final_speed))

            else:
                weave_speed = PNS1B

            weaving_speed_year1peak_build_modelcalc_widget.value = round(weave_speed, 2)

        except Exception:
            weaving_speed_year1peak_build_modelcalc_widget.value = 0

    update_weave_year1peak_Build_speed()
    
    PWV1B_widget.observe(update_weave_year1peak_Build_speed, names='value')
    PTV1B_widget.observe(update_weave_year1peak_Build_speed, names='value')
    PNS1B_widget.observe(update_weave_year1peak_Build_speed, names='value')
    projectinfo_widgets.free_flow_speed_build_widget.observe(update_weave_year1peak_Build_speed, names='value')
    projectinfo_widgets.peak_period_widget.observe(update_weave_year1peak_Build_speed, names='value')
    projectinfo_widgets.one_two_way_widget.observe(update_weave_year1peak_Build_speed, names='value')
    projectinfo_widgets.subcategory_dropdown.observe(update_weave_year1peak_Build_speed, names='value')
    projectinfo_widgets.iri_base_year_build_widget.observe(update_weave_year1peak_Build_speed, names='value')

    def calculate_pws1b(change):
        try:
            if isinstance(weaving_speed_year1peak_build_userchanged_widget.value, (int, float)) or (
                isinstance(weaving_speed_year1peak_build_userchanged_widget.value, str) and
                weaving_speed_year1peak_build_userchanged_widget.value.replace('.', '', 1).isdigit()
            ):
                PWS1B = max(float(weaving_speed_year1peak_build_userchanged_widget.value), 5)
            else:
                PWS1B = max(weaving_speed_year1peak_build_modelcalc_widget.value, 5)

            PWS1B_widget.value = round(PWS1B, 2)
        except Exception:
            PWS1B_widget.value = max(weaving_speed_year1peak_build_modelcalc_widget.value, 5)


    weaving_speed_year1peak_build_userchanged_widget.observe(calculate_pws1b, names='value')

    Weaving_Speed_year1peak_build_widgets = widgets.HBox([weaving_speed_year1peak_build_modelcalc_widget,  weaving_speed_year1peak_build_userchanged_widget,  PWS1B_explanation_widget])
    
   #######################################################################    
    truck_speed_year1peak_build_modelcalc_widget = widgets.FloatText(
        value=0,
        description="Truck Speed (Calculated by Model):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    truck_speed_year1peak_build_userchanged_widget = widgets.Text(
        value='',
        description="Truck Speed (Changed by User):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    PTS1B_widget = widgets.FloatText(
        value=truck_speed_year1peak_build_modelcalc_widget.value,
        description="Truck Speed (Used for Project Evaluation):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    PTS1B_explanation_widget = widgets.Text(
        value=None,
        description="Reasons for Change:",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )
    
    def update_truck_year1peak_Build_speed(change=None):
        try:
            # Get widget values
            PTV1B = PTV1B_widget.value
            PWS1B = PWS1B_widget.value
            PNS1B = PNS1B_widget.value

            if PTV1B == 0:
                truck_speed = 55
            else:
                # Lookup IRI adjustment
                closest_iri_key = min(SpeedPavAdj.keys(), key=lambda x: abs(x - IRI1B))

                # Apply adjustment values only if ProjType == "Pavement"
                speed_adj_auto = SpeedPavAdj[closest_iri_key]["Auto"] if ProjType == "Pavement" else 1
                speed_adj_truck = SpeedPavAdj[closest_iri_key]["Truck"] if ProjType == "Pavement" else 1

                # Pick correct speed limit based on ProjType == "Auxiliary Lane"
                limit_speed = PWS1B if ProjType == "Auxiliary Lane" else PNS1B

                # Calculate adjusted speed
                base_speed = min(TruckSpeed, limit_speed / speed_adj_auto)
                truck_speed = base_speed * speed_adj_truck

            # Output result
            truck_speed_year1peak_build_modelcalc_widget.value = round(truck_speed, 2)

        except Exception:
            truck_speed_year1peak_build_modelcalc_widget.value = 0
            
        
    update_truck_year1peak_Build_speed()
    
    PTV1B_widget.observe(update_truck_year1peak_Build_speed, names='value')
    PWS1B_widget.observe(update_truck_year1peak_Build_speed, names='value')
    PNS1B_widget.observe(update_truck_year1peak_Build_speed, names='value')
    projectinfo_widgets.iri_base_year_build_widget.observe(update_truck_year1peak_Build_speed, names='value') #IRI1B
    projectinfo_widgets.subcategory_dropdown.observe(update_truck_year1peak_Build_speed, names='value') #ProjType
    projectinfo_widgets.truck_speed_widget.observe(update_truck_year1peak_Build_speed, names='value') #TruckSpeed 
    
    
    def calculate_pts1b(change):
        try:
            if isinstance(truck_speed_year1peak_build_userchanged_widget.value, (int, float)) or (
                isinstance(truck_speed_year1peak_build_userchanged_widget.value, str) and
                truck_speed_year1peak_build_userchanged_widget.value.replace('.', '', 1).isdigit()
            ):
                PTS1B = max(float(truck_speed_year1peak_build_userchanged_widget.value), 5)
            else:
                PTS1B = max(truck_speed_year1peak_build_modelcalc_widget.value, 5)

            PTS1B_widget.value = round(PTS1B, 2)
        except Exception:
            PTS1B_widget.value = max(truck_speed_year1peak_build_modelcalc_widget.value, 5)
            
    truck_speed_year1peak_build_userchanged_widget.observe(calculate_pts1b, names='value')
    
    Truck_Speed_year1peak_build_widgets = widgets.HBox([truck_speed_year1peak_build_modelcalc_widget,  truck_speed_year1peak_build_userchanged_widget,  PTS1B_explanation_widget])
    
###################################################################################################################################################################
    # Create the Non-HOV Volume Build widget to display the calculated value
    Non_HOV_Vol_year1nonpeak_build_modelcalc_widget = widgets.IntText(
        value=0,  # Set initial value to 0, or any other valid integer
        description="Non-HOV Volume (Calculated by Model):",
        disabled=True,  # Make it read-only so the user cannot modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Create the Non-HOV Volume Build widget for user-modified value
    Non_HOV_Vol_year1nonpeak_build_userchanged_widget = widgets.Text(
        value='',  # Initially set to 0 or a valid integer value
        description="Non-HOV Volume (Changed by User):",
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Widget for Non-HOV Volume (Used for Project Evaluation)
    NNV1B_widget = widgets.IntText(
        value=Non_HOV_Vol_year1nonpeak_build_modelcalc_widget.value,  # Set initially to the calculated value
        description="Non-HOV Volume (Used for Proj Evaluation):",
        disabled=True,  # Make it read-only
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Explanation widget
    NNV1B_explanation_widget = widgets.Text(
        value=None,  # Allow users to enter a text explanation
        description="Reasons for Change:",  # Label for the input field
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,  # Optional layout style, if needed
        style={'description_width': 'initial'}  # Optional style for description width
    )
    
    # Non-HOV Volume Build Widget update function
    def update_NonHOV_year1nonpeak_build_Volume(change):
        try:
            # Check for ProjType to determine formula logic
            if ProjType == "Hwy-Rail Grade Crossing":
                result = (
                    (ArrRate1 * GateTime1 / 60)  # Calculate the base formula for Hwy-Rail
                    / (1 - (ArrRate1 / DepRate1))  # Consider the ratio of arrival/departure rates
                    * (NumTrain1 / AnnualFactor)  # Adjust by number of trains and annual factor
                    * (1 - PerTruckNB)  # Adjust for non-truck percentage
                    * ADT20B / ADT20NB  # Adjust based on ADT ratios
                )
            else:
                # Default logic if ProjType is not Hwy-Rail
                traffic_factor = PerWeaveB if (ProjType == "Auxiliary Lane" or ProjType == "Off-Ramp Widening") else PerTruckB
                result = ((1 - PerPeakADT) * ADT1B) * (1 - traffic_factor)

                # Adjust based on PassRail, LRT, or Bus conditions
                if ProjType == "Passenger Rail" or ProjType == "Light-Rail" or ProjType == "Bus":
                    result -= (1 - TPerPeak) * TPerHwy * (TAPT1B - TAPT1NB) / AnnualFactor / AVONonNB

            # Update the output widget
            Non_HOV_Vol_year1nonpeak_build_modelcalc_widget.value = round(result, 0)

        except Exception as e:
            Non_HOV_Vol_year1nonpeak_build_modelcalc_widget.value = 0
                 
    

    # Observers to trigger updates when relevant widget values change
    projectinfo_widgets.subcategory_dropdown.observe(update_NonHOV_year1nonpeak_build_Volume, names='value')  #ProjType 
    projectinfo_widgets.hov_hot_lanes_build_widget.observe(update_NonHOV_year1nonpeak_build_Volume, names='value')  # HOVLanesB
    projectinfo_widgets.arrival_rate_base_year_no_build_widget.observe(update_NonHOV_year1nonpeak_build_Volume, names='value')  # ArrRate1
    projectinfo_widgets.GateTime1_widget.observe(update_NonHOV_year1nonpeak_build_Volume, names='value')  # GateTime1
    projectinfo_widgets.departure_rate_forecast_year_no_build_widget.observe(update_NonHOV_year1nonpeak_build_Volume, names='value')  # DepRate1
    projectinfo_widgets.NumTrain1_widget.observe(update_NonHOV_year1nonpeak_build_Volume, names='value')  # NumTrain1
    projectinfo_widgets.percent_trucks_nobuild_widget.observe(update_NonHOV_year1nonpeak_build_Volume, names='value')  # PerTruckNB
    projectinfo_widgets.adt_base_year_build_widget.observe(update_NonHOV_year1nonpeak_build_Volume, names='value')  # ADT1B
    projectinfo_widgets.percent_traffic_weave_build_widget.observe(update_NonHOV_year1nonpeak_build_Volume, names='value')  # PerWeaveB
    projectinfo_widgets.percent_trucks_build_widget.observe(update_NonHOV_year1nonpeak_build_Volume, names='value')  # PerTruckB
    projectinfo_widgets.TPerPeak_widget.observe(update_NonHOV_year1nonpeak_build_Volume, names='value') #TPerPeak
    projectinfo_widgets.TPerHwy_widget.observe(update_NonHOV_year1nonpeak_build_Volume, names='value') #TPerHwy
    projectinfo_widgets.TAPT1B_widget.observe(update_NonHOV_year1nonpeak_build_Volume, names='value') #TAPT1B
    projectinfo_widgets.TAPT1NB_widget.observe(update_NonHOV_year1nonpeak_build_Volume, names='value') #TAPT1NB
    projectinfo_widgets.AVO_traffic_NP_no_build_widget.observe(update_NonHOV_year1nonpeak_build_Volume, names='value') #AVONonNB
    
    
    # Function to calculate NNV1B (Non-Peak)
    def calculate_nnv1b_build_nonpeak(change):
        try:
            # Use user-modified value or default to model value if invalid
            if isinstance(Non_HOV_Vol_year1nonpeak_build_userchanged_widget.value, (int, float)) and Non_HOV_Vol_year1nonpeak_build_userchanged_widget.value >= 0:
                NNV1B = Non_HOV_Vol_year1nonpeak_build_userchanged_widget.value
            else:
                NNV1B = Non_HOV_Vol_year1nonpeak_build_modelcalc_widget.value

            # Update NNV1B widget
            NNV1B_widget.value = round(NNV1B, 0)

        except Exception as e:
            NNV1B_widget.value = 0

    # Link the NNV1B widget update to changes in Non-HOV Build User Modified Widget
    Non_HOV_Vol_year1nonpeak_build_userchanged_widget.observe(calculate_nnv1b_build_nonpeak, names='value')

    # Combine all widgets into a horizontal layout for Non-HOV Volume (Build)
    Non_HOV_vol_year1nonpeak_build_widgets = widgets.HBox([Non_HOV_Vol_year1nonpeak_build_modelcalc_widget,  Non_HOV_Vol_year1nonpeak_build_userchanged_widget, NNV1B_explanation_widget])
    
    
    #######################################################################################################


    # Define widgets
    weaving_vol_year1nonpeak_build_modelcalc_widget = widgets.IntText(
        value=0,
        description="Weaving Volume (Calculated by Model):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    weaving_vol_year1nonpeak_build_userchanged_widget = widgets.Text(
        value='',
        description="Weaving Volume (Changed by User):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Weaving Volume (Used for Project Evaluation)
    NWV1B_widget = widgets.IntText(
        value=weaving_vol_year1nonpeak_build_modelcalc_widget.value,
        description="Weaving Volume (Used for Project Evaluation):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Explanation widget for user-modified values
    NWV1B_explanation_widget = widgets.Text(
        value=None,
        description="Reasons for Change:",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Function to calculate Weaving Volume Year 1 Non-Peak Build
    def update_weaving_year1nonpeak_Build_volume(change=None):
        try:
            if ProjType in ["Auxiliary Lane", "Off-Ramp Widening"]:
                # Formula: Volume = ((1 - PerPeakADT) * ADT1B) * (PerWeaveB - PerTruckB)
                volume = ((1 - PerPeakADT) * ADT1B) * (PerWeaveB - PerTruckB)
            else:
                volume = 0  # Default to 0 if ProjType is not one of the specified types

            # If ProjType is "Auxiliary Lane", add RampVolNP * (24 - PeakLngthNB) to the volume
            if ProjType == "Auxiliary Lane":
                volume += RampVolNP * (24 - PeakLngthNB)

            # Set the calculated volume value to the widget
            weaving_vol_year1nonpeak_build_modelcalc_widget.value = round(volume, 2)

        except Exception:
            # If there's an error in the calculation, set the value to 0
            weaving_vol_year1nonpeak_build_modelcalc_widget.value = 0

    # Trigger updates based on used variables
    projectinfo_widgets.adt_base_year_build_widget.observe(update_weaving_year1nonpeak_Build_volume, names='value')  # ADT1B
    projectinfo_widgets.percent_traffic_weave_build_widget.observe(update_weaving_year1nonpeak_Build_volume, names='value')  # PerWeaveB
    projectinfo_widgets.percent_trucks_build_widget.observe(update_weaving_year1nonpeak_Build_volume, names='value')  # PerTruckB
    projectinfo_widgets.hourly_ramp_volume_peak_widget.observe(update_weaving_year1nonpeak_Build_volume, names='value')  # RampVolNP
    projectinfo_widgets.peak_period_widget.observe(update_weaving_year1nonpeak_Build_volume, names='value')  # PeakLngthNB


    # Function to calculate NWV1B (for user-modified values)
    def calculate_nwv1b(change):
        try:
            if isinstance(weaving_vol_year1nonpeak_build_userchanged_widget.value, (int, float)) and weaving_vol_year1nonpeak_build_userchanged_widget.value >= 0:
                NWV1B = max(float(weaving_vol_year1nonpeak_build_userchanged_widget.value), 0)
            else:
                NWV1B = max(weaving_vol_year1nonpeak_build_modelcalc_widget.value, 0)

            NWV1B_widget.value = NWV1B
        except Exception:
            NWV1B_widget.value = max(weaving_vol_year1nonpeak_build_modelcalc_widget.value, 0)

    # Link the function to the user input widget change
    weaving_vol_year1nonpeak_build_userchanged_widget.observe(calculate_nwv1b, names='value')

    # Combine all widgets into a horizontal layout for Weaving Volume
    Weaving_Vol_year1nonpeak_build_widgets = widgets.HBox([
        weaving_vol_year1nonpeak_build_modelcalc_widget,
        weaving_vol_year1nonpeak_build_userchanged_widget,
        NWV1B_explanation_widget
    ])

    #######################################################################################################
    
    # Define widgets
    truck_vol_year1nonpeak_build_modelcalc_widget = widgets.IntText(
        value=0,
        description="Truck Volume (Calculated by Model):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    truck_vol_year1nonpeak_build_userchanged_widget = widgets.Text(
        value='',
        description="Truck Volume (Changed by User):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Truck Volume (Used for Project Evaluation)
    NTV1B_widget = widgets.IntText(
        value=truck_vol_year1nonpeak_build_modelcalc_widget.value,
        description="Truck Volume (Used for Project Evaluation):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Explanation widget for user-modified values
    NTV1B_explanation_widget = widgets.Text(
        value=None,
        description="Reasons for Change:",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )
    
    
    def update_truck_year1nonpeak_Build_volume(change=None):
        try:
            if ProjType == "Hwy-Rail Grade Crossing":
                result = (
                    (ArrRate1 * GateTime1 / 60)
                    / (1 - (ArrRate1 / DepRate1))
                    * (NumTrain1 / AnnualFactor)
                    * PerTruckNB
                    * ADT20B / ADT20NB
                )
            else:
                result = ((1 - PerPeakADT) * ADT1B) * PerTruckB

            truck_vol_year1nonpeak_build_modelcalc_widget.value = round(result, 0)

        except Exception:
            truck_vol_year1nonpeak_build_modelcalc_widget.value = 0
            

    projectinfo_widgets.subcategory_dropdown.observe(update_truck_year1nonpeak_Build_volume, names='value')  # ProjType
    projectinfo_widgets.arrival_rate_base_year_no_build_widget.observe(update_truck_year1nonpeak_Build_volume, names='value')  # ArrRate1
    projectinfo_widgets.GateTime1_widget.observe(update_truck_year1nonpeak_Build_volume, names='value')  # GateTime1
    projectinfo_widgets.departure_rate_forecast_year_no_build_widget.observe(update_truck_year1nonpeak_Build_volume, names='value')  # DepRate1
    projectinfo_widgets.NumTrain1_widget.observe(update_truck_year1nonpeak_Build_volume, names='value')  # NumTrain1
    projectinfo_widgets.percent_trucks_nobuild_widget.observe(update_truck_year1nonpeak_Build_volume, names='value')  # PerTruckNB
    projectinfo_widgets.adt_20_year_build_widget.observe(update_truck_year1nonpeak_Build_volume, names='value')  # ADT20B
    projectinfo_widgets.ADT_20NB_widget.observe(update_truck_year1nonpeak_Build_volume, names='value')  # ADT20NB
    projectinfo_widgets.adt_base_year_build_widget.observe(update_truck_year1nonpeak_Build_volume, names='value')  # ADT1B
    projectinfo_widgets.percent_trucks_build_widget.observe(update_truck_year1nonpeak_Build_volume, names='value')  # PerTruckB

    def calculate_ntv1b(change):
        try:
            if isinstance(truck_vol_year1nonpeak_build_userchanged_widget.value, (int, float)) and truck_vol_year1nonpeak_build_userchanged_widget.value >= 0:
                NTV1B = max(float(truck_vol_year1nonpeak_build_userchanged_widget.value), 0)
            else:
                NTV1B = max(truck_vol_year1nonpeak_build_modelcalc_widget.value, 0)

            NTV1B_widget.value = NTV1B
        except Exception:
            NTV1B_widget.value = max(truck_vol_year1nonpeak_build_modelcalc_widget.value, 0)

    # Link the function to user input
    truck_vol_year1nonpeak_build_userchanged_widget.observe(calculate_ntv1b, names='value')
    
    
    Truck_Vol_year1nonpeak_build_widgets = widgets.HBox([
        truck_vol_year1nonpeak_build_modelcalc_widget,
        truck_vol_year1nonpeak_build_userchanged_widget,
        NTV1B_explanation_widget
    ])

    
    #######################################################################################################

    # Model-calculated Non-HOV Speed (Non-Peak)
    nonhov_speed_year1nonpeak_build_modelcalc_widget = widgets.FloatText(
        value=0,
        description="Non-HOV Speed (Calculated by Model):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # User input Non-HOV Speed (Non-Peak)
    nonhov_speed_year1nonpeak_build_userchanged_widget = widgets.Text(
        value='',
        description="Non-HOV Speed (Changed by User):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Final value used for evaluation
    NNS1B_widget = widgets.FloatText(
        value=nonhov_speed_year1nonpeak_build_modelcalc_widget.value,
        description="Non-HOV Speed (Used for Project Evaluation):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Explanation input
    NNS1B_explanation_widget = widgets.Text(
        value=None,
        description="Reasons for Change:",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )
    
    
    def update_nonhov_year1nonpeak_Build_speed(change=None):
        try:
            # Volume values
            NNV1B = NNV1B_widget.value
            NWV1B = NWV1B_widget.value
            NTV1B = NTV1B_widget.value

            total_volume = NNV1B + NWV1B + NTV1B

            if ProjType == "Hwy-Rail Grade Crossing":
                NonHOVSpeed = FFSpeedB
            elif total_volume == 0:
                NonHOVSpeed = 55
            else:
                GenAlphaB = roadway_capacity_non_HOV["Non-HOV Lanes"]["Build"]["GenAlphaB"]
                GenBetaB = roadway_capacity_non_HOV["Non-HOV Lanes"]["Build"]["GenBetaB"]
                GenLaneCapB = roadway_capacity_non_HOV["Non-HOV Lanes"]["Build"]["GenLaneCapB"]

                denominator = (GenLanesB + HOVLanesB) * GenLaneCapB * (24 - PeakLngthNB)
                vc_ratio = min((total_volume / denominator) if denominator else 0, MaxVC)

                speed = FFSpeedB / (1 + GenAlphaB * (vc_ratio ** GenBetaB))

                # Adjust for Freeway Connector
                if ProjType == "Freeway Connector":
                    closest_weave_key = min(SpeedWeaveAdj.keys(), key=lambda x: abs(x - PerWeaveB))
                    speed *= SpeedWeaveAdj[closest_weave_key].get("Freeway", 1)

                # Adjust for HOV Connector or Drop Ramp
                if ProjType in ["HOV Connector", "HOV Drop Ramp"]:
                    closest_weave_key = min(SpeedWeaveAdj.keys(), key=lambda x: abs(x - PerWeaveB))
                    speed *= SpeedWeaveAdj[closest_weave_key].get("HOV", 1)

                # Adjust for Pavement
                if ProjType == "Pavement":
                    closest_iri = min(SpeedPavAdj.keys(), key=lambda x: abs(x - IRI1B))
                    speed *= SpeedPavAdj[closest_iri].get("Auto", 1)

                NonHOVSpeed = min(speed, FFSpeedB)

            nonhov_speed_year1nonpeak_build_modelcalc_widget.value = round(NonHOVSpeed, 2)

        except Exception:
            nonhov_speed_year1nonpeak_build_modelcalc_widget.value = 0
            
    update_nonhov_year1nonpeak_Build_speed()
            
            
    # Trigger updates based on used variables
    NNV1B_widget.observe(update_nonhov_year1nonpeak_Build_speed, names='value')  # NNV1B
    NWV1B_widget.observe(update_nonhov_year1nonpeak_Build_speed, names='value')  # NWV1B
    NTV1B_widget.observe(update_nonhov_year1nonpeak_Build_speed, names='value')  # NTV1B
    projectinfo_widgets.free_flow_speed_build_widget.observe(update_nonhov_year1nonpeak_Build_speed, names='value')  # FFSpeedB
    projectinfo_widgets.peak_period_widget.observe(update_nonhov_year1nonpeak_Build_speed, names='value')  # PeakLngthNB
    projectinfo_widgets.percent_traffic_weave_build_widget.observe(update_nonhov_year1nonpeak_Build_speed, names='value')  # PerWeaveB
    projectinfo_widgets.iri_base_year_build_widget.observe(update_nonhov_year1nonpeak_Build_speed, names='value')  # IRI1B
    projectinfo_widgets.subcategory_dropdown.observe(update_nonhov_year1nonpeak_Build_speed, names='value')  # ProjType
    
    def calculate_nns1b(change):
        try:
            if isinstance(nonhov_speed_year1nonpeak_build_userchanged_widget.value, (int, float)) and nonhov_speed_year1nonpeak_build_userchanged_widget.value >= 0:
                NNS1B = max(float(nonhov_speed_year1nonpeak_build_userchanged_widget.value), 5)
            else:
                NNS1B = max(nonhov_speed_year1nonpeak_build_modelcalc_widget.value, 5)

            NNS1B_widget.value = round(NNS1B, 2)
        except Exception:
            NNS1B_widget.value = max(nonhov_speed_year1nonpeak_build_modelcalc_widget.value, 5)

    nonhov_speed_year1nonpeak_build_userchanged_widget.observe(calculate_nns1b, names='value')
    
    NonHOV_Speed_Year1NonPeak_Build_Widgets = widgets.HBox([
        nonhov_speed_year1nonpeak_build_modelcalc_widget,
        nonhov_speed_year1nonpeak_build_userchanged_widget,
        NNS1B_explanation_widget
    ])


    #######################################################################################################


    # Weaving Speed Year 1 Non-Peak Build Widgets

    weaving_speed_year1nonpeak_build_modelcalc_widget = widgets.FloatText(
        value=0,
        description="Weaving Speed (Calculated by Model):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    weaving_speed_year1nonpeak_build_userchanged_widget = widgets.Text(
        value='',
        description="Weaving Speed (Changed by User):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    NWS1B_widget = widgets.FloatText(
        value=weaving_speed_year1nonpeak_build_modelcalc_widget.value,
        description="Weaving Speed (Used for Project Evaluation):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    NWS1B_explanation_widget = widgets.Text(
        value=None,
        description="Reasons for Change:",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    def update_weave_year1nonpeak_Build_speed(change=None):
        try:
            NWV1B = NWV1B_widget.value
            NTV1B = NTV1B_widget.value
            NNS1B = NNS1B_widget.value

            if NWV1B == 0:
                weave_speed = 55
            elif ProjType == "Auxiliary Lane":
                exp_component = math.exp((NWV1B + NTV1B) / NumDirections / (24 - PeakLngthNB) / 1000)
                ramp_factor = 1083 if ProjType == "Off-Ramp Widening" else SegmentB * 5280
                ramp_effect = 0.002 * (ramp_factor * RampFFSpdB / 1000)

                base_speed = FFSpeedB - (FFSpeedB - 42) * (0.321 + 0.0039 * exp_component - ramp_effect)
                adjusted_speed = 1.1 * base_speed

                # Pavement Adjustment
                pavement_adj = 1
                if ProjType == "Pavement":
                    closest_iri_key = min(SpeedPavAdj.keys(), key=lambda x: abs(x - IRI1B))
                    pavement_adj = SpeedPavAdj[closest_iri_key]["Auto"]

                # Final Speed
                final_speed = adjusted_speed * pavement_adj
                weave_speed = max(5, min(NNS1B, final_speed))

            else:
                weave_speed = NNS1B

            weaving_speed_year1nonpeak_build_modelcalc_widget.value = round(weave_speed, 2)

        except Exception:
            weaving_speed_year1nonpeak_build_modelcalc_widget.value = 0

    # Initial speed calculation
    update_weave_year1nonpeak_Build_speed()

    # Trigger updates
    NWV1B_widget.observe(update_weave_year1nonpeak_Build_speed, names='value')  # NWV1B
    NTV1B_widget.observe(update_weave_year1nonpeak_Build_speed, names='value')  # NTV1B
    NNS1B_widget.observe(update_weave_year1nonpeak_Build_speed, names='value')  # NNS1B
    projectinfo_widgets.free_flow_speed_build_widget.observe(update_weave_year1nonpeak_Build_speed, names='value')  # FFSpeedB
    projectinfo_widgets.peak_period_widget.observe(update_weave_year1nonpeak_Build_speed, names='value')  # PeakLngthNB
    projectinfo_widgets.one_two_way_widget.observe(update_weave_year1nonpeak_Build_speed, names='value')  # NumDirections
    projectinfo_widgets.subcategory_dropdown.observe(update_weave_year1nonpeak_Build_speed, names='value')  # ProjType
    projectinfo_widgets.iri_base_year_build_widget.observe(update_weave_year1nonpeak_Build_speed, names='value')  # IRI1B
    projectinfo_widgets.highway_segment_build_widget.observe(update_weave_year1nonpeak_Build_speed, names='value') #SegmentB
    projectinfo_widgets.ramp_design_speed_build_widget.observe(update_weave_year1nonpeak_Build_speed, names='value') #RampFFSpeedB

    # User changed weaving speed
    def calculate_nws1b(change):
        try:
            if isinstance(weaving_speed_year1nonpeak_build_userchanged_widget.value, (int, float)) or (
                isinstance(weaving_speed_year1nonpeak_build_userchanged_widget.value, str) and
                weaving_speed_year1nonpeak_build_userchanged_widget.value.replace('.', '', 1).isdigit()
            ):
                NWS1B = max(float(weaving_speed_year1nonpeak_build_userchanged_widget.value), 5)
            else:
                NWS1B = max(weaving_speed_year1nonpeak_build_modelcalc_widget.value, 5)

            NWS1B_widget.value = round(NWS1B, 2)
        except Exception:
            NWS1B_widget.value = max(weaving_speed_year1nonpeak_build_modelcalc_widget.value, 5)

    # Link user input to calculation
    weaving_speed_year1nonpeak_build_userchanged_widget.observe(calculate_nws1b, names='value')

    # Combine widgets for layout
    Weaving_Speed_year1nonpeak_build_widgets = widgets.HBox([weaving_speed_year1nonpeak_build_modelcalc_widget, weaving_speed_year1nonpeak_build_userchanged_widget, NWS1B_explanation_widget])


    #######################################################################################################
    # Truck Speed Year 1 Non-Peak Build Widgets

    truck_speed_year1nonpeak_build_modelcalc_widget = widgets.FloatText(
        value=0,
        description="Truck Speed (Calculated by Model):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    truck_speed_year1nonpeak_build_userchanged_widget = widgets.Text(
        value='',
        description="Truck Speed (Changed by User):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    NTS1B_widget = widgets.FloatText(
        value=truck_speed_year1nonpeak_build_modelcalc_widget.value,
        description="Truck Speed (Used for Project Evaluation):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    NTS1B_explanation_widget = widgets.Text(
        value=None,
        description="Reasons for Change:",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    def update_truck_year1nonpeak_Build_speed(change=None):
        try:
            NTV1B = NTV1B_widget.value
            NNS1B = NNS1B_widget.value
            NWS1B = NWS1B_widget.value 

            # If HwyRail is true, set truck speed to Free Flow Speed
            if ProjType == "Hwy-Rail Grade Crossing":
                truck_speed = FFSpeedB
            elif NTV1B == 0:
                truck_speed = 55
            else:
                # Use the provided formula to calculate the truck speed
                if ProjType == "Auxiliary Lane":
                    truck_speed = min(TruckSpeed, max(NWS1B, NNS1B) / (SpeedPavAdj.get(IRI1B, {}).get("Auto", 1)))
                else:
                    truck_speed = min(TruckSpeed, max(NWS1B, NNS1B) / SpeedPavAdj.get(IRI1B, {}).get("Auto", 1))

                # Pavement Adjustment
                if ProjType == "Pavement":
                    closest_iri_key = min(SpeedPavAdj.keys(), key=lambda x: abs(x - IRI1B))
                    pavement_adj = SpeedPavAdj[closest_iri_key].get("Truck", 1)
                    truck_speed *= pavement_adj

            # Set the calculated truck speed value
            truck_speed_year1nonpeak_build_modelcalc_widget.value = round(truck_speed, 2)

        except Exception:
            truck_speed_year1nonpeak_build_modelcalc_widget.value = 0

    # Initial speed calculation
    update_truck_year1nonpeak_Build_speed()

    # Trigger updates for truck speed calculation
    NTV1B_widget.observe(update_truck_year1nonpeak_Build_speed, names='value')  # NTV1B
    NNS1B_widget.observe(update_truck_year1nonpeak_Build_speed, names='value')  # NNS1B
    NWS1B_widget.observe(update_truck_year1nonpeak_Build_speed, names='value')  # NWS1B
    projectinfo_widgets.truck_speed_widget.observe(update_truck_year1nonpeak_Build_speed, names='value')  # TruckSpeed
    projectinfo_widgets.free_flow_speed_build_widget.observe(update_truck_year1nonpeak_Build_speed, names='value')  # FFSpeedB
    projectinfo_widgets.subcategory_dropdown.observe(update_truck_year1nonpeak_Build_speed, names='value')  # ProjType
    projectinfo_widgets.iri_base_year_build_widget.observe(update_truck_year1nonpeak_Build_speed, names='value')  # IRI1B

    # User changed truck speed
    def calculate_nts1b(change):
        try:
            if isinstance(truck_speed_year1nonpeak_build_userchanged_widget.value, (int, float)) or (
                isinstance(truck_speed_year1nonpeak_build_userchanged_widget.value, str) and
                truck_speed_year1nonpeak_build_userchanged_widget.value.replace('.', '', 1).isdigit()
            ):
                NTS1B = max(float(truck_speed_year1nonpeak_build_userchanged_widget.value), 5)
            else:
                NTS1B = max(truck_speed_year1nonpeak_build_modelcalc_widget.value, 5)

            NTS1B_widget.value = round(NTS1B, 2)
        except Exception:
            NTS1B_widget.value = max(truck_speed_year1nonpeak_build_modelcalc_widget.value, 5)

    # Link user input to calculation
    truck_speed_year1nonpeak_build_userchanged_widget.observe(calculate_nts1b, names='value')

    # Combine widgets for layout
    Truck_Speed_year1nonpeak_build_widgets = widgets.HBox([truck_speed_year1nonpeak_build_modelcalc_widget, truck_speed_year1nonpeak_build_userchanged_widget, NTS1B_explanation_widget])

###################################################################################################################################################################

    # Create the HOV Volume widget to display the calculated value
    HOV_Vol_year20peak_build_modelcalc_widget = widgets.IntText(
        value=0,  # Set initial value to 0, or any other valid integer
        description="HOV Volume(Calculated by Model):",
        disabled=True,  # Make it read-only so the user cannot modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Create the HOV Volume Peak Period widget for user-modified value
    HOV_Vol_year20peak_build_userchanged_widget = widgets.Text(
        value='',  # Initially set to 0 or a valid integer value
        description="HOV Volume (Changed by User):",
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Create the PHV20B widget based on the formula
    PHV20B_widget = widgets.IntText(
        value=HOV_Vol_year20peak_build_modelcalc_widget.value,  # Set initially to the calculated value
        description="HOV Volume (Used for Proj Evaluation):",
        disabled=True,  # Make it read-only 
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    PHV20B_explanation_widget = widgets.Text(
        value=None,  
        description="Reasons for Change:",  # Label for the input field
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,  # Optional layout style, if needed
        style={'description_width': 'initial'}  # Optional style for description width
    )

    # Function to update HOV Volume dynamically
    def update_HOV_Year20Peak_Build_Volume(change):
        try:
            # Check if project type is "Hwy-Rail Grade Crossing"
            if ProjType == "Hwy-Rail Grade Crossing":
                HOV_Volume_Year20Peak_Build_Model = 0

            # Check if project type is "Queuing"
            elif ProjType == "Queuing":
                numerator = PeakLngthNB * (DepRate1 - ADT1NB * (1 - PerPeakADT) / (24 - PeakLngthNB))
                denominator = (ADT1NB / ADT20NB * DepRate20 - ADT1NB * (1 - PerPeakADT) / (24 - PeakLngthNB))
                HOV_Volume_Year20Peak_Build_Model = numerator / denominator if denominator != 0 else 0

            # Default case for other project types
            else:
                hov_factor = (1 - PerWeaveNB) if ProjType in ["HOV Connector", "HOV Drop Ramp"] else 1
                HOV_Volume_Year20Peak_Build_Model = PeakLngthNB * HOVvolB * hov_factor

            # Update the widget with the result
            HOV_Vol_year20peak_build_modelcalc_widget.value = round(HOV_Volume_Year20Peak_Build_Model, 2)

        except Exception:
            HOV_Vol_year20peak_build_modelcalc_widget.value = 0

    # Attach observers to the relevant widgets to update the HOV Volume widget dynamically
    projectinfo_widgets.subcategory_dropdown.observe(update_HOV_Year20Peak_Build_Volume, names='value')  # ProjType
    projectinfo_widgets.peak_period_widget.observe(update_HOV_Year20Peak_Build_Volume, names='value')  # PeakLngthNB
    projectinfo_widgets.percent_traffic_weave_no_build_widget.observe(update_HOV_Year20Peak_Build_Volume, names='value')  # PerPeakADT
    projectinfo_widgets.departure_rate_forecast_year_no_build_widget.observe(update_HOV_Year20Peak_Build_Volume, names='value')  # DepRate1
    projectinfo_widgets.adt_base_year_no_build_widget.observe(update_HOV_Year20Peak_Build_Volume, names='value')  # ADT1NB
    projectinfo_widgets.ADT_20NB_widget.observe(update_HOV_Year20Peak_Build_Volume, names='value')  # ADT20NB
    projectinfo_widgets.departure_rate_forecast_year_build_widget.observe(update_HOV_Year20Peak_Build_Volume, names='value')  # DepRate20
    projectinfo_widgets.HOV_lane_build_widget.observe(update_HOV_Year20Peak_Build_Volume, names='value') #HOVVolB
    
    


    # Function to calculate PHV20B
    def calculate_phv20b(change):
        # Access the user-modified value directly from the widget
        if isinstance(HOV_Vol_year20peak_build_userchanged_widget.value, (int, float)) and HOV_Vol_year20peak_build_userchanged_widget.value >= 0:
            PHV20B = HOV_Vol_year20peak_build_userchanged_widget.value  # Use the user-modified value if valid
        else:
            PHV20B = HOV_Vol_year20peak_build_modelcalc_widget.value  # Use the model value if the user value is invalid

        # Update the value of PHV20B widget
        PHV20B_widget.value = PHV20B

    # Link the PHV20B widget update to changes in HOV_Vol_peak_userchanged_widget
    HOV_Vol_year20peak_build_userchanged_widget.observe(calculate_phv20b, names='value')

    # Combine all widgets into a horizontal layout for HOV Volume
    HOV_vol_year20peak_build_widgets = widgets.HBox([HOV_Vol_year20peak_build_modelcalc_widget, HOV_Vol_year20peak_build_userchanged_widget, PHV20B_explanation_widget])

    
    #######################################################################################################
    
    # Create the Non-HOV Volume widget to display the calculated value
    nonHOV_Vol_year20peak_build_modelcalc_widget = widgets.FloatText(
        value=0,
        description="Non-HOV Volume (Calculated by Model):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Create the Non-HOV Volume widget for user-modified value
    nonHOV_Vol_year20peak_build_userchanged_widget = widgets.Text(
        value='',
        description="Non-HOV Volume (Changed by User):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Final value used for project evaluation
    PNV20B_widget = widgets.FloatText(
        value=nonHOV_Vol_year20peak_build_modelcalc_widget.value,
        description="Non-HOV Volume (Used for Proj Evaluation):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    PNV20B_explanation_widget = widgets.Text(
        value=None,
        description="Reasons for Change:",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Function to update Non-HOV Volume dynamically
    def update_nonHOV_Year20Peak_Build_Volume(change):
        try:
            if ProjType == "Hwy-Rail Grade Crossing":
                nonHOV_Volume_Year20Peak_Build_Model = 0

            elif ProjType == "Queuing":
                numerator = ADT20B * DepRate20 * PeakLngthNB * (DepRate1 - ADT1NB * (1 - PerPeakADT) / (24 - PeakLngthNB))
                denominator = (ADT1NB / ADT20NB * DepRate20 - ADT1NB * (1 - PerPeakADT) / (24 - PeakLngthNB)) / ADT20NB
                nonHOV_Volume_Year20Peak_Build_Model = numerator / denominator if denominator != 0 else 0

            else:
                # Determine appropriate percentage
                if ProjType in ["Auxiliary Lane", "Off-Ramp Widening"]:
                    subtract_pct = PerWeaveB
                else:
                    subtract_pct = PerTruckB

                hov_adjustment = 0
                if ProjType == "Queuing":
                    hov_adjustment = HOVvolB / DepRate20 * ADT20NB / ADT20B

                tms_factor = TMSAdj.get(TMSLookup, {}).get("VolumeWith", 1)

                transit_deduction = 0
                if ProjType in ["Passenger Rail", "Light-Rail", "Bus"]:
                    transit_deduction = TPerPeak * TPerHwy * (TAPT20B - TAPT20NB) / AnnualFactor / AVOPeakNB

                nonHOV_Volume_Year20Peak_Build_Model = (
                    PerPeakADT * ADT20B *
                    (1 - subtract_pct - hov_adjustment) *
                    tms_factor -
                    HOVvolB * PeakLngthNB -
                    transit_deduction
                )

            nonHOV_Vol_year20peak_build_modelcalc_widget.value = round(nonHOV_Volume_Year20Peak_Build_Model, 2)

        except Exception:
            nonHOV_Vol_year20peak_build_modelcalc_widget.value = 0

    # Observer setup
    projectinfo_widgets.subcategory_dropdown.observe(update_nonHOV_Year20Peak_Build_Volume, names='value')  # ProjType
    projectinfo_widgets.adt_20_year_build_widget.observe(update_nonHOV_Year20Peak_Build_Volume, names='value')  # ADT20B
    projectinfo_widgets.departure_rate_forecast_year_build_widget.observe(update_nonHOV_Year20Peak_Build_Volume, names='value')  # DepRate20
    projectinfo_widgets.peak_period_widget.observe(update_nonHOV_Year20Peak_Build_Volume, names='value')  # PeakLngthNB
    projectinfo_widgets.departure_rate_forecast_year_no_build_widget.observe(update_nonHOV_Year20Peak_Build_Volume, names='value')  # DepRate1
    projectinfo_widgets.adt_base_year_no_build_widget.observe(update_nonHOV_Year20Peak_Build_Volume, names='value')  # ADT1NB
    projectinfo_widgets.percent_traffic_weave_build_widget.observe(update_nonHOV_Year20Peak_Build_Volume, names='value')  # PerWeaveB
    projectinfo_widgets.percent_trucks_build_widget.observe(update_nonHOV_Year20Peak_Build_Volume, names='value')  # PerTruckB
    projectinfo_widgets.HOV_lane_build_widget.observe(update_nonHOV_Year20Peak_Build_Volume, names='value')  # HOVvolB
    projectinfo_widgets.ADT_20NB_widget.observe(update_nonHOV_Year20Peak_Build_Volume, names='value')  # ADT20NB
    projectinfo_widgets.subcategory_dropdown.observe(update_nonHOV_Year20Peak_Build_Volume, names='value')  # ProjType (again for transit checks)
    projectinfo_widgets.TPerPeak_widget.observe(update_nonHOV_Year20Peak_Build_Volume, names='value')  # TPerPeak
    projectinfo_widgets.TPerHwy_widget.observe(update_nonHOV_Year20Peak_Build_Volume, names='value')  # TPerHwy
    projectinfo_widgets.TAPT20B_widget.observe(update_nonHOV_Year20Peak_Build_Volume, names='value')  # TAPT20B
    projectinfo_widgets.TAPT20NB_widget.observe(update_nonHOV_Year20Peak_Build_Volume, names='value')  # TAPT20NB
    projectinfo_widgets.AVO_traffic_P_no_build_widget.observe(update_nonHOV_Year20Peak_Build_Volume, names='value')  # AVOPeakNB

    
    # Final value widget logic
    def calculate_pnv20b(change):
        try:
            val = nonHOV_Vol_year20peak_build_userchanged_widget.value
            if isinstance(val, (int, float)) or (isinstance(val, str) and val.replace('.', '', 1).isdigit()):
                PNV20B = max(float(val), 0)
            else:
                PNV20B = max(nonHOV_Vol_year20peak_build_modelcalc_widget.value, 0)

            PNV20B_widget.value = round(PNV20B, 2)
        except Exception:
            PNV20B_widget.value = max(nonHOV_Vol_year20peak_build_modelcalc_widget.value, 0)

    nonHOV_Vol_year20peak_build_userchanged_widget.observe(calculate_pnv20b, names='value')

    # Combine into layout
    nonHOV_vol_year20peak_build_widgets = widgets.HBox([
        nonHOV_Vol_year20peak_build_modelcalc_widget,
        nonHOV_Vol_year20peak_build_userchanged_widget,
        PNV20B_explanation_widget
    ])

    #######################################################################################################
    
    # Create the Weaving Volume widget to display the calculated value
    weaving_Vol_year20peak_build_modelcalc_widget = widgets.FloatText(
        value=0,
        description="Weaving Volume (Calculated by Model):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Create the Weaving Volume widget for user-modified value
    weaving_Vol_year20peak_build_userchanged_widget = widgets.Text(
        value='',
        description="Weaving Volume (Changed by User):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Final value used for project evaluation
    PWV20B_widget = widgets.FloatText(
        value=weaving_Vol_year20peak_build_modelcalc_widget.value,
        description="Weaving Volume (Used for Proj Evaluation):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    PWV20B_explanation_widget = widgets.Text(
        value=None,
        description="Reasons for Change:",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Function to update Weaving Volume dynamically
    def update_weaving_Year20Peak_Build_Volume(change):
        try:
            weaving_volume = 0

            if ProjType in ["Auxiliary Lane", "Off-Ramp Widening"]:
                tms_factor = TMSAdj.get(TMSLookup, {}).get("VolumeWith", 1)
                weaving_volume += (PerPeakADT * ADT20B) * (PerWeaveB - PerTruckB) * tms_factor

            if ProjType == "Auxiliary Lane":
                weaving_volume += RampVolP * PeakLngthNB

            if ProjType in ["HOV Connector", "HOV Drop Ramp"]:
                weaving_volume += PerWeaveNB * HOVvolB * PeakLngthNB

            weaving_Vol_year20peak_build_modelcalc_widget.value = round(weaving_volume, 2)

        except Exception:
            weaving_Vol_year20peak_build_modelcalc_widget.value = 0

    # Observer setup
    projectinfo_widgets.subcategory_dropdown.observe(update_weaving_Year20Peak_Build_Volume, names='value')  # ProjType
    projectinfo_widgets.adt_20_year_build_widget.observe(update_weaving_Year20Peak_Build_Volume, names='value')  # ADT20B
    projectinfo_widgets.percent_traffic_weave_build_widget.observe(update_weaving_Year20Peak_Build_Volume, names='value')  # PerWeaveB
    projectinfo_widgets.percent_trucks_build_widget.observe(update_weaving_Year20Peak_Build_Volume, names='value')  # PerTruckB
    projectinfo_widgets.hourly_ramp_volume_peak_widget.observe(update_weaving_Year20Peak_Build_Volume, names='value')  # RampVolP
    projectinfo_widgets.peak_period_widget.observe(update_weaving_Year20Peak_Build_Volume, names='value')  # PeakLngthNB
    projectinfo_widgets.percent_traffic_weave_no_build_widget.observe(update_weaving_Year20Peak_Build_Volume, names='value')  # PerWeaveNB
    projectinfo_widgets.HOV_lane_build_widget.observe(update_weaving_Year20Peak_Build_Volume, names='value')  # HOVvolB

    # Final value widget logic
    def calculate_pwv20b(change):
        try:
            val = weaving_Vol_year20peak_build_userchanged_widget.value
            if isinstance(val, (int, float)) or (isinstance(val, str) and val.replace('.', '', 1).isdigit()):
                PWV20B = max(float(val), 0)
            else:
                PWV20B = max(weaving_Vol_year20peak_build_modelcalc_widget.value, 0)

            PWV20B_widget.value = round(PWV20B, 2)
        except Exception:
            PWV20B_widget.value = max(weaving_Vol_year20peak_build_modelcalc_widget.value, 0)

    weaving_Vol_year20peak_build_userchanged_widget.observe(calculate_pwv20b, names='value')

    # Combine into layout
    Weaving_vol_year20peak_build_widgets = widgets.HBox([
        weaving_Vol_year20peak_build_modelcalc_widget,
        weaving_Vol_year20peak_build_userchanged_widget,
        PWV20B_explanation_widget
    ])
    
    #######################################################################################################    
    
    # Create the Truck Volume widget to display the calculated value
    truck_Vol_year20peak_build_modelcalc_widget = widgets.FloatText(
        value=0,
        description="Truck Volume (Calculated by Model):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Create the Truck Volume widget for user-modified value
    truck_Vol_year20peak_build_userchanged_widget = widgets.Text(
        value='',
        description="Truck Volume (Changed by User):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Final value used for project evaluation
    PTV20B_widget = widgets.FloatText(
        value=truck_Vol_year20peak_build_modelcalc_widget.value,
        description="Truck Volume (Used for Proj Evaluation):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    PTV20B_explanation_widget = widgets.Text(
        value=None,
        description="Reasons for Change:",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Function to update Truck Volume dynamically
    def update_truck_Year20Peak_Build_Volume(change):
        try:
            if ProjType == "Hwy-Rail Grade Crossing":
                truck_volume = 0

            elif ProjType == "Queuing":
                numerator = ADT20B * DepRate20 * PeakLngthNB * (DepRate1 - ADT1NB * (1 - PerPeakADT) / (24 - PeakLngthNB))
                denominator = (ADT1NB / ADT20NB * DepRate20 - ADT1NB * (1 - PerPeakADT) / (24 - PeakLngthNB)) / ADT20NB
                truck_volume = numerator / denominator if denominator != 0 else 0

            else:
                tms_factor = TMSAdj.get(TMSLookup, {}).get("VolumeWith", 1)
                truck_volume = PerPeakADT * ADT20B * PerTruckB * tms_factor

            truck_Vol_year20peak_build_modelcalc_widget.value = round(truck_volume, 2)

        except Exception:
            truck_Vol_year20peak_build_modelcalc_widget.value = 0

    # Observer setup
    projectinfo_widgets.subcategory_dropdown.observe(update_truck_Year20Peak_Build_Volume, names='value')  # ProjType
    projectinfo_widgets.adt_20_year_build_widget.observe(update_truck_Year20Peak_Build_Volume, names='value')  # ADT20B
    projectinfo_widgets.departure_rate_forecast_year_build_widget.observe(update_truck_Year20Peak_Build_Volume, names='value')  # DepRate20
    projectinfo_widgets.peak_period_widget.observe(update_truck_Year20Peak_Build_Volume, names='value')  # PeakLngthNB
    projectinfo_widgets.departure_rate_forecast_year_no_build_widget.observe(update_truck_Year20Peak_Build_Volume, names='value')  # DepRate1
    projectinfo_widgets.adt_base_year_no_build_widget.observe(update_truck_Year20Peak_Build_Volume, names='value')  # ADT1NB
    projectinfo_widgets.ADT_20NB_widget.observe(update_truck_Year20Peak_Build_Volume, names='value')  # ADT20NB
    projectinfo_widgets.percent_trucks_build_widget.observe(update_truck_Year20Peak_Build_Volume, names='value')  # PerTruckB


    # Final value widget logic
    def calculate_ptv20b(change):
        try:
            val = truck_Vol_year20peak_build_userchanged_widget.value
            if isinstance(val, (int, float)) or (isinstance(val, str) and val.replace('.', '', 1).isdigit()):
                PTV20B = max(float(val), 0)
            else:
                PTV20B = max(truck_Vol_year20peak_build_modelcalc_widget.value, 0)

            PTV20B_widget.value = round(PTV20B, 2)
        except Exception:
            PTV20B_widget.value = max(truck_Vol_year20peak_build_modelcalc_widget.value, 0)

    truck_Vol_year20peak_build_userchanged_widget.observe(calculate_ptv20b, names='value')

    # Combine into layout
    Truck_vol_year20peak_build_widgets = widgets.HBox([
        truck_Vol_year20peak_build_modelcalc_widget,
        truck_Vol_year20peak_build_userchanged_widget,
        PTV20B_explanation_widget
    ])
    
    
    ####################################################################################################### 
    
    # Non-HOV Speed widgets for Year 20 Peak Build
    nonhov_speed_year20peak_build_modelcalc_widget = widgets.IntText(
        value=0,  # Set initial value to 0 or any other valid integer
        description="Non-HOV Speed (Calculated by Model):",
        disabled=True,  # Make it read-only so the user cannot modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    nonhov_speed_year20peak_build_userchanged_widget = widgets.Text(
        value='',  # Initially set to 0 or a valid integer value
        description="Non-HOV Speed (Changed by User):",
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Non-HOV Speed Volume (Used for Project Evaluation)
    PNS20B_widget = widgets.IntText(
        value=nonhov_speed_year20peak_build_modelcalc_widget.value,  # Set initially to the calculated value
        description="Non-HOV Speed (Used for Proj Evaluation):",
        disabled=True,  # Make it read-only
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Explanation widget for user-modified values
    PNS20B_explanation_widget = widgets.Text(
        value=None,  # Allow users to enter a text explanation
        description="Reasons for Change:",  # Label for the input field
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,  # Optional layout style, if needed
        style={'description_width': 'initial'}  # Optional style for description width
    )

    def update_nonhov_year20peak_build_speed(change=None):
        # Accessing the relevant traffic volume widgets (PHV20B, PNV20B, PWV20B, PTV20B)
        traffic_volumes = [
            PHV20B_widget.value,  
            PNV20B_widget.value,  
            PWV20B_widget.value,  
            PTV20B_widget.value   
        ]

        sum_all = sum(traffic_volumes)

        # Step 1: Formula for Non-HOV Speed calculation
        if sum_all == 0:
            nonhov_speed = 55  # If total volume is zero, use default value
        else:
            if ProjType == "Queuing":
                # Special case for queuing calculation
                try:
                    part1 = (
                        PeakLngthNB / DepRate20 / 2
                        * (ArrRate20 - DepRate20)
                        * (DepRate1 - ADT1NB * (1 - PerPeakADT) / (24 - PeakLngthNB))
                        / (ArrRate1 - ADT1NB * (1 - PerPeakADT) / (24 - PeakLngthNB))
                    )
                except ZeroDivisionError:
                    part1 = float("inf")

                nonhov_speed = ImpactedNB / (max(part1, 0) + ImpactedNB / FFSpeedNB)
            else:
                # Normal speed calculation using "No Build" parameters from the formula
                flow_sum = sum(traffic_volumes[1:]) if HOVLanesNB != 0 else sum(traffic_volumes)

                # Access the "Build" parameters from the roadway_capacity_non_HOV dictionary
                capacity_params = roadway_capacity_non_HOV["Non-HOV Lanes"]["Build"]
                GenAlphaB = capacity_params["GenAlphaB"]
                GenBetaB = capacity_params["GenBetaB"]
                GenLaneCapB = capacity_params["GenLaneCapB"]

                # Apply the speed calculation formula
                volume_term = flow_sum / (GenLanesNB * GenLaneCapB * PeakLngthNB)
                delay_speed = FFSpeedB / (IRI20B * (1 + GenAlphaB * min(volume_term, MaxVC) ** GenBetaB))
                base_speed = delay_speed * TMSAdj[TMSLookup]["VolumeWithout"]

                if ProjType == "Passing":
                    nonhov_speed = (TruckSpeed + FFSpeedB) / 2
                else:
                    nonhov_speed = min(base_speed, FFSpeedB)

        # === Apply adjustments based on project type ===

        # Adjust for Freeway Connector using SpeedWeaveAdj
        if ProjType == "Freeway Connector":
            nonhov_speed *= SpeedWeaveAdj.get(PerWeaveB, {"Freeway": 1.0})["Freeway"]

        # Adjust for HOV Connector / Drop Ramp using SpeedWeaveAdj
        if ProjType in ["HOV Connector", "HOV Drop Ramp"]:
            nonhov_speed *= SpeedWeaveAdj.get(PerWeaveB, {"HOV": 1.0})["HOV"]

        # Apply pavement condition adjustments using SpeedPavAdj
        closest_iri_key = min(SpeedPavAdj.keys(), key=lambda x: abs(x - IRI20B))
        nonhov_speed *= SpeedPavAdj[closest_iri_key]["Auto"]

        # Update the widget with the final calculated speed value
        nonhov_speed_year20peak_build_modelcalc_widget.value = round(nonhov_speed, 1)

    # Trigger the calculation once or observe widget changes
    update_nonhov_year20peak_build_speed()  # To calculate initially


    # Link the update function to changes in relevant widgets
    PHV20B_widget.observe(update_nonhov_year20peak_build_speed, names='value')
    PNV20B_widget.observe(update_nonhov_year20peak_build_speed, names='value')
    PWV20B_widget.observe(update_nonhov_year20peak_build_speed, names='value')
    PTV20B_widget.observe(update_nonhov_year20peak_build_speed, names='value')
    projectinfo_widgets.subcategory_dropdown.observe(update_nonhov_year20peak_build_speed, names='value')  # ProjType
    projectinfo_widgets.peak_period_widget.observe(update_nonhov_year20peak_build_speed, names='value')     # PeakLngthNB
    projectinfo_widgets.departure_rate_forecast_year_build_widget.observe(update_nonhov_year20peak_build_speed, names='value')  # DepRate20
    projectinfo_widgets.departure_rate_forecast_year_no_build_widget.observe(update_nonhov_year20peak_build_speed, names='value')  # DepRate1
    projectinfo_widgets.arrival_rate_base_year_build_widget.observe(update_nonhov_year20peak_build_speed, names='value')  # ArrRate20
    projectinfo_widgets.arrival_rate_base_year_no_build_widget.observe(update_nonhov_year20peak_build_speed, names='value')  # ArrRate1
    projectinfo_widgets.adt_base_year_no_build_widget.observe(update_nonhov_year20peak_build_speed, names='value')  # ADT1NB
    projectinfo_widgets.free_flow_speed_no_build_widget.observe(update_nonhov_year20peak_build_speed, names='value')  # FFSpeedNB
    projectinfo_widgets.impacted_length_no_build_widget.observe(update_nonhov_year20peak_build_speed, names='value')  # ImpactedNB
    projectinfo_widgets.general_traffic_lanes_no_build_widget.observe(update_nonhov_year20peak_build_speed, names='value')  # GenLanesNB
    projectinfo_widgets.hov_hot_lanes_no_build_widget.observe(update_nonhov_year20peak_build_speed, names='value')  # HOVLanesNB
    projectinfo_widgets.percent_traffic_weave_no_build_widget.observe(update_nonhov_year20peak_build_speed, names='value')  # PerWeaveNB
    projectinfo_widgets.iri_forecast_year_no_build_widget.observe(update_nonhov_year20peak_build_speed, names='value')  # IRI20B


    def calculate_pns20b(change):
        # Access the user-modified value directly from the widget
        if isinstance(nonhov_speed_year20peak_build_userchanged_widget.value, (int, float)) and nonhov_speed_year20peak_build_userchanged_widget.value >= 0:
            updated_NonHOV_year20peak_speed = max(nonhov_speed_year20peak_build_userchanged_widget.value, 5)  # Ensure the speed is at least 5
        else:
            updated_NonHOV_year20peak_speed = max(nonhov_speed_year20peak_build_modelcalc_widget.value, 5)  # Use the model value if the user value is invalid

        # Update the value of PNS20B widget
        PNS20B_widget.value = updated_NonHOV_year20peak_speed


    nonhov_speed_year20peak_build_userchanged_widget.observe(calculate_pns20b, names='value')

    # Combine into layout
    NonHOV_Year20Peak_Build_Speed_widgets = widgets.HBox([nonhov_speed_year20peak_build_modelcalc_widget, nonhov_speed_year20peak_build_userchanged_widget, PNS20B_explanation_widget])
    
     ####################################################################################################### 
    # HOV Speed widgets for Year 20 Peak Build
    hov_speed_year20peak_build_modelcalc_widget = widgets.IntText(
        value=0,  # Set initial value to 0 or any other valid integer
        description="HOV Speed (Calculated by Model):",
        disabled=True,  # Make it read-only so the user cannot modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    hov_speed_year20peak_build_userchanged_widget = widgets.Text(
        value='',  # Initially set to 0 or a valid integer value
        description="HOV Speed (Changed by User):",
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # HOV Speed Volume (Used for Project Evaluation)
    PHS20B_widget = widgets.IntText(
        value=hov_speed_year20peak_build_modelcalc_widget.value,  # Set initially to the calculated value
        description="HOV Speed (Used for Proj Evaluation):",
        disabled=True,  # Make it read-only
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Explanation widget for user-modified values
    PHS20B_explanation_widget = widgets.Text(
        value=None,  # Allow users to enter a text explanation
        description="Reasons for Change:",  # Label for the input field
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,  # Optional layout style, if needed
        style={'description_width': 'initial'}  # Optional style for description width
    )

    def update_hov_year20peak_build_speed(change=None):
        print("subcategory_dropdown changed:", change) 
        # Extracting necessary values for the formula
        PHV20B = PHV20B_widget.value
        PNS20B = PNS20B_widget.value
        hov_capacity_params = roadway_capacity["HOV Lanes"]
        HOVAlpha = hov_capacity_params["HOVAlpha"]
        HOVBeta = hov_capacity_params["HOVBeta"]
        HOVLaneCap = hov_capacity_params["HOVLaneCap"]

        if PHV20B == 0:
            hov_speed = 55  # If PHV20B is zero, use 55 miles/h
        elif HOVLanesB == 0:
            hov_speed = PNS20B  # If no HOV lanes, use PNS20B
        else:
            # Perform the speed calculation based on the provided formula
            # Queuing Adjustment for the formula
            if ProjType == "Queuing":
                queuing_term = (DepRate1 - ADT1NB * (1 - PerPeakADT) / (24 - PeakLngthNB)) / (
                    (ADT1NB / ADT20NB) * DepRate20 - ADT1NB * (1 - PerPeakADT) / (24 - PeakLngthNB))
            else:
                queuing_term = 1  # No queuing effect

            volume_term = PHV20B / (HOVLanesB * HOVLaneCap * PeakLngthNB * queuing_term)
            delay_speed = FFSpeedB / (1 + HOVAlpha * min(volume_term, MaxVC) ** HOVBeta)

            # Apply Pavement adjustment if applicable
            if ProjType == "Pavement":
                pav_adj = SpeedPavAdj.get(IRI20B, {"Auto": 1.0})["Auto"]
                hov_speed = delay_speed * pav_adj
            else:
                hov_speed = delay_speed

        # Update the widget with the final calculated speed value
        hov_speed_year20peak_build_modelcalc_widget.value = round(hov_speed, 1)

    # Trigger the calculation once or observe widget changes
    update_hov_year20peak_build_speed()  # To calculate initially

    # Link the update function to changes in relevant widgets
    PHV20B_widget.observe(update_hov_year20peak_build_speed, names='value')
    projectinfo_widgets.subcategory_dropdown.observe(update_hov_year20peak_build_speed, names='value')  # ProjType
    projectinfo_widgets.peak_period_widget.observe(update_hov_year20peak_build_speed, names='value')     # PeakLngthNB
    projectinfo_widgets.departure_rate_forecast_year_build_widget.observe(update_hov_year20peak_build_speed, names='value')  # DepRate20
    projectinfo_widgets.departure_rate_forecast_year_no_build_widget.observe(update_hov_year20peak_build_speed, names='value')  # DepRate1
    projectinfo_widgets.adt_base_year_no_build_widget.observe(update_hov_year20peak_build_speed, names='value')  # ADT1NB
    projectinfo_widgets.iri_forecast_year_no_build_widget.observe(update_hov_year20peak_build_speed, names='value')  # IRI20B
    

    def calculate_phs20b(change):
        # Access the user-modified value directly from the widget
        if isinstance(hov_speed_year20peak_build_userchanged_widget.value, (int, float)) and hov_speed_year20peak_build_userchanged_widget.value >= 0:
            updated_HOV_year20peak_speed = max(hov_speed_year20peak_build_userchanged_widget.value, 5)  # Ensure the speed is at least 5
        else:
            updated_HOV_year20peak_speed = max(hov_speed_year20peak_build_modelcalc_widget.value, 5)  # Use the model value if the user value is invalid

        # Update the value of PHS20B widget
        PHS20B_widget.value = updated_HOV_year20peak_speed

    hov_speed_year20peak_build_userchanged_widget.observe(calculate_phs20b, names='value')

    # Combine into layout
    HOV_Year20Peak_Build_Speed_widgets = widgets.HBox([hov_speed_year20peak_build_modelcalc_widget, hov_speed_year20peak_build_userchanged_widget, PHS20B_explanation_widget])
      

     ####################################################################################################### 
    
    # Widgets for Build Speed Calculation
    weave_speed_year20peak_build_modelcalc_widget = widgets.IntText(
        value=0,  # Set initial value to 0 or any other valid integer
        description="Weaving Speed (Calculated by Model):",
        disabled=True,  # Make it read-only
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    weave_speed_year20peak_build_userchanged_widget = widgets.Text(
        value='',  # Initially set to 0 or a valid integer value
        description="Weaving Speed (Changed by User):",
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Non-HOV Speed Volume (Used for Project Evaluation) for Build
    PWS20B_widget = widgets.IntText(
        value=weave_speed_year20peak_build_modelcalc_widget.value,  # Set initially to the calculated value
        description="Weaving Speed (Used for Proj Evaluation):",
        disabled=True,  # Make it read-only
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Explanation widget for user-modified values
    PWS20B_explanation_widget = widgets.Text(
        value=None,  # Allow users to enter a text explanation
        description="Reasons for Change:",
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,  # Optional layout style, if needed
        style={'description_width': 'initial'}  # Optional style for description width
    )

    def update_year20peak_build_weave_speed(change=None):
        try:
            # Retrieve widget/input values
            PWV20B = PWV20B_widget.value  # PWV20B
            PTV20B = PTV20B_widget.value  # PTV20B
            PNS20B = PNS20B_widget.value  # PNS20B

            if PWV20B == 0:
                Year20PeakBuildWeaveSpeed = 55

            elif ProjType == "Auxiliary Lane":
                # Compute exponential part
                exponent_part = math.exp((PWV20B + PTV20B) / NumDirections / PeakLngthNB / 1000)  # NumDirections, PeakLngthNB

                # Ramp factor (1083 for off-ramp, else SegmentB * 5280)
                ramp_factor = 1083 if ProjType == "Off-Ramp Widening" else SegmentB * 5280  # SegmentB, RampFFSpdB

                # Unadjusted speed formula
                base_speed = FFSpeedB - (FFSpeedB - 42) * (
                    0.321 + 0.0039 * exponent_part - 0.002 * ramp_factor * RampFFSpdB / 1000)  # FFSpeedB, RampFFSpdB

                adjusted_speed = 1.1 * base_speed

                # Get TMS adjustment
                tms_adj = TMSAdj.get(TMSLookup, {}).get("SpeedWith", 1.0)  # TMSLookup

                # Pavement adjustment (Auto type)
                if ProjType == "Pavement":
                    closest_iri_key = min(SpeedPavAdj.keys(), key=lambda x: abs(x - IRI20B))  # IRI20B
                    pavement_adj = SpeedPavAdj[closest_iri_key]["Auto"]
                else:
                    pavement_adj = 1

                # Final adjusted speed
                final_speed = max(5, min(PNS20B, adjusted_speed * tms_adj * pavement_adj))  # PNS20B
                Year20PeakBuildWeaveSpeed = final_speed

            else:
                Year20PeakBuildWeaveSpeed = PNS20B

            weave_speed_year20peak_build_modelcalc_widget.value = round(Year20PeakBuildWeaveSpeed, 2)

        except Exception:
            weave_speed_year20peak_build_modelcalc_widget.value = 0

    # Initial call to set the value based on the current widget state
    update_year20peak_build_weave_speed()

    # Add observers to trigger the function when relevant widget values change
    PWV20B_widget.observe(update_year20peak_build_weave_speed, names='value')  # PWV20B
    PNS20B_widget.observe(update_year20peak_build_weave_speed, names='value')  # PNS20B
    PTV20B_widget.observe(update_year20peak_build_weave_speed, names='value')  # PTV20B
    projectinfo_widgets.subcategory_dropdown.observe(update_year20peak_build_weave_speed, names='value')  # ProjType
    projectinfo_widgets.free_flow_speed_no_build_widget.observe(update_year20peak_build_weave_speed, names='value')  # FFSpeedB
    projectinfo_widgets.ramp_design_speed_no_build_widget.observe(update_year20peak_build_weave_speed, names='value')  # RampFFSpdB
    projectinfo_widgets.hov_hot_lanes_no_build_widget.observe(update_year20peak_build_weave_speed, names='value')  # HOV lane info
    projectinfo_widgets.highway_segment_no_build_widget.observe(update_year20peak_build_weave_speed, names='value')  # SegmentB
    projectinfo_widgets.iri_forecast_year_no_build_widget.observe(update_year20peak_build_weave_speed, names='value')  # IRI20B

    def calculate_pws20b(change):
        # Access the user-modified value directly from the widget
        if isinstance(weave_speed_year20peak_build_userchanged_widget.value, (int, float)) and weave_speed_year20peak_build_userchanged_widget.value >= 0:
            updated_Weave_year20peak_speed = max(weave_speed_year20peak_build_userchanged_widget.value, 5)  # Ensure the speed is at least 5
        else:
            updated_Weave_year20peak_speed = max(weave_speed_year20peak_build_modelcalc_widget.value, 5)  # Use the model value if the user value is invalid

        # Update the value of PWS20B widget (project evaluation widget)
        PWS20B_widget.value = updated_Weave_year20peak_speed

    # Link the function to the user input widget change
    weave_speed_year20peak_build_userchanged_widget.observe(calculate_pws20b, names='value')  # User-modified speed input

    # Combine into layout for display
    Weave_Year20Peak_Build_Speed_widgets = widgets.HBox([weave_speed_year20peak_build_modelcalc_widget, weave_speed_year20peak_build_userchanged_widget, PWS20B_explanation_widget])

     #######################################################################################################  
    
    # Widgets for Build Truck Speed Calculation
    truck_speed_year20peak_build_modelcalc_widget = widgets.IntText(
        value=0,  # Set initial value to 0 or any other valid integer
        description="Truck Speed (Calculated by Model):",
        disabled=True,  # Make it read-only
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    truck_speed_year20peak_build_userchanged_widget = widgets.Text(
        value='',  # Initially set to 0 or a valid integer value
        description="Truck Speed (Changed by User):",
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Non-HOV Speed Volume (Used for Project Evaluation) for Build
    PTS20B_widget = widgets.IntText(
        value=truck_speed_year20peak_build_modelcalc_widget.value,  # Set initially to the calculated value
        description="Truck Speed (Used for Proj Evaluation):",
        disabled=True,  # Make it read-only
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Explanation widget for user-modified values
    PTS20B_explanation_widget = widgets.Text(
        value=None,  # Allow users to enter a text explanation
        description="Reasons for Change:",
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,  # Optional layout style, if needed
        style={'description_width': 'initial'}  # Optional style for description width
    )

    # Function to update truck speed calculation based on relevant parameters

    def update_year20peak_build_truck_speed(change=None):
        try:
            # Retrieve relevant widget values
            PTV20B = PTV20B_widget.value  # PTV20B
            PNS20B = PNS20B_widget.value  # PNS20B
            PWS20B = PWS20B_widget.value  # PWS20B

            if PTV20B == 0:
                truck_speed_year20peak_build_modelcalc_widget.value = 55
                return

            # Lookup adjustment values from SpeedPavAdj
            closest_iri_key = min(SpeedPavAdj.keys(), key=lambda x: abs(x - IRI20B))  # SpeedPavAdj, IRI20B
            auto_adj = SpeedPavAdj[closest_iri_key]["Auto"]  # SpeedPavAdj
            truck_adj = SpeedPavAdj[closest_iri_key]["Truck"]  # SpeedPavAdj

            # Calculate truck speed using formula
            base_speed = PWS20B if ProjType == "Auxiliary Lane" else PNS20B
            adjusted_speed = min(TruckSpeed, base_speed / (auto_adj if ProjType == "Pavement" else 1))
            final_speed = adjusted_speed * (truck_adj if ProjType == "Pavement" else 1)

            truck_speed_year20peak_build_modelcalc_widget.value = round(final_speed, 2)

        except:
            truck_speed_year20peak_build_modelcalc_widget.value = 0
            
    update_year20peak_build_truck_speed()

    # Add observers to trigger the function when relevant widget values change
    PTV20B_widget.observe(update_year20peak_build_truck_speed, names='value')  # PTV20B
    PNS20B_widget.observe(update_year20peak_build_truck_speed, names='value')  # PNS20B
    PWS20B_widget.observe(update_year20peak_build_truck_speed, names='value')  # PWS20B
    projectinfo_widgets.truck_speed_widget.observe(update_year20peak_build_truck_speed, names='value')  # TruckSpeed
    projectinfo_widgets.subcategory_dropdown.observe(update_year20peak_build_truck_speed, names='value')  # ProjType
    projectinfo_widgets.free_flow_speed_no_build_widget.observe(update_year20peak_build_truck_speed, names='value')  # FFSpeedB
    projectinfo_widgets.ramp_design_speed_no_build_widget.observe(update_year20peak_build_truck_speed, names='value')  # RampFFSpdB
    projectinfo_widgets.hov_hot_lanes_no_build_widget.observe(update_year20peak_build_truck_speed, names='value')  # HOV lane info
    projectinfo_widgets.highway_segment_no_build_widget.observe(update_year20peak_build_truck_speed, names='value')  # SegmentB
    projectinfo_widgets.iri_forecast_year_no_build_widget.observe(update_year20peak_build_truck_speed, names='value')  # IRI20B

    # Function to calculate the updated project evaluation speed (PTS20B)
    def calculate_pts20b(change):
        # Access the user-modified value directly from the widget
        if isinstance(truck_speed_year20peak_build_userchanged_widget.value, (int, float)) and truck_speed_year20peak_build_userchanged_widget.value >= 0:
            updated_Truck_year20peak_speed = max(truck_speed_year20peak_build_userchanged_widget.value, 5)  # Ensure the speed is at least 5
        else:
            updated_Truck_year20peak_speed = max(truck_speed_year20peak_build_modelcalc_widget.value, 5)  # Use the model value if the user value is invalid

        # Update the value of PTS20B widget (project evaluation widget)
        PTS20B_widget.value = updated_Truck_year20peak_speed

    # Link the function to the user input widget change
    truck_speed_year20peak_build_userchanged_widget.observe(calculate_pts20b, names='value')  # User-modified speed input

    # Combine into layout for display
    Truck_Year20Peak_Build_Speed_widgets = widgets.HBox([truck_speed_year20peak_build_modelcalc_widget, truck_speed_year20peak_build_userchanged_widget, PTS20B_explanation_widget])

    
###################################################################################################################################################################
        
    # Create the Non-HOV Volume widget to display the calculated value
    nonHOV_Vol_year20nonpeak_build_modelcalc_widget = widgets.FloatText(
        value=0,
        description="Non-HOV Volume (Calculated by Model):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Create the Non-HOV Volume widget for user-modified value
    nonHOV_Vol_year20nonpeak_build_userchanged_widget = widgets.Text(
        value='',
        description="Non-HOV Volume (Changed by User):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Final value used for project evaluation
    NNV20B_widget = widgets.FloatText(
        value=nonHOV_Vol_year20nonpeak_build_modelcalc_widget.value,
        description="Non-HOV Volume (Used for Proj Evaluation):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Explanation field for manual user entry
    NNV20B_explanation_widget = widgets.Text(
        value=None,
        description="Reasons for Change:",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )
    
    
    def update_NonHOV_year20nonpeak_Volume(change=None):
        try:
            # Hwy-Rail case
            if ProjType == "Hwy-Rail Grade Crossing":
                NonHOV_year20nonpeak_Volume = (
                    (ArrRate20 * GateTime20 / 60) /
                    (1 - ArrRate20 / DepRate20) *
                    NumTrain20 / AnnualFactor *
                    (1 - PerTruckNB) *
                    ADT20B / ADT20NB
                )

            # Queuing case
            elif ProjType == "Queuing":
                numerator = ADT20B * (
                    1 - DepRate20 * PeakLngthNB *
                    (DepRate1 - ADT1NB * (1 - PerPeakADT) / (24 - PeakLngthNB))
                )
                denominator = (
                    (ADT1NB / ADT20NB * DepRate20 - ADT1NB * (1 - PerPeakADT) / (24 - PeakLngthNB)) / ADT20NB
                )
                NonHOV_year20nonpeak_Volume = numerator / denominator if denominator != 0 else 0

            # General case
            else:
                # Base volume
                base_volume = (1 - PerPeakADT) * ADT20B

                # Determine percentage to subtract
                subtract_pct = PerWeaveB if ProjType in ["Auxiliary Lane", "Off-Ramp Widening"] else PerTruckB

                # Transit deduction
                if ProjType in ["Passenger Rail", "Light-Rail", "Bus"]:
                    transit_deduction = (
                        (1 - TPerPeak) * TPerHwy *
                        (TAPT20B - TAPT20NB) /
                        AnnualFactor / AVONonNB
                    )
                else:
                    transit_deduction = 0

                # Final non-HOV volume
                NonHOV_year20nonpeak_Volume = base_volume * (1 - subtract_pct) - transit_deduction

            # Assign the result to the widget
            nonHOV_Vol_year20nonpeak_build_modelcalc_widget.value = round(NonHOV_year20nonpeak_Volume, 2)

        except Exception:
            nonHOV_Vol_year20nonpeak_build_modelcalc_widget.value = 0
            
            
    # Observer setup for NNV20B calculation based on relevant project widgets
    projectinfo_widgets.subcategory_dropdown.observe(update_NonHOV_year20nonpeak_Volume, names='value')  # ProjType
    projectinfo_widgets.arrival_rate_base_year_build_widget.observe(update_NonHOV_year20nonpeak_Volume, names='value')  # ArrRate20
    projectinfo_widgets.GateTime20_widget.observe(update_NonHOV_year20nonpeak_Volume, names='value')  # GateTime20
    projectinfo_widgets.departure_rate_forecast_year_build_widget.observe(update_NonHOV_year20nonpeak_Volume, names='value')  # DepRate20
    projectinfo_widgets.NumTrain20_widget.observe(update_NonHOV_year20nonpeak_Volume, names='value')  # NumTrain20
    projectinfo_widgets.percent_trucks_nobuild_widget.observe(update_NonHOV_year20nonpeak_Volume, names='value')  # PerTruckNB
    projectinfo_widgets.ADT_20NB_widget.observe(update_NonHOV_year20nonpeak_Volume, names='value')  # ADT20NB
    projectinfo_widgets.adt_20_year_build_widget.observe(update_NonHOV_year20nonpeak_Volume, names='value')  # ADT20B
    projectinfo_widgets.peak_period_widget.observe(update_NonHOV_year20nonpeak_Volume, names='value')  # PeakLngthNB
    projectinfo_widgets.departure_rate_forecast_year_no_build_widget.observe(update_NonHOV_year20nonpeak_Volume, names='value')  # DepRate1
    projectinfo_widgets.adt_base_year_no_build_widget.observe(update_NonHOV_year20nonpeak_Volume, names='value')  # ADT1NB
    projectinfo_widgets.percent_traffic_weave_build_widget.observe(update_NonHOV_year20nonpeak_Volume, names='value')  # PerWeaveB
    projectinfo_widgets.percent_trucks_build_widget.observe(update_NonHOV_year20nonpeak_Volume, names='value')  # PerTruckB
    projectinfo_widgets.TAPT20B_widget.observe(update_NonHOV_year20nonpeak_Volume, names='value')  # TAPT20B
    projectinfo_widgets.TAPT20NB_widget.observe(update_NonHOV_year20nonpeak_Volume, names='value')  # TAPT20NB
    projectinfo_widgets.TPerPeak_widget.observe(update_NonHOV_year20nonpeak_Volume, names='value')  # TPerPeak
    projectinfo_widgets.TPerHwy_widget.observe(update_NonHOV_year20nonpeak_Volume, names='value')  # TPerHwy
    projectinfo_widgets.AVO_traffic_NP_no_build_widget.observe(update_NonHOV_year20nonpeak_Volume, names='value')  # AVONonNB

   

    # Function to calculate the updated project evaluation volume (NNV20B)
    def calculate_nnv20b(change):
        # Access the user-modified value directly from the widget
        if isinstance(nonHOV_Vol_year20nonpeak_build_userchanged_widget.value, (int, float)) and nonHOV_Vol_year20nonpeak_build_userchanged_widget.value >= 0:
            updated_nonHOV_volume = max(nonHOV_Vol_year20nonpeak_build_userchanged_widget.value, 0)
        else:
            updated_nonHOV_volume = max(nonHOV_Vol_year20nonpeak_build_modelcalc_widget.value, 0)

        # Update the value of NNV20B widget (project evaluation widget)
        NNV20B_widget.value = round(updated_nonHOV_volume, 2)

    # Link the function to the user input widget change
    nonHOV_Vol_year20nonpeak_build_userchanged_widget.observe(calculate_nnv20b, names='value')

    # Combine into layout for display
    NonHOV_Year20NonPeak_Build_Volume_widgets = widgets.HBox([
        nonHOV_Vol_year20nonpeak_build_modelcalc_widget,
        nonHOV_Vol_year20nonpeak_build_userchanged_widget,
        NNV20B_explanation_widget
    ])
    
     #######################################################################################################  
    # Create the Weaving Volume (Non-Peak Year 20) widget to display the calculated value
    weaving_Vol_year20nonpeak_build_modelcalc_widget = widgets.FloatText(
        value=0,
        description="Weaving Volume (Calculated by Model):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Create the Weaving Volume widget for user-modified value (Non-Peak Year 20)
    weaving_Vol_year20nonpeak_build_userchanged_widget = widgets.Text(
        value='',
        description="Weaving Volume (Changed by User):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Final value used for project evaluation (Non-Peak Year 20)
    NWV20B_widget = widgets.FloatText(
        value=weaving_Vol_year20nonpeak_build_modelcalc_widget.value,
        description="Weaving Volume (Used for Proj Evaluation):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    NWV20B_explanation_widget = widgets.Text(
        value=None,
        description="Reasons for Change:",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Function to update Weaving Volume dynamically for Non-Peak Year 20
    def update_weaving_Year20NonPeak_Build_Volume(change):
        try:
            weaving_volume = 0

            # Calculate the volume based on the formula
            if ProjType in ["Auxiliary Lane", "Off-Ramp Widening"]:
                weaving_volume += ((1 - PerPeakADT) * ADT20B) * (PerWeaveB - PerTruckB)

            if ProjType == "Auxiliary Lane":
                weaving_volume += RampVolNP * (24 - PeakLngthNB)

            weaving_Vol_year20nonpeak_build_modelcalc_widget.value = round(weaving_volume, 2)

        except Exception:
            weaving_Vol_year20nonpeak_build_modelcalc_widget.value = 0

    # Observer setup for Weaving Volume (Non-Peak Year 20)
    projectinfo_widgets.subcategory_dropdown.observe(update_weaving_Year20NonPeak_Build_Volume, names='value')  # ProjType
    projectinfo_widgets.adt_20_year_build_widget.observe(update_weaving_Year20NonPeak_Build_Volume, names='value')  # ADT20B
    projectinfo_widgets.percent_traffic_weave_build_widget.observe(update_weaving_Year20NonPeak_Build_Volume, names='value')  # PerWeaveB
    projectinfo_widgets.percent_trucks_build_widget.observe(update_weaving_Year20NonPeak_Build_Volume, names='value')  # PerTruckB
    projectinfo_widgets.hourly_ramp_volume_nonpeak_widget.observe(update_weaving_Year20NonPeak_Build_Volume, names='value')  # RampVolNP
    projectinfo_widgets.peak_period_widget.observe(update_weaving_Year20NonPeak_Build_Volume, names='value')  # PeakLngthNB


    # Final value widget logic for NWV20B
    def calculate_nwv20b(change):
        try:
            val = weaving_Vol_year20nonpeak_build_userchanged_widget.value
            if isinstance(val, (int, float)) or (isinstance(val, str) and val.replace('.', '', 1).isdigit()):
                NWV20B = max(float(val), 0)
            else:
                NWV20B = max(weaving_Vol_year20nonpeak_build_modelcalc_widget.value, 0)

            NWV20B_widget.value = round(NWV20B, 2)
        except Exception:
            NWV20B_widget.value = max(weaving_Vol_year20nonpeak_build_modelcalc_widget.value, 0)

    weaving_Vol_year20nonpeak_build_userchanged_widget.observe(calculate_nwv20b, names='value')

    # Combine into layout for display (Non-Peak Year 20)
    Weaving_vol_year20nonpeak_build_widgets = widgets.HBox([
        weaving_Vol_year20nonpeak_build_modelcalc_widget,
        weaving_Vol_year20nonpeak_build_userchanged_widget,
        NWV20B_explanation_widget
    ])

     #######################################################################################################  
    
    # Create the Truck Volume for Non-Peak widget to display the calculated value
    truck_Vol_year20nonpeak_build_modelcalc_widget = widgets.FloatText(
        value=0,
        description="Truck Volume (Calculated by Model - Non-Peak):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Create the Truck Volume widget for user-modified value
    truck_Vol_year20nonpeak_build_userchanged_widget = widgets.Text(
        value='',
        description="Truck Volume (Changed by User - Non-Peak):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Final value used for project evaluation
    NTV20B_widget = widgets.FloatText(
        value=truck_Vol_year20nonpeak_build_modelcalc_widget.value,
        description="Truck Volume (Used for Proj Evaluation - Non-Peak):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    NTV20B_explanation_widget = widgets.Text(
        value=None,
        description="Reasons for Change - Non-Peak:",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Function to update Truck Volume for Non-Peak dynamically
    def update_truck_Year20NonPeak_Build_Volume(change):
        try:
            if ProjType == "Hwy-Rail Grade Crossing":
   
                truck_volume = (ArrRate20 * GateTime20 / 60) / (1 - ArrRate20 / DepRate20) * NumTrain20 / AnnualFactor * PerTruckNB * ADT20B / ADT20NB
            elif ProjType == "Queuing":

                numerator = ADT20B * (1 - DepRate20 * PeakLngthNB * (DepRate1 - ADT1NB * (1 - PerPeakADT)) / (24 - PeakLngthNB))
                denominator = (ADT1NB / ADT20NB * DepRate20 - ADT1NB * (1 - PerPeakADT) / (24 - PeakLngthNB)) / ADT20NB
                truck_volume = numerator / denominator if denominator != 0 else 0
            else:
                # Apply default formula for other project types
                truck_volume = (1 - PerPeakADT) * ADT20B * PerTruckB

            # Update the truck volume model calculation widget with the calculated value
            truck_Vol_year20nonpeak_build_modelcalc_widget.value = round(truck_volume, 2)

        except Exception:
            # In case of any error, set the value to 0
            truck_Vol_year20nonpeak_build_modelcalc_widget.value = 0

    # Observer setup for non-peak truck volume
    projectinfo_widgets.subcategory_dropdown.observe(update_truck_Year20NonPeak_Build_Volume, names='value')  # ProjType
    projectinfo_widgets.adt_20_year_build_widget.observe(update_truck_Year20NonPeak_Build_Volume, names='value')  # ADT20B
    projectinfo_widgets.departure_rate_forecast_year_build_widget.observe(update_truck_Year20NonPeak_Build_Volume, names='value')  # DepRate20
    projectinfo_widgets.peak_period_widget.observe(update_truck_Year20NonPeak_Build_Volume, names='value')  # PeakLngthNB
    projectinfo_widgets.departure_rate_forecast_year_no_build_widget.observe(update_truck_Year20NonPeak_Build_Volume, names='value')  # DepRate1
    projectinfo_widgets.adt_base_year_no_build_widget.observe(update_truck_Year20NonPeak_Build_Volume, names='value')  # ADT1NB
    projectinfo_widgets.ADT_20NB_widget.observe(update_truck_Year20NonPeak_Build_Volume, names='value')  # ADT20NB
    projectinfo_widgets.percent_trucks_build_widget.observe(update_truck_Year20NonPeak_Build_Volume, names='value')  # PerTruckB


    # Final value widget logic for Non-Peak Truck Volume
    def calculate_ntv20b(change):
        try:
            # Access the user-modified value directly from the widget
            val = truck_Vol_year20nonpeak_build_userchanged_widget.value
            if isinstance(val, (int, float)) or (isinstance(val, str) and val.replace('.', '', 1).isdigit()):
                NTV20B = max(float(val), 0)
            else:
                NTV20B = max(truck_Vol_year20nonpeak_build_modelcalc_widget.value, 0)

            # Update the NTV20B widget with the final calculated value
            NTV20B_widget.value = round(NTV20B, 2)
        except Exception:
            NTV20B_widget.value = max(truck_Vol_year20nonpeak_build_modelcalc_widget.value, 0)

    # Link the function to the user-modified truck volume input widget
    truck_Vol_year20nonpeak_build_userchanged_widget.observe(calculate_ntv20b, names='value')

    # Combine into layout for display
    Truck_vol_year20nonpeak_build_widgets = widgets.HBox([
        truck_Vol_year20nonpeak_build_modelcalc_widget,
        truck_Vol_year20nonpeak_build_userchanged_widget,
        NTV20B_explanation_widget
    ])


     #######################################################################################################  
    # Non-HOV Speed widgets for Year 20 Non-Peak Build
    nonhov_speed_year20nonpeak_build_modelcalc_widget = widgets.IntText(
        value=0,  # Set initial value to 0 or any other valid integer
        description="Non-HOV Speed (Calculated by Model):",
        disabled=True,  # Make it read-only so the user cannot modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    nonhov_speed_year20nonpeak_build_userchanged_widget = widgets.Text(
        value='',  # Initially set to 0 or a valid integer value
        description="Non-HOV Speed (Changed by User):",
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Non-HOV Speed Volume (Used for Project Evaluation)
    NNS20B_widget = widgets.IntText(
        value=nonhov_speed_year20nonpeak_build_modelcalc_widget.value,  # Set initially to the calculated value
        description="Non-HOV Speed (Used for Proj Evaluation):",
        disabled=True,  # Make it read-only
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Explanation widget for user-modified values
    NNS20B_explanation_widget = widgets.Text(
        value=None,  # Allow users to enter a text explanation
        description="Reasons for Change:",  # Label for the input field
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,  # Optional layout style, if needed
        style={'description_width': 'initial'}  # Optional style for description width
    )

    def update_nonhov_year20nonpeak_build_speed(change=None):
        # Accessing the relevant traffic volume widgets (NNV20B, NWV20B, NTV20B)
        traffic_volumes = [
            NNV20B_widget.value,  
            NWV20B_widget.value,  
            NTV20B_widget.value   
        ]
        
        GenAlphaB = roadway_capacity_non_HOV["Non-HOV Lanes"]["Build"]["GenAlphaB"]
        GenBetaB = roadway_capacity_non_HOV["Non-HOV Lanes"]["Build"]["GenBetaB"]
        GenLaneCapB = roadway_capacity_non_HOV["Non-HOV Lanes"]["Build"]["GenLaneCapB"]

        sum_all = sum(traffic_volumes)

        # Step 1: Formula for Non-HOV Speed calculation
        if ProjType == "Hwy-Rail Grade Crossing":
            nonhov_speed = FFSpeedB  # If it's a Hwy-Rail grade crossing, no calculation needed
        else:
            if sum_all == 0:
                nonhov_speed = 55  # If total volume is zero, use default value
            else:
                volume_term = sum_all / ((GenLanesB + HOVLanesB) * GenLaneCapB * (24 - PeakLngthNB))

                # Check if the queuing adjustment needs to be applied
                if ProjType == "Queuing":
                    try:
                        queuing_factor = (
                            (DepRate1 - ADT1NB * (1 - PerPeakADT) / (24 - PeakLngthNB)) /
                            ((ADT1NB / ADT20NB * DepRate20) - ADT1NB * (1 - PerPeakADT) / (24 - PeakLngthNB))
                        )
                    except ZeroDivisionError:
                        queuing_factor = float("inf")  # Handle division by zero error
                else:
                    queuing_factor = 1

                # Calculate the delay speed component
                delay_speed = FFSpeedB / (1 + GenAlphaB * min(volume_term * queuing_factor, MaxVC) ** GenBetaB)

                nonhov_speed = delay_speed

                # Apply adjustments based on project type
                if ProjType == "Freeway Connector":
                    nonhov_speed *= SpeedWeaveAdj.get(PerWeaveB, {"Freeway": 1.0})["Freeway"]

                if ProjType == "HOV Connector" or ProjType == "HOV Drop Ramp":
                    nonhov_speed *= SpeedWeaveAdj.get(PerWeaveB, {"HOV": 1.0})["HOV"]

                # Apply pavement condition adjustments using SpeedPavAdj
                if ProjType == "Pavement":  # Checking if pavement condition adjustment needs to be applied
                    closest_iri_key = min(SpeedPavAdj.keys(), key=lambda x: abs(x - IRI20B))
                    nonhov_speed *= SpeedPavAdj[closest_iri_key]["Auto"]

        # Update the widget with the final calculated speed value
        nonhov_speed_year20nonpeak_build_modelcalc_widget.value = round(nonhov_speed, 1)

    # Trigger the calculation once or observe widget changes
    update_nonhov_year20nonpeak_build_speed()  # To calculate initially

    # Link the update function to changes in relevant widgets
    NNV20B_widget.observe(update_nonhov_year20nonpeak_build_speed, names='value')
    NWV20B_widget.observe(update_nonhov_year20nonpeak_build_speed, names='value')
    NTV20B_widget.observe(update_nonhov_year20nonpeak_build_speed, names='value')
    projectinfo_widgets.subcategory_dropdown.observe(update_nonhov_year20nonpeak_build_speed, names='value')  # ProjType
    projectinfo_widgets.peak_period_widget.observe(update_nonhov_year20nonpeak_build_speed, names='value')     # PeakLngthNB
    projectinfo_widgets.departure_rate_forecast_year_build_widget.observe(update_nonhov_year20nonpeak_build_speed, names='value')  # DepRate20
    projectinfo_widgets.departure_rate_forecast_year_no_build_widget.observe(update_nonhov_year20nonpeak_build_speed, names='value')  # DepRate1
    projectinfo_widgets.arrival_rate_base_year_build_widget.observe(update_nonhov_year20nonpeak_build_speed, names='value')  # ArrRate20
    projectinfo_widgets.arrival_rate_base_year_no_build_widget.observe(update_nonhov_year20nonpeak_build_speed, names='value')  # ArrRate1
    projectinfo_widgets.adt_base_year_no_build_widget.observe(update_nonhov_year20nonpeak_build_speed, names='value')  # ADT1NB
    projectinfo_widgets.free_flow_speed_no_build_widget.observe(update_nonhov_year20nonpeak_build_speed, names='value')  # FFSpeedNB
    projectinfo_widgets.impacted_length_no_build_widget.observe(update_nonhov_year20nonpeak_build_speed, names='value')  # ImpactedNB
    projectinfo_widgets.general_traffic_lanes_no_build_widget.observe(update_nonhov_year20nonpeak_build_speed, names='value')  # GenLanesNB
    projectinfo_widgets.hov_hot_lanes_no_build_widget.observe(update_nonhov_year20nonpeak_build_speed, names='value')  # HOVLanesNB
    projectinfo_widgets.percent_traffic_weave_no_build_widget.observe(update_nonhov_year20nonpeak_build_speed, names='value')  # PerWeaveNB
    projectinfo_widgets.iri_forecast_year_no_build_widget.observe(update_nonhov_year20nonpeak_build_speed, names='value')  # IRI20B


    def calculate_nns20b(change):
        # Access the user-modified value directly from the widget
        if isinstance(nonhov_speed_year20nonpeak_build_userchanged_widget.value, (int, float)) and nonhov_speed_year20nonpeak_build_userchanged_widget.value >= 0:
            updated_NonHOV_year20nonpeak_speed = max(nonhov_speed_year20nonpeak_build_userchanged_widget.value, 5)  # Ensure the speed is at least 5
        else:
            updated_NonHOV_year20nonpeak_speed = max(nonhov_speed_year20nonpeak_build_modelcalc_widget.value, 5)  # Use the model value if the user value is invalid

        # Update the value of NNS20B widget
        NNS20B_widget.value = updated_NonHOV_year20nonpeak_speed

    # Link user-modified value to NNS20B calculation
    nonhov_speed_year20nonpeak_build_userchanged_widget.observe(calculate_nns20b, names='value')

    # Combine into layout
    NonHOV_Year20NonPeak_Build_Speed_widgets = widgets.HBox([nonhov_speed_year20nonpeak_build_modelcalc_widget, nonhov_speed_year20nonpeak_build_userchanged_widget, NNS20B_explanation_widget])

    
     #######################################################################################################     
    # Widgets for Non-Peak Weaving Speed Calculation (Non-Peak Build)
    weave_speed_year20nonpeak_build_modelcalc_widget = widgets.IntText(
        value=0,  # Set initial value to 0 or any other valid integer
        description="Weaving Speed (Calculated by Model):",
        disabled=True,  # Make it read-only
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    weave_speed_year20nonpeak_build_userchanged_widget = widgets.Text(
        value='',  # Initially set to 0 or a valid integer value
        description="Weaving Speed (Changed by User):",
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Non-HOV Speed Volume (Used for Project Evaluation) for Non-Peak Build
    NWS20B_widget = widgets.IntText(
        value=weave_speed_year20nonpeak_build_modelcalc_widget.value,  # Set initially to the calculated value
        description="Weaving Speed (Used for Proj Evaluation):",
        disabled=True,  # Make it read-only
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Explanation widget for user-modified values
    NWS20B_explanation_widget = widgets.Text(
        value=None,  # Allow users to enter a text explanation
        description="Reasons for Change:",
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,  # Optional layout style, if needed
        style={'description_width': 'initial'}  # Optional style for description width
    )

    def update_year20nonpeak_build_weave_speed(change=None):
        try:
            # Retrieve widget/input values
            NWV20B = NWV20B_widget.value  # NWV20B
            NTV20B = NTV20B_widget.value  # NTV20B
            NNS20B = NNS20B_widget.value  # NNS20B

            if NWV20B == 0:
                # If NWV20B is zero, use the default value of 55
                Year20NonPeakBuildWeaveSpeed = 55
            elif ProjType == "Auxiliary Lane":
                # Auxiliary Lane formula
                exponent_part = math.exp((NWV20B + NTV20B) / NumDirections / (24 - PeakLngthNB) / 1000)
                ramp_factor = 1083 if ProjType == "Off-Ramp Widening" else SegmentB * 5280  # Ramp adjustment

                # Unadjusted speed formula
                base_speed = FFSpeedB - (FFSpeedB - 42) * (
                    0.321 + 0.0039 * exponent_part - 0.002 * ramp_factor * RampFFSpdB / 1000
                )

                # Apply 10% adjustment factor
                adjusted_speed = 1.1 * base_speed

                # Apply pavement condition adjustment (if applicable)
                if ProjType == "Pavement":
                    closest_iri_key = min(SpeedPavAdj.keys(), key=lambda x: abs(x - IRI20B))
                    pavement_adj = SpeedPavAdj[closest_iri_key]["Auto"]
                else:
                    pavement_adj = 1

                # Final adjusted speed
                final_speed = max(5, min(NNS20B, adjusted_speed * pavement_adj))  # Ensure the speed is at least 5
                Year20NonPeakBuildWeaveSpeed = final_speed
            else:
                # Use NNS20B if no auxiliary lane adjustments are applied
                Year20NonPeakBuildWeaveSpeed = NNS20B

            # Update the calculated value widget
            weave_speed_year20nonpeak_build_modelcalc_widget.value = round(Year20NonPeakBuildWeaveSpeed, 2)

        except Exception:
            # In case of any error, reset the value to 0
            weave_speed_year20nonpeak_build_modelcalc_widget.value = 0

    # Initial call to set the value based on the current widget state
    update_year20nonpeak_build_weave_speed()

    # Add observers to trigger the function when relevant widget values change
    NWV20B_widget.observe(update_year20nonpeak_build_weave_speed, names='value')  # NWV20B
    NTV20B_widget.observe(update_year20nonpeak_build_weave_speed, names='value')  # NTV20B
    NNS20B_widget.observe(update_year20nonpeak_build_weave_speed, names='value')  # NNS20B
    projectinfo_widgets.subcategory_dropdown.observe(update_year20nonpeak_build_weave_speed, names='value')  # ProjType
    projectinfo_widgets.free_flow_speed_no_build_widget.observe(update_year20nonpeak_build_weave_speed, names='value')  # FFSpeedB
    projectinfo_widgets.ramp_design_speed_no_build_widget.observe(update_year20nonpeak_build_weave_speed, names='value')  # RampFFSpdB
    projectinfo_widgets.highway_segment_no_build_widget.observe(update_year20nonpeak_build_weave_speed, names='value')  # SegmentB
    projectinfo_widgets.iri_forecast_year_no_build_widget.observe(update_year20nonpeak_build_weave_speed, names='value')  # IRI20B

    # Function to handle user-modified value for NWS20B
    def calculate_nws20b(change):
        # Access the user-modified value directly from the widget
        if isinstance(weave_speed_year20nonpeak_build_userchanged_widget.value, (int, float)) and weave_speed_year20nonpeak_build_userchanged_widget.value >= 0:
            updated_Weave_year20nonpeak_speed = max(weave_speed_year20nonpeak_build_userchanged_widget.value, 5)  # Ensure the speed is at least 5
        else:
            updated_Weave_year20nonpeak_speed = max(weave_speed_year20nonpeak_build_modelcalc_widget.value, 5)  # Use the model value if the user value is invalid

        # Update the value of NWS20B widget (project evaluation widget)
        NWS20B_widget.value = updated_Weave_year20nonpeak_speed

    # Link the function to the user input widget change
    weave_speed_year20nonpeak_build_userchanged_widget.observe(calculate_nws20b, names='value')  # User-modified speed input

    # Combine into layout for display
    Weave_Year20NonPeak_Build_Speed_widgets = widgets.HBox([
        weave_speed_year20nonpeak_build_modelcalc_widget,
        weave_speed_year20nonpeak_build_userchanged_widget,
        NWS20B_explanation_widget
    ])
    
     #######################################################################################################  
        
    # Widgets for Non-Peak Truck Speed Calculation
    truck_speed_year20nonpeak_build_modelcalc_widget = widgets.IntText(
        value=0,  # Set initial value to 0 or any other valid integer
        description="Truck Speed (Calculated by Model):",
        disabled=True,  # Make it read-only
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    truck_speed_year20nonpeak_build_userchanged_widget = widgets.Text(
        value='',  # Initially set to 0 or a valid integer value
        description="Truck Speed (Changed by User):",
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Non-HOV Speed Volume (Used for Project Evaluation) for Build
    NTS20B_widget = widgets.IntText(
        value=truck_speed_year20nonpeak_build_modelcalc_widget.value,  # Set initially to the calculated value
        description="Truck Speed (Used for Proj Evaluation):",
        disabled=True,  # Make it read-only
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Explanation widget for user-modified values
    NTS20B_explanation_widget = widgets.Text(
        value=None,  # Allow users to enter a text explanation
        description="Reasons for Change:",
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,  # Optional layout style, if needed
        style={'description_width': 'initial'}  # Optional style for description width
    )

    # Function to update truck speed calculation for non-peak period
    def update_year20nonpeak_build_truck_speed(change=None):
        try:
            # Retrieve relevant widget values
            NTV20B = NTV20B_widget.value  # NTV20B
            NNS20B = NNS20B_widget.value  # NNS20B
            NWS20B = NWS20B_widget.value  # NWS20B

            # If HwyRail is true, use FFSpeedB
            if ProjType == "Hwy-Rail Grade Crossing":
                truck_speed_year20nonpeak_build_modelcalc_widget.value = FFSpeedB
                return

            # If NTV20B is 0, set the speed to 55
            if NTV20B == 0:
                truck_speed_year20nonpeak_build_modelcalc_widget.value = 55
                return

            # Lookup adjustment values from SpeedPavAdj
            # Find the closest IRI value from the dictionary keys
            closest_iri_key = min(SpeedPavAdj.keys(), key=lambda x: abs(x - IRI20B))
            auto_adj = SpeedPavAdj[closest_iri_key]["Auto"]  # Auto adjustment factor
            truck_adj = SpeedPavAdj[closest_iri_key]["Truck"]  # Truck adjustment factor

            # Calculate truck speed based on the formula
            if ProjType == "Auxiliary Lane":
                base_speed = NWS20B
            else:
                base_speed = NNS20B

            adjusted_speed = min(TruckSpeed, base_speed / (auto_adj if ProjType == "Pavement" else 1))
            final_speed = adjusted_speed * (truck_adj if ProjType == "Pavement" else 1)

            # Set the truck speed value to the final calculated value
            truck_speed_year20nonpeak_build_modelcalc_widget.value = round(final_speed, 2)

        except:
            # In case of any error, set the speed to 0
            truck_speed_year20nonpeak_build_modelcalc_widget.value = 0
 

    # Initial call to set the value based on the current widget state
    update_year20nonpeak_build_truck_speed()

    # Add observers to trigger the function when relevant widget values change
    NTV20B_widget.observe(update_year20nonpeak_build_truck_speed, names='value')  # NTV20B
    NNS20B_widget.observe(update_year20nonpeak_build_truck_speed, names='value')  # NNS20B
    NWS20B_widget.observe(update_year20nonpeak_build_truck_speed, names='value')  # NWS20B
    projectinfo_widgets.truck_speed_widget.observe(update_year20nonpeak_build_truck_speed, names='value')  # TruckSpeed
    projectinfo_widgets.subcategory_dropdown.observe(update_year20nonpeak_build_truck_speed, names='value')  # ProjType
    projectinfo_widgets.free_flow_speed_no_build_widget.observe(update_year20nonpeak_build_truck_speed, names='value')  # FFSpeedB
    projectinfo_widgets.ramp_design_speed_no_build_widget.observe(update_year20nonpeak_build_truck_speed, names='value')  # RampFFSpdB
    projectinfo_widgets.hov_hot_lanes_no_build_widget.observe(update_year20nonpeak_build_truck_speed, names='value')  # HOV lane info
    projectinfo_widgets.highway_segment_no_build_widget.observe(update_year20nonpeak_build_truck_speed, names='value')  # SegmentB
    projectinfo_widgets.iri_forecast_year_no_build_widget.observe(update_year20nonpeak_build_truck_speed, names='value')  # IRI20B

    # Function to calculate the updated project evaluation speed (NTS20B)
    def calculate_nts20b(change):
        # Access the user-modified value directly from the widget
        if isinstance(truck_speed_year20nonpeak_build_userchanged_widget.value, (int, float)) and truck_speed_year20nonpeak_build_userchanged_widget.value >= 0:
            updated_Truck_year20nonpeak_speed = max(truck_speed_year20nonpeak_build_userchanged_widget.value, 5)  # Ensure the speed is at least 5
        else:
            updated_Truck_year20nonpeak_speed = max(truck_speed_year20nonpeak_build_modelcalc_widget.value, 5)  # Use the model value if the user value is invalid

        # Update the value of NTS20B widget (project evaluation widget)
        NTS20B_widget.value = updated_Truck_year20nonpeak_speed

    # Link the function to the user input widget change
    truck_speed_year20nonpeak_build_userchanged_widget.observe(calculate_nts20b, names='value')  # User-modified speed input

    # Combine into layout for display
    Truck_Year20NonPeak_Build_Speed_widgets = widgets.HBox([truck_speed_year20nonpeak_build_modelcalc_widget, truck_speed_year20nonpeak_build_userchanged_widget,  NTS20B_explanation_widget])

    
    
=======
    # Link the PHV1NB widget update to changes in HOV_Vol_peak_userchanged_widget
    HOV_Vol_peak_userchanged_widget.observe(calculate_phv1nb, names='value')  
    
    # Combine all three inputs into a horizontal layout
    HOV_vol_peak_widgets = widgets.HBox([HOV_Vol_peak_modelcalc_widget, HOV_Vol_peak_userchanged_widget, PHV1NB_explaination_widget])   
    
    
    # Non-HOV Volume Widget
    def update_Non_HOV_Volume(change):
        # Access the necessary widget values from projectinfo_widgets
        PerPeakADT = params.per_peak_adt 
        ADT1NB = projectinfo_widgets.adt_base_year_no_build_widget.value
        PerWeaveNB = projectinfo_widgets.percent_traffic_weave_no_build_widget.value
        PerTruckNB = projectinfo_widgets.percent_trucks_nobuild_widget.value
        TMSLookup = params.TMSLookup
        TMSAdj = params.tms_adj
        subcategory_value = projectinfo_widgets.subcategory_dropdown.value

        # Formula for HOV volume model calculated widget
        if subcategory_value == "Hwy-Rail Grade Crossing":
            HOV_Volume_Peak_Model = 0
        else:
            # Check for HOVConn (HOV Connector) or HOVDrop (HOV Drop Ramp)
            if subcategory_value == "HOV Connector" or subcategory_value == "HOV Drop Ramp":
                HOV_Volume_Peak_Model = HOVvolNB * PeakLngthNB * (1 - PerWeaveNB)
            else:
                HOV_Volume_Peak_Model = HOVvolNB * PeakLngthNB  # Default case if no HOVConn or HOVDrop
        
        # Update the HOV Volume Peak Period widget dynamically
        HOV_Vol_peak_modelcalc_widget.value = round(HOV_Volume_Peak_Model, 0)    
>>>>>>> 3ce506f0b22b27317d6525ffa8fe8b5e58771617
    
    
    
    
    
    
    
    
    
    
    # Highway Speed and Volume Inputs Section
<<<<<<< HEAD
    
    highway_subsections_nobuild = [
        {
            'subtitle': 'Year 1 - Peak Period',
            'widgets': [HOV_vol_year1peak_nobuild_widgets, Non_HOV_vol_year1peak_nobuild_widgets, Weaving_Volume_year1peak_nobuild_widgets, Truck_Volume_year1peak_nobuild_widgets, HOV_Speed_year1peak_nobuild_widgets, NonHOV_speed_year1peak_nobuild_widgets, Weave_Speed_year1peak_nobuild_widgets, Truck_Speed_year1peak_nobuild_widgets],
            'info_texts': highway_speed_and_volume_input_info[:8]  # Use the first 8 info items for Year 1 Peak
        },
        {
            'subtitle': 'Year 1 - Non-Peak Period',
            'widgets': [Non_HOV_vol_year1nonpeak_widgets, Weaving_volume_year1nonpeak_widgets, Truck_volume_year1nonpeak_widgets, NonHOV_speed_year1nonpeak_widgets, Weave_speed_year1nonpeak_widgets, Truck_speed_year1nonpeak_widgets],
            'info_texts': highway_speed_and_volume_input_info[8:14]  
        },
        {
            'subtitle': 'Year 20 - Peak Period',  
            'widgets': [HOV_vol_year20peak_widgets, Non_HOV_vol_year20peak_widgets, Weaving_Volume_year20peak_widgets, Truck_Volume_year20peak_widgets, HOV_Year20Peak_Speed_widgets, NonHOV_Year20Peak_Speed_widgets,  Weave_Year20Peak_Speed_widgets, Truck_Year20Peak_Speed_widgets],
            'info_texts': highway_speed_and_volume_input_info[:8]
        },
        {
            'subtitle': 'Year 20 - Non Peak Period',  
            'widgets': [ Non_HOV_Vol_year20nonpeak_widgets, Weaving_Vol_year20nonpeak_widgets, Truck_Volume_year20nonpeak_widgets, NonHOV_speed_year20nonpeak_widgets, Weave_Speed_year20nonpeak_widgets, Truck_Speed_year20nonpeak_widgets],
            'info_texts': highway_speed_and_volume_input_info[8:14]
        }
    ]
    
    
    highway_subsections_build = [
        {
            'subtitle': 'Year 1 - Peak Period', 
            'widgets': [HOV_Vol_year1peak_build_widgets, Non_HOV_Vol_year1peak_build_widgets, Weaving_Vol_year1peak_build_widgets, Truck_Vol_year1peak_build_widgets, HOV_Speed_year1peak_build_widgets, NonHOV_Speed_Year1Peak_Build_Widgets, Weaving_Speed_year1peak_build_widgets, Truck_Speed_year1peak_build_widgets ],
            'info_texts': highway_speed_and_volume_input_info[:8]
        },
        {
            'subtitle': 'Year 1 - Non-Peak Period',  
            'widgets': [Non_HOV_vol_year1nonpeak_build_widgets, Weaving_Vol_year1nonpeak_build_widgets, Truck_Vol_year1nonpeak_build_widgets, NonHOV_Speed_Year1NonPeak_Build_Widgets, Weaving_Speed_year1nonpeak_build_widgets, Truck_Speed_year1nonpeak_build_widgets],
            'info_texts': highway_speed_and_volume_input_info[8:14]
        },
        {
            'subtitle': 'Year 20 - Peak Period',  
            'widgets': [HOV_vol_year20peak_build_widgets, nonHOV_vol_year20peak_build_widgets, Weaving_vol_year20peak_build_widgets, Truck_vol_year20peak_build_widgets, NonHOV_Year20Peak_Build_Speed_widgets, HOV_Year20Peak_Build_Speed_widgets, Weave_Year20Peak_Build_Speed_widgets, Truck_Year20Peak_Build_Speed_widgets ],
            'info_texts': highway_speed_and_volume_input_info[:8]
        },
        {
            'subtitle': 'Year 20 - Non-Peak Period',  
            'widgets': [NonHOV_Year20NonPeak_Build_Volume_widgets, Weaving_vol_year20nonpeak_build_widgets, Truck_vol_year20nonpeak_build_widgets, NonHOV_Year20NonPeak_Build_Speed_widgets, Weave_Year20NonPeak_Build_Speed_widgets, Truck_Year20NonPeak_Build_Speed_widgets ],
            'info_texts': highway_speed_and_volume_input_info[8:14]
        }
    ]
         
    highway_speed_and_volume_input_nobuild_section = create_section_with_subsections(
        highway_speed_and_volume_input_nobuild_title,
        highway_speed_and_volume_input_nobuild_subtitle,
        subsections=highway_subsections_nobuild
    )
        
    highway_speed_and_volume_input_build_section = create_section_with_subsections(
        highway_speed_and_volume_input_build_title,
        highway_speed_and_volume_input_build_subtitle,
        subsections=highway_subsections_build
    )
    

    
    
    
    

    
    
=======
    highway_speed_and_volume_input_section = create_section(
        highway_speed_and_volume_input_title,
        highway_speed_and_volume_input_subtitle,
        [HOV_vol_peak_widgets],
        highway_speed_and_volume_input_info
    )
>>>>>>> 3ce506f0b22b27317d6525ffa8fe8b5e58771617

    # Non-HOV Volume Widget
    
    
<<<<<<< HEAD
    all_sections = widgets.VBox([highway_speed_and_volume_input_nobuild_section, highway_speed_and_volume_input_build_section])
=======
    all_sections = widgets.VBox([highway_speed_and_volume_input_section])
>>>>>>> 3ce506f0b22b27317d6525ffa8fe8b5e58771617
    
    display(all_sections)
    
    
    
    
    
    