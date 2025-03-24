import ipywidgets as widgets
from ipywidgets import interactive
from IPython.display import display
from Parameter import parameters
params = parameters()

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
    
    # Define AVOHov widgets
    AVOHovNB_widget = widgets.FloatText(
        description="High Occupancy Vehicle (if HOV/HOT lanes) (No Build):",
        value=2.15,  # Default value set to 2.15
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    AVOHovB_widget = widgets.FloatText(
        description="High Occupancy Vehicle (if HOV/HOT lanes) (Build):",
        value=3.15,  # Default value set to 3.15
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

        # Allow user to override calculated value if they input manually
        if HOV_lane_build_widget.value != hov_hot_traffic:
            HOV_lane_build_widget.disabled = False


            
            
    # Link the widgets to trigger the calculation
    project_type_dropdown.observe(update_subcategory, names='value')  # Observe changes in project type
    HOV_lane_nobuild_widget.observe(calculate_hov_hot_traffic, names='value')  # Observe changes in HOVvolNB
    HOV_lane_build_widget.observe(calculate_hov_hot_traffic, names='value')  # Observe changes in HOVvolB
    AVOHovNB_widget.observe(calculate_hov_hot_traffic, names='value')  # Observe changes in AVOHovNB
    AVOHovB_widget.observe(calculate_hov_hot_traffic, names='value')  # Observe changes in AVOHovB
    subcategory_dropdown.observe(calculate_hov_hot_traffic, names='value')  # Observe changes in subcategory


    
    hourly_hov_lane_traffic_widget = widgets.HBox([HOV_lane_nobuild_widget, HOV_lane_build_widget])    
    AVO_HOV_widget = widgets.HBox([AVOHovNB_widget, AVOHovB_widget])
    
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
                percent_traffic_weave_no_build_widget.value = 100
            else:
                percent_traffic_weave_no_build_widget.value = (2 * num_directions) / gen_lanes_nb * 100
        elif subcategory == "Off-Ramp Widening":
            if gen_lanes_nb < 3 * num_directions:
                percent_traffic_weave_no_build_widget.value = 100
            else:
                percent_traffic_weave_no_build_widget.value = (3 * num_directions) / gen_lanes_nb * 100
        elif subcategory == "Freeway Connector":
            percent_traffic_weave_no_build_widget.value = 2.5
        elif subcategory == "HOV Connector" or subcategory == "HOV Drop Ramp":
            percent_traffic_weave_no_build_widget.value = 4
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
        value=9.0,  # Default value set to 9% (this can be adjusted)
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    percent_trucks_build_widget = widgets.FloatText(
        description="Percent Trucks (Build):",
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

    hourly_ramp_volume_nobuild_widget = widgets.IntText(
        description="Hourly Ramp Volume (No Build):",
        value=0,  # Default value set to 0
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    hourly_ramp_volume_build_widget = widgets.FloatText(
        description="Hourly Ramp Volume (Build):",
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
            hourly_ramp_volume_nobuild_widget.value = 1350
        elif OnRampSelected:
            hourly_ramp_volume_nobuild_widget.value = 800
        else:
            hourly_ramp_volume_nobuild_widget.value = 0  # Default value when no matching subcategory is selected

        # Get the required values from the class instance (params)
        RampVolP = hourly_ramp_volume_nobuild_widget.value  # Ramp Volume from the No Build widget
        PerPeakAvgHr = params.per_peak_avg_hr  # Per Peak Average Hourly Traffic (from the params instance)
        PerPeakADT = params.per_peak_adt  # Per Peak ADT (from the params instance)
        PeakLngthNB = peak_period_widget.value  # Peak Length (No Build scenario) from the peak_period_widget

        # Calculate Hourly Ramp Volume (Build) using the provided formula
        # Always calculate the Build volume regardless of RampVolP
        build_value = (RampVolP / PerPeakAvgHr) * (1 - PerPeakADT) / (24 - PeakLngthNB)
        
        hourly_ramp_volume_build_widget.value = round(build_value, 0)

    # Link the widgets to trigger the calculation
    subcategory_dropdown.observe(calculate_ramp_volume, names='value')  # Observe changes in subcategory dropdown
    peak_period_widget.observe(calculate_ramp_volume, names='value')  # Observe changes in Peak Length (No Build)
    hourly_ramp_volume_nobuild_widget.observe(calculate_ramp_volume, names='value')
    

    # Define the layout for the widgets (assuming common_layout is defined elsewhere)
    hourly_ramp_volume_widget = widgets.HBox([hourly_ramp_volume_nobuild_widget, hourly_ramp_volume_build_widget])
    

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
        description="Arrival Rate Base Year (No Build, Year 1):",
        value=None,  # Initially empty
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )

    # Arrival Rate Base Year Build widget (calculated)
    arrival_rate_base_year_build_widget = widgets.FloatText(
        description="Arrival Rate Base Year (Build):",
        value=None,  # Initially empty
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

        # Calculate Arrival Rate Base Year No Build
        if subcategory == "Hwy-Rail Grade Crossing":  # Check if subcategory is Hwy-Rail Grade Crossing
            arrival_rate_base_year_no_build = ADT1NB / 12  # Formula: ADT1NB / 12
        else:
            arrival_rate_base_year_no_build = 0  # Otherwise set to 0 (No Build scenario)

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
    arrival_rate_base_year_no_build_widget.observe(calculate_arrival_rate, names='value')
    ADT_20NB_widget.observe(calculate_arrival_rate, names='value')
    adt_base_year_no_build_widget.observe(calculate_arrival_rate, names='value')
    subcategory_dropdown.observe(calculate_arrival_rate, names='value')

    # Combine both "No Build" and "Build" input fields into a horizontal layout
    arrival_rate_widgets = widgets.HBox([arrival_rate_base_year_no_build_widget, arrival_rate_base_year_build_widget])
   
    
    # Departure Rate Forecast No Build widget (Year 20)
    departure_rate_forecast_year_no_build_widget = widgets.FloatText(
        description="Departure Rate Forecast Year (No Build, Year 20):",
        value=None,  # Initially empty
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )

    # Departure Rate Year 20 Build widget (calculated)
    departure_rate_forecast_year_build_widget = widgets.FloatText(
        description="Departure Rate Forecast Year (Build, Year 20):",
        value=None,  # Initially empty
        disabled=False,  # Allow user to enter values
        style={'description_width': 'initial'},
        layout=common_layout
    )    
    

    def create_section(title, widget_list):
        title_widget = widgets.HTML(value=f"<b style='color: darkblue;'>{title}</b>")

        divider = widgets.HTML(value="<hr>")  # Divider between sections

        # Combine title, divider, and widgets into a vertical box
        section = widgets.VBox([title_widget, divider] + widget_list)
        return section

    # Corrected assignments
    project_info_section = create_section("Project Data", [
        projloc_widget, project_type_dropdown, subcategory_dropdown, construct_widget, 
        one_two_way_widget, peak_period_widget
    ])

    highway_design_and_traffic_data_section = create_section("Highway Design and Traffic Data", [
        roadway_type_widgets, general_traffic_lanes_widgets, hov_hot_lanes_widgets, HOVRest_widget, 
        Exclusive_widget, free_flow_speed_widgets, ramp_design_speed_widgets, highway_segment_widgets, 
        impacted_length_widgets, ADT_current_widget, adt_base_widgets, adt_20_widget, hourly_hov_lane_traffic_widget, 
        percent_induced_trip_widget, percent_traffic_weave_widgets, percent_trucks_widget, truck_speed_widget, AVO_HOV_widget
    ])

    on_ramp_volume_section = create_section("On-Ramp Volume", [
        hourly_ramp_volume_widget, metering_strategy_widget 
    ])
    
    queue_formation_section = create_section("Queue Formation (if queuing or grade crossing project)",[arrival_rate_widgets])

    # Stack all sections vertically
    all_sections = widgets.VBox([project_info_section, highway_design_and_traffic_data_section, on_ramp_volume_section, queue_formation_section])

    # Display the stacked sections
    display(all_sections)
