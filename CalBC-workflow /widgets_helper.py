import ipywidgets as widgets

# Function to create info button with toggle popup feature
def info_button_popup(info_text):
    # Create an info button
    info_button = widgets.Button(description="i", button_style="info", tooltip="Click for more information",
                             layout=widgets.Layout(width="20px", height="20px", padding="0px", font_size="14px", justify_content="center", align_items="center", 
                                                   border="2px solid black",background_color="2px solid black", color="white", border_radius="50%", position="relative", 
                                                   top="-10px", left="10px"))

    # Create the content for the info popup (hidden by default)
    info_popup = widgets.HTML(value=f"<i style='line-height: 1.2; margin: 0;'>{info_text}</i>")
    info_popup.layout.display = 'none'  # Start with the popup hidden

    # Function to toggle popup visibility when the info button is clicked
    def on_info_button_click(b):
        # Toggle the visibility of the info popup
        if info_popup.layout.display == 'none':
            info_popup.layout.display = 'block'
        else:
            info_popup.layout.display = 'none'

    # Attach the click handler to the button
    info_button.on_click(on_info_button_click)

    return info_button, info_popup


def create_section(title, subtitle, widget_list, widget_info_list):
    # Create title and subtitle widgets
    title_widget = widgets.HTML(value=f"<b style='color: darkblue;'>{title}</b>")
    subtitle_widget = widgets.HTML(value=f"<i>{subtitle}</i>")

    # Divider between title/subtitle and the widgets
    divider = widgets.HTML(value="<hr>")

    # Section container to hold everything
    section = [title_widget, subtitle_widget, divider]

    # Add each widget with its corresponding info button
    for widget, info_text in zip(widget_list, widget_info_list):
        info_button, info_popup = info_button_popup(info_text)  # Create info button and popup
        section.append(widgets.HBox([widget, info_button]))  # Place widget and info button in the same row (HBox)
        section.append(info_popup)  # Add info popup under the widget

    # Create the section as a VBox and add spacing between items
    entire_section = widgets.VBox(section, layout=widgets.Layout(margin="5px 0"))  # Adds margin between sections

    # Return the entire section wrapped in a larger container (another VBox for layout if needed)
    return widgets.VBox([entire_section], layout=widgets.Layout(margin="10px 0"))  # Adds margin between sections



# Descriptive texts for project info section
project_info_title = "Project Data"
project_info_subtitle = "This section provides general information about the project and is used for highway, rail, and transit projects."
project_info_info = [
    "Choose from Northern, Southern and Rural California. This information is used to estimate peak traffic and emissions benefits.",
    "Please select the appropriate type of highway, rail, or transit project from the pull-down menu.",
    "Select the subcategory of the project.",
    "Insert the number of construction years before benefits begin. This must be a whole number.",
    "Indicate whether Highway Design and Traffic Data to be entered in Highway Design and Traffic Section is for a single direction or both directions of highway.",
    "Insert the number of peak period hours per typical day. The model provides a default of 5 hours (statewide average). Model estimates total % daily traffic occurring during peak period using a lookup table developed from Traffic Census data. Model does not distinguish between weekdays and weekends. To model a 24-hour HOV or HOT lane, enter 24 hours so peak is 100% of ADT. To model a ramp metering project, user should enter the number of hours per day that metering is operational."
]

# Descriptive texts for highway design and traffic data section
highway_design_and_traffic_data_title = "Highway Design and Traffic Data"
highway_design_and_traffic_data_subtitle = "Enter highway design and traffic data for highway projects. Data should align with one- or two-way responses in the Project Data Section. Some inputs have statewide default values."
highway_design_and_traffic_data_info = [
    "Indicate if the road is a freeway, expressway, or conventional highway in build and no build cases.",
    "Insert number of general purpose (not HOV or bus) lanes in both directions for build and no build cases.",
    "Insert number of HOV, HOT, or managed lanes in both directions for the build and no build cases. A value must be provided if an HOV restriction is entered on the next row.",
    "If highway facility has/will have HOV lanes, enter the HOV restriction (e.g., 2 means 2 people per vehicle). Must be entered for an HOV project. Enter for a non-HOV project, if facility has HOV lanes. Changes in HOV restrictions are special project types and handled automatically by model.",
    "If bus project, indicate yes or no whether buses have exclusive right-of-way. This information is used to estimate emissions.",
    "Insert free-flow speed for build and no build cases. Model assumes build is same as no build, if not entered.",
    "If auxiliary lane or off-ramp project, enter the design speed of the appropriate on- or off-ramp. This is used to estimate the speed of traffic affected by weaving.",
    "Insert segment length for build and no build cases. Model assumes build is same as no build, if not entered.",
    "The model estimates an area affected by the project. In most cases, this equals the segment length. Default affected area for passing lane projects, auxiliary lane, off-ramp projects, connectors and HOV drop ramps, are in the model. User can change these lengths.",
    "Enter Currrent Average Daily Traffic (ADT)",
    "For most projects, insert current two-way ADT on facility. For operational improvements, enter only the one-way ADT applicable to the project",
    "Insert projected ADT for 20 years after construction completion for build and no build cases. Make sure to account for induced demand, if applicable. The model assumes build is same as no build, if not entered. User can change base (Year 1) forecasts.",
    "Insert hourly HOV, HOT, or managed lane volumes for build and no build cases in a typical peak hour.",
    "Specify the percent of induced trips for the project.",
    "For operational improvements, insert % traffic affected by weaving. Model suggests a % based on the type of project. User can change values for project conditions.",
    "Insert estimated % of ADT comprised of trucks in build and no build cases. Model provides a default value (statewide average).",
    "If passing lane project, enter estimated speed (in MPH) for slow vehicles (trucks, recreational vehicles, etc.). Values must be entered for passing lane projects."
]

# Pavement Condition Section
pavement_condition_title = "Pavement Condition"
pavement_condition_subtitle = "For pavement rehabilitation projects"
pavement_condition_info = [
            "Enter the base (Year 1) International Roughness Index (IRI) for build and no-build scenarios.",
            "Model will calculate Year 20 values using standard parameters unless entered by user."
]


# On Ramp Volume Section
on_ramp_volume_title = "On-Ramp Volume"
on_ramp_volume_subtitle = "For Auxiliary Lane/On-Ramp Widening projects."
on_ramp_volume_info = ["Insert average hourly ramp volume to estimate traffic affected by weaving for auxiliary lanes and metering effectiveness for on-ramp widening. No entry needed for ramp metering projects.",
            "If on-ramp widening project, enter 1, 2, or 3 for vehicles allowed per green signal. Enter \"D\" for dual metering. No entry should be made for ramp metering projects."
]

# Queue Formation Section
queue_formation_title = "Queue Formation"
queue_formation_subtitle = "For Queuing and Rail Grade Crossing projects."
queue_formation_info = ["Enter Arrival Rate (vehicles/hour entering queue). Arrival rate applies only while the queue grows; dissipation is modeled automatically.",
        "For queuing and rail crossing projects, enter vehicles per hour leaving queue."
]


# Average Vehicle Occupancy (AVO) Section
avo_section_title = "Average Vehicle Occupancy (AVO)"
avo_section_subtitle = "Model provides default values. The figures change automatically, depending on presence of HOV lanes. Adjust if project-specific data are available."
avo_section_info = ["AVO General Traffic Non-Peak Build and No Build",
                    "AVO General Traffic Non-Peak Build and Build",
    "High Occupancy Vehicle  (if HOV/HOT lanes)"]

# Statewide Average Crash Rate Section
statewide_avg_crash_title = "Statewide Basic Average Crash Rate"
statewide_avg_crash_subtitle = "The model uses adjustment factors (the ratio of actual rates to statewide rates for existing facility) to estimate crash rates by crash type for the new road classification. Additional adjustments (crash savings) are made for highway TMS projects. Results are presented in the Model Inputs worksheet and can be changed by the user."
statewide_avg_crash_info = ["Include Base Rate if applicable",
                    "Insert statewide average crash rates per million vehicle-miles (or million vehicles, as appropriate) for build and no build highway rate groups. ",
    "Insert statewide % of fatal crashes for road classifications similar to build and no build facilities.",
                           "Insert statewide % of injury crashes for road classifications similar to build and no build facilities."]