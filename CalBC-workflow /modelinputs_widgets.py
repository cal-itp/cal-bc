import ipywidgets as widgets
from ipywidgets import Widget
from ipywidgets import interactive
from IPython.display import display, Markdown
from parameters import parameters
params = parameters()

from widgets_helper import (highway_speed_and_volume_input_title, highway_speed_and_volume_input_subtitle, highway_speed_and_volume_input_info
)

import projectinfo_widgets 

from widgets_helper import info_button_popup, create_section

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
PerPeakADT = params.per_peak_adt
TMSLookup = params.TMSLookup
TMSAdj = params.tms_adj





def create_new_widgets():

    # Create the HOV Volume widget to display the calculated value
    HOV_Vol_peak_modelcalc_widget = widgets.IntText(
        value=0,  # Set initial value to 0, or any other valid integer
        description="HOV Volume(Calculated by Model):",
        disabled=True,  # Make it read-only so the user cannot modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Create the HOV Volume Peak Period widget for user-modified value
    HOV_Vol_peak_userchanged_widget = widgets.IntText(
        value=0,  # Initially set to 0 or a valid integer value
        description="HOV Volume (Changed by User):",
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Create the PHV1NB widget based on the formula
    PHV1NB_widget = widgets.IntText(
        value=HOV_Vol_peak_modelcalc_widget.value,  # Set initially to the calculated value
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
    def update_HOV_Volume(change):


        # Formula for HOV volume model calculated widget
        if ProjType == "Hwy-Rail Grade Crossing":
            HOV_Volume_Peak_Model = 0
        else:
            if ProjType == "HOV Connector" or ProjType == "HOV Drop Ramp":
                HOV_Volume_Peak_Model = HOVvolNB * PeakLngthNB * (1 - PerWeaveNB)
            else:
                HOV_Volume_Peak_Model = HOVvolNB * PeakLngthNB  # Default case if no HOVConn or HOVDrop
        
        # Update the HOV Volume Peak Period widget dynamically
        HOV_Vol_peak_modelcalc_widget.value = round(HOV_Volume_Peak_Model, 0)

    # Function to calculate PHV1NB
    def calculate_phv1nb(change):
        # Access the user-modified value directly from the widget
        if isinstance(HOV_Vol_peak_userchanged_widget.value, (int, float)) and HOV_Vol_peak_userchanged_widget.value >= 0:
            PHV1NB = HOV_Vol_peak_userchanged_widget.value  # Use the user-modified value if valid
        else:
            PHV1NB = HOV_Vol_peak_modelcalc_widget.value  # Use the model value if the user value is invalid

        # Update the value of PHV1NB widget
        PHV1NB_widget.value = PHV1NB

    # Link the PHV1NB widget update to changes in HOV_Vol_peak_userchanged_widget
    HOV_Vol_peak_userchanged_widget.observe(calculate_phv1nb, names='value')  

    # Combine all widgets into a horizontal layout for HOV Volume
    HOV_vol_peak_widgets = widgets.HBox([HOV_Vol_peak_modelcalc_widget, HOV_Vol_peak_userchanged_widget, PHV1NB_explaination_widget])

    # Attach observers to the relevant widgets to update the HOV Volume widget dynamically
    projectinfo_widgets.subcategory_dropdown.observe(update_HOV_Volume, names='value')
    projectinfo_widgets.HOV_lane_nobuild_widget.observe(update_HOV_Volume, names='value')
    projectinfo_widgets.peak_period_widget.observe(update_HOV_Volume, names='value')
    projectinfo_widgets.percent_traffic_weave_no_build_widget.observe(update_HOV_Volume, names='value')
    HOV_Vol_peak_modelcalc_widget.observe(calculate_phv1nb, names='value')
    HOV_Vol_peak_userchanged_widget.observe(calculate_phv1nb, names='value')
    HOV_Vol_peak_userchanged_widget.observe(calculate_phv1nb, names='value') 
    
    
  
    # Create the Non-HOV Volume widget to display the calculated value
    Non_HOV_Vol_peak_modelcalc_widget = widgets.IntText(
        value=0,  # Set initial value to 0, or any other valid integer
        description="Non-HOV Volume (Calculated by Model):",
        disabled=True,  # Make it read-only so the user cannot modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Create the Non-HOV Volume Peak Period widget for user-modified value
    Non_HOV_Vol_peak_userchanged_widget = widgets.IntText(
        value=0,  # Initially set to 0 or a valid integer value
        description="Non-HOV Volume(Changed by User):",
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )
    
    PNV1NB_widget = widgets.IntText(
        value=Non_HOV_Vol_peak_modelcalc_widget.value,  # Set initially to the calculated value
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
    def update_Non_HOV_Volume(change):
        # Access the necessary widget values from projectinfo_widgets


        # Check for "Hwy-Rail" subcategory
        if ProjType == "Hwy-Rail Grade Crossing":
            Non_HOV_Volume_Peak_Model = 0
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
        Non_HOV_Volume_Peak_Model = (PerPeakADT * ADT1NB) * (1 - traffic_factor) * TMS_value - HOVvolNB * PeakLngthNB
    
        # Update the Non-HOV Volume Peak Period widget
        Non_HOV_Vol_peak_modelcalc_widget.value = round(Non_HOV_Volume_Peak_Model, 0)

    # Attach observers to the relevant widgets to update the Non-HOV Volume widget dynamically
    projectinfo_widgets.adt_base_year_no_build_widget.observe(update_Non_HOV_Volume, names='value')
    projectinfo_widgets.percent_traffic_weave_no_build_widget.observe(update_Non_HOV_Volume, names='value')
    projectinfo_widgets.percent_trucks_nobuild_widget.observe(update_Non_HOV_Volume, names='value')
    projectinfo_widgets.HOV_lane_nobuild_widget.observe(update_Non_HOV_Volume, names='value')
    projectinfo_widgets.peak_period_widget.observe(update_Non_HOV_Volume, names='value')
    projectinfo_widgets.subcategory_dropdown.observe(update_Non_HOV_Volume, names='value')


        
    # Non-HOV PNV1NB update function (similar to PHV1NB)
    def calculate_pnv1nb(change):
        # Access the user-modified value directly from the widget
        if isinstance(Non_HOV_Vol_peak_userchanged_widget.value, (int, float)) and Non_HOV_Vol_peak_userchanged_widget.value >= 0:
            PNV1NB = Non_HOV_Vol_peak_userchanged_widget.value  # Use the user-modified value if valid
        else:
            PNV1NB = Non_HOV_Vol_peak_modelcalc_widget.value  # Use the model value if the user value is invalid

        # Update the value of PNV1NB widget
        PNV1NB_widget.value = PNV1NB

    # Link the PNV1NB widget update to changes in Non-HOV Volume Peak User widget
    Non_HOV_Vol_peak_userchanged_widget.observe(calculate_pnv1nb, names='value')

    # Combine all the Non-HOV volume widgets into a horizontal layout for display
    Non_HOV_vol_peak_widgets = widgets.HBox([Non_HOV_Vol_peak_modelcalc_widget, Non_HOV_Vol_peak_userchanged_widget, PNV1NB_explanation_widget])        
    
    
    # Weaving Volume (Calculated by Model)
    weaving_volume_modelcalc_widget = widgets.IntText(
        value=0,  # Set initial value to 0 or any other valid integer
        description="Weaving Volume (Calculated by Model):",
        disabled=True,  # Make it read-only so the user cannot modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Weaving Volume (User-modified value)
    weaving_volume_userchanged_widget = widgets.IntText(
        value=0,  # Initially set to 0 or a valid integer value
        description="Weaving Volume (Changed by User):",
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Weaving Volume (Used for Project Evaluation)
    PWV1NB_widget = widgets.IntText(
        value=weaving_volume_modelcalc_widget.value,  # Set initially to the calculated value
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
        weaving_volume_modelcalc_widget.value = round(Weaving_Volume_Model, 0)  # Correct widget name

    # Link the update function to changes in relevant widgets
    projectinfo_widgets.adt_base_year_no_build_widget.observe(update_weaving_volume, names='value')
    projectinfo_widgets.percent_traffic_weave_no_build_widget.observe(update_weaving_volume, names='value')
    projectinfo_widgets.percent_trucks_nobuild_widget.observe(update_weaving_volume, names='value')
    projectinfo_widgets.hourly_ramp_volume_nobuild_widget.observe(update_weaving_volume, names='value')
    projectinfo_widgets.peak_period_widget.observe(update_weaving_volume, names='value')
    projectinfo_widgets.HOV_lane_nobuild_widget.observe(update_weaving_volume, names='value')
    projectinfo_widgets.subcategory_dropdown.observe(update_weaving_volume, names='value')

    # Function to update PWV1NB widget when user modifies the value
    def calculate_pwv1nb(change):
        # Access the user-modified value directly from the widget
        if isinstance(weaving_volume_userchanged_widget.value, (int, float)) and weaving_volume_userchanged_widget.value >= 0:
            PWV1NB = weaving_volume_userchanged_widget.value  # Use the user-modified value if valid
        else:
            PWV1NB = weaving_volume_modelcalc_widget.value  # Use the model value if the user value is invalid

        # Update the value of PWV1NB widget
        PWV1NB_widget.value = PWV1NB

    # Link the PWV1NB widget update to changes in Weaving Volume User widget
    weaving_volume_userchanged_widget.observe(calculate_pwv1nb, names='value')

    # Combine all the Weaving Volume widgets into a horizontal layout for display
    Weaving_Volume_widgets = widgets.HBox([weaving_volume_modelcalc_widget, weaving_volume_userchanged_widget, PWV1NB_explanation_widget])    

    # Truck Volume (Calculated by Model)
    truck_volume_modelcalc_widget = widgets.IntText(
        value=0,  # Set initial value to 0 or any other valid integer
        description="Truck Volume (Calculated by Model):",
        disabled=True,  # Make it read-only so the user cannot modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Truck Volume (User-modified value)
    truck_volume_userchanged_widget = widgets.IntText(
        value=0,  # Initially set to 0 or a valid integer value
        description="Truck Volume (Changed by User):",
        disabled=False,  # Allow the user to modify the value
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Truck Volume (Used for Project Evaluation)
    PTV1NB_widget = widgets.IntText(
        value=truck_volume_modelcalc_widget.value,  # Set initially to the calculated value
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
        truck_volume_modelcalc_widget.value = round(Truck_Volume_Model, 0)  # Correct widget name

    # Link the update function to changes in relevant widgets
    projectinfo_widgets.adt_base_year_no_build_widget.observe(update_truck_volume, names='value')
    projectinfo_widgets.percent_trucks_nobuild_widget.observe(update_truck_volume, names='value')
    projectinfo_widgets.subcategory_dropdown.observe(update_truck_volume, names='value')

    # Function to update PTV1NB widget when user modifies the value
    def calculate_ptv1nb(change):
        # Access the user-modified value directly from the widget
        if isinstance(truck_volume_userchanged_widget.value, (int, float)) and truck_volume_userchanged_widget.value >= 0:
            PTV1NB = truck_volume_userchanged_widget.value  # Use the user-modified value if valid
        else:
            PTV1NB = truck_volume_modelcalc_widget.value  # Use the model value if the user value is invalid

        # Update the value of PTV1NB widget
        PTV1NB_widget.value = PTV1NB

    # Link the PTV1NB widget update to changes in Truck Volume User widget
    truck_volume_userchanged_widget.observe(calculate_ptv1nb, names='value')

    # Combine all the Truck Volume widgets into a horizontal layout for display
    Truck_Volume_widgets = widgets.HBox([truck_volume_modelcalc_widget, truck_volume_userchanged_widget, PTV1NB_explanation_widget])
    
    
        
    # Highway Speed and Volume Inputs Section
    highway_speed_and_volume_input_section = create_section(
        highway_speed_and_volume_input_title,
        highway_speed_and_volume_input_subtitle,
        [HOV_vol_peak_widgets, Non_HOV_vol_peak_widgets, Weaving_Volume_widgets],
        highway_speed_and_volume_input_info
    )

    # Non-HOV Volume Widget
    
    
    all_sections = widgets.VBox([highway_speed_and_volume_input_section])
    
    display(all_sections)
    
    
    
    
    
    