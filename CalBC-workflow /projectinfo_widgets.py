import ipywidgets as widgets
from ipywidgets import Widget
from ipywidgets import interactive
from IPython.display import display, Markdown
from parameters import parameters
params = parameters()

from widgets_helper import (
    project_info_title, project_info_subtitle, project_info_info,
    highway_design_and_traffic_data_title, highway_design_and_traffic_data_subtitle, highway_design_and_traffic_data_info,
    pavement_condition_title, pavement_condition_subtitle, pavement_condition_info,
    avo_section_title, avo_section_subtitle, avo_section_info,
    on_ramp_volume_title, on_ramp_volume_subtitle, on_ramp_volume_info,
    queue_formation_title, queue_formation_subtitle, queue_formation_info,
    actual_3years_crash_title, actual_3years_crash_subtitle, actual_3years_crash_info,
    statewide_avg_crash_title, statewide_avg_crash_subtitle, statewide_avg_crash_info,
    rail_and_transit_data_title, rail_and_transit_data_subtitle, rail_and_transit_data_info
)

from widgets_helper import info_button_popup, create_section

# Define project types and subtypes
ProjType = [
    "Highway Capacity Expansion",
    "Rail or Transit Cap Expansion",
    "Hwy Operational Improvement",
    "Transp Mgmt Systems (TMS)"
]

# Define subcategories for each project type
highway_subtypes = [
    "General Highway", "HOV Lane Addition", "HOT Lane Addition", "Passing Lane", 
    "Intersection", "Truck Only Lane", "Bypass", "Queuing", "Pavement"
]

rail_transit_subtypes = [
    "Passenger Rail", "Light-Rail (LRT)", "Bus", "Hwy-Rail Grade Crossing"
]

hwy_op_improvement_subtypes = [
    "Auxiliary Lane", "Freeway Connector", "HOV Connector", "HOV Drop Ramp", 
    "Off-Ramp Widening", "On-Ramp Widening", "HOV-2 to HOV-3 Conv", "HOT Lane Conversion"
]

tms_subtypes = [
    "Ramp Metering", "Ramp Metering Signal Coord", "Incident Management", "Traveler Information", 
    "Arterial Signal Management", "Transit Vehicle Location (AVL)", "Transit Vehicle Signal Priority", 
    "Bus Rapid Transit (BRT)"
]

# Function to update the subcategory dropdown based on the project type selected
def update_subcategory(ProjType):
    if ProjType == "Highway Capacity Expansion":
        subcategory_dropdown.options = highway_subtypes
    elif ProjType == "Rail or Transit Cap Expansion":
        subcategory_dropdown.options = rail_transit_subtypes
    elif ProjType == "Hwy Operational Improvement":
        subcategory_dropdown.options = hwy_op_improvement_subtypes
    elif ProjType == "Transp Mgmt Systems (TMS)":
        subcategory_dropdown.options = tms_subtypes

# Function to get user inputs and prepare them for export
def get_inputs():
    widget_values = {}
    for widget_name, widget in globals().items():
        if isinstance(widget, Widget):  # Check if it's a widget
            if hasattr(widget, 'value'):  # Check if the widget has the 'value' attribute
                widget_values[widget_name] = widget.value
    return widget_values


common_layout = widgets.Layout(
    width='500px', 
    background_color='#CCFFCC',  # Background color for all widgets
    padding='2px',
    border='2px solid gray'  # Border color and thickness
)

# Function to create the widgets and display them in the notebook
def create_project_info_widgets():
    global projloc_widget, project_type_dropdown, subcategory_dropdown, construct_widget, one_two_way_widget, peak_period_widget, roadway_type_no_build_widget, roadway_type_build_widget, \
        general_traffic_lanes_no_build_widget, general_traffic_lanes_build_widget, hov_hot_lanes_no_build_widget, hov_hot_lanes_build_widget, HOVRest_widget, Exclusive_widget, free_flow_speed_no_build_widget, \
        free_flow_speed_build_widget, ramp_design_speed_no_build_widget, ramp_design_speed_build_widget, highway_segment_no_build_widget, highway_segment_build_widget, \
        impacted_length_no_build_widget, impacted_length_build_widget, ADT_current_widget, adt_base_year_no_build_widget, adt_base_year_build_widget, ADT_20NB_widget, adt_20_year_build_widget, \
        AVO_traffic_NP_no_build_widget, AVO_traffic_NP_build_widget, AVO_traffic_P_no_build_widget, AVO_traffic_P_build_widget, AVOHovNB_widget, AVOHovB_widget, \
        HOV_lane_nobuild_widget, HOV_lane_build_widget, percent_traffic_weave_no_build_widget, percent_traffic_weave_build_widget, percent_induced_trip_widget, percent_trucks_nobuild_widget, \
        percent_trucks_build_widget, truck_speed_widget, hourly_ramp_volume_peak_widget, hourly_ramp_volume_nonpeak_widget, metering_strategy_widget, arrival_rate_base_year_no_build_widget, \
        arrival_rate_base_year_build_widget, departure_rate_forecast_year_no_build_widget, departure_rate_forecast_year_build_widget, iri_base_year_no_build_widget, \
        iri_base_year_build_widget, iri_forecast_year_no_build_widget, iri_forecast_year_build_widget, actual_3_year_totalcrash_count_widget, \
        actual_3_year_totalcrash_rate_widget, actual_3_year_fatalcrash_count_widget, actual_3_year_fatalcrash_rate_widget, actual_3_year_injurycrash_count_widget, \
        actual_3_year_injurycrash_rate_widget, actual_3_year_pdocrash_count_widget, actual_3_year_pdocrash_rate_widget, state_crash_rate_group_nobuild_widget, \
        state_crash_rate_group_build_widget, crash_rate_permvm_nobuild_widget, crash_rate_permvm_build_widget, percent_fatal_crash_nobuild_widget, \
        percent_fatal_crash_build_widget, percent_injury_crash_nobuild_widget, percent_injury_crash_build_widget, GateTime1_widget, NumTrain1_widget, GateTime20_widget, NumTrain20_widget, TPerPeak_widget, \
        TPerHwy_widget, TAPT1B_widget, TAPT1NB_widget,TAPT20NB_widget,TAPT20B_widget


    
    # Create Project Location widget
    projloc_widget = widgets.Dropdown(
        options=[('So. Cal.', 1), ('No. Cal.', 2), ('Rural', 3)],
        value=1,  # Default value is 1 (So. Cal.)
        description='Project Location:',
        disabled=False,
        layout=common_layout,  # Set width to allow the description to be more visible
        style={'description_width': 'initial'}  # Ensures description text doesn't get cut off
    )

    # Main Project Type dropdown
    project_type_dropdown = widgets.Dropdown(
        options=ProjType,
        description="Select project type from list:",
        layout=common_layout,  # Set width to allow the description to be more visible
        style={'description_width': 'initial'}  # Ensures description text doesn't get cut off
    )

    # Subcategory dropdown (initially empty)
    subcategory_dropdown = widgets.Dropdown(
        description="Subcategory:",
        layout=common_layout,  # Set width to allow the description to be more visible
        style={'description_width': 'initial'}  # Ensures description text doesn't get cut off
    )
    

    # Link project type dropdown to update subcategory dropdown
    widgets.interactive(update_subcategory, ProjType=project_type_dropdown)
    
    # Create Length of Construction Period widget
    construct_widget = widgets.IntText(
        value=None,  
        description="Construct (Years):",
        min=1,  
        step=1,  
        disabled=False,
        layout=common_layout,  # Set width to allow the description to be more visible
        style={'description_width': 'initial'}  # Ensures description text doesn't get cut off
    )    
    
    one_two_way_widget = widgets.Dropdown(
        options=[('One-Way', 1), ('Two-Way', 2)],  # Dropdown options with values 1 and 2
        value=2,  # Default value is One-Way (1)
        description='One- or Two-Way Data: ',  # Full descriptive label
        disabled=False,  # Allow the dropdown to be used
        layout=common_layout,  # Set width to allow the description to be more visible
        style={'description_width': 'initial'}  # Ensures description text doesn't get cut off
    )
    
    def validate_peak_period(change):
        if change['new'] < 1:
            peak_period_widget.value = 1  # Reset to 1 if less than 1
        elif change['new'] > 24:
            peak_period_widget.value = 24  # Reset to 24 if more than 24

    # Create an IntText widget to allow the user to input the length of the peak period(s)
    peak_period_widget = widgets.IntText(
        value=5,  # Default value, assuming 5 hours is the average
        description='Length of Peak Period(s):',  # Full descriptive label
        min=1,  # Minimum value of 1 hour
        max=24,  # Maximum value of 24 hours
        step=1,  # Step size of 1 hour
        style={'description_width': 'initial'},  # Ensure description doesn't get cut off
        layout=common_layout  # Adjust width to accommodate description
    )

    # Attach the observer to the widget to validate input
    peak_period_widget.observe(validate_peak_period, names='value')
    
    # Roadway Type Mapping (Mapping abbreviations to full names in params)
    roadway_type_mapping = {
        'F': 'Freeway',
        'E': 'Expressway',
        'C': 'Conventional Highway'
    }
    
    # Function to update Roadway Type based on selected subcategory
    def update_roadway_type(change):
        subcategory = change['new']  # Get the new subcategory value
        if subcategory == "Hwy-Rail Grade Crossing":
            roadway_type_no_build_widget.value = "C"  # Automatically set to "C" if Hwy-Rail Grade Crossing
            roadway_type_build_widget.value = "C"  # Build should also be set to "C"
        else:
            roadway_type_no_build_widget.value = "F"  # Set default to "F" otherwise
            roadway_type_build_widget.value = "F"  # Build should also default to "F"

    # Roadway Type dropdown for No Build (initially 'F' for Freeway)
    roadway_type_no_build_widget = widgets.Dropdown(
        options=[('Freeway', 'F'), ('Expressway', 'E'), ('Conventional Hwy', 'C')],  # Options with descriptions
        value='F',  # Default value is 'F' (Freeway)
        description='Roadway Type No Build:',
        disabled=False,
        style={'description_width': 'initial'},  # Ensure the description is not cut off
        layout=common_layout  # Adjust width to accommodate description
    )

    # Roadway Type dropdown for Build (initially 'F' for Freeway)
    roadway_type_build_widget = widgets.Dropdown(
        options=[('Freeway', 'F'), ('Expressway', 'E'), ('Conventional Hwy', 'C')],  # Options with descriptions
        value='F',  # Default value is 'F' (Freeway)
        description='Roadway Type Build:',
        disabled=False,
        style={'description_width': 'initial'},  # Ensure the description is not cut off
        layout=common_layout  # Adjust width to accommodate description
    )

    # Combine both "No Build" and "Build" dropdowns into a horizontal layout
    roadway_type_widgets = widgets.HBox([roadway_type_no_build_widget, roadway_type_build_widget])

    # Link the subcategory dropdown to update the roadway type based on the selected subcategory
    subcategory_dropdown.observe(update_roadway_type, names='value')  # Trigger update on subcategory change

    
    # Number of General Traffic Lanes for No Build (initially 2)
    general_traffic_lanes_no_build_widget = widgets.IntText(
        description='Number of General Traffic Lanes ( No Build):',
        disabled=False,
        style={'description_width': 'initial'},  # Ensure the description is not cut off
        layout=common_layout  # Adjust width to accommodate description
    )

    # Number of General Traffic Lanes for Build (initially 2)
    general_traffic_lanes_build_widget = widgets.IntText(
        description='Number of General Traffic Lanes (Build):',
        disabled=False,
        style={'description_width': 'initial'},  # Ensure the description is not cut off
        layout=common_layout  # Adjust width to accommodate description
    )

    # Combine both "No Build" and "Build" number input fields into a horizontal layout
    general_traffic_lanes_widgets = widgets.HBox([general_traffic_lanes_no_build_widget, general_traffic_lanes_build_widget])
    
    hov_hot_lanes_no_build_widget = widgets.IntText(
        description='Number of HOV/HOT Lanes (No Build):',
        disabled=False,
        style={'description_width': 'initial'},  # Ensure the description is not cut off
        layout=common_layout  # Adjust width to accommodate description
    )

    # Number of HOV/HOT Lanes for Build (initially 1)
    hov_hot_lanes_build_widget = widgets.IntText(
        description='Number of HOV/HOT Lanes (Build):',
        disabled=False,
        style={'description_width': 'initial'},  # Ensure the description is not cut off
        layout=common_layout  # Adjust width to accommodate description
    )

    # Combine both "No Build" and "Build" number input fields into a horizontal layout
    hov_hot_lanes_widgets = widgets.HBox([hov_hot_lanes_no_build_widget, hov_hot_lanes_build_widget])
    
    HOVRest_widget = widgets.IntText(
        description="HOV Restriction (people per vehicle):",
        step=1,  # Step by 1 year
        disabled=False,
        layout=common_layout,  # Set width to allow the description to be more visible
        style={'description_width': 'initial'}  # Ensures description text doesn't get cut off
    )    

    Exclusive_widget = widgets.Dropdown(
        options=[('Yes', 'Y'), ('No', 'N')],  # Options for Yes or No
        value='N',  # Default value is 'No' (N)
        description='Exclusive ROW for Buses: ',  # Descriptive label
        disabled=False,  # Allow the dropdown to be used
        layout=common_layout,  # Set width to allow the description to be more visible
        style={'description_width': 'initial'}  # Ensure the description width is not cut off
    )
    

    free_flow_speed_no_build_widget = widgets.IntText(
        description='Highway Free-Flow Speed (No Build):',
        value=None,  # Default is None (blank)
        disabled=False,
        style={'description_width': 'initial'},
        layout=common_layout  # Adjust width to accommodate description
    )

    # Highway Free-Flow Speed for Build (initially mirrors No Build)
    free_flow_speed_build_widget = widgets.IntText(
        description='Highway Free-Flow Speed (Build):',
        value=None,  # Default is None (blank)
        disabled=False,
        style={'description_width': 'initial'},
        layout=common_layout  # Adjust width to accommodate description
    )

    # Function to update Build field when No Build field is changed
    def sync_build_value(change):
        # If No Build value is changed, set Build to the same value
        if free_flow_speed_no_build_widget.value is not None:
            free_flow_speed_build_widget.value = free_flow_speed_no_build_widget.value

    # Link the No Build widget to update Build widget
    free_flow_speed_no_build_widget.observe(sync_build_value, names='value')

    # Combine both "No Build" and "Build" input fields into a horizontal layout
    free_flow_speed_widgets = widgets.HBox([free_flow_speed_no_build_widget, free_flow_speed_build_widget])
    


    # Ramp Design Speed for No Build (initially 35 mph, can be changed)
    ramp_design_speed_no_build_widget = widgets.IntText(
        description='Ramp Design Speed (No Build):',
        value=35,  # Default value is 35 mph
        disabled=False,
        style={'description_width': 'initial'},
        layout=common_layout  # Adjust width to accommodate description
    )

    # Ramp Design Speed for Build (initially mirrors No Build)
    ramp_design_speed_build_widget = widgets.IntText(
        description='Ramp Design Speed (Build):',
        value=35,  # Default value is 35 mph
        disabled=False,
        style={'description_width': 'initial'},
        layout=common_layout  # Adjust width to accommodate description
    )

    # Function to sync the Build field with No Build field
    def sync_ramp_design_speed_build(change):
        # If No Build value is changed, set Build to the same value
        if ramp_design_speed_no_build_widget.value is not None:
            ramp_design_speed_build_widget.value = ramp_design_speed_no_build_widget.value

    # Link the No Build widget to update Build widget
    ramp_design_speed_no_build_widget.observe(sync_ramp_design_speed_build, names='value')

    # Combine both "No Build" and "Build" input fields into a horizontal layout
    ramp_design_speed_widgets = widgets.HBox([ramp_design_speed_no_build_widget, ramp_design_speed_build_widget])

    
    # Highway Segment No Build widget (initially empty)
    highway_segment_no_build_widget = widgets.FloatText(
        description='Highway Segment (No Build):',
        value=None,  # Default is None (blank)
        disabled=False,
        style={'description_width': 'initial'},
        layout=common_layout  # Adjust width to accommodate description
    )

    # Highway Segment Build widget (initially mirrors No Build)
    highway_segment_build_widget = widgets.FloatText(
        description='Highway Segment (Build):',
        value=None,  # Default is None (blank)
        disabled=False,
        style={'description_width': 'initial'},
        layout=common_layout,  # Adjust width to accommodate description
        readout_format='.1f'  # Ensures the value displays with 1 decimal point
    )

    # Function to update Build field when No Build field is changed
    def sync_build_value(change):
        # If No Build value is changed and not None, set Build to the same value
        if highway_segment_no_build_widget.value is not None:
            highway_segment_build_widget.value = highway_segment_no_build_widget.value
        # If No Build is 0, set Build to 0.0
        elif highway_segment_no_build_widget.value == 0:
            highway_segment_build_widget.value = 0.0

    # Link the No Build widget to update Build widget
    highway_segment_no_build_widget.observe(sync_build_value, names='value')

    # Combine both "No Build" and "Build" input fields into a horizontal layout
    highway_segment_widgets = widgets.HBox([highway_segment_no_build_widget, highway_segment_build_widget])
    
    def calculate_impacted_length(change):
        # Get current values
        highway_segment_no_build = highway_segment_no_build_widget.value
        subcategory = subcategory_dropdown.value

        # Initialize impacted length no build to the No Build value
        impacted_length_no_build = highway_segment_no_build

        # Check the subcategory and calculate Impacted Length (No Build)
        if subcategory == "Auxiliary Lane" or subcategory == "Off-Ramp Widening":
            impacted_length_no_build = 1500 / 5280  # Add 1500 feet (converted to miles)
        elif subcategory == "Freeway Connector" or subcategory == "HOV Connector" or subcategory == "HOV Drop Ramp":
            impacted_length_no_build = 3250 / 5280  # Add 3250 feet (converted to miles)
        elif subcategory == "Passing Lane":
            impacted_length_no_build += 3  # Add 3 miles if Passing Lane is selected
        else:
            # For all other cases, keep the Highway Segment No Build value
            impacted_length_no_build = highway_segment_no_build

        # Update the Impacted Length (No Build) widget value
        impacted_length_no_build_widget.value = round(impacted_length_no_build, 0)  # Round to 1 decimal place

        # Set the Build value to be the same as No Build
        impacted_length_build_widget.value = impacted_length_no_build

    # Link the Highway Segment No Build widget, Subcategory dropdown to the calculation
    highway_segment_no_build_widget.observe(calculate_impacted_length, names='value')
    subcategory_dropdown.observe(calculate_impacted_length, names='value')

        # Define Impacted Length No Build widget
    impacted_length_no_build_widget = widgets.FloatText(
        description='Impacted Length (No Build):',
        value=0.0,  # Default value set to 0.0
        disabled=False,
        style={'description_width': 'initial'},
        layout=common_layout
    )

    # Define Impacted Length Build widget
    impacted_length_build_widget = widgets.FloatText(
        description='Impacted Length (Build):',
        value=None,  # Default is None (blank)
        disabled=False,
        style={'description_width': 'initial'},
        layout=common_layout,
        readout_format='.1f'  # Ensures the value displays with 1 decimal point
    )
    
    
    # Combine both "No Build" and "Build" input fields into a horizontal layout
    impacted_length_widgets = widgets.HBox([impacted_length_no_build_widget, impacted_length_build_widget])
    
    ADT_current_widget = widgets.IntText(
        description="Current Average Daily Traffic:",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # ADT in 20 Years (No Build) widget (changed to ADT_20NB_widget)
    ADT_20NB_widget = widgets.IntText(
        description="ADT Year 20 (No Build):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )


    # ADT Base Year No Build widget (calculated)
    adt_base_year_no_build_widget = widgets.FloatText(
        description="ADT Base Year (No Build):",
        value=None,  # Initially empty
        disabled=False,  # Read-only since it will be calculated
        style={'description_width': 'initial'},
        layout=common_layout
    )

    # ADT Base Year Build widget (calculated)
    adt_base_year_build_widget = widgets.FloatText(
        description="ADT Base Year (Build):",
        value=None,  # Initially empty
        disabled=False,  # Read-only since it will be calculated
        style={'description_width': 'initial'},
        layout=common_layout
    )

    # ADT 20 Year Build widget (calculated based on Truck Lane selection)
    adt_20_year_build_widget = widgets.FloatText(
        description="ADT Year 20 (Build):",
        value=None,  # Initially empty
        disabled=False,  # Read-only since it will be calculated
        style={'description_width': 'initial'},
        layout=common_layout
    )

    # Function to calculate ADT Base Year (No Build), ADT Base Year (Build), and ADT 20 Year Build
    def calculate_adt_base_year(change):
        # Get the current values from the widgets
        ADT_current = ADT_current_widget.value
        ADT_20NB = ADT_20NB_widget.value  # ADT in 20 years (No Build)
        construct_years = construct_widget.value
        subcategory = subcategory_dropdown.value  # Get selected subcategory

        # Check if "Truck Only Lane" is selected in the subcategory dropdown
        truck_only_lane_selected = (subcategory == "Truck Only Lane")

        # Calculate ADT Base Year (No Build)
        adt_base_year_no_build = ADT_current + (ADT_20NB - ADT_current) * (construct_years / (construct_years + 19))

        # If the user hasn't input any value, let the formula calculate and display it
        if ADT_current == 0 or ADT_20NB == 0:
            adt_base_year_no_build_widget.value = adt_base_year_no_build
        elif adt_base_year_no_build_widget.value == 0:  # If user hasn't entered a custom value, set calculated value
            adt_base_year_no_build_widget.value = adt_base_year_no_build

        # Formula for ADT Base Year (Build)
        ADT1NB = adt_base_year_no_build_widget.value  # ADT Base Year No Build value

        if ADT_20NB == 0:
            adt_base_year_build = 0
        else:
            adt_base_year_build = (ADT_20NB / ADT_20NB) * ADT1NB  # Using ADT1NB as ADT Base Year No Build

        if ADT_20NB == 0:
            adt_base_year_build_widget.value = adt_base_year_build
        else:
            adt_base_year_build_widget.value = adt_base_year_build  # Set to calculated value

        # Formula for ADT 20 Year Build (adjusted based on Truck Only Lane)
        if truck_only_lane_selected:
            ADT_20B = ADT_20NB * (1 - 0.10)  # Example: Assuming 10% reduction for trucks
        else:
            ADT_20B = ADT_20NB  # No change to ADT_20B for other subcategories

        if ADT_20NB == 0:
            adt_20_year_build_widget.value = ADT_20B
        else:
            adt_20_year_build_widget.value = ADT_20B  # Set to calculated value

        # Allow user to override calculated value if they input manually
        if adt_base_year_no_build_widget.value != adt_base_year_no_build:
            # If user entered a custom value, allow them to edit it
            adt_base_year_no_build_widget.disabled = False

        if adt_base_year_build_widget.value != adt_base_year_build:
            # If user entered a custom value, allow them to edit it
            adt_base_year_build_widget.disabled = False

        if adt_20_year_build_widget.value != ADT_20B:
            # If user entered a custom value, allow them to edit it
            adt_20_year_build_widget.disabled = False

    # Link the widgets to the calculate function
    ADT_current_widget.observe(calculate_adt_base_year, names='value')
    ADT_20NB_widget.observe(calculate_adt_base_year, names='value')
    construct_widget.observe(calculate_adt_base_year, names='value')
    subcategory_dropdown.observe(calculate_adt_base_year, names='value')



    # Combine both "No Build" and "Build" input fields into a horizontal layout
    adt_base_widgets = widgets.HBox([adt_base_year_no_build_widget, adt_base_year_build_widget])
    adt_20_widget = widgets.HBox([ADT_20NB_widget, adt_20_year_build_widget])
    
    # Define AVOHov widgets
    AVO_traffic_NP_no_build_widget = widgets.FloatText(
        description="General Traffic Non-Peak (No Build):",
        value=1.30,
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )  
    
    AVO_traffic_NP_build_widget = widgets.FloatText(
        description="General Traffic Non-Peak (Build):",
        value=AVO_traffic_NP_no_build_widget.value,
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    ) 
    
    AVO_traffic_P_no_build_widget = widgets.FloatText(
        description="General Traffic Peak (No Build):",
        value=1.15,
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )
    
    AVO_traffic_P_build_widget = widgets.FloatText(
        description="General Traffic Peak (Build):",
        value=AVO_traffic_P_no_build_widget.value,
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )     
    
    def calculate_avo_traffic_peak_build(change=None):
        # Get the current values from the widgets
        HOV2to3_selected = (subcategory_dropdown.value == "HOV-2 to HOV-3 Conv")
        AVOPeakNB = AVO_traffic_P_no_build_widget.value  # Average Traffic Peak (No Build)
        ADT1NB = adt_base_year_no_build_widget.value  # Base Year ADT (No Build)
        ADT20NB = ADT_20NB_widget.value  # 20 Year ADT (No Build)
        PerPeakADT = params.per_peak_adt  # Per Peak ADT
        PerTruckNB = percent_trucks_nobuild_widget.value  # Percent Trucks (No Build)
        HOVvolNB = HOV_lane_nobuild_widget.value  # HOV Volume (No Build)
        PeakLngthNB = peak_period_widget.value  # Peak Length (No Build)
        ADT1B = adt_base_year_build_widget.value  # Base Year ADT (Build)
        ADT20B = adt_20_year_build_widget.value  # 20 Year ADT (Build)
        PerTruckB = percent_trucks_build_widget.value  # Percent Trucks (Build)
        HOVvolB = HOV_lane_build_widget.value  # HOV Volume (Build)
        
        # Calculate Average Traffic Peak (Build) based on the formula
        if HOV2to3_selected:  # If "HOV-2 to HOV-3 Conv" is selected
            avo_traffic_peak_build = (
                AVOPeakNB * (( (ADT1NB + ADT20NB) / 2 ) * (PerPeakADT * (1 - PerTruckNB)) - HOVvolNB * PeakLngthNB)
                + 2 * (HOVvolNB - HOVvolB) * PeakLngthNB
            ) / (( (ADT1B + ADT20B) / 2 ) * (PerPeakADT * (1 - PerTruckB)) - HOVvolB * PeakLngthNB)
        else:  # If not "HOV-2 to HOV-3 Conv", use AVOPeakNB
            avo_traffic_peak_build = AVOPeakNB

        # Update AVO_traffic_P_build_widget with the calculated value
        AVO_traffic_P_build_widget.value = avo_traffic_peak_build

    # Link the function to the subcategory dropdown change
    subcategory_dropdown.observe(calculate_avo_traffic_peak_build, names='value')
    adt_base_year_no_build_widget.observe(calculate_avo_traffic_peak_build, names='value')  
    ADT_20NB_widget.observe(calculate_avo_traffic_peak_build, names='value')  
    
    AVOHovNB_widget = widgets.FloatText(
        description="High Occupancy Vehicle (if HOV/HOT lanes) (No Build):",
        value=2.15,  # Initially empty
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )    
    

    AVOHovB_widget = widgets.FloatText(
        description="High Occupancy Vehicle (if HOV/HOT lanes) (Build):",
        value=AVOHovNB_widget.value,  # Default value set to 2.15
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )
    
    def calculate_avo_hov_build(change=None):
        HOV2to3_selected = (subcategory_dropdown.value == "HOV-2 to HOV-3 Conv")
        HOT_selected = (subcategory_dropdown.value == "HOT Lane Addition")
        HOTConv_selected = (subcategory_dropdown.value == "HOT Lane Conversion")
        AVOHovNB = AVOHovNB_widget.value  # Average Vehicle Occupancy HOV (No Build)
        
        #Calculate Average Vehicle Occupancy for High Occupancy Vehicle (Build) based on the formula 
        if HOV2to3_selected: 
            avo_hov_build = 3.15
        elif HOT_selected or HOTConv_selected:
            avo_hov_build = "0"  # Set to empty string if either HOT Lane Addition or HOT Lane Conversion is selected
        else:
            avo_hov_build = AVOHovNB  # Otherwise, use the value from AVOHovNB_widget
            
        AVOHovB_widget.value = avo_hov_build
    
    subcategory_dropdown.observe(calculate_avo_hov_build, names='value')  # Observe changes in subcategory
        
    AVO_GenTraffic_NonPeak_widgets = widgets.HBox([AVO_traffic_NP_no_build_widget, AVO_traffic_NP_build_widget])
    AVO_GenTraffic_Peak_widgets = widgets.HBox([AVO_traffic_P_no_build_widget, AVO_traffic_P_build_widget])
    AVO_HOV_widgets = widgets.HBox([AVOHovNB_widget, AVOHovB_widget])
    
    
    # Define other widgets
    HOV_lane_nobuild_widget = widgets.IntText(
        description="Average Hourly HOV/HOT Lane Traffic (No Build):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    HOV_lane_build_widget = widgets.IntText(
        description="Average Hourly HOV/HOT Lane Traffic (Build):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )
        
    def calculate_hov_hot_traffic(change=None):
        # Get the current values from the widgets
        HOV2to3_selected = (subcategory_dropdown.value == "HOV-2 to HOV-3 Conv")  # Check if "HOV-2 to HOV-3 Conv" is selected
        AVOHovNB = AVOHovNB_widget.value  # Average Vehicle Occupancy HOV (No Build)
        HOVvolNB = HOV_lane_nobuild_widget.value  # Average Hourly HOV/HOT Lane Traffic (No Build)
        HOVvolB = HOV_lane_build_widget.value  # Average Hourly HOV/HOT Lane Traffic (Build)
        AVOHovB = AVOHovB_widget.value  # Average Vehicle Occupancy HOV (Build)


        # Calculate Average Hourly HOV/HOT Lane Traffic based on the formula
        if HOV2to3_selected:  # If "HOV-2 to HOV-3 Conv" is selected, use the adjusted formula
            hov_hot_traffic = (AVOHovNB - 2) / (AVOHovB - 2) * HOVvolNB  # Corrected formula using AVOHovB
        else:
            hov_hot_traffic = HOVvolNB  # If not "HOV2to3", use the No Build value

        # Update the HOV_lane_build_widget with the calculated value
        HOV_lane_build_widget.value = hov_hot_traffic
        
            
    # Link the widgets to trigger the calculation
    project_type_dropdown.observe(update_subcategory, names='value')  # Observe changes in project type
    HOV_lane_nobuild_widget.observe(calculate_hov_hot_traffic, names='value')  # Observe changes in HOVvolNB
    HOV_lane_build_widget.observe(calculate_hov_hot_traffic, names='value')  # Observe changes in HOVvolB
    AVOHovNB_widget.observe(calculate_hov_hot_traffic, names='value')  # Observe changes in AVOHovNB
    AVOHovB_widget.observe(calculate_hov_hot_traffic, names='value')  # Observe changes in AVOHovB
    subcategory_dropdown.observe(calculate_hov_hot_traffic, names='value')  # Observe changes in subcategory
   
    hourly_hov_lane_traffic_widget = widgets.HBox([HOV_lane_nobuild_widget, HOV_lane_build_widget])    

    
    percent_induced_trip_widget = widgets.IntText(
        description='Percent of Induced Trips in HOV (if HOT or 2-to-3 conv.):',
        value=100,  # Default value is 100%
        disabled=False,
        style={'description_width': 'initial'},
        layout=common_layout  # Adjust width to accommodate description
    )

    # Initially hide the widget by setting it into a VBox and controlling its visibility separately
    percent_induced_trip_container = widgets.VBox([percent_induced_trip_widget])
    percent_induced_trip_container.layout.display = 'none'  # Hide initially

    # Function to show/hide the Percent Induced Trip widget based on subcategory selection
    def show_percent_induced_trip(change):
        subcategory = change['new']  # Get the new subcategory value
        if subcategory in ["HOV-2 to HOV-3 Conv", "HOT Lane Conversion"]:
            percent_induced_trip_container.layout.display = 'flex'  # Show the widget
        else:
            percent_induced_trip_container.layout.display = 'none'  # Hide the widget

    # Observe changes on the subcategory dropdown to trigger the visibility change
    subcategory_dropdown.observe(show_percent_induced_trip, names='value')
    
    
    # Create the "Build" widget for Percent Traffic in Weave
    percent_traffic_weave_build_widget = widgets.FloatText(
        description='Percent Traffic in Weave (Build):',
        value=0.0,  # Default value is 0%
        disabled=False,
        style={'description_width': 'initial'},
        layout=common_layout  # Adjust width to accommodate description
    )

    # Create the "No Build" widget for Percent Traffic in Weave
    percent_traffic_weave_no_build_widget = widgets.FloatText(
        description='Percent Traffic in Weave (No Build):',
        value=0.0,  # Initially 0%, will be calculated
        disabled=False,  
        style={'description_width': 'initial'},
        layout=common_layout  # Adjust width to accommodate description
    )

    # Define the logic for calculating Percent Traffic in Weave (No Build)
    def update_percent_traffic_weave_no_build(subcategory, gen_lanes_nb, num_directions):
        if subcategory == "Auxiliary Lane":
            if gen_lanes_nb < 2 * num_directions:
                percent_traffic_weave_no_build_widget.value = 1
            else:
                percent_traffic_weave_no_build_widget.value = (2 * num_directions) / gen_lanes_nb * 1
        elif subcategory == "Off-Ramp Widening":
            if gen_lanes_nb < 3 * num_directions:
                percent_traffic_weave_no_build_widget.value = 1
            else:
                percent_traffic_weave_no_build_widget.value = (3 * num_directions) / gen_lanes_nb * 100
        elif subcategory == "Freeway Connector":
            percent_traffic_weave_no_build_widget.value = 0.025
        elif subcategory == "HOV Connector" or subcategory == "HOV Drop Ramp":
            percent_traffic_weave_no_build_widget.value = 0.04
        else:
            percent_traffic_weave_no_build_widget.value = 0.0  # Default value if no condition is met

    # Observe changes in widgets that affect the calculation (e.g., subcategory, gen lanes, num directions)
    def update_traffic_weave(change):
        subcategory = subcategory_dropdown.value
        gen_lanes_nb = general_traffic_lanes_no_build_widget.value
        num_directions = one_two_way_widget.value
        update_percent_traffic_weave_no_build(subcategory, gen_lanes_nb, num_directions)

    # Add observers to listen for changes in relevant widgets
    subcategory_dropdown.observe(update_traffic_weave, names='value')
    general_traffic_lanes_no_build_widget.observe(update_traffic_weave, names='value')
    one_two_way_widget.observe(update_traffic_weave, names='value')

    # Keep the widget visible at all times, but set to blank or default if conditions are not met
    percent_traffic_weave_container = widgets.VBox([
        percent_traffic_weave_build_widget,
        percent_traffic_weave_no_build_widget
    ])

    # Function to reset the value of Percent Traffic in Weave (No Build) based on subcategory selection
    def reset_percent_traffic_weave_value(change):
        subcategory = change['new']
        if subcategory not in ["Auxiliary Lane", "Off-Ramp Widening", "Freeway Connector", "HOV Connector", "HOV Drop Ramp"]:
            # Reset to default value (or empty if needed) when the subcategory doesn't match
            percent_traffic_weave_no_build_widget.value = 0.0  # Default or empty value

    # Observe changes to subcategory dropdown to reset value if necessary
    subcategory_dropdown.observe(reset_percent_traffic_weave_value, names='value')
    
    percent_traffic_weave_widgets = widgets.HBox([percent_traffic_weave_no_build_widget, percent_traffic_weave_build_widget])
    
    # Define Percent Trucks (No Build) and Percent Trucks (Build) widgets
    percent_trucks_nobuild_widget = widgets.FloatText(
        description="Percent Trucks (No Build):",
        value=0.09,  # Default value set to 9% (this can be adjusted)
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    percent_trucks_build_widget = widgets.FloatText(
        description="Percent Trucks (Build):",
        value=percent_trucks_nobuild_widget.value,
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Define a function to calculate the Percent Trucks (Build) based on the No Build value and subcategory selection
    def calculate_truck_percentage(change=None):
        # Get the current values from the widgets
        TruckLaneSelected = (subcategory_dropdown.value == "Truck Only Lane")  # Check if "Truck Only Lane" is selected
        PerTruckNB = percent_trucks_nobuild_widget.value  # Percent Trucks (No Build)

        # Calculate Percent Trucks (Build) based on the condition
        if TruckLaneSelected:  # If "Truck Only Lane" is selected, the Build value should be 0%
            percent_trucks_build_widget.value = 0.0
        else:  # Otherwise, set the Build value based on No Build value
            percent_trucks_build_widget.value = PerTruckNB  # Same as No Build for now, can be adjusted if needed

        # Allow user to override the calculated value for Build
        if percent_trucks_build_widget.value != PerTruckNB:
            percent_trucks_build_widget.disabled = False


    # Link the widgets to trigger the calculation
    subcategory_dropdown.observe(calculate_truck_percentage, names='value')  # Observe changes in subcategory
    percent_trucks_nobuild_widget.observe(calculate_truck_percentage, names='value')  # Observe changes in Percent Trucks (No Build)

    # Define the layout for the widgets
    percent_trucks_widget = widgets.HBox([percent_trucks_nobuild_widget, percent_trucks_build_widget])
    
    truck_speed_widget = widgets.FloatText(
        description="Truck Speed:",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    hourly_ramp_volume_peak_widget = widgets.IntText(
        description="Hourly Ramp Volume (Peak):",
        value=0,  # Default value set to 0
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    hourly_ramp_volume_nonpeak_widget = widgets.FloatText(
        description="Hourly Ramp Volume (Non Peak):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )
    
    def calculate_ramp_volume(change=None):
        # Get the current subcategory selection
        AuxLaneSelected = (subcategory_dropdown.value == "Auxiliary Lane")  # Check if "Auxiliary Lane" is selected
        OnRampSelected = (subcategory_dropdown.value == "On-Ramp Widening")  # Check if "On-Ramp Widening" is selected

        # Calculate Hourly Ramp Volume (No Build) based on the selected subcategory
        if AuxLaneSelected:
            hourly_ramp_volume_peak_widget.value = 1350
        elif OnRampSelected:
            hourly_ramp_volume_peak_widget.value = 800
        else:
            hourly_ramp_volume_peak_widget.value = 0  # Default value when no matching subcategory is selected

        # Get the required values from the class instance (params)
        RampVolP = hourly_ramp_volume_peak_widget.value  # Ramp Volume from the No Build widget
        PerPeakAvgHr = params.per_peak_avg_hr  # Per Peak Average Hourly Traffic (from the params instance)
        PerPeakADT = params.per_peak_adt  # Per Peak ADT (from the params instance)
        PeakLngthNB = peak_period_widget.value  # Peak Length (No Build scenario) from the peak_period_widget

        # Calculate Hourly Ramp Volume (Build) using the provided formula
        # Always calculate the Build volume regardless of RampVolP
        build_value = (RampVolP / PerPeakAvgHr) * (1 - PerPeakADT) / (24 - PeakLngthNB)
        
        hourly_ramp_volume_nonpeak_widget.value = round(build_value, 0)

    # Link the widgets to trigger the calculation
    subcategory_dropdown.observe(calculate_ramp_volume, names='value')  # Observe changes in subcategory dropdown
    peak_period_widget.observe(calculate_ramp_volume, names='value')  # Observe changes in Peak Length (No Build)
    hourly_ramp_volume_peak_widget.observe(calculate_ramp_volume, names='value')
    

    # Define the layout for the widgets (assuming common_layout is defined elsewhere)
    hourly_ramp_volume_widget = widgets.HBox([hourly_ramp_volume_peak_widget, hourly_ramp_volume_nonpeak_widget])
    

    # Define the Metering Strategy widget
    metering_strategy_widget = widgets.Dropdown(
        options=[
            ('1 vehicle allowed per green signal', 1),
            ('2 vehicles allowed per green signal', 2),
            ('3 vehicles allowed per green signal', 3),
            ('Dual Metering', 'D')  # 'D' for Dual Metering
        ],
        description='Metering Strategy (For On-Ramp Widening):',
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial', 'background_color': '#CCFFCC'},  # Ensure description fits well
    )

    # Arrival Rate Base Year No Build widget (Year 1)
    arrival_rate_base_year_no_build_widget = widgets.FloatText(
        description="Arrival Rate Base Year (Year 1):",
        value=0,  # Initially empty
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )

    # Arrival Rate Base Year Build widget (calculated)
    arrival_rate_base_year_build_widget = widgets.FloatText(
        description="Arrival Rate Base Year (Year 20):",
        value=0,  # Initially empty
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )

    # Function to calculate Arrival Rate Base Year (No Build) and Base Year Build
    def calculate_arrival_rate(change):
        subcategory = subcategory_dropdown.value  # Get selected subcategory
        ADT1NB = adt_base_year_no_build_widget.value  # ADT Base Year No Build
        ADT20NB = ADT_20NB_widget.value  # ADT Year 20 (No Build)
        ArrRate1 = arrival_rate_base_year_no_build_widget.value  # Arrival Rate Base Year No Build (user input)

        # Save the original value of Arrival Rate Base Year No Build to retain if needed
        original_arrival_rate_no_build = arrival_rate_base_year_no_build_widget.value

        # Calculate Arrival Rate Base Year No Build
        if subcategory == "Hwy-Rail Grade Crossing":  # Check if subcategory is Hwy-Rail Grade Crossing
            arrival_rate_base_year_no_build = ADT1NB / 12  # Formula: ADT1NB / 12
        else:
            arrival_rate_base_year_no_build = 0  # Keep the original value (No Build scenario)

        # Set the Arrival Rate Base Year Build value (no extra logic)
        if subcategory == "Queuing":  # Check if subcategory is Queuing
            arrival_rate_base_year_build = ArrRate1 * ADT20NB / ADT1NB  # Formula: ArrRate1 * ADT20NB / ADT1NB
        elif subcategory == "Hwy-Rail Grade Crossing":  # Check if subcategory is Hwy-Rail Grade Crossing
            arrival_rate_base_year_build = ADT20NB / 12  # Formula: ADT20NB / 12
        else:
            arrival_rate_base_year_build = 0  # Otherwise set to 0 (No Build scenario)

        # Set the values for Arrival Rate widgets
        arrival_rate_base_year_no_build_widget.value = arrival_rate_base_year_no_build
        arrival_rate_base_year_build_widget.value = arrival_rate_base_year_build

    # Link the widgets to the calculate function
    subcategory_dropdown.observe(calculate_arrival_rate, names='value')
    arrival_rate_base_year_no_build_widget.observe(calculate_arrival_rate, names='value')
    ADT_20NB_widget.observe(calculate_arrival_rate, names='value')
    adt_base_year_no_build_widget.observe(calculate_arrival_rate, names='value')


    # Combine both "No Build" and "Build" input fields into a horizontal layout
    arrival_rate_widgets = widgets.HBox([arrival_rate_base_year_no_build_widget, arrival_rate_base_year_build_widget])
   
    
    # Departure Rate Forecast No Build widget (Year 20)
    departure_rate_forecast_year_no_build_widget = widgets.FloatText(
        description="Departure Rate Forecast Year ( Year 1):",
        value=None,  # Initially empty
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )

    # Departure Rate Year 20 Build widget (calculated)
    departure_rate_forecast_year_build_widget = widgets.FloatText(
        description="Departure Rate Forecast Year (Year 20):",
        value=None,  # Initially empty
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    ) 
    
    # Function to update the Departure Rate Forecast (No Build and Build are the same)
    def update_departure_rate_forecast(change):
        # Get the current values from the widgets
        subcategory = subcategory_dropdown.value  # Subcategory selected
        roadway_type_abbr = roadway_type_no_build_widget.value  # Roadway type (No Build)

        # Map the abbreviation to the full name for the dictionary lookup
        roadway_type_full = roadway_type_mapping.get(roadway_type_abbr, None)

        # If the subcategory is "Queuing" or "Hwy-Rail Grade Crossing", calculate departure rates
        if subcategory in ["Queuing", "Hwy-Rail Grade Crossing"] and roadway_type_full:
            # Fetch the departure rate from the params.roadway_capacity dictionary
            if roadway_type_full in params.roadway_capacity:
                # Get the appropriate departure rate from the dictionary
                if roadway_type_full == "Freeway":
                    departure_rate = params.roadway_capacity["Freeway"]["DepRateFwy"]
                elif roadway_type_full == "Expressway":
                    departure_rate = params.roadway_capacity["Expressway"]["DepRateExp"]
                elif roadway_type_full == "Conventional Highway":
                    departure_rate = params.roadway_capacity["Conventional Highway"]["DepRateConv"]
                else:
                    departure_rate = 0  # Default to 0 if not found
            else:
                departure_rate = 0  # Default to 0 if not found

            # Get the general lanes and HOV lanes values
            GenLanesNB = general_traffic_lanes_no_build_widget.value
            HOVLanesNB = hov_hot_lanes_no_build_widget.value

            # Calculate the departure rate forecast for No Build
            departure_rate_no_build = departure_rate * (GenLanesNB + HOVLanesNB)
            departure_rate_forecast_year_no_build_widget.value = departure_rate_no_build

            # Build = No Build, so we set the Build widget to the same value
            departure_rate_forecast_year_build_widget.value = departure_rate_no_build
        else:
            # If subcategory is not "Queuing" or "Hwy-Rail Grade Crossing", set both to 0
            departure_rate_forecast_year_no_build_widget.value = 0
            departure_rate_forecast_year_build_widget.value = 0

    # Link the widgets to the update function
    subcategory_dropdown.observe(update_departure_rate_forecast, names='value')
    roadway_type_no_build_widget.observe(update_departure_rate_forecast, names='value')
    general_traffic_lanes_no_build_widget.observe(update_departure_rate_forecast, names='value')
    hov_hot_lanes_no_build_widget.observe(update_departure_rate_forecast, names='value')
    
    
    # Combine both "No Build" and "Build" input fields into a horizontal layout
    departure_rate_widgets = widgets.HBox([departure_rate_forecast_year_no_build_widget, departure_rate_forecast_year_build_widget])        
    
    # Pavement Condition IRI Base Year No Build widget (Year 1)
    iri_base_year_no_build_widget = widgets.FloatText(
        description="International Roughness Index (inches/mile) (No Build, Year 1):",
        value=None,  # Initially empty
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )

    # Pavement Condition IRI Base Year Build widget (Year 1)
    iri_base_year_build_widget = widgets.FloatText(
        description="International Roughness Index (inches/mile) (Build, Year 1):",
        value=None,  # Initially empty
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )
    
    # Pavement Condition IRI Forecast Year No Build widget (Year 20)
    iri_forecast_year_no_build_widget = widgets.FloatText(
        description="International Roughness Index (inches/mile) (No Build, Year 20):",
        value=None,  # Initially empty
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )

    # Pavement Condition IRI Forecast Year Build widget (Year 20)
    iri_forecast_year_build_widget = widgets.FloatText(
        description="International Roughness Index (inches/mile) (Build, Year 20):",
        value=None,  # Initially empty
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )

    
    # Function to update Pavement Condition IRI Forecast
    def update_iri_forecast(change):
        # Check if "Pavement" is selected from the subcategory dropdown
        subcategory = subcategory_dropdown.value
        if subcategory == "Pavement":
            # Get the necessary values for No Build and Build
            GenLanesNB = general_traffic_lanes_no_build_widget.value
            HOVLanesNB = hov_hot_lanes_no_build_widget.value
            IRINB = iri_base_year_no_build_widget.value  # IRI1NB is iri_base_year_no_build_widget
            ADT1NB = adt_base_year_no_build_widget.value

            GenLanesB = general_traffic_lanes_build_widget.value
            HOVLanesB = hov_hot_lanes_build_widget.value
            IRIB = iri_base_year_build_widget.value  # IRI1B is iri_base_year_build_widget
            ADT1B = adt_base_year_build_widget.value

            # Function to lookup the closest IRI value and return the corresponding forecast
            def get_iri_forecast(iri_value, adt_value, gen_lanes, hov_lanes):
                # Check for valid input values
                if iri_value is None or adt_value is None or gen_lanes + hov_lanes == 0:
                    return 0  # Return 0 if the inputs are invalid (IRI is None, or no lanes)

                # Find the closest IRI key in the dictionary (assumes the keys are sorted)
                iri_key = min(params.pave_det.keys(), key=lambda k: abs(k - iri_value))  # Find closest key

                # Calculate the forecast based on ADT and the number of lanes
                if adt_value / (gen_lanes + hov_lanes) < 2182:
                    return params.pave_det[iri_key]["Year20Light"]
                elif adt_value / (gen_lanes + hov_lanes) < 10909:
                    return params.pave_det[iri_key]["Year20Medium"]
                else:
                    return params.pave_det[iri_key]["Year20Heavy"]

            # Calculate the IRI forecast for No Build and Build
            if GenLanesNB + HOVLanesNB > 0:  # Ensure there are lanes for No Build
                iri_forecast_no_build = get_iri_forecast(IRINB, ADT1NB, GenLanesNB, HOVLanesNB)
                iri_forecast_year_no_build_widget.value = iri_forecast_no_build
            else:
                iri_forecast_year_no_build_widget.value = 0  # Set to 0 if no lanes are provided

            if GenLanesB + HOVLanesB > 0:  # Ensure there are lanes for Build
                iri_forecast_build = get_iri_forecast(IRIB, ADT1B, GenLanesB, HOVLanesB)
                iri_forecast_year_build_widget.value = iri_forecast_build
            else:
                iri_forecast_year_build_widget.value = 0  # Set to 0 if no lanes are provided
        else:
            # If Pavement is not selected, set both forecasts to 0 or leave them as is
            iri_forecast_year_no_build_widget.value = 0
            iri_forecast_year_build_widget.value = 0

    # Link the subcategory dropdown to the update function (assuming it's a widget)
    subcategory_dropdown.observe(update_iri_forecast, names='value')

    # If you need to link other widgets (like ADT, IRI, or Lanes) to this function:
    general_traffic_lanes_no_build_widget.observe(update_iri_forecast, names='value')
    hov_hot_lanes_no_build_widget.observe(update_iri_forecast, names='value')
    iri_base_year_no_build_widget.observe(update_iri_forecast, names='value')
    adt_base_year_no_build_widget.observe(update_iri_forecast, names='value')

    general_traffic_lanes_build_widget.observe(update_iri_forecast, names='value')
    hov_hot_lanes_build_widget.observe(update_iri_forecast, names='value')
    iri_base_year_build_widget.observe(update_iri_forecast, names='value')
    adt_base_year_build_widget.observe(update_iri_forecast, names='value')

    general_traffic_lanes_build_widget.observe(update_iri_forecast, names='value')
    hov_hot_lanes_build_widget.observe(update_iri_forecast, names='value')
    adt_base_year_build_widget.observe(update_iri_forecast, names='value')

    
    # Combine both "No Build" and "Build" input fields into a horizontal layout
    iri_base_year_widgets = widgets.HBox([iri_base_year_no_build_widget, iri_base_year_build_widget])       
    iri_forecast_year_widgets = widgets.HBox([iri_forecast_year_no_build_widget, iri_forecast_year_build_widget]) 

    
    # Highway Crash Data 
    # Actual 3-year Crash Data
    actual_3_year_totalcrash_count_widget = widgets.FloatText(
        description="Total Accidents/Crashes Count (No):",
        value=None,  # Initially empty
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )    
    
    actual_3_year_totalcrash_rate_widget = widgets.FloatText(
        description="Total Accidents/Crashes Rate:",
        value=None,  # Initially empty
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )

    actual_3_year_fatalcrash_count_widget = widgets.FloatText(
        description="Fatal Accidents/Crashes Count (No):",
        value=None,  # Initially empty
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )    
    
    actual_3_year_fatalcrash_rate_widget = widgets.FloatText(
        description="Fatal Accidents/Crashes Rate:",
        value=None,  # Initially empty
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )    
    
    actual_3_year_injurycrash_count_widget = widgets.FloatText(
        description="Injury Accidents/Crashes Count (No):",
        value=None,  # Initially empty
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )    
    
    actual_3_year_injurycrash_rate_widget = widgets.FloatText(
        description="Injury Accidents/Crashes Rate:",
        value=None,  # Initially empty
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )

    actual_3_year_pdocrash_count_widget = widgets.FloatText(
        description="PDO Accidents/Crashes Count (No):",
        value=None,  # Initially empty
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )    
    
    actual_3_year_pdocrash_rate_widget = widgets.FloatText(
        description="PDO Accidents/Crashes Rate:",
        value=None,  # Initially empty
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )    
    
    actual_3_year_totalcrash_widgets = widgets.HBox([actual_3_year_totalcrash_count_widget, actual_3_year_totalcrash_rate_widget])
    actual_3_year_fatalcrash_widgets =  widgets.HBox([actual_3_year_fatalcrash_count_widget, actual_3_year_fatalcrash_rate_widget])
    actual_3_year_injurycrash_widgets = widgets.HBox([actual_3_year_injurycrash_count_widget, actual_3_year_injurycrash_rate_widget])
    actual_3_year_pdocrash_widgets = widgets.HBox([actual_3_year_pdocrash_count_widget, actual_3_year_pdocrash_rate_widget])
    
    
    
    # Statewide Average Crash Rate Build and No Build 
    state_crash_rate_group_nobuild_widget = widgets.Text(
        description="Rate Group (No Build):",
        value='',  # Initially empty
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )
    
    state_crash_rate_group_build_widget = widgets.Text(
        description="Rate Group (Build):",
        value='',  # Initially empty
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )
    
    crash_rate_permvm_nobuild_widget = widgets.Text(
        description="Crash Rate (per million vehicle-miles) (No Build):",
        value='',  # Initially empty
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )
    
    crash_rate_permvm_build_widget = widgets.Text(
        description="Crash Rate (per million vehicle-miles) (Build):",
        value='',  # Initially empty
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )
     
    percent_fatal_crash_nobuild_widget = widgets.Text(
        description="Percent Fatal Crashes (Pct Fat) (No Build):",
        value='',  # Initially empty
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )    
    
    percent_fatal_crash_build_widget = widgets.Text(
        description="Percent Fatal Crashes (Pct Fat) (Build):",
        value='',  # Initially empty
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )   
    
    percent_injury_crash_nobuild_widget = widgets.Text(
        description="Percent Injury Crashes (Pct Inj) (No Build):",
        value='',  # Initially empty
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )    
    
    percent_injury_crash_build_widget = widgets.Text(
        description="Percent Injury Crashes (Pct Inj) (Build):",
        value='',  # Initially empty
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    ) 
    
    state_crash_rategroup_widgets = widgets.HBox([state_crash_rate_group_nobuild_widget, state_crash_rate_group_build_widget])
    crash_rate_permvm_widgets =  widgets.HBox([crash_rate_permvm_nobuild_widget, crash_rate_permvm_build_widget])
    fatal_crash_rate_widgets = widgets.HBox([percent_fatal_crash_nobuild_widget, percent_fatal_crash_build_widget])
    injury_crash_rate_widgets = widgets.HBox([percent_injury_crash_nobuild_widget, percent_injury_crash_build_widget])
    
    #Rail and Transit Data 
    # Annual Person Trips Data 
    TAPT1NB_widget = widgets.Text(
        description="Annual Person Trips Base Year, Year 1, (No Build):",
        value='',  # Initially empty
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )
    
    TAPT1B_widget = widgets.Text(
        description="Annual Person Trips Base Year, Year 1, (Build):",
        value='',  # Initially empty
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )
    
    TAPT20NB_widget = widgets.Text(
        description="Annual Person Trips Forecast Year, Year 20, (No Build):",
        value='',  # Initially empty
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )
    
    TAPT20B_widget = widgets.Text(
        description="Annual Person Trips Forecast Year, Year 20, (Build):",
        value='',  # Initially empty
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )
    
    annual_persontrips_year1_widgets = widgets.HBox([TAPT1NB_widget, TAPT1B_widget])
    annual_persontrips_year20_widgets = widgets.HBox([TAPT20NB_widget, TAPT20B_widget])
    
    
    TPerPeak_widget = widgets.FloatText(
        description="Percent Trips during Peak Period:",
        value=params.per_peak_adt,  # Initialize with 0
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )
    
    TPerHwy_widget = widgets.FloatText(
        description="Percent New Trips from Parallel Highway:",
        value=1,  # 100%
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )
    
    TVehMi1NB_widget = widgets.Text(
        description="Annual Vehicle Miles Base Year, Year 1 (No Build):",
        value='',  # Initialize with 0
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )
    
    TVehMi1B_widget = widgets.Text(
        description="Annual Vehicle Miles Base Year, Year 1 (Build):",
        value='',  
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )
    
    TVehMi20NB_widget = widgets.Text(
        description="Annual Vehicle Miles Forecast Year, Year 20 (No Build):",
        value='',  # Initialize with 0
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )
    
    TVehMi20B_widget = widgets.Text(
        description="Annual Vehicle Miles Forecast Year, Year 20 (Build):",
        value='', 
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )
    
    annual_vehmiles_year1_widgets = widgets.HBox([TVehMi1NB_widget, TVehMi1B_widget])
    annual_vehmiles_year20_widgets = widgets.HBox([TVehMi20NB_widget, TVehMi20B_widget])
    
    TVehPerTrainNB_widget = widgets.Text(
        description="Average Vehicles/Train (No Build):",
        value='',  # Initialize with 0
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )
    
    TVehPerTrainB_widget = widgets.Text(
        description="Average Vehicles/Train (Build):",
        value='',  # Initialize with 0
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )
    annual_vehicle_per_train_widgets = widgets.HBox([TVehPerTrainNB_widget, TVehPerTrainB_widget])

    TAccReductPer = widgets.Text(
        description="Percent Reduction in Transit Accidents:",
        value='',  
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )
    
    #Average Transit Travel Time
    TInTimeNBN_widget = widgets.Text(
        description="In Vehicle: Average Transit Travel Time Non Peak (No Build):",
        value='',  # Initialize with 0
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )
    
    TInTimeBN_widget = widgets.IntText(
        description="In Vehicle: Average Transit Travel Time Non Peak (Build):",
        value=None,  
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )
    
    # Function to update the TInTimeBN_widget based on TInTimeNBN_widget and subcategory
    def update_transit_travel_time_nonpeak(change=None):
        # Retrieve relevant widget values
        subcategory = subcategory_dropdown.value  # Get the selected subcategory
        TInTimeNBN = TInTimeNBN_widget.value  # Get the entered value for TInTimeNBN

        # Ensure TInTimeNBN has a valid number, otherwise set a default value (0)
        if TInTimeNBN is None or TInTimeNBN == '':
            TInTimeBN = 0  # Default value if no input is given
        else:
            # Apply the formula based on the subcategory selected
            if subcategory == "Transit Vehicle Location (AVL)":
                # Apply AVL savings
                TInTimeBN = TInTimeNBN * (1 - params.transit_savings["Transit Vehicle Location (AVL)"]["AVLTTsaving"])
            elif subcategory == "Transit Vehicle Signal Priority":
                # Apply Signal Priority savings
                TInTimeBN = TInTimeNBN * (1 - params.transit_savings["Transit Vehicle Signal Priority"]["SigTTsaving"])
            elif subcategory == "Bus Rapid Transit (BRT)":
                # Apply BRT savings
                TInTimeBN = TInTimeNBN * (1 - params.transit_savings["Bus Rapid Transit (BRT)"]["BrtTTsaving"])
            else:
                # No savings applied if the subcategory is not one of the above
                TInTimeBN = TInTimeNBN

    # Initialize the calculation (this will execute once when the code runs)
    update_transit_travel_time_nonpeak()
    
    # Attach observers to relevant widgets
    TInTimeNBN_widget.observe(update_transit_travel_time_nonpeak, names='value')  # Observe changes to TInTimeNBN_widget
    subcategory_dropdown.observe(update_transit_travel_time_nonpeak, names='value')  # Observe changes to subcategory_dropdown
    
    transit_travel_time_nonpeak_widgets = widgets.HBox([TInTimeNBN_widget, TInTimeBN_widget])
        
    # Define the widget for displaying the result (Transit Travel Time for Peak)
    TInTimeNBP_widget = widgets.Text(
        description="In Vehicle: Average Transit Travel Time Peak (No Build):",
        value='',  # Initialize with an empty value
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )

    TInTimeBP_widget = widgets.IntText(
        description="In Vehicle: Average Transit Travel Time Peak (Build):",
        value=None,  # Initialize with None or default value
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )

    # Function to update the TInTimeBP_widget based on TInTimeNBP_widget and subcategory
    def update_transit_travel_time_peak(change=None):
        # Retrieve relevant widget values
        subcategory = subcategory_dropdown.value  # Get the selected subcategory
        TInTimeNBP = TInTimeNBP_widget.value  # Get the entered value for TInTimeNBP

        # Ensure TInTimeNBP has a valid number, otherwise set a default value (0)
        if TInTimeNBP == '' or TInTimeNBP is None:
            TInTimeBP = 0  # Default value if no input is given
        else:
            TInTimeNBP = float(TInTimeNBP)  # Convert to float for calculations

            # Apply the formula based on the subcategory selected
            if subcategory == "Transit Vehicle Location (AVL)":
                # Apply AVL savings
                TInTimeBP = TInTimeNBP * (1 - params.transit_savings["Transit Vehicle Location (AVL)"]["AVLTTsaving"])
            elif subcategory == "Transit Vehicle Signal Priority":
                # Apply Signal Priority savings
                TInTimeBP = TInTimeNBP * (1 - params.transit_savings["Transit Vehicle Signal Priority"]["SigTTsaving"])
            elif subcategory == "Bus Rapid Transit (BRT)":
                # Apply BRT savings
                TInTimeBP = TInTimeNBP * (1 - params.transit_savings["Bus Rapid Transit (BRT)"]["BrtTTsaving"])
            else:
                # No savings applied if the subcategory is not one of the above
                TInTimeBP = TInTimeNBP


    # Initialize the calculation
    update_transit_travel_time_peak()

    # Attach observers to relevant widgets
    TInTimeNBP_widget.observe(update_transit_travel_time_peak, names='value')  # Observe changes to TInTimeNBP_widget
    subcategory_dropdown.observe(update_transit_travel_time_peak, names='value')  # Observe changes to subcategory_dropdown

    # Widgets container to display both the input and the result for Peak Period
    transit_travel_time_peak_widgets = widgets.HBox([TInTimeNBP_widget, TInTimeBP_widget])
        
    #Average Transit Travel Time Out of Vehicle
    TOutTimeNBN_widget = widgets.IntText(
        description="Out-of-Vehicle: Average Transit Travel Time Non Peak (No Build):",
        value=0.0,  # Initialize with 0
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )
    
    TOutTimeBN_widget = widgets.IntText(
        description="Out-of-Vehicle: Average Transit Travel Time Non Peak (Build):",
        value=0.0,  
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )
    
    def update_outofveh_transit_travel_time_nonpeak(change=None):
        # Retrieve relevant widget values
        subcategory = subcategory_dropdown.value  # Get the selected subcategory
        TOutTimeNBN = TOutTimeNBN_widget.value  # Get the entered value for TOutTimeNBN

        # Initialize TOutTimeBN with the same value as TOutTimeNBN initially
        TOutTimeBN = TOutTimeNBN

        # Apply the formula based on the subcategory selected
        if subcategory == "Transit Vehicle Location (AVL)":
            # Apply AVL savings (TOutTimeNBN * (1 - AVLTTsaving))
            TOutTimeBN = TOutTimeNBN * (1 - params.transit_savings["Transit Vehicle Location (AVL)"]["AVLTTsaving"])



    # Initialize the calculation (this will execute once when the code runs)
    update_outofveh_transit_travel_time_nonpeak()

    # Attach observers to relevant widgets
    TOutTimeNBN_widget.observe(update_outofveh_transit_travel_time_nonpeak, names='value')  # Observe changes to TOutTimeNBN_widget
    subcategory_dropdown.observe(update_outofveh_transit_travel_time_nonpeak, names='value')  # Observe changes to subcategory_dropdown
        
    # Widgets container to display both the input and the result for Peak Period
    transit_travel_time_outofveh_nonpeak_widgets = widgets.HBox([TOutTimeNBN_widget, TOutTimeBN_widget]) 
    

    #Average Transit Travel Time Out of Vehicle
    TOutTimeNBP_widget = widgets.IntText(
        description="Out-of-Vehicle: Average Transit Travel Time Peak (No Build):",
        value=0.0,  # Initialize with 0
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )
    
    TOutTimeBP_widget = widgets.IntText(
        description="Out-of-Vehicle: Average Transit Travel Time Peak (Build):",
        value=0.0,  
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )
    
    def update_outofveh_transit_travel_time_peak(change=None):
        # Retrieve relevant widget values
        subcategory = subcategory_dropdown.value  # Get the selected subcategory
        TOutTimeNBP = TOutTimeNBP_widget.value  # Get the entered value for TOutTimeNBN

        # Initialize TOutTimeBN with the same value as TOutTimeNBN initially
        TOutTimeBP = TOutTimeNBP

        # Apply the formula based on the subcategory selected
        if subcategory == "Transit Vehicle Location (AVL)":
            # Apply AVL savings (TOutTimeNBN * (1 - AVLTTsaving))
            TOutTimeBP = TOutTimeNBP * (1 - params.transit_savings["Transit Vehicle Location (AVL)"]["AVLTTsaving"])



    # Initialize the calculation (this will execute once when the code runs)
    update_outofveh_transit_travel_time_peak()

    # Attach observers to relevant widgets
    TOutTimeNBP_widget.observe(update_outofveh_transit_travel_time_peak, names='value')  # Observe changes to TOutTimeNBN_widget
    subcategory_dropdown.observe(update_outofveh_transit_travel_time_peak, names='value')  # Observe changes to subcategory_dropdown
        
    # Widgets container to display both the input and the result for Peak Period
    transit_travel_time_outofveh_peak_widgets = widgets.HBox([TOutTimeNBP_widget, TOutTimeBP_widget]) 
    
    NumTrain0_widget = widgets.Text(
        description="Hwy Grade Crossing Annual Number of Trains (Current Year):",
        value="",  # Initialize with 0
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )
    
    NumTrain1_widget = widgets.IntText(
        description="Hwy Grade Crossing Annual Number of Trains (Year 1):",
        value=0,  
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )
    
    NumTrain20_widget = widgets.Text(
        description="Hwy Grade Crossing Annual Number of Trains (Year 20):",
        value="",  
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )
    
    def update_numtrain1(change=None):
        try:
            # Convert inputs to float for calculation
            NumTrain0 = float(NumTrain0_widget.value)
            NumTrain20 = float(NumTrain20_widget.value)
            Construct = float(construct_widget.value)

            # Apply the formula:

            NumTrain1 = NumTrain0 + (NumTrain20 - NumTrain0) * Construct / (Construct + 19)

            # Update the widget value
            NumTrain1_widget.value = round(NumTrain1)
        except (ValueError, TypeError):
            # If values are not valid numbers, fall back to 0
            NumTrain1_widget.value = 0
        
    # Initial call to set default value
    update_numtrain1()
    
    NumTrain0_widget.observe(update_numtrain1, names='value')
    NumTrain20_widget.observe(update_numtrain1, names='value')
    construct_widget.observe(update_numtrain1, names='value')

    # Widgets container 
    annual_number_of_train_widgets = widgets.HBox([NumTrain0_widget, NumTrain1_widget, NumTrain20_widget]) 
    
    
    GateTime0_widget = widgets.Text(
        description="Hwy Grade Crossing Avg. Gate Down Time (Current Year):",
        value="",  # Initialize with 0
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )
    
    GateTime1_widget = widgets.IntText(
        description="Hwy Grade Crossing Avg. Gate Down Time (Year 1):",
        value=0.0,  
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )
    
    GateTime20_widget = widgets.Text(
        description="Hwy Grade Crossing Avg. Gate Down Time (Year 20):",
        value="",  
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )
    
    def update_gatetime1(change=None):
        try:
            # Convert inputs to float for calculation
            GateTime0 = float(GateTime0_widget.value)
            GateTime20 = float(GateTime20_widget.value)
            Construct = float(construct_widget.value)

            # Apply the formula:

            GateTime1 = GateTime0 + (GateTime20 - GateTime0) * Construct / (Construct + 19)

        except (ValueError, TypeError):
            # If values are not valid numbers, fall back to 0
            GateTime1_widget.value = 0.0
        
    # Initial call to set default value
    update_gatetime1()
    
    GateTime0_widget.observe(update_gatetime1, names='value')
    GateTime20_widget.observe(update_gatetime1, names='value')
    construct_widget.observe(update_gatetime1, names='value')

    # Widgets container 
    average_gate_down_time_widgets = widgets.HBox([GateTime0_widget, GateTime1_widget, GateTime20_widget]) 
        
    #Transit Agency Cost
    TCapCostNB_widget = widgets.Text(
        description="Transit Agency Expenditure (No Build):",
        value='',  # Initialize with 0
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )
    
    TCapCostB_widget = widgets.IntText(
        description="Transit Agency Expenditure (Build):",
        value=0,  
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )
    
    def update_annual_capex(change=None):
        # Retrieve relevant widget values
        subcategory = subcategory_dropdown.value  # Get the selected subcategory
        TCapCostNB = TCapCostNB_widget.value  # Get the entered value for TOutTimeNBN

        # Initialize TOutTimeBN with the same value as TOutTimeNBN initially
        TCapCostB = TCapCostNB

        # Apply the formula based on the subcategory selected
        if subcategory == "Transit Vehicle Location (AVL)":
            # Apply AVL savings (TOutTimeNBN * (1 - AVLTTsaving))
            TCapCostB = TCapCostNB* (1 - params.transit_savings["Transit Vehicle Location (AVL)"]["AVLCapSaving"])
            
    # Initialize the calculation (this will execute once when the code runs)
    update_annual_capex()

    # Attach observers to relevant widgets
    TCapCostNB_widget.observe(update_annual_capex, names='value')  # Observe changes to TOutTimeNBN_widget
    subcategory_dropdown.observe(update_annual_capex, names='value')  # Observe changes to subcategory_dropdown   
    
    # Widgets container 
    annual_capex_widgets = widgets.HBox([TCapCostNB_widget, TCapCostB_widget]) 
    
    #Opex Widget 
    TOMCostNB_widget = widgets.Text(
        description="Annual Ops and Maintenance Expenditure (No Build):",
        value='',  # Initialize with 0
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )
    
    TOMCostB_widget = widgets.IntText(
        description="Annual Ops and Maintenance Expenditure (Build):",
        value=0,  
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )
    
    def update_annual_opex(change=None):
        # Retrieve relevant widget values
        subcategory = subcategory_dropdown.value  # Get the selected subcategory
        TOMCostNB = TOMCostNB_widget.value  # Get the entered value for TOutTimeNBN

        # Initialize TOutTimeBN with the same value as TOutTimeNBN initially
        TOMCostB = TOMCostNB

        # Apply the formula based on the subcategory selected
        if subcategory == "Transit Vehicle Location (AVL)":
            TOMCostB = TOMCostNB* (1 - params.transit_savings["Transit Vehicle Location (AVL)"]["AvlOMsaving"])
            
    # Initialize the calculation (this will execute once when the code runs)
    update_annual_opex()

    # Attach observers to relevant widgets
    TOMCostNB_widget.observe(update_annual_opex, names='value')  # Observe changes to TOutTimeNBN_widget
    subcategory_dropdown.observe(update_annual_opex, names='value')  # Observe changes to subcategory_dropdown   
    

    # Widgets container 
    annual_opex_widgets = widgets.HBox([TOMCostNB_widget, TOMCostB_widget]) 
    
        

    #Create Project Info Section
    # Project Info Section
    project_info_section = create_section(
        project_info_title, 
        project_info_subtitle, 
        [projloc_widget, project_type_dropdown, subcategory_dropdown, construct_widget, one_two_way_widget, peak_period_widget],
        project_info_info
    )

    # Highway Design and Traffic Data Section
    highway_design_and_traffic_data_section = create_section(
        highway_design_and_traffic_data_title,
        highway_design_and_traffic_data_subtitle,
        [
            roadway_type_widgets, general_traffic_lanes_widgets, hov_hot_lanes_widgets, HOVRest_widget, 
            Exclusive_widget, free_flow_speed_widgets, ramp_design_speed_widgets, highway_segment_widgets, 
            impacted_length_widgets, ADT_current_widget, adt_base_widgets, adt_20_widget, hourly_hov_lane_traffic_widget, 
            percent_induced_trip_widget, percent_traffic_weave_widgets, percent_trucks_widget, truck_speed_widget
        ],
        highway_design_and_traffic_data_info
    )

    # On-Ramp Volume Section
    on_ramp_volume_section = create_section(
        on_ramp_volume_title, 
        on_ramp_volume_subtitle,
        [hourly_ramp_volume_widget, metering_strategy_widget],
        on_ramp_volume_info
    )


    # Queue Formation Section
    queue_formation_section = create_section(
        queue_formation_title, 
        queue_formation_subtitle,
        [arrival_rate_widgets, departure_rate_widgets],
        queue_formation_info
    )

    # Pavement Condition Section
    pavement_condition_section = create_section(
        pavement_condition_title, 
        pavement_condition_subtitle, 
        [iri_base_year_widgets, iri_forecast_year_widgets],
        pavement_condition_info
    )
    
    # AVO Section
    avo_section = create_section(
        avo_section_title, 
        avo_section_subtitle, 
        [AVO_GenTraffic_NonPeak_widgets, AVO_GenTraffic_Peak_widgets, AVO_HOV_widgets ],
        avo_section_info
    )
    
    #Actual 3 Years Crash Data Section 
    actual_3years_crash_data_section = create_section(
        actual_3years_crash_title, 
        actual_3years_crash_subtitle, 
        [actual_3_year_totalcrash_widgets, actual_3_year_fatalcrash_widgets, actual_3_year_injurycrash_widgets, actual_3_year_pdocrash_widgets],
        actual_3years_crash_info
    )
    
    # Statewide Crash Rate Section
    statewide_avg_crashrate_info_section = create_section(
        statewide_avg_crash_title, 
        statewide_avg_crash_subtitle, 
        [state_crash_rategroup_widgets, crash_rate_permvm_widgets, fatal_crash_rate_widgets, injury_crash_rate_widgets],
        statewide_avg_crash_info
    )
    
    # Rail and Transit Data Section
    rail_and_transit_data_section = create_section(
        rail_and_transit_data_title, 
        rail_and_transit_data_subtitle, 
        [annual_persontrips_year1_widgets, annual_persontrips_year20_widgets, TPerPeak_widget, TPerHwy_widget, annual_vehmiles_year1_widgets, annual_vehmiles_year20_widgets, annual_vehicle_per_train_widgets, TAccReductPer, transit_travel_time_nonpeak_widgets, transit_travel_time_peak_widgets, transit_travel_time_outofveh_nonpeak_widgets, transit_travel_time_outofveh_peak_widgets, annual_number_of_train_widgets, average_gate_down_time_widgets, annual_capex_widgets, annual_opex_widgets],
        rail_and_transit_data_info
    )

    

    

    # Stack all sections vertically
    all_sections = widgets.VBox([project_info_section, highway_design_and_traffic_data_section, avo_section, on_ramp_volume_section, queue_formation_section, pavement_condition_section, actual_3years_crash_data_section, statewide_avg_crashrate_info_section, rail_and_transit_data_section])


#     # Update the visibility of sections based on subcategory selection
#     def update_visible_section(change):
#         subcategory = subcategory_dropdown.value

#         # Hide all sections that depend on subcategory value
#         pavement_condition_section.layout.display = 'none'
#         on_ramp_volume_section.layout.display = 'none'  # Hide on_ramp_volume_section initially


#         # Show sections based on the selected subcategory
#         if subcategory == "Pavement":
#             pavement_condition_section.layout.display = 'flex'  # Show Pavement Condition section
#         elif subcategory == "Auxiliary Lane" or subcategory == "On-Ramp Widening":
#             on_ramp_volume_section.layout.display = 'flex'  # Show On-Ramp Volume section


#     # Link the subcategory dropdown to the visibility update function
#     subcategory_dropdown.observe(update_visible_section, names='value')

#     # Initially, update the visible section based on the initial subcategory value
#     update_visible_section(None)  
    
    
    # Display the stacked sections
    display(all_sections)


    # # Return dictionary of key widgets for reuse elsewhere
    # return {
    #     "ProjLoc": projloc_widget,
    #     "ProjType": project_type_dropdown,
    #     "ProjSubType": subcategory_dropdown,
    #     "Construct": construct_widget,
    #     "NumDirections": one_two_way_widget,
    #     "PeakLngthNB": peak_period_widget,
    #     "RoadTypeNB": roadway_type_no_build_widget,
    #     "RoadTypeB": roadway_type_build_widget,
    #     "GenLanesNB": general_traffic_lanes_no_build_widget,
    #     "GenLanesB": general_traffic_lanes_build_widget,
    #     "HOVLanesNB": hov_hot_lanes_no_build_widget,
    #     "HOVLanesB": hov_hot_lanes_build_widget,
    #     "HOVRest": HOVRest_widget,
    #     "Exclusive": Exclusive_widget,
    #     "FFSpeedNB": free_flow_speed_no_build_widget,
    #     "FFSpeedB": free_flow_speed_build_widget,
    #     "RampFFSpdNB": ramp_design_speed_no_build_widget,
    #     "RampFFSpdB": ramp_design_speed_build_widget,
    #     "SegmentNB": highway_segment_no_build_widget,
    #     "SegmentB": highway_segment_build_widget,
    #     "ImpactedNB": impacted_length_no_build_widget,
    #     "ImpactedB": impacted_length_build_widget,
    #     "ADT0": ADT_current_widget,
    #     "ADT1NB": adt_base_year_no_build_widget,
    #     "ADT1B": adt_base_year_build_widget,
    #     "ADT20NB": ADT_20NB_widget,
    #     "ADT20B": adt_20_year_build_widget,
    #     "HOVvolNB": HOV_lane_nobuild_widget,
    #     "HOVvolB": HOV_lane_build_widget,
    #     "PerWeaveNB": percent_traffic_weave_no_build_widget,
    #     "PerWeaveB": percent_traffic_weave_build_widget,
    #     "PerIndHOV": percent_induced_trip_widget,
    #     "PerTruckNB": percent_trucks_nobuild_widget,
    #     "PerTruckB": percent_trucks_build_widget,
    #     "TruckSpeed": truck_speed_widget,
    #     "RampVolP": hourly_ramp_volume_peak_widget,
    #     "RampVolNP": hourly_ramp_volume_nonpeak_widget,
    #     "MeterStrat": metering_strategy_widget,
    #     "ArrRate1": arrival_rate_base_year_no_build_widget,
    #     "ArrRate20": arrival_rate_base_year_build_widget,
    #     "DepRate1": departure_rate_forecast_year_no_build_widget,
    #     "DepRate20": departure_rate_forecast_year_build_widget,
    #     "IRI1NB": iri_base_year_no_build_widget,
    #     "IRI1B": iri_base_year_build_widget,
    #     "IRI20NB": iri_forecast_year_no_build_widget,
    #     "IRI20B": iri_forecast_year_build_widget,
    #     "AVONonNB": AVO_traffic_NP_no_build_widget,
    #     "AVONonB": AVO_traffic_NP_build_widget,
    #     "AVOPeakNB": AVO_traffic_P_no_build_widget,
    #     "AVOPeakB": AVO_traffic_P_build_widget,
    #     "AVOHovNB": AVOHovNB_widget,
    #     "AVOHovB": AVOHovB_widget,
    #     "GateTime1": GateTime1_widget,
    #     "GateTime20": GateTime20_widget,
    #     "NumTrain1": NumTrain1_widget,
    #     "NumTrain20": NumTrain20_widget,
    #     "TPerPeak": TPerPeak_widget,
    #     "TPerHwy": TPerHwy_widget,
    #     "TAPT1B": TAPT1B_widget,
    #     "TAPT1NB": TAPT1NB_widget,
    #     "TAPT20NB": TAPT20NB_widget,
    #     "TAPT20B": TAPT20B_widget
    # }