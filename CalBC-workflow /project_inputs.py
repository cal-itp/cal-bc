import ipywidgets as widgets
from ipywidgets import interactive
from IPython.display import display

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
    ProjLoc_value = projloc_widget.value
    ProjType_value = project_type_dropdown.value
    subcategory_value = subcategory_dropdown.value
    return ProjLoc_value, ProjType_value, subcategory_value

common_layout = widgets.Layout(
    width='500px', 
    background_color='#CCFFCC',  # Background color for all widgets
    padding='2px',
    border='2px solid gray'  # Border color and thickness
)

# Function to create the widgets and display them in the notebook
def create_widgets():
    global project_type_dropdown, subcategory_dropdown, projloc_widget
    
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
        value=1,  # Default value for the number of years is 1
        description="Construct (Years):",
        min=1,  # Minimum value of 1 year
        step=1,  # Step by 1 year
        disabled=False,
        layout=common_layout,  # Set width to allow the description to be more visible
        style={'description_width': 'initial'}  # Ensures description text doesn't get cut off
    )    
    
    one_two_way_widget = widgets.Dropdown(
        options=[('One-Way', 1), ('Two-Way', 2)],  # Dropdown options with values 1 and 2
        value=1,  # Default value is One-Way (1)
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
    
    # Function to update Roadway Type based on selected subcategory
    def update_roadway_type(subcategory):
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
    
    def show_ramp_design_speed(subcategory):
        if subcategory in ["Auxiliary Lane", "Off-Ramp Widening"]:
            ramp_design_speed_widgets.layout.display = 'flex'  # Show the widgets
        else:
            ramp_design_speed_widgets.layout.display = 'none'  # Hide the widgets

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

    # Initially hide the Ramp Design Speed widgets
    ramp_design_speed_widgets.layout.display = 'none'

    # Display the Ramp Design Speed widgets only when appropriate
    widgets.interactive(show_ramp_design_speed, subcategory=subcategory_dropdown)
    
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
        impacted_length_no_build_widget.value = round(impacted_length_no_build, 1)  # Round to 1 decimal place

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
        description="ADT Year 20 (Build):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )


    # ADT Base Year No Build widget (calculated)
    adt_base_year_no_build_widget = widgets.FloatText(
        description="ADT Base Year (No Build):",
        value=None,  # Initially empty
        disabled=True,  # Read-only since it will be calculated
        style={'description_width': 'initial'},
        layout=common_layout
    )

    # ADT Base Year Build widget (calculated)
    adt_base_year_build_widget = widgets.FloatText(
        description="ADT Base Year (Build):",
        value=None,  # Initially empty
        disabled=True,  # Read-only since it will be calculated
        style={'description_width': 'initial'},
        layout=common_layout
    )

    # ADT 20 Year Build widget (calculated based on Truck Lane selection)
    adt_20_year_build_widget = widgets.FloatText(
        description="ADT Year 20 (Build):",
        value=None,  # Initially empty
        disabled=True,  # Read-only since it will be calculated
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

      
    def create_section(title, widget_list):
        title_widget = widgets.Label(value=title)  # Section title
        divider = widgets.HTML(value="<hr>")  # Divider between sections
        section = widgets.VBox([title_widget, divider] + widget_list)  # Combine title, divider, and widgets
        return section
    
    
    project_info_section = create_section("Project Data", [projloc_widget, project_type_dropdown, subcategory_dropdown, construct_widget, one_two_way_widget, peak_period_widget])
    highway_design_and_traffic_data_section = create_section("Highway Design and Traffic Data", [roadway_type_widgets, general_traffic_lanes_widgets, hov_hot_lanes_widgets, HOVRest_widget, Exclusive_widget, free_flow_speed_widgets, ramp_design_speed_widgets, highway_segment_widgets, impacted_length_widgets, ADT_current_widget, adt_base_widgets, adt_20_widget ])
    

    # Stack all sections vertically
    all_sections = widgets.VBox([
        project_info_section,
        highway_design_and_traffic_data_section,
    ])

    # Display the stacked sections
    display(all_sections)