import ipywidgets as widgets
from ipywidgets import Widget
from ipywidgets import interactive
from IPython.display import display, Markdown
from parameters import parameters
params = parameters()

from widgets_helper import (highway_speed_and_volume_input_nobuild_title, highway_speed_and_volume_input_nobuild_subtitle, highway_speed_and_volume_input_info, highway_speed_and_volume_input_build_title, highway_speed_and_volume_input_build_subtitle
)

import projectinfo_widgets
project_inputs = projectinfo_widgets.create_project_info_widgets()

from widgets_helper import info_button_popup, create_section, create_section_with_subsections

common_layout = widgets.Layout(
    width='450px', 
    background_color='#CCFFCC',  # Background color for all widgets
    padding='2px',
    border='2px solid gray'  # Border color and thickness
)


# Now reference the widgets from the dictionary
ProjLoc = project_inputs["ProjLoc"].value
ProjType = project_inputs["ProjSubType"].value
Construct = project_inputs["Construct"].value
NumDirections = project_inputs["NumDirections"].value
PeakLngthNB = project_inputs["PeakLngthNB"].value
RoadTypeNB = project_inputs["RoadTypeNB"].value
RoadTypeB = project_inputs["RoadTypeB"].value
GenLanesNB = project_inputs["GenLanesNB"].value
GenLanesB = project_inputs["GenLanesB"].value
HOVLanesNB = project_inputs["HOVLanesNB"].value
HOVLanesB = project_inputs["HOVLanesB"].value
HOVRest = project_inputs["HOVRest"].value
Exclusive = project_inputs["Exclusive"].value
FFSpeedNB = project_inputs["FFSpeedNB"].value
FFSpeedB = project_inputs["FFSpeedB"].value
RampFFSpdNB = project_inputs["RampFFSpdNB"].value
RampFFSpdB = project_inputs["RampFFSpdB"].value
SegmentNB = project_inputs["SegmentNB"].value
SegmentB = project_inputs["SegmentB"].value
ImpactedNB = project_inputs["ImpactedNB"].value
ImpactedB = project_inputs["ImpactedB"].value
ADT0 = project_inputs["ADT0"].value
ADT1NB = project_inputs["ADT1NB"].value
ADT1B = project_inputs["ADT1B"].value
ADT20NB = project_inputs["ADT20NB"].value
ADT20B = project_inputs["ADT20B"].value
HOVvolNB = project_inputs["HOVvolNB"].value
HOVvolB = project_inputs["HOVvolB"].value
PerWeaveNB = project_inputs["PerWeaveNB"].value
PerWeaveB = project_inputs["PerWeaveB"].value
PerIndHOV = project_inputs["PerIndHOV"].value
PerTruckNB = project_inputs["PerTruckNB"].value
PerTruckB = project_inputs["PerTruckB"].value
TruckSpeed = project_inputs["TruckSpeed"].value
RampVolP = project_inputs["RampVolP"].value
RampVolNP = project_inputs["RampVolNP"].value
MeterStrat = project_inputs["MeterStrat"].value
ArrRate1 = project_inputs["ArrRate1"].value
ArrRate20 = project_inputs["ArrRate20"].value
DepRate1 = project_inputs["DepRate1"].value
DepRate20 = project_inputs["DepRate20"].value
IRI1NB = project_inputs["IRI1NB"].value
IRI1B = project_inputs["IRI1B"].value
IRI20NB = project_inputs["IRI20NB"].value
IRI20B = project_inputs["IRI20B"].value
AVONonNB = project_inputs["AVONonNB"].value
AVONonB = project_inputs["AVONonB"].value
AVOPeakNB = project_inputs["AVOPeakNB"].value
AVOPeakB = project_inputs["AVOPeakB"].value
AVOHovNB = project_inputs["AVOHovNB"].value
AVOHovB = project_inputs["AVOHovB"].value
GateTime1 = project_inputs["GateTime1"].value
GateTime20 = project_inputs["GateTime20"].value
NumTrain1 = project_inputs["NumTrain1"].value
NumTrain20 = project_inputs["NumTrain20"].value
TPerPeak = project_inputs["TPerPeak"].value
TPerHwy = project_inputs["TPerHwy"].value
TAPT1B = project_inputs["TAPT1B"].value
TAPT1NB = project_inputs["TAPT1NB"].value
TAPT20NB = project_inputs["TAPT20NB"].value
TAPT20B = project_inputs["TAPT20B"].value
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
    project_inputs["ProjType"].observe(update_HOV_Year1Peak_Volume, names='value')
    project_inputs["HOVLaneNB"].observe(update_HOV_Year1Peak_Volume, names='value')
    project_inputs["PeakLngthNB"].observe(update_HOV_Year1Peak_Volume, names='value')
    project_inputs["PerWeaveNB"].observe(update_HOV_Year1Peak_Volume, names='value')
    HOV_Vol_year1peak_modelcalc_widget.observe(calculate_phv1nb, names='value')
    HOV_Vol_year1peak_userchanged_widget.observe(calculate_phv1nb, names='value')
    
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
    
    def update_hov_year1peak_speed(change=None):
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

    update_hov_year1peak_speed()  # Initial HOV speed calculation
    
    #Adding Observers
    # List of widget keys that need to trigger the update function
    widgets_to_observe = [
        "PHV1NB_widget",
        "PNS1NB_widget",
        "subcategory_dropdown",
        "impacted_length_no_build_widget",
        "peak_period_widget",
        "departure_rate_forecast_year_no_build_widget",
        "arrival_rate_base_year_no_build_widget",
        "adt_base_year_no_build_widget",
        "percent_induced_trip_widget",
        "hov_hot_lanes_no_build_widget",
        "free_flow_speed_no_build_widget",
        "iri_base_year_no_build_widget"
    ]

    # Attach observers for all widgets in the list
    for widget_key in widgets_to_observe:
        project_inputs[widget_key].observe(update_hov_year1peak_speed, names='value')
    
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

    ###################################################################    
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
# List of widget keys that need to trigger the update function
    widgets_to_observe = [
        "PWV1NB_widget",
        "PNS1NB_widget",
        "PTV1NB_widget",
        "subcategory_dropdown",
        "impacted_length_no_build_widget",
        "peak_period_widget",
        "departure_rate_forecast_year_no_build_widget",
        "arrival_rate_base_year_no_build_widget",
        "adt_base_year_no_build_widget",
        "percent_induced_trip_widget",
        "hov_hot_lanes_no_build_widget",
        "free_flow_speed_no_build_widget",
        "iri_base_year_no_build_widget"
    ]

    # Attach the observer for all widgets in the list
    for widget_key in widgets_to_observe:
        project_inputs[widget_key].observe(update_weaving_year1peak_speed, names='value')
    
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
    
    ###################################################################    
    
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
# List of widget keys that need to trigger the update function
    widgets_to_observe_truck_speed = [
        "PTV1NB_widget",
        "PWS1NB_widget",
        "PNS1NB_widget",
        "truck_speed_widget",  # Assuming this is defined in project_inputs
        "subcategory_dropdown",  # Assuming this is defined in project_inputs
        "iri_base_year_no_build_widget"  # Assuming this is defined in project_inputs
    ]

    # Attach the observer for all widgets in the list
    for widget_key in widgets_to_observe_truck_speed:
        project_inputs[widget_key].observe(update_truck_speed, names='value')
        
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
    
    
 # Highway Speed and Volume Inputs Section
    
    highway_subsections_nobuild = [
        {
            'subtitle': 'Year 1 - Peak Period',
            'widgets': [HOV_vol_year1peak_widgets, Non_HOV_vol_year1peak_widgets, Weaving_Volume_year1peak_widgets, Truck_Volume_year1peak_widgets, HOV_Speed_Volume_widgets, NonHOV_Year1Peak_Volume_widgets, Weave_Speed_Year1Peak_widgets, Truck_Speed_Year1Peak_widgets],
            'info_texts': highway_speed_and_volume_input_info[:8]  # Use the first 8 info items for Year 1 Peak
        }
    ]
    
    
    
    highway_speed_and_volume_input_nobuild_section = create_section_with_subsections(
        highway_speed_and_volume_input_nobuild_title,
        highway_speed_and_volume_input_nobuild_subtitle,
        subsections=highway_subsections_nobuild
    )
        

  

    # Non-HOV Volume Widget
    
    
    all_sections = widgets.VBox([highway_speed_and_volume_input_nobuild_section])
    
    display(all_sections)