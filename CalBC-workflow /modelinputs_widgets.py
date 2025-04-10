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
    
    
    
    
    
    
    
    
    
    
    # Highway Speed and Volume Inputs Section
    highway_speed_and_volume_input_section = create_section(
        highway_speed_and_volume_input_title,
        highway_speed_and_volume_input_subtitle,
        [HOV_vol_peak_widgets],
        highway_speed_and_volume_input_info
    )

    # Non-HOV Volume Widget
    
    
    all_sections = widgets.VBox([highway_speed_and_volume_input_section])
    
    display(all_sections)
    
    
    
    
    
    