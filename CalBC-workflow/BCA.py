import pandas as pd
import numpy as np
import ipywidgets as widgets
from ipywidgets import interact
from IPython.display import display, clear_output, HTML


pd.set_option('display.max_columns', None)  
pd.set_option('display.width', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.float_format', '{:.2f}'.format)




from travel_time import total_tt_benefit_widget
# from safety import total_safety_benefit_widget
# from emissions import total_emissions_benefit_widget



common_layout = widgets.Layout(
    width='450px', 
    background_color='#CCFFCC',  # Background color for all widgets
    padding='5px',
    border='2px solid gray'  # Border color and thickness
)


# Create the input widget for Total Cost
total_cost_widget = widgets.FloatText(
    value=1000000,
    description='Total Cost ($):',
    layout = common_layout,
    style={'description_width': 'initial'},
    disabled=False
)

total_benefit_widget = widgets.FloatText(
    value=0,
    description='Total Benefit ($):',
    layout = common_layout,
    style={'description_width': 'initial'},
    disabled=False
)

# Create the input widget for Total Cost
BCR_widget = widgets.FloatText(
    value=0.0,
    description='Benefit-Cost Ratio:',
    layout = common_layout,
    style={'description_width': 'initial'},
    disabled=True
)

# Display everything together
display(widgets.VBox([total_cost_widget, total_benefit_widget, BCR_widget]))


benefit_widgets = [
    total_tt_benefit_widget,
    # total_safety_benefit_widget,
    # total_emissions_benefit_widget,
]

def update_total_benefit(change=None):
    """Sum up all benefit widgets and update total_benefit_widget."""
    total = sum(w.value for w in benefit_widgets)
    total_benefit_widget.value =total  

# Set up observers to automatically update total benefit when any widget changes
for widget in benefit_widgets:
    widget.observe(update_total_benefit, names='value')




def calculate_benefit_cost_ratio(change, sum_by_year=None):
    total_cost = total_cost_widget.value
    total_benefit = total_benefit_widget.value  
    
    # Compute and assign BCR
    BCR_widget.value = total_benefit / total_cost if total_cost != 0 else float('inf')

# Observing widget changes and passing sum_by_year
total_cost_widget.observe(calculate_benefit_cost_ratio, names='value')
total_benefit_widget.observe(calculate_benefit_cost_ratio, names='value')



