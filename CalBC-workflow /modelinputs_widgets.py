import ipywidgets as widgets
from ipywidgets import Widget
from ipywidgets import interactive
from IPython.display import display, Markdown
from parameters import parameters
params = parameters()

from widgets_helper import (highway_speed_and_volume_input_title, highway_speed_and_volume_input_subtitle, highway_speed_and_volume_input_info
)

import projectinfo_widgets 

from widgets_helper import info_button_popup, create_section, create_section_with_subsections

common_layout = widgets.Layout(
    width='450px', 
    background_color='#CCFFCC',  # Background color for all widgets
    padding='2px',
    border='2px solid gray'  # Border color and thickness
)


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
NumTrain1 = projectinfo_widgets.NumTrain1_widget.value
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

    # Create the HOV Volume widget to display the calculated value
    HOV_Vol_year1peak_modelcalc_widget = widgets.IntText(
        value=0,  # Set initial value to 0, or any other valid integer
        description="HOV Volume(Calculated by Model):",
        disabled=True,  # Make it read-only so the user cannot modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Create the HOV Volume Peak Period widget for user-modified value
    HOV_Vol_year1peak_userchanged_widget = widgets.Text(
        value='',  # Initially set to 0 or a valid integer value
        description="HOV Volume (Changed by User):",
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Create the PHV1NB widget based on the formula
    PHV1NB_widget = widgets.IntText(
        value=HOV_Vol_year1peak_modelcalc_widget.value,  # Set initially to the calculated value
        description="HOV Volume (Used for Proj Evaluation):",
        disabled=True,  # Make it read-only 
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    PHV1NB_explaination_widget = widgets.Text(
        value=None,  
        description="Reasons for Change:",  # Label for the input field
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,  # Optional layout style, if needed
        style={'description_width': 'initial'}  # Optional style for description width
    )

    # Function to update HOV Volume dynamically
    def update_HOV_Year1Peak_Volume(change):


        # Formula for HOV volume model calculated widget
        if ProjType == "Hwy-Rail Grade Crossing":
            HOV_Volume_Year1Peak_Model = 0
        else:
            if ProjType == "HOV Connector" or ProjType == "HOV Drop Ramp":
                HOV_Volume_Year1Peak_Model = HOVvolNB * PeakLngthNB * (1 - PerWeaveNB)
            else:
                HOV_Volume_Year1Peak_Model = HOVvolNB * PeakLngthNB  # Default case if no HOVConn or HOVDrop
        
        # Update the HOV Volume Peak Period widget dynamically
        HOV_Vol_year1peak_modelcalc_widget.value = round(HOV_Volume_Year1Peak_Model, 0)

    # Function to calculate PHV1NB
    def calculate_phv1nb(change):
        # Access the user-modified value directly from the widget
        if isinstance(HOV_Vol_year1peak_userchanged_widget.value, (int, float)) and HOV_Vol_year1peak_userchanged_widget.value >= 0:
            PHV1NB = HOV_Vol_year1peak_userchanged_widget.value  # Use the user-modified value if valid
        else:
            PHV1NB = HOV_Vol_year1peak_modelcalc_widget.value  # Use the model value if the user value is invalid

        # Update the value of PHV1NB widget
        PHV1NB_widget.value = PHV1NB

    # Link the PHV1NB widget update to changes in HOV_Vol_peak_userchanged_widget
    HOV_Vol_year1peak_userchanged_widget.observe(calculate_phv1nb, names='value')  

    # Combine all widgets into a horizontal layout for HOV Volume
    HOV_vol_year1peak_widgets = widgets.HBox([HOV_Vol_year1peak_modelcalc_widget, HOV_Vol_year1peak_userchanged_widget, PHV1NB_explaination_widget])

    # Attach observers to the relevant widgets to update the HOV Volume widget dynamically
    projectinfo_widgets.subcategory_dropdown.observe(update_HOV_Year1Peak_Volume, names='value')
    projectinfo_widgets.HOV_lane_nobuild_widget.observe(update_HOV_Year1Peak_Volume, names='value')
    projectinfo_widgets.peak_period_widget.observe(update_HOV_Year1Peak_Volume, names='value')
    projectinfo_widgets.percent_traffic_weave_no_build_widget.observe(update_HOV_Year1Peak_Volume, names='value')
    HOV_Vol_year1peak_modelcalc_widget.observe(calculate_phv1nb, names='value')
    HOV_Vol_year1peak_userchanged_widget.observe(calculate_phv1nb, names='value')
    
    
 
  
    # Create the Non-HOV Volume widget to display the calculated value
    Non_HOV_Vol_year1peak_modelcalc_widget = widgets.IntText(
        value=0,  # Set initial value to 0, or any other valid integer
        description="Non-HOV Volume (Calculated by Model):",
        disabled=True,  # Make it read-only so the user cannot modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Create the Non-HOV Volume Peak Period widget for user-modified value
    Non_HOV_Vol_year1peak_userchanged_widget = widgets.Text(
        value='',  # Initially set to 0 or a valid integer value
        description="Non-HOV Volume(Changed by User):",
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )
    
    PNV1NB_widget = widgets.IntText(
        value=Non_HOV_Vol_year1peak_modelcalc_widget.value,  # Set initially to the calculated value
        description="Non-HOV Volume (Used for Proj Evaluation):",
        disabled=True,  # Make it read-only
        layout=common_layout,
        style={'description_width': 'initial'}
    )
    
    PNV1NB_explanation_widget = widgets.Text(
        value=None,  # Allow users to enter a text explanation
        description="Reasons for Change:",  # Label for the input field
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,  # Optional layout style, if needed
        style={'description_width': 'initial'}  # Optional style for description width
    )
    

    # Non-HOV Volume Widget update function
    def update_Non_HOV_Year1Peak_Volume(change):
        # Access the necessary widget values from projectinfo_widgets


        # Check for "Hwy-Rail" subcategory
        if ProjType == "Hwy-Rail Grade Crossing":
            Non_HOV_Volume_Year1Peak_Model = 0
        else:
            # Determine the traffic factor based on subcategory
            if ProjType == "Auxiliary Lane" or ProjType == "Off-Ramp Widening":
                traffic_factor = PerWeaveNB
            else:
                traffic_factor = PerTruckNB

            # Look up the value from TMSAdj dictionary using TMSLookup key
            if TMSLookup in TMSAdj:
                TMS_value = TMSAdj[TMSLookup]["VolumeWithout"]  # No need to adjust column, directly use "VolumeWithout"
            else:
                TMS_value = 1  # Default value if TMSLookup is not found in TMSAdj   
    
        # Formula for Non-HOV Volume model
        Non_HOV_Volume_Year1Peak_Model = (PerPeakADT * ADT1NB) * (1 - traffic_factor) * TMS_value - HOVvolNB * PeakLngthNB
    
        # Update the Non-HOV Volume Peak Period widget
        Non_HOV_Vol_year1peak_modelcalc_widget.value = round(Non_HOV_Volume_Year1Peak_Model, 0)
    
    update_Non_HOV_Year1Peak_Volume()

    # Attach observers to the relevant widgets to update the Non-HOV Volume widget dynamically
    projectinfo_widgets.adt_base_year_no_build_widget.observe(update_Non_HOV_Year1Peak_Volume, names='value')
    projectinfo_widgets.percent_traffic_weave_no_build_widget.observe(update_Non_HOV_Year1Peak_Volume, names='value')
    projectinfo_widgets.percent_trucks_nobuild_widget.observe(update_Non_HOV_Year1Peak_Volume, names='value')
    projectinfo_widgets.HOV_lane_nobuild_widget.observe(update_Non_HOV_Year1Peak_Volume, names='value')
    projectinfo_widgets.peak_period_widget.observe(update_Non_HOV_Year1Peak_Volume, names='value')
    projectinfo_widgets.subcategory_dropdown.observe(update_Non_HOV_Year1Peak_Volume, names='value')


        
    # Non-HOV PNV1NB update function (similar to PHV1NB)
    def calculate_pnv1nb(change):
        # Access the user-modified value directly from the widget
        if isinstance(Non_HOV_Vol_year1peak_userchanged_widget.value, (int, float)) and Non_HOV_Vol_year1peak_userchanged_widget.value >= 0:
            PNV1NB = Non_HOV_Vol_year1peak_userchanged_widget.value  # Use the user-modified value if valid
        else:
            PNV1NB = Non_HOV_Vol_year1peak_modelcalc_widget.value  # Use the model value if the user value is invalid

        # Update the value of PNV1NB widget
        PNV1NB_widget.value = PNV1NB

    # Link the PNV1NB widget update to changes in Non-HOV Volume Peak User widget
    Non_HOV_Vol_year1peak_userchanged_widget.observe(calculate_pnv1nb, names='value')

    # Combine all the Non-HOV volume widgets into a horizontal layout for display
    Non_HOV_vol_year1peak_widgets = widgets.HBox([Non_HOV_Vol_year1peak_modelcalc_widget, Non_HOV_Vol_year1peak_userchanged_widget, PNV1NB_explanation_widget])        
    
    
    # Weaving Volume (Calculated by Model)
    weaving_volume_year1peak_modelcalc_widget = widgets.IntText(
        value=0,  # Set initial value to 0 or any other valid integer
        description="Weaving Volume (Calculated by Model):",
        disabled=True,  # Make it read-only so the user cannot modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Weaving Volume (User-modified value)
    weaving_volume_year1peak_userchanged_widget = widgets.Text(
        value='',  # Initially set to 0 or a valid integer value
        description="Weaving Volume (Changed by User):",
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Weaving Volume (Used for Project Evaluation)
    PWV1NB_widget = widgets.IntText(
        value=weaving_volume_year1peak_modelcalc_widget.value,  # Set initially to the calculated value
        description="Weaving Volume (Used for Proj Evaluation):",
        disabled=True,  # Make it read-only
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Explanation widget for user-modified values
    PWV1NB_explanation_widget = widgets.Text(
        value=None,  # Allow users to enter a text explanation
        description="Reasons for Change:",  # Label for the input field
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,  # Optional layout style, if needed
        style={'description_width': 'initial'}  # Optional style for description width
    )

    # Update Weaving Volume Calculation based on widget values
    def update_weaving_volume(change):


        # Calculate VLOOKUP(TMSLookup, TMSAdj, 3) value
        if TMSLookup in TMSAdj:
            TMS_value = TMSAdj[TMSLookup]["VolumeWithout"]  
        else:
            TMS_value = 1  # Default value if TMSLookup is not found in TMSAdj

        # Initialize Weaving Volume Model as 0
        Weaving_Volume_Model = 0

        # Apply the first condition: Check for "Auxiliary Lane" or "Off-Ramp"
        if ProjType == "Auxiliary Lane" or ProjType == "Off-Ramp Widening":
            Weaving_Volume_Model += (PerPeakADT * ADT1NB) * (PerWeaveNB - PerTruckNB) * TMS_value

        # Apply the second condition: Check for "Auxiliary Lane"
        if ProjType == "Auxiliary Lane":
            Weaving_Volume_Model += RampVolP * PeakLngthNB

        # Apply the third condition: Check for "HOV Connector" or "HOV Drop Ramp"
        if ProjType == "HOV Connector" or ProjType == "HOV Drop Ramp":
            Weaving_Volume_Model += PerWeaveNB * HOVvolNB * PeakLngthNB

        # Update the Weaving Volume widget dynamically
        weaving_volume_year1peak_modelcalc_widget.value = round(Weaving_Volume_Model, 0)  # Correct widget name

    # Link the update function to changes in relevant widgets
    projectinfo_widgets.adt_base_year_no_build_widget.observe(update_weaving_volume, names='value')
    projectinfo_widgets.percent_traffic_weave_no_build_widget.observe(update_weaving_volume, names='value')
    projectinfo_widgets.percent_trucks_nobuild_widget.observe(update_weaving_volume, names='value')
    projectinfo_widgets.hourly_ramp_volume_peak_widget.observe(update_weaving_volume, names='value')
    projectinfo_widgets.peak_period_widget.observe(update_weaving_volume, names='value')
    projectinfo_widgets.HOV_lane_nobuild_widget.observe(update_weaving_volume, names='value')
    projectinfo_widgets.subcategory_dropdown.observe(update_weaving_volume, names='value')

    # Function to update PWV1NB widget when user modifies the value
    def calculate_pwv1nb(change):
        # Access the user-modified value directly from the widget
        if isinstance(weaving_volume_year1peak_userchanged_widget.value, (int, float)) and weaving_volume_year1peak_userchanged_widget.value >= 0:
            PWV1NB = weaving_volume_year1peak_userchanged_widget.value  # Use the user-modified value if valid
        else:
            PWV1NB = weaving_volume_year1peak_modelcalc_widget.value  # Use the model value if the user value is invalid

        # Update the value of PWV1NB widget
        PWV1NB_widget.value = PWV1NB

    # Link the PWV1NB widget update to changes in Weaving Volume User widget
    weaving_volume_year1peak_userchanged_widget.observe(calculate_pwv1nb, names='value')

    # Combine all the Weaving Volume widgets into a horizontal layout for display
    Weaving_Volume_year1peak_widgets = widgets.HBox([weaving_volume_year1peak_modelcalc_widget, weaving_volume_year1peak_userchanged_widget, PWV1NB_explanation_widget])    

    # Truck Volume (Calculated by Model)
    truck_volume_year1peak_modelcalc_widget = widgets.IntText(
        value=0,  # Set initial value to 0 or any other valid integer
        description="Truck Volume (Calculated by Model):",
        disabled=True,  # Make it read-only so the user cannot modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Truck Volume (User-modified value)
    truck_volume_year1peak_userchanged_widget = widgets.Text(
        value='',  # Initially set to 0 or a valid integer value
        description="Truck Volume (Changed by User):",
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Truck Volume (Used for Project Evaluation)
    PTV1NB_widget = widgets.IntText(
        value=truck_volume_year1peak_modelcalc_widget.value,  # Set initially to the calculated value
        description="Truck Volume (Used for Proj Evaluation):",
        disabled=True,  # Make it read-only
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Explanation widget for user-modified values
    PTV1NB_explanation_widget = widgets.Text(
        value=None,  # Allow users to enter a text explanation
        description="Reasons for Change:",  # Label for the input field
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,  # Optional layout style, if needed
        style={'description_width': 'initial'}  # Optional style for description width
    )

    # Update Truck Volume Calculation based on widget values
    def update_truck_volume(change):
        # Access the necessary widget values from projectinfo_widgets


        # Calculate VLOOKUP(TMSLookup, TMSAdj, 3) value
        if TMSLookup in TMSAdj:
            TMS_value = TMSAdj[TMSLookup]["VolumeWithout"]  # Adjust column value if needed
        else:
            TMS_value = 1  # Default value if TMSLookup is not found in TMSAdj

        # Initialize Truck Volume Model as 0
        Truck_Volume_Model = 0

        # Apply the condition: Check for "Hwy-Rail Grade Crossing"
        if ProjType == "Hwy-Rail Grade Crossing":
            Truck_Volume_Model = 0  # Set volume to 0 if subcategory is "Hwy-Rail Grade Crossing"
        else:
            Truck_Volume_Model = (PerPeakADT * ADT1NB) * PerTruckNB * TMS_value  # Apply formula for other subcategories

        # Update the Truck Volume widget dynamically
        truck_volume_year1peak_modelcalc_widget.value = round(Truck_Volume_Model, 0)  # Correct widget name

    # Link the update function to changes in relevant widgets
    projectinfo_widgets.adt_base_year_no_build_widget.observe(update_truck_volume, names='value')
    projectinfo_widgets.percent_trucks_nobuild_widget.observe(update_truck_volume, names='value')
    projectinfo_widgets.subcategory_dropdown.observe(update_truck_volume, names='value')

    # Function to update PTV1NB widget when user modifies the value
    def calculate_ptv1nb(change):
        # Access the user-modified value directly from the widget
        if isinstance(truck_volume_year1peak_userchanged_widget.value, (int, float)) and truck_volume_year1peak_userchanged_widget.value >= 0:
            PTV1NB = truck_volume_year1peak_userchanged_widget.value  # Use the user-modified value if valid
        else:
            PTV1NB = truck_volume_year1peak_modelcalc_widget.value  # Use the model value if the user value is invalid

        # Update the value of PTV1NB widget
        PTV1NB_widget.value = PTV1NB

    # Link the PTV1NB widget update to changes in Truck Volume User widget
    truck_volume_year1peak_userchanged_widget.observe(calculate_ptv1nb, names='value')

    # Combine all the Truck Volume widgets into a horizontal layout for display
    Truck_Volume_year1peak_widgets = widgets.HBox([truck_volume_year1peak_modelcalc_widget, truck_volume_year1peak_userchanged_widget, PTV1NB_explanation_widget])
    
    
    #Non-HOV Speed widgets 
    nonhov_speed_year1peak_modelcalc_widget = widgets.IntText(
        value=0,  # Set initial value to 0 or any other valid integer
        description="Non-HOV Speed (Calculated by Model):",
        disabled=True,  # Make it read-only so the user cannot modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )
    
    nonhov_speed_year1peak_userchanged_widget = widgets.Text(
        value='',  # Initially set to 0 or a valid integer value
        description="Non-HOV Speed (Changed by User):",
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )
    
    # Non-HOV Speed Volume (Used for Project Evaluation)
    PNS1NB_widget = widgets.IntText(
        value=nonhov_speed_year1peak_modelcalc_widget.value,  # Set initially to the calculated value
        description="Non-HOV Speed (Used for Proj Evaluation):",
        disabled=True,  # Make it read-only
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Explanation widget for user-modified values
    PNS1NB_explanation_widget = widgets.Text(
        value=None,  # Allow users to enter a text explanation
        description="Reasons for Change:",  # Label for the input field
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,  # Optional layout style, if needed
        style={'description_width': 'initial'}  # Optional style for description width
    )    

    def update_nonhov_year1peak_speed(change=None):
        traffic_volumes = [
            PHV1NB_widget.value,  
            PNV1NB_widget.value,  
            PWV1NB_widget.value,
            PTV1NB_widget.value
        ]

        sum_all = sum(traffic_volumes)
        sum_hov_zero = sum(traffic_volumes)
        sum_hov_nonzero = sum(traffic_volumes[1:])  # skip HOV volume

        # Step 2: Formula for Non-HOV Speed calculation
        if sum_all == 0:
            nonhov_speed = 55  # If total volume is zero, use default value
        else:
            if ProjType == "Queuing":
                # Special case for queuing calculation
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
                # Normal speed calculation using "No Build" parameters from the formula
                flow_sum = sum_hov_nonzero if HOVLanesNB != 0 else sum_hov_zero

                # Access the "No Build" parameters from the roadway_capacity_non_HOV dictionary
                capacity_params = roadway_capacity_non_HOV["Non-HOV Lanes"]["No Build"]
                GenAlphaNB = capacity_params["GenAlphaNB"]
                GenBetaNB = capacity_params["GenBetaNB"]
                GenLaneCapNB = capacity_params["GenLaneCapNB"]

                # Apply the speed calculation formula
                volume_term = flow_sum / (GenLanesNB * GenLaneCapNB * PeakLngthNB)
                delay_speed = FFSpeedNB / (IRI1NB * (1 + GenAlphaNB * min(volume_term, MaxVC) ** GenBetaNB))
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
        closest_iri_key = min(SpeedPavAdj.keys(), key=lambda x: abs(x - IRI1NB))
        nonhov_speed *= SpeedPavAdj[closest_iri_key]["Auto"]

        # Update the widget with the final calculated speed value
        nonhov_speed_year1peak_modelcalc_widget.value = round(nonhov_speed, 1)

    # Trigger the calculation once or observe widget changes
    update_nonhov_year1peak_speed()  # To calculate initially
    
    # Link the update function to changes in relevant widgets
    PHV1NB_widget.observe(update_nonhov_year1peak_speed, names='value')
    PNV1NB_widget.observe(update_nonhov_year1peak_speed, names='value')
    PWV1NB_widget.observe(update_nonhov_year1peak_speed, names='value')
    PTV1NB_widget.observe(update_nonhov_year1peak_speed, names='value')
    projectinfo_widgets.subcategory_dropdown.observe(update_nonhov_year1peak_speed, names='value')  
    projectinfo_widgets.percent_traffic_weave_no_build_widget.observe(update_nonhov_year1peak_speed, names='value')  
    projectinfo_widgets.iri_base_year_no_build_widget.observe(update_nonhov_year1peak_speed, names='value')  

    def calculate_pns1nb(change):
        # Access the user-modified value directly from the widget
        if isinstance(nonhov_speed_year1peak_userchanged_widget.value, (int, float)) and nonhov_speed_year1peak_userchanged_widget.value >= 0:
            updated_nonHOV_year1peak_speed = max(nonhov_speed_peak_userchanged_widget.value, 5)  # Ensure the speed is at least 5
        else:
            updated_nonHOV_year1peak_speed = max(nonhov_speed_year1peak_modelcalc_widget.value, 5)  # Use the model value if the user value is invalid

        # Update the value of PNS1NB widget
        PNS1NB_widget.value = updated_nonHOV_year1peak_speed


    # Link the function to the user input widget change
    nonhov_speed_year1peak_userchanged_widget.observe(calculate_pns1nb, names='value')
    
    # Combine all the Non HOV Speed widgets into a horizontal layout for display
    NonHOV_Year1Peak_Volume_widgets = widgets.HBox([nonhov_speed_year1peak_modelcalc_widget, nonhov_speed_year1peak_userchanged_widget, PNS1NB_explanation_widget])    

    
    #HOV Speed widgets 
    hov_speed_year1peak_modelcalc_widget = widgets.IntText(
        value=0,  # Set initial value to 0 or any other valid integer
        description="HOV Speed (Calculated by Model):",
        disabled=True,  # Make it read-only so the user cannot modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )
    
    hov_speed_year1peak_userchanged_widget = widgets.Text(
        value='',  # Initially set to 0 or a valid integer value
        description="HOV Speed (Changed by User):",
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )
    
    # Non-HOV Speed Volume (Used for Project Evaluation)
    PHS1NB_widget = widgets.IntText(
        value=hov_speed_year1peak_modelcalc_widget.value,  # Set initially to the calculated value
        description="HOV Speed (Used for Proj Evaluation):",
        disabled=True,  # Make it read-only
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Explanation widget for user-modified values
    PHS1NB_explanation_widget = widgets.Text(
        value=None,  # Allow users to enter a text explanation
        description="Reasons for Change:",  # Label for the input field
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,  # Optional layout style, if needed
        style={'description_width': 'initial'}  # Optional style for description width
    )    
    
    def update_hov_speed(change=None):
        # Grab HOV capacity parameters
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

        hov_speed_year1peak_modelcalc_widget.value = round(hov_speed, 1)

    update_hov_speed()  # Initial HOV speed calculation
    
    #Adding Observers
    PHV1NB_widget.observe(update_hov_speed, names='value')
    PNS1NB_widget.observe(update_hov_speed, names='value')
    projectinfo_widgets.subcategory_dropdown.observe(update_hov_speed, names='value')
    projectinfo_widgets.impacted_length_no_build_widget.observe(update_hov_speed, names='value')
    projectinfo_widgets.peak_period_widget.observe(update_hov_speed, names='value')
    projectinfo_widgets.departure_rate_forecast_year_no_build_widget.observe(update_hov_speed, names='value')
    projectinfo_widgets.arrival_rate_base_year_no_build_widget.observe(update_hov_speed, names='value')
    projectinfo_widgets.adt_base_year_no_build_widget.observe(update_hov_speed, names='value')
    projectinfo_widgets.percent_induced_trip_widget.observe(update_hov_speed, names='value')
    projectinfo_widgets.hov_hot_lanes_no_build_widget.observe(update_hov_speed, names='value')
    projectinfo_widgets.free_flow_speed_no_build_widget.observe(update_hov_speed, names='value')
    projectinfo_widgets.iri_base_year_no_build_widget.observe(update_hov_speed, names='value')
    
    def calculate_phs1nb(change):
        # Access the user-modified value directly from the widget
        if isinstance(hov_speed_year1peak_userchanged_widget.value, (int, float)) and hov_speed_year1peak_userchanged_widget.value >= 0:
            updated_HOV_speed = max(hov_speed_peak_userchanged_widget.value, 5)  # Ensure the speed is at least 5
        else:
            updated_HOV_speed = max(hov_speed_year1peak_modelcalc_widget.value, 5)  # Use the model value if the user value is invalid

        # Update the value of PHS1NB widget
        PHS1NB_widget.value = updated_HOV_speed
        
    # Link the function to the user input widget change
    hov_speed_year1peak_userchanged_widget.observe(calculate_phs1nb, names='value')
    
    # Combine all the Non HOV Speed widgets into a horizontal layout for display
    HOV_Speed_Volume_widgets = widgets.HBox([hov_speed_year1peak_modelcalc_widget, hov_speed_year1peak_userchanged_widget, PHS1NB_explanation_widget])  

    
    # Weaving Speed widgets 
    weave_speed_year1peak_modelcalc_widget = widgets.IntText(
        value=0,  # Set initial value to 0 or any other valid integer
        description="Weaving Speed (Calculated by Model):",
        disabled=True,  # Make it read-only so the user cannot modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    weave_speed_year1peak_userchanged_widget = widgets.Text(
        value='',  # Initially set to 0 or a valid integer value
        description="Weaving Speed (Changed by User):",
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Non-HOV Speed Volume (Used for Project Evaluation)
    PWS1NB_widget = widgets.IntText(
        value=weave_speed_year1peak_modelcalc_widget.value,  # Set initially to the calculated value
        description="Weaving Speed (Used for Proj Evaluation):",
        disabled=True,  # Make it read-only
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Explanation widget for user-modified values
    PWS1NB_explanation_widget = widgets.Text(
        value=None,  # Allow users to enter a text explanation
        description="Reasons for Change:",  # Label for the input field
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,  # Optional layout style, if needed
        style={'description_width': 'initial'}  # Optional style for description width
    )  

    # Function to update weaving speed
# Function to update weaving speed
    def update_weaving_year1peak_speed(change=None):
        # Grab the necessary parameters from the provided dictionaries and widgets
        PWV1NB = PWV1NB_widget.value
        PNS1NB = PNS1NB_widget.value
        PTV1NB = PTV1NB_widget.value
        Pavement = ProjType == "Pavement"  # Check if ProjType is "Pavement"

        if PWV1NB == 0:
            weaving_speed = 55  # If PWV1NB is zero, set default weaving speed
        else:
            # Step 2: Check for Auxiliary Lane, Off-Ramp, or Pavement
            if ProjType == "Auxiliary Lane" or ProjType == "Off-Ramp Widening":
                try:
                    # Compute the weaving speed based on the given formula
                    base_speed = 1.1 * (
                        FFSpeedNB - (FFSpeedNB - 42) * (
                            0.321 +
                            0.0039 * exp((PWV1NB + PTV1NB) / NumDirections / PeakLngthNB / 1000) -
                            0.002 * (
                                1083 if ProjType == "Off-Ramp Widening" else SegmentNB * 5280
                            ) * RampFFSpdNB / 1000
                        )
                    )

                    # TMSAdj assumed to be a dictionary
                    tms_factor = TMSAdj.get(TMSLookup, 1)

                    # Pavement speed adjustment from SpeedPavAdj dictionary
                    pavement_factor = SpeedPavAdj[
                        max([k for k in sorted(SpeedPavAdj.keys()) if k <= IRI1NB], default=0)
                    ]["Auto"] if Pavement else 1

                    weaving_speed = max(5, min(PNS1NB, base_speed) * tms_factor * pavement_factor)

                except ZeroDivisionError:
                    print("Error calculating weaving speed due to division by zero.")
                    weaving_speed = 55  # Default to 55 in case of error
                except Exception as e:
                    print(f"Error calculating weaving speed: {e}")
                    weaving_speed = 55  # Default in case of any other exception
            else:
                # Step 3: If no Auxiliary Lane or Off-Ramp, use PNS1NB as the weaving speed
                weaving_speed = PNS1NB

        # Update the weaving speed widget with the calculated value (rounded to 1 decimal place)
        weave_speed_year1peak_modelcalc_widget.value = round(weaving_speed, 1)

    update_weaving_year1peak_speed()  # Initial Weaving speed calculation

    # Adding Observers for the widgets to trigger the weaving speed calculation when the user changes values
    PWV1NB_widget.observe(update_weaving_year1peak_speed, names='value')
    PNS1NB_widget.observe(update_weaving_year1peak_speed, names='value')
    PTV1NB_widget.observe(update_weaving_year1peak_speed, names='value')
    projectinfo_widgets.subcategory_dropdown.observe(update_weaving_year1peak_speed, names='value')
    projectinfo_widgets.impacted_length_no_build_widget.observe(update_weaving_year1peak_speed, names='value')
    projectinfo_widgets.peak_period_widget.observe(update_weaving_year1peak_speed, names='value')
    projectinfo_widgets.departure_rate_forecast_year_no_build_widget.observe(update_weaving_year1peak_speed, names='value')
    projectinfo_widgets.arrival_rate_base_year_no_build_widget.observe(update_weaving_year1peak_speed, names='value')
    projectinfo_widgets.adt_base_year_no_build_widget.observe(update_weaving_year1peak_speed, names='value')
    projectinfo_widgets.percent_induced_trip_widget.observe(update_weaving_year1peak_speed, names='value')
    projectinfo_widgets.hov_hot_lanes_no_build_widget.observe(update_weaving_year1peak_speed, names='value')
    projectinfo_widgets.free_flow_speed_no_build_widget.observe(update_weaving_year1peak_speed, names='value')
    projectinfo_widgets.iri_base_year_no_build_widget.observe(update_weaving_year1peak_speed, names='value')
    
    def calculate_pws1nb(change):
        # Access the user-modified value directly from the widget
        if isinstance(weave_speed_year1peak_modelcalc_widget.value, (int, float)) and weave_speed_year1peak_userchanged_widget.value >= 0:
            updated_weave_speed = max(weave_speed_year1peak_userchanged_widget.value, 5)  # Ensure the speed is at least 5
        else:
            updated_weave_speed = max(weave_speed_year1peak_modelcalc_widget.value, 5)  # Use the model value if the user value is invalid

        # Update the value of PHS1NB widget
        PWS1NB_widget.value = updated_weave_speed
        
    # Link the function to the user input widget change
    weave_speed_year1peak_userchanged_widget.observe(calculate_pws1nb, names='value')
    
    # Combine all the Non HOV Speed widgets into a horizontal layout for display
    Weave_Speed_Year1Peak_widgets = widgets.HBox([weave_speed_year1peak_modelcalc_widget, weave_speed_year1peak_userchanged_widget, PWS1NB_explanation_widget])  
    
    
    
    # Truck Speed widgets 
    truck_speed_year1peak_modelcalc_widget = widgets.IntText(
        value=0,  # Set initial value to 0 or any other valid integer
        description="Truck Speed (Calculated by Model):",
        disabled=True,  # Make it read-only so the user cannot modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    truck_speed_year1peak_userchanged_widget = widgets.Text(
        value='',  # Initially set to 0 or a valid integer value
        description="Truck Speed (Changed by User):",
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Non-HOV Speed Volume (Used for Project Evaluation)
    PTS1NB_widget = widgets.IntText(
        value=truck_speed_year1peak_modelcalc_widget.value,  # Set initially to the calculated value
        description="Truck Speed (Used for Proj Evaluation):",
        disabled=True,  # Make it read-only
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Explanation widget for user-modified values
    PTS1NB_explanation_widget = widgets.Text(
        value=None,  # Allow users to enter a text explanation
        description="Reasons for Change:",  # Label for the input field
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,  # Optional layout style, if needed
        style={'description_width': 'initial'}  # Optional style for description width
    )  
    
    def update_truck_speed(change=None):
        # Retrieve relevant widget values
        PTV1NB = PTV1NB_widget.value
        PWS1NB = PWS1NB_widget.value
        PNS1NB = PNS1NB_widget.value
        Pavement = ProjType == "Pavement"

        if PTV1NB == 0:
            truck_speed = 55
        else:
            # Use PWS1NB if it's Auxiliary or Off-Ramp, otherwise use PNS1NB
            base_speed = PWS1NB if ProjType in ["Auxiliary Lane", "Off-Ramp Widening"] else PNS1NB

            if Pavement:
                # Find the closest IRI key less than or equal to IRI1NB
                iri_keys = [k for k in SpeedPavAdj if k <= IRI1NB]
                closest_iri = max(iri_keys) if iri_keys else 0

                # Apply divisor and multiplier
                pavement_divisor = SpeedPavAdj[closest_iri]["Truck"]
                adjusted_speed = min(TruckSpeed, base_speed / pavement_divisor)
                pavement_multiplier = SpeedPavAdj[closest_iri]["Truck"]
                truck_speed = adjusted_speed * pavement_multiplier
            else:
                truck_speed = min(TruckSpeed, base_speed)

        # Update the truck speed model calculation widget
        truck_speed_year1peak_modelcalc_widget.value = round(truck_speed, 1)
        
    update_truck_speed()  # Initial Weaving speed calculation
    
    # Adding Observers to trigger truck speed calculation
    PTV1NB_widget.observe(update_truck_speed, names='value')
    PWS1NB_widget.observe(update_truck_speed, names='value')
    PNS1NB_widget.observe(update_truck_speed, names='value')
    projectinfo_widgets.truck_speed_widget.observe(update_truck_speed, names='value')
    projectinfo_widgets.subcategory_dropdown.observe(update_truck_speed, names='value')
    projectinfo_widgets.iri_base_year_no_build_widget.observe(update_truck_speed, names='value')
        
    def calculate_pts1nb(change):
        # Access the user-modified value directly from the widget
        if isinstance(truck_speed_year1peak_userchanged_widget.value, (int, float)) and truck_speed_year1peak_userchanged_widget.value >= 0:
            updated_truck_speed = max(truck_speed_year1peak_userchanged_widget.value, 5)  # Ensure the speed is at least 5
        else:
            updated_truck_speed = max(truck_speed_year1peak_modelcalc_widget.value, 5)  # Use the model value if the user value is invalid

        # Update the value of PHS1NB widget
        PTS1NB_widget.value = updated_truck_speed
        
    # Link the function to the user input widget change
    truck_speed_year1peak_userchanged_widget.observe(calculate_pts1nb, names='value')
    
    # Combine all the Non HOV Speed widgets into a horizontal layout for display
    Truck_Speed_Year1Peak_widgets = widgets.HBox([truck_speed_year1peak_modelcalc_widget, truck_speed_year1peak_userchanged_widget, PTS1NB_explanation_widget]) 
    
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
        Non_HOV_Vol_year1peak_modelcalc_widget.value = round(result, 0)
    
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
        value=None,  
        description="Reasons for Change:",  # Label for the input field
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,  # Optional layout style, if needed
        style={'description_width': 'initial'}  # Optional style for description width
    )

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

    # Attach observers to the relevant widgets to update the HOV Volume widget dynamically
    projectinfo_widgets.subcategory_dropdown.observe(update_HOV_Year20Peak_Volume, names='value')
    projectinfo_widgets.HOV_lane_nobuild_widget.observe(update_HOV_Year20Peak_Volume, names='value')
    projectinfo_widgets.peak_period_widget.observe(update_HOV_Year20Peak_Volume, names='value')
    projectinfo_widgets.percent_traffic_weave_no_build_widget.observe(update_HOV_Year20Peak_Volume, names='value')
    projectinfo_widgets.departure_rate_forecast_year_no_build_widget.observe(update_HOV_Year20Peak_Volume, names='value')
    projectinfo_widgets.adt_base_year_no_build_widget.observe(update_HOV_Year20Peak_Volume, names='value')
    projectinfo_widgets.ADT_20NB_widget.observe(update_HOV_Year20Peak_Volume, names='value')
    projectinfo_widgets.departure_rate_forecast_year_build_widget.observe(update_HOV_Year20Peak_Volume, names='value')
    HOV_Vol_year20peak_modelcalc_widget.observe(calculate_phv20nb, names='value')
    HOV_Vol_year20peak_userchanged_widget.observe(calculate_phv20nb, names='value')    
    
    
    
 ########################################################################################################################################################################   
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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # Highway Speed and Volume Inputs Section
    
    highway_subsections = [
        {
            'subtitle': 'Year 1 - Peak Period',
            'widgets': [HOV_vol_year1peak_widgets, Non_HOV_vol_year1peak_widgets, Weaving_Volume_year1peak_widgets, Truck_Volume_year1peak_widgets, HOV_Speed_Volume_widgets, NonHOV_Year1Peak_Volume_widgets, Weave_Speed_Year1Peak_widgets, Truck_Speed_Year1Peak_widgets],
            'info_texts': highway_speed_and_volume_input_info[:8]  # Use the first 8 info items for Year 1 Peak
        },
        {
            'subtitle': 'Year 1 - Non-Peak Period',
            'widgets': [Non_HOV_vol_year1nonpeak_widgets, Weaving_volume_year1nonpeak_widgets, Truck_volume_year1nonpeak_widgets, NonHOV_speed_year1nonpeak_widgets, Weave_speed_year1nonpeak_widgets, Truck_speed_year1nonpeak_widgets],
            'info_texts': highway_speed_and_volume_input_info[8:14]  # Use the next 6 info items for Year 1 Non-Peak
        },
        {
            'subtitle': 'Year 20 - Peak Period',  # Fix the missing opening brace for this dictionary
            'widgets': [HOV_vol_year20peak_widgets, Non_HOV_vol_year20peak_widgets],
            'info_texts': highway_speed_and_volume_input_info[14:15]
        }
    ]

         
    highway_speed_and_volume_input_section = create_section_with_subsections(
        highway_speed_and_volume_input_title,
        highway_speed_and_volume_input_subtitle,
        subsections=highway_subsections
    )
    
    
#     # Non Peak 
#     # Create the Non-HOV Volume widget to display the calculated value
#     Non_HOV_Vol_nonpeak_modelcalc_widget = widgets.IntText(
#         value=0,  # Set initial value to 0, or any other valid integer
#         description="Non-HOV Volume (Calculated by Model):",
#         disabled=True,  # Make it read-only so the user cannot modify the value
#         layout=common_layout,
#         style={'description_width': 'initial'}
#     )

#     # Create the Non-HOV Volume Peak Period widget for user-modified value
#     Non_HOV_Vol_nonpeak_userchanged_widget = widgets.Text(
#         value='',  # Initially set to 0 or a valid integer value
#         description="Non-HOV Volume(Changed by User):",
#         disabled=False,  # Allow the user to modify the value
#         layout=common_layout,
#         style={'description_width': 'initial'}
#     )

#     # Create the PHV1NB widget based on the formula
#     NNV1NB_widget = widgets.IntText(
#         value=Non_HOV_Vol_nonpeak_modelcalc_widget.value,  # Set initially to the calculated value
#         description="Non HOV Volume (Used for Proj Evaluation):",
#         disabled=True,  # Make it read-only 
#         layout=common_layout,
#         style={'description_width': 'initial'}
#     )

#     NNV1NB_explaination_widget = widgets.Text(
#         value=None,  
#         description="Reasons for Change:",  # Label for the input field
#         disabled=False,  # Allow the user to modify the value
#         layout=common_layout,  # Optional layout style, if needed
#         style={'description_width': 'initial'}  # Optional style for description width
#     )
    
    
    
    
    

    
    

    # Non-HOV Volume Widget
    
    
    all_sections = widgets.VBox([highway_speed_and_volume_input_section])
    
    display(all_sections)
    
    
    
    
    
    