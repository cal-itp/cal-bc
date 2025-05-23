import ipywidgets as widgets
from ipywidgets import Widget
from ipywidgets import interactive
from IPython.display import display, Markdown
from parameters import parameters
params = parameters()

from widgets_helper import (highway_speed_and_volume_input_nobuild_title, highway_speed_and_volume_input_nobuild_subtitle, highway_speed_and_volume_input_info, highway_speed_and_volume_input_build_title, highway_speed_and_volume_input_build_subtitle, ramp_and_arterial_input_title, ramp_and_arterial_input_subtitle, ramp_and_arterial_input_info, annual_person_trips_title, annual_person_trips_subtitle, annual_person_trips_info)

import projectinfo_widgets
from widgets_helper import info_button_popup, create_section, create_section_with_subsections

common_layout = widgets.Layout(
    width='450px', 
    background_color='#CCFFCC',  # Background color for all widgets
    padding='2px',
    border='2px solid gray'  # Border color and thickness
)



def create_modelinputs_widgets():
    global PHV1NB_widget, PHV1B_widget, PHV20NB_widget, PHV20B_widget, PNV1NB_widget,  \
    PNV1B_widget, PNV20NB_widget, PNV20B_widget, PWV1NB_widget, PWV1B_widget,  \
    PWV20NB_widget, PWV20B_widget, PTV1NB_widget, PTV1B_widget, PTV20NB_widget,  \
    PTV20B_widget, PRV1NB_widget, PRV1B_widget, PRV20NB_widget, PRV20B_widget,  \
    PAV1NB_widget, PAV1B_widget, PAV20NB_widget, PAV20B_widget, NNV1NB_widget,  \
    NNV1B_widget, NNV20NB_widget, NNV20B_widget, NWV1NB_widget, NWV1B_widget,  \
    NWV20NB_widget, NWV20B_widget, NTV1NB_widget, NTV1B_widget, NTV20NB_widget,  \
    NTV20B_widget, PHS1NB_widget, PHS1B_widget, PHS20NB_widget, PHS20B_widget,  \
    PNS1NB_widget, PNS1B_widget, PNS20NB_widget, PNS20B_widget, PWS1NB_widget,  \
    PWS1B_widget, PWS20NB_widget, PWS20B_widget, PTS1NB_widget, PTS1B_widget,  \
    PTS20NB_widget, PTS20B_widget, PRS1NB_widget, PRS1B_widget, PRS20NB_widget,  \
    PRS20B_widget, PAS1NB_widget, PAS1B_widget, PAS20NB_widget, PAS20B_widget,  \
    NNS1NB_widget, NNS1B_widget, NNS20NB_widget, NNS20B_widget, NWS1NB_widget,  \
    NWS1B_widget, NWS20NB_widget, NWS20B_widget, NTS1NB_widget, NTS1B_widget,  \
    NTS20NB_widget, NTS20B_widget, RADataAvail_widget, SegmentA_widget, SegmentR_widget,  \
    PNT1Ind_widget, PTT1Ind_widget, NNT1Ind_widget, NTT1Ind_widget, PNT20Ind_widget,  \
    PTT20Ind_widget, NNT20Ind_widget, NTT20Ind_widget




    
#     #Defining functions from Project Info for easy calculations
#     ProjLoc = projectinfo_widgets.projloc_widget.value
#     ProjType = projectinfo_widgets.subcategory_dropdown.value
#     Construct = projectinfo_widgets.construct_widget.value
#     NumDirections = projectinfo_widgets.one_two_way_widget.value
#     PeakLngthNB = projectinfo_widgets.peak_period_widget.value
#     RoadTypeNB = projectinfo_widgets.roadway_type_no_build_widget.value
#     RoadTypeB = projectinfo_widgets.roadway_type_build_widget.value
#     GenLanesNB = projectinfo_widgets.general_traffic_lanes_no_build_widget.value
#     GenLanesB = projectinfo_widgets.general_traffic_lanes_build_widget.value
#     HOVLanesNB = projectinfo_widgets.hov_hot_lanes_no_build_widget.value
#     HOVLanesB = projectinfo_widgets.hov_hot_lanes_build_widget.value
#     HOVRest = projectinfo_widgets.HOVRest_widget.value
#     Exclusive = projectinfo_widgets.Exclusive_widget.value
#     FFSpeedNB = projectinfo_widgets.free_flow_speed_no_build_widget.value
#     FFSpeedB = projectinfo_widgets.free_flow_speed_build_widget.value
#     RampFFSpdNB = projectinfo_widgets.ramp_design_speed_no_build_widget.value
#     RampFFSpdB = projectinfo_widgets.ramp_design_speed_build_widget.value
#     SegmentNB = projectinfo_widgets.highway_segment_no_build_widget.value
#     SegmentB = projectinfo_widgets.highway_segment_build_widget.value
#     ImpactedNB = projectinfo_widgets.impacted_length_no_build_widget.value
#     ImpactedB = projectinfo_widgets.impacted_length_build_widget.value
#     ADT0 = projectinfo_widgets.ADT_current_widget.value
#     ADT1NB = projectinfo_widgets.adt_base_year_no_build_widget.value
#     ADT1B = projectinfo_widgets.adt_base_year_build_widget.value
#     ADT20NB = projectinfo_widgets.ADT_20NB_widget.value
#     ADT20B = projectinfo_widgets.adt_20_year_build_widget.value
#     HOVvolNB = projectinfo_widgets.HOV_lane_nobuild_widget.value
#     HOVvolB = projectinfo_widgets.HOV_lane_build_widget.value
#     PerWeaveNB = projectinfo_widgets.percent_traffic_weave_no_build_widget.value
#     PerWeaveB = projectinfo_widgets.percent_traffic_weave_build_widget.value
#     PerIndHOV = projectinfo_widgets.percent_induced_trip_widget.value
#     PerTruckNB = projectinfo_widgets.percent_trucks_nobuild_widget.value
#     PerTruckB = projectinfo_widgets.percent_trucks_build_widget.value
#     TruckSpeed = projectinfo_widgets.truck_speed_widget.value
#     RampVolP = projectinfo_widgets.hourly_ramp_volume_peak_widget.value
#     RampVolNP = projectinfo_widgets.hourly_ramp_volume_nonpeak_widget.value
#     MeterStrat = projectinfo_widgets.metering_strategy_widget.value
#     ArrRate1 = projectinfo_widgets.arrival_rate_base_year_no_build_widget.value
#     ArrRate20 = projectinfo_widgets.arrival_rate_base_year_build_widget.value
#     DepRate1 = projectinfo_widgets.departure_rate_forecast_year_no_build_widget.value
#     DepRate20 = projectinfo_widgets.departure_rate_forecast_year_build_widget.value
#     IRI1NB = projectinfo_widgets.iri_base_year_no_build_widget.value
#     IRI1B = projectinfo_widgets.iri_base_year_build_widget.value
#     IRI20NB = projectinfo_widgets.iri_forecast_year_no_build_widget.value
#     IRI20B = projectinfo_widgets.iri_forecast_year_build_widget.value
#     AVONonNB = projectinfo_widgets.AVO_traffic_NP_no_build_widget.value
#     AVONonB = projectinfo_widgets.AVO_traffic_NP_build_widget.value
#     AVOPeakNB = projectinfo_widgets.AVO_traffic_P_no_build_widget.value
#     AVOPeakB = projectinfo_widgets.AVO_traffic_P_build_widget.value
#     AVOHovNB = projectinfo_widgets.AVOHovNB_widget.value
#     AVOHovB = projectinfo_widgets.AVOHovB_widget.value
#     GateTime1 = projectinfo_widgets.GateTime1_widget.value
#     GateTime20 = projectinfo_widgets.GateTime20_widget.value
#     NumTrain1 = projectinfo_widgets.NumTrain1_widget.value
#     NumTrain20 = projectinfo_widgets.NumTrain20_widget.value
#     TPerPeak = projectinfo_widgets.TPerPeak_widget.value
#     TPerHwy = projectinfo_widgets.TPerHwy_widget.value
#     TAPT1B = projectinfo_widgets.TAPT1B_widget.value
#     TAPT1NB = projectinfo_widgets.TAPT1NB_widget.value
#     TAPT20NB =  projectinfo_widgets.TAPT20NB_widget.value
#     TAPT20B = projectinfo_widgets.TAPT20B_widget.value
#     PerPeakADT = params.per_peak_adt
#     TMSLookup = params.TMSLookup
#     TMSAdj = params.tms_adj
#     roadway_capacity = params.roadway_capacity
#     roadway_capacity_non_HOV = params.roadway_capacity_non_HOV
#     MaxVC = params.MaxVC
#     AnnualFactor = params.AnnualFactor
#     SpeedWeaveAdj = params.SpeedWeaveAdj 
#     SpeedPavAdj = params.SpeedPavAdj
#     IdleSpeed = params.IdleSpeed
    
#     print(projectinfo_widgets.peak_period_widget.value)
#     print(PeakLngthNB)
    
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
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    PHV1NB_explaination_widget = widgets.Text(
        value=None,
        description="Reasons for Change:",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Function to update HOV Volume dynamically
    def update_HOV_Year1Peak_nobuild_Volume(change):
        ProjType = projectinfo_widgets.subcategory_dropdown.value
        HOVvolNB = projectinfo_widgets.HOV_lane_nobuild_widget.value
        PeakLngthNB = projectinfo_widgets.peak_period_widget.value
        PerWeaveNB = projectinfo_widgets.percent_traffic_weave_no_build_widget.value

        if ProjType == "Hwy-Rail Grade Crossing":
            HOV_Volume_Year1Peak_nobuild_Model = 0
        else:
            if ProjType in ["HOV Connector", "HOV Drop Ramp"]:
                HOV_Volume_Year1Peak_nobuild_Model = HOVvolNB * PeakLngthNB * (1 - PerWeaveNB)
            else:
                HOV_Volume_Year1Peak_nobuild_Model = HOVvolNB * PeakLngthNB

        HOV_Vol_year1peak_nobuild_modelcalc_widget.value = round(HOV_Volume_Year1Peak_nobuild_Model, 0)
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
    HOV_Vol_year1peak_nobuild_modelcalc_widget.observe(calculate_phv1nb, names='value')

    # Combine all widgets into a horizontal layout
    HOV_vol_year1peak_nobuild_widgets = widgets.HBox([
        HOV_Vol_year1peak_nobuild_modelcalc_widget,
        HOV_Vol_year1peak_nobuild_userchanged_widget,
        PHV1NB_widget,
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
    Non_HOV_Vol_year1peak_nobuild_modelcalc_widget = widgets.FloatText(
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
    def update_Non_HOV_Year1Peak_nobuild_Volume(change=None):
        # Initialize the volume with a default value (0)
        volume = 0

        # Get input values from the widgets
        ProjType = projectinfo_widgets.subcategory_dropdown.value
        PerWeaveNB = projectinfo_widgets.percent_traffic_weave_no_build_widget.value
        PerTruckNB = projectinfo_widgets.percent_trucks_nobuild_widget.value
        ADT1NB = projectinfo_widgets.adt_base_year_no_build_widget.value
        HOVvolNB = projectinfo_widgets.HOV_lane_nobuild_widget.value
        PeakLngthNB = projectinfo_widgets.peak_period_widget.value

        PerPeakADT = params.per_peak_adt
        TMSLookup = params.TMSLookup
        TMSAdj = params.tms_adj

        # Start the calculation based on the project type
        if ProjType == "Hwy-Rail Grade Crossing":
            volume = 0  # This is your default for this project type
        else:
            if ProjType in ["Auxiliary Lane", "Off-Ramp Widening"]:
                traffic_factor = PerWeaveNB
            else:
                traffic_factor = PerTruckNB

            # Fetch the TMS adjustment value
            TMS_value = TMSAdj.get(TMSLookup, {}).get("VolumeWithout", 1)

            # Perform the calculation
            volume = (PerPeakADT * ADT1NB) * (1 - traffic_factor) * TMS_value - HOVvolNB * PeakLngthNB

        # Update the widget with the calculated volume
        Non_HOV_Vol_year1peak_nobuild_modelcalc_widget.value = round(volume, 1)

        
    # Attach observers to update dynamically
    projectinfo_widgets.subcategory_dropdown.observe(update_Non_HOV_Year1Peak_nobuild_Volume, names='value')
    projectinfo_widgets.adt_base_year_no_build_widget.observe(update_Non_HOV_Year1Peak_nobuild_Volume, names='value')
    projectinfo_widgets.ADT_20NB_widget.observe(update_Non_HOV_Year1Peak_nobuild_Volume, names='value')
    projectinfo_widgets.ADT_current_widget.observe(update_Non_HOV_Year1Peak_nobuild_Volume, names='value')
    projectinfo_widgets.percent_traffic_weave_no_build_widget.observe(update_Non_HOV_Year1Peak_nobuild_Volume, names='value')
    projectinfo_widgets.percent_trucks_nobuild_widget.observe(update_Non_HOV_Year1Peak_nobuild_Volume, names='value')
    projectinfo_widgets.HOV_lane_nobuild_widget.observe(update_Non_HOV_Year1Peak_nobuild_Volume, names='value')
    projectinfo_widgets.peak_period_widget.observe(update_Non_HOV_Year1Peak_nobuild_Volume, names='value')
    

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
    Non_HOV_Vol_year1peak_nobuild_modelcalc_widget.observe(calculate_pnv1nb, names='value')

    # Combine for layout
    Non_HOV_vol_year1peak_nobuild_widgets = widgets.HBox([
        Non_HOV_Vol_year1peak_nobuild_modelcalc_widget,
        Non_HOV_Vol_year1peak_nobuild_userchanged_widget,
        PNV1NB_widget,
        PNV1NB_explanation_widget
    ])
     
    
    ###################################################################    
    # Weaving Volume (Calculated by Model)
    weaving_volume_year1peak_nobuild_modelcalc_widget = widgets.FloatText(
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
    def update_weaving_year1peak_nobuild_volume(change=None):
        TMSLookup = params.TMSLookup
        TMSAdj = params.tms_adj
        ProjType = projectinfo_widgets.subcategory_dropdown.value
        PerPeakADT = params.per_peak_adt
        ADT1NB = projectinfo_widgets.adt_base_year_no_build_widget.value
        PerWeaveNB = projectinfo_widgets.percent_traffic_weave_no_build_widget.value
        PerTruckNB = projectinfo_widgets.percent_trucks_nobuild_widget.value
        RampVolP = projectinfo_widgets.hourly_ramp_volume_peak_widget.value
        PeakLngthNB = projectinfo_widgets.peak_period_widget.value
        HOVvolNB = projectinfo_widgets.HOV_lane_nobuild_widget.value

        TMS_value = TMSAdj.get(TMSLookup, {}).get("VolumeWithout", 1)

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
    weaving_volume_year1peak_nobuild_modelcalc_widget.observe(calculate_pwv1nb, names='value')


    # Display layout
    Weaving_Volume_year1peak_nobuild_widgets = widgets.HBox([
        weaving_volume_year1peak_nobuild_modelcalc_widget,
        weaving_volume_year1peak_nobuild_userchanged_widget,
        PWV1NB_widget,
        PWV1NB_explanation_widget
    ])

    
    ###################################################################    
    # Truck Volume (Calculated by Model)
    truck_volume_year1peak_nobuild_modelcalc_widget = widgets.FloatText(
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
    def update_truck_volume_year1peak_nobuild(change=None):
        TMSLookup = params.TMSLookup
        TMSAdj = params.tms_adj
        ProjType = projectinfo_widgets.subcategory_dropdown.value
        PerPeakADT = params.per_peak_adt
        ADT1NB = projectinfo_widgets.adt_base_year_no_build_widget.value
        PerTruckNB = projectinfo_widgets.percent_trucks_nobuild_widget.value

        TMS_value = TMSAdj.get(TMSLookup, {}).get("VolumeWithout", 1)

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
    truck_volume_year1peak_nobuild_modelcalc_widget.observe(calculate_ptv1nb, names='value')

    # Layout for display
    Truck_Volume_year1peak_nobuild_widgets = widgets.HBox([
        truck_volume_year1peak_nobuild_modelcalc_widget,
        truck_volume_year1peak_nobuild_userchanged_widget,
        PTV1NB_widget,
        PTV1NB_explanation_widget
    ])

    
    ###################################################################     
    # Non-HOV Speed widgets 
    nonhov_speed_year1peak_nobuild_modelcalc_widget = widgets.FloatText(
        value=0.0,
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

    PNS1NB_widget = widgets.FloatText(
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
        ProjType = projectinfo_widgets.subcategory_dropdown.value
        PeakLngthNB = projectinfo_widgets.peak_period_widget.value
        DepRate1 = projectinfo_widgets.departure_rate_forecast_year_no_build_widget.value
        ArrRate1 = projectinfo_widgets.arrival_rate_base_year_no_build_widget.value
        ADT1NB = projectinfo_widgets.adt_base_year_no_build_widget.value
        PerPeakADT = params.per_peak_adt
        ImpactedNB = projectinfo_widgets.impacted_length_no_build_widget.value
        FFSpeedNB = projectinfo_widgets.free_flow_speed_no_build_widget.value
        HOVLanesNB = projectinfo_widgets.hov_hot_lanes_no_build_widget.value
        GenLanesNB = projectinfo_widgets.general_traffic_lanes_no_build_widget.value
        IRI1NB = projectinfo_widgets.iri_base_year_no_build_widget.value
        TruckSpeed = projectinfo_widgets.truck_speed_widget.value
        PerWeaveNB = projectinfo_widgets.percent_traffic_weave_no_build_widget.value

        TMSLookup = params.TMSLookup
        TMSAdj = params.tms_adj
        SpeedWeaveAdj = params.SpeedWeaveAdj
        SpeedPavAdj = params.SpeedPavAdj
        MaxVC = params.MaxVC
        roadway_capacity_non_HOV = params.roadway_capacity_non_HOV

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
                TMS_value = TMSAdj.get(TMSLookup, {}).get("SpeedWithout", 1)

                volume_term = flow_sum / (GenLanesNB * GenLaneCapNB * PeakLngthNB)
                delay_speed = FFSpeedNB / (1 + GenAlphaNB * min(volume_term, MaxVC) ** GenBetaNB)

                base_speed = delay_speed * TMS_value

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
    nonhov_speed_year1peak_nobuild_modelcalc_widget.observe(calculate_pns1nb, names='value')

    NonHOV_speed_year1peak_nobuild_widgets = widgets.HBox([
        nonhov_speed_year1peak_nobuild_modelcalc_widget,
        nonhov_speed_year1peak_nobuild_userchanged_widget,
        PNS1NB_widget,
        PNS1NB_explanation_widget
    ])


    ###################################################################     
    # HOV Speed widgets 
    hov_speed_year1peak_nobuild_modelcalc_widget = widgets.FloatText(
        value=0.0,
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

    PHS1NB_widget = widgets.FloatText(
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
        ProjType = projectinfo_widgets.subcategory_dropdown.value
        PeakLngthNB = projectinfo_widgets.peak_period_widget.value
        DepRate1 = projectinfo_widgets.departure_rate_forecast_year_no_build_widget.value
        ArrRate1 = projectinfo_widgets.arrival_rate_base_year_no_build_widget.value
        ADT1NB = projectinfo_widgets.adt_base_year_no_build_widget.value
        PerPeakADT = params.per_peak_adt
        ImpactedNB = projectinfo_widgets.impacted_length_no_build_widget.value
        FFSpeedNB = projectinfo_widgets.free_flow_speed_no_build_widget.value
        HOVLanesNB = projectinfo_widgets.hov_hot_lanes_no_build_widget.value
        IRI1NB = projectinfo_widgets.iri_base_year_no_build_widget.value
        SpeedPavAdj = params.SpeedPavAdj
        roadway_capacity = params.roadway_capacity
        MaxVC = params.MaxVC

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
    hov_speed_year1peak_nobuild_modelcalc_widget.observe(calculate_phs1nb, names='value')

    HOV_Speed_year1peak_nobuild_widgets = widgets.HBox([
        hov_speed_year1peak_nobuild_modelcalc_widget,
        hov_speed_year1peak_nobuild_userchanged_widget,
        PHS1NB_widget,
        PHS1NB_explanation_widget
    ])


    ###################################################################    
    # Weaving Speed widgets 
    weave_speed_year1peak_nobuild_modelcalc_widget = widgets.FloatText(
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

    PWS1NB_widget = widgets.FloatText(
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
        ProjType = projectinfo_widgets.subcategory_dropdown.value
        NumDirections = projectinfo_widgets.one_two_way_widget.value
        PeakLngthNB = projectinfo_widgets.peak_period_widget.value
        SegmentNB = projectinfo_widgets.highway_segment_no_build_widget.value
        RampFFSpdNB = projectinfo_widgets.ramp_design_speed_no_build_widget.value
        TMSLookup = params.TMSLookup
        TMSAdj = params.tms_adj
        IRI1NB = projectinfo_widgets.iri_base_year_no_build_widget.value
        SpeedPavAdj = params.SpeedPavAdj
        FFSpeedNB = projectinfo_widgets.free_flow_speed_no_build_widget.value

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
    weave_speed_year1peak_nobuild_modelcalc_widget.observe(calculate_pws1nb, names='value')

    Weave_Speed_year1peak_nobuild_widgets = widgets.HBox([
        weave_speed_year1peak_nobuild_modelcalc_widget,
        weave_speed_year1peak_nobuild_userchanged_widget,
        PWS1NB_widget,
        PWS1NB_explanation_widget
    ])
    


    
    ###################################################################    
    # Truck Speed widgets 
    truck_speed_year1peak_nobuild_modelcalc_widget = widgets.FloatText(
        value=0.0,
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

    PTS1NB_widget = widgets.FloatText(
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
        ProjType = projectinfo_widgets.subcategory_dropdown.value
        TruckSpeed = projectinfo_widgets.truck_speed_widget.value
        IRI1NB = projectinfo_widgets.iri_base_year_no_build_widget.value
        SpeedPavAdj = params.SpeedPavAdj

        PTV1NB = PTV1NB_widget.value
        PWS1NB = PWS1NB_widget.value
        PNS1NB = PNS1NB_widget.value

        if PTV1NB == 0:
            truck_speed = 55
        else:
            base_speed = PWS1NB if ProjType in ["Auxiliary Lane", "Off-Ramp Widening"] else PNS1NB

            if ProjType == "Pavement":
                iri_keys = [k for k in SpeedPavAdj if k <= IRI1NB]
                closest_iri = max(iri_keys) if iri_keys else 0

                pavement_divisor = SpeedPavAdj[closest_iri]["Truck"]
                adjusted_speed = min(TruckSpeed, base_speed / pavement_divisor)
                pavement_multiplier = SpeedPavAdj[closest_iri]["Truck"]
                truck_speed = adjusted_speed * pavement_multiplier
            else:
                truck_speed = min(TruckSpeed, base_speed)

        truck_speed_year1peak_nobuild_modelcalc_widget.value = round(truck_speed, 1)

    

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
    truck_speed_year1peak_nobuild_modelcalc_widget.observe(calculate_pts1nb, names='value')

    Truck_Speed_year1peak_nobuild_widgets = widgets.HBox([
        truck_speed_year1peak_nobuild_modelcalc_widget,
        truck_speed_year1peak_nobuild_userchanged_widget,
        PTS1NB_widget,
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
        ProjType = projectinfo_widgets.subcategory_dropdown.value
        ArrRate1 = projectinfo_widgets.arrival_rate_base_year_no_build_widget.value
        GateTime1 = projectinfo_widgets.GateTime1_widget.value
        DepRate1 = projectinfo_widgets.departure_rate_forecast_year_no_build_widget.value
        NumTrain1 = projectinfo_widgets.NumTrain1_widget.value
        AnnualFactor = params.AnnualFactor
        PerTruckNB = projectinfo_widgets.percent_trucks_nobuild_widget.value
        PerWeaveNB = projectinfo_widgets.percent_traffic_weave_no_build_widget.value
        PerPeakADT = params.per_peak_adt
        ADT1NB = projectinfo_widgets.adt_base_year_no_build_widget.value

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
        Non_HOV_Vol_year1nonpeak_modelcalc_widget.value = round(result, 0)
    
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
    Non_HOV_Vol_year1nonpeak_modelcalc_widget.observe(calculate_nnv1nb, names='value')

    # Combine all widgets into a horizontal layout for HOV Volume
    Non_HOV_vol_year1nonpeak_widgets = widgets.HBox([Non_HOV_Vol_year1nonpeak_modelcalc_widget, Non_HOV_Vol_year1nonpeak_userchanged_widget, NNV1NB_widget, NNV1NB_explanation_widget])
    
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
        ProjType = projectinfo_widgets.subcategory_dropdown.value
        PerPeakADT = params.per_peak_adt
        PerWeaveNB = projectinfo_widgets.percent_traffic_weave_no_build_widget.value
        PerTruckNB = projectinfo_widgets.percent_trucks_nobuild_widget.value
        RampVolNP = projectinfo_widgets.hourly_ramp_volume_nonpeak_widget.value
        ADT1NB = projectinfo_widgets.adt_base_year_no_build_widget.value
        PeakLngthNB = projectinfo_widgets.peak_period_widget.value

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
    weaving_volume_year1nonpeak_modelcalc_widget.observe(calculate_nwv1nb, names='value')

    # Combine all widgets into a horizontal layout for HOV Volume
    Weaving_volume_year1nonpeak_widgets = widgets.HBox([weaving_volume_year1nonpeak_modelcalc_widget, weaving_volume_year1nonpeak_userchanged_widget, NWV1NB_widget, NWV1NB_explanation_widget])
    
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
        # Define variables from widgets and parameters
        ProjType = projectinfo_widgets.subcategory_dropdown.value
        ArrRate1 = projectinfo_widgets.arrival_rate_base_year_no_build_widget.value
        GateTime1 = projectinfo_widgets.GateTime1_widget.value
        NumTrain1 = projectinfo_widgets.NumTrain1_widget.value
        DepRate1 = projectinfo_widgets.departure_rate_forecast_year_no_build_widget.value
        AnnualFactor = params.AnnualFactor
        PerTruckNB = projectinfo_widgets.percent_trucks_nobuild_widget.value
        PerPeakADT = params.per_peak_adt
        ADT1NB = projectinfo_widgets.adt_base_year_no_build_widget.value

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
    truck_volume_year1nonpeak_modelcalc_widget.observe(calculate_ntv1nb, names='value')

    # Combine all widgets into a horizontal layout for HOV Volume
    Truck_volume_year1nonpeak_widgets = widgets.HBox([truck_volume_year1nonpeak_modelcalc_widget, truck_volume_year1nonpeak_userchanged_widget, NTV1NB_widget, NTV1NB_explanation_widget])
    
    
    ###################################################################    
    #Non-HOV Speed widgets 
    nonhov_speed_year1nonpeak_modelcalc_widget = widgets.FloatText(
        value=0.0,  # Set initial value to 0 or any other valid integer
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
    NNS1NB_widget = widgets.FloatText(
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
        ProjType = projectinfo_widgets.subcategory_dropdown.value
        GenLanesNB = projectinfo_widgets.general_traffic_lanes_no_build_widget.value
        HOVLanesNB = projectinfo_widgets.hov_hot_lanes_no_build_widget.value
        FFSpeedNB = projectinfo_widgets.free_flow_speed_no_build_widget.value
        TruckSpeed = projectinfo_widgets.truck_speed_widget.value
        PerWeaveNB = projectinfo_widgets.percent_traffic_weave_no_build_widget.value
        SpeedWeaveAdj = params.SpeedWeaveAdj
        SpeedPavAdj = params.SpeedPavAdj
        IdleSpeed = params.IdleSpeed
        roadway_capacity_non_HOV = params.roadway_capacity_non_HOV
        MaxVC = params.MaxVC
        NNV1NB = NNV1NB_widget.value
        NWV1NB = NWV1NB_widget.value
        NTV1NB = NTV1NB_widget.value
        PeakLngthNB = projectinfo_widgets.peak_period_widget.value

        
        GenAlphaNB = roadway_capacity_non_HOV["Non-HOV Lanes"]["No Build"]["GenAlphaNB"]
        GenBetaNB = roadway_capacity_non_HOV["Non-HOV Lanes"]["No Build"]["GenBetaNB"]
        GenLaneCapNB = roadway_capacity_non_HOV["Non-HOV Lanes"]["No Build"]["GenLaneCapNB"]
        
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
        try:
            val = float(nonhov_speed_year1nonpeak_userchanged_widget.value)
            updated_speed = max(val, 5)
        except:
            updated_speed = max(nonhov_speed_year1nonpeak_modelcalc_widget.value, 5)

        NNS1NB_widget.value = updated_speed

    # Link the PHV1NB widget update to changes in HOV_Vol_peak_userchanged_widget
    nonhov_speed_year1nonpeak_userchanged_widget.observe(calculate_nns1nb, names='value')
    nonhov_speed_year1nonpeak_modelcalc_widget.observe(calculate_nns1nb, names='value')

    # Combine all widgets into a horizontal layout for HOV Volume
    NonHOV_speed_year1nonpeak_widgets = widgets.HBox([nonhov_speed_year1nonpeak_modelcalc_widget, nonhov_speed_year1nonpeak_userchanged_widget, NNS1NB_widget, NNS1NB_widget, NNS1NB_explanation_widget])
    
    
    

    
    ###################################################################    
    
    # Weaving Non Peak Speed widgets 
    weave_speed_year1nonpeak_modelcalc_widget = widgets.FloatText(
        value=0.0,  # Set initial value to 0 or any other valid integer
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
    NWS1NB_widget = widgets.FloatText(
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
        # Retrieve relevant widget values
        NWV1NB = NWV1NB_widget.value
        NNS1NB = NNS1NB_widget.value
        NTV1NB = NTV1NB_widget.value

        # Retrieve project information values
        ProjType = projectinfo_widgets.subcategory_dropdown.value
        FFSpeedNB = projectinfo_widgets.free_flow_speed_no_build_widget.value
        RampFFSpdNB = projectinfo_widgets.ramp_design_speed_no_build_widget.value
        SegmentNB = projectinfo_widgets.highway_segment_no_build_widget.value
        NumDirections = projectinfo_widgets.one_two_way_widget.value
        PeakLngthNB = projectinfo_widgets.peak_period_widget.value
        SpeedPavAdj = params.SpeedPavAdj
        IRI1NB = projectinfo_widgets.iri_base_year_no_build_widget.value

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
 
    # Function to calculate NWS1NB        
    def calculate_nws1nb(change):
        try:
            val = float(weave_speed_year1nonpeak_userchanged_widget.value)
            updated_speed = max(val, 5)
        except:
            updated_speed = max(weave_speed_year1nonpeak_modelcalc_widget.value, 5)

        NWS1NB_widget.value = updated_speed

    # Link the PHV1NB widget update to changes in HOV_Vol_peak_userchanged_widget
    weave_speed_year1nonpeak_userchanged_widget.observe(calculate_nws1nb, names='value')
    weave_speed_year1nonpeak_modelcalc_widget.observe(calculate_nws1nb, names='value')

    # Combine all widgets into a horizontal layout for HOV Volume
    Weave_speed_year1nonpeak_widgets = widgets.HBox([weave_speed_year1nonpeak_modelcalc_widget, weave_speed_year1nonpeak_userchanged_widget, NWS1NB_widget, NWS1NB_explanation_widget])

    ###################################################################
    # Truck Non Peak Speed widgets 
    truck_speed_year1nonpeak_modelcalc_widget = widgets.FloatText(
        value=0.0,  # Set initial value to 0 or any other valid integer
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
    NTS1NB_widget = widgets.FloatText(
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
        ProjType = projectinfo_widgets.subcategory_dropdown.value
        IRI1NB = projectinfo_widgets.iri_base_year_no_build_widget.value
        TruckSpeed = projectinfo_widgets.truck_speed_widget.value
        IdleSpeed = params.IdleSpeed
        SpeedPavAdj = params.SpeedPavAdj
        
        # Retrieve relevant widget values
        NTV1NB = NTV1NB_widget.value
        NWS1NB = NWS1NB_widget.value
        NNS1NB = NNS1NB_widget.value


        if ProjType == "Hwy-Rail Grade Crossing":
            truck_speed = IdleSpeed
        elif NTV1NB == 0:
            truck_speed = 55
        else:
            # Use NWS1NB if it's Auxiliary or Off-Ramp, otherwise use NNS1NB
            base_speed = NWS1NB if ProjType in ["Auxiliary Lane", "Off-Ramp Widening"] else NNS1NB

            if ProjType == "Pavement":
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
    truck_speed_year1nonpeak_modelcalc_widget.observe(calculate_nts1nb, names='value')
    
    # Combine all the Non HOV Speed widgets into a horizontal layout for display
    Truck_speed_year1nonpeak_widgets = widgets.HBox([truck_speed_year1nonpeak_modelcalc_widget, truck_speed_year1nonpeak_userchanged_widget, NTS1NB_widget, NTS1NB_explanation_widget])     
    
    
######################################################################################################################################################################
################################################## Year 20 ##################################################
############################### Peak Period ###############################
   
    # Create the HOV Volume widget to display the calculated value
    HOV_Vol_year20peak_modelcalc_widget = widgets.FloatText(
        value=0.0,  # Set initial value to 0, or any other valid integer
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
        # Retrieve relevant widget values from the provided list
        ProjType = projectinfo_widgets.subcategory_dropdown.value
        PeakLngthNB = projectinfo_widgets.peak_period_widget.value
        ADT1NB = projectinfo_widgets.adt_base_year_no_build_widget.value
        DepRate1 = projectinfo_widgets.departure_rate_forecast_year_no_build_widget.value
        ADT20NB = projectinfo_widgets.ADT_20NB_widget.value
        PerPeakADT = params.per_peak_adt
        PerWeaveNB = projectinfo_widgets.percent_traffic_weave_no_build_widget.value
        HOVvolNB = projectinfo_widgets.HOV_lane_nobuild_widget.value

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
        HOV_Vol_year20peak_modelcalc_widget.value = round(HOV_Volume_Year20Peak_Model, 2)

            
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
        try:
            val = float(HOV_Vol_year20peak_userchanged_widget.value)
            if val >= 0:
                PHV20NB = val
            else:
                PHV20NB = HOV_Vol_year20peak_modelcalc_widget.value
        except:
            PHV20NB = HOV_Vol_year20peak_modelcalc_widget.value

        PHV20NB_widget.value = PHV20NB
        

    # Link the PHV1NB widget update to changes in HOV_Vol_peak_userchanged_widget
    HOV_Vol_year20peak_userchanged_widget.observe(calculate_phv20nb, names='value')
    HOV_Vol_year20peak_modelcalc_widget.observe(calculate_phv20nb, names='value')

    # Combine all widgets into a horizontal layout for HOV Volume
    HOV_vol_year20peak_widgets = widgets.HBox([HOV_Vol_year20peak_modelcalc_widget, HOV_Vol_year20peak_userchanged_widget, PHV20NB_widget, PHV20NB_explaination_widget])


    
    
    ###################################################################    
  
    # Create the Non-HOV Volume widget to display the calculated value
    Non_HOV_Vol_year20peak_modelcalc_widget = widgets.FloatText(
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

    def update_Non_HOV_Year20Peak_Volume(change=None):
        # Retrieve relevant widget values from the provided list
        ProjType = projectinfo_widgets.subcategory_dropdown.value
        PeakLngthNB = projectinfo_widgets.peak_period_widget.value
        ADT1NB = projectinfo_widgets.adt_base_year_no_build_widget.value
        DepRate1 = projectinfo_widgets.departure_rate_forecast_year_no_build_widget.value
        ADT20NB = projectinfo_widgets.ADT_20NB_widget.value
        PerPeakADT = params.per_peak_adt
        PerWeaveNB = projectinfo_widgets.percent_traffic_weave_no_build_widget.value
        PerTruckNB = projectinfo_widgets.percent_trucks_nobuild_widget.value
        HOVvolNB = projectinfo_widgets.HOV_lane_nobuild_widget.value
        DepRate20 = projectinfo_widgets.departure_rate_forecast_year_build_widget.value
        TMSLookup = params.TMSLookup
        TMSAdj = params.tms_adj


        # Check if project type is "Hwy-Rail Grade Crossing"
        if ProjType == "Hwy-Rail Grade Crossing":
            Non_HOV_Volume_Year20Peak = 0  # Set volume to 0 for this project type

        # If the project type is "Queuing"
        elif ProjType == "Queuing":
            # Calculate the numerator and denominator for the queuing formula
            numerator = PeakLngthNB * (DepRate1 - ADT1NB * (1 - PerPeakADT) / (24 - PeakLngthNB))
            denominator = (
                (ADT1NB / ADT20NB) * DepRate20 -
                ADT1NB * (1 - PerPeakADT) / (24 - PeakLngthNB)
            )
            # Base volume calculation
            if denominator != 0:
                base_volume = (numerator / denominator) * DepRate20
            else:
                base_volume = 0
            Non_HOV_Volume_Year20Peak = base_volume  # Set the calculated base volume

        # For other project types, calculate based on ADT20NB
        else:
            Non_HOV_Volume_Year20Peak = PerPeakADT * ADT20NB

        # Apply volume adjustment factor based on the project type
        if ProjType in ["Auxiliary Lane", "Off-Ramp Widening"]:
            adj_factor = 1 - PerWeaveNB  # Weave adjustment for these project types
        else:
            adj_factor = 1 - PerTruckNB  # Truck adjustment for other project types

        if ProjType == "Queuing":
            adj_factor -= (HOVvolNB / DepRate20 if DepRate20 != 0 else 0)  # Adjust for HOV volume in queuing

        # Apply TMS adjustment
        tms_factor = TMSAdj.get(TMSLookup, {}).get("VolumeWithout", 1)

        # Final volume calculation
        Non_HOV_Volume_Year20Peak *= adj_factor * tms_factor

        # Final adjustment to subtract HOV volume, except for "Queuing" project type
        if ProjType != "Queuing":
            Non_HOV_Volume_Year20Peak -= HOVvolNB * PeakLngthNB

        # Update the widget with the calculated volume, rounded to one decimal place
        Non_HOV_Vol_year20peak_modelcalc_widget.value = round(Non_HOV_Volume_Year20Peak, 1)

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
        try:
            val = float(Non_HOV_Vol_year20peak_userchanged_widget.value)
            if val >= 0:
                PNV20NB = val
            else:
                PNV20NB = Non_HOV_Vol_year20peak_modelcalc_widget.value
        except:
            PNV20NB = Non_HOV_Vol_year20peak_modelcalc_widget.value
            
        PNV20NB_widget.value = PNV20NB 
            

    # Link the PNV1NB widget update to changes in Non-HOV Volume Peak User widget
    Non_HOV_Vol_year20peak_modelcalc_widget.observe(calculate_pnv20nb, names='value')
    Non_HOV_Vol_year20peak_userchanged_widget.observe(calculate_pnv20nb, names='value')    

    # Combine all the Non-HOV volume widgets into a horizontal layout for display
    Non_HOV_vol_year20peak_widgets = widgets.HBox([Non_HOV_Vol_year20peak_modelcalc_widget, Non_HOV_Vol_year20peak_userchanged_widget, PNV20NB_widget, PNV20NB_explanation_widget])
    
    ###################################################################
       
    # Weaving Volume (Calculated by Model)
    weaving_volume_year20peak_modelcalc_widget = widgets.FloatText(
        value=0.0,  # Set initial value to 0 or any other valid integer
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
    def update_weaving_year20peak_volume(change=None):
        # Retrieve relevant widget values from the provided list
        ProjType = projectinfo_widgets.subcategory_dropdown.value
        PerPeakADT = params.per_peak_adt
        ADT20NB = projectinfo_widgets.ADT_20NB_widget.value
        PerWeaveNB = projectinfo_widgets.percent_traffic_weave_no_build_widget.value
        PerTruckNB = projectinfo_widgets.percent_trucks_nobuild_widget.value
        TMSLookup = params.TMSLookup
        TMSAdj = params.tms_adj
        RampVolP = projectinfo_widgets.hourly_ramp_volume_peak_widget.value
        PeakLngthNB = projectinfo_widgets.peak_period_widget.value
        HOVvolNB = projectinfo_widgets.HOV_lane_nobuild_widget.value

        # Look up the TMS adjustment factor
        TMS_value = TMSAdj.get(TMSLookup, {}).get("VolumeWithout", 1)

        # Initialize total weaving volume model for year 20 peak
        Weaving_Volume_Model_20peak = 0

        # First condition
        if ProjType in ["Auxiliary Lane", "Off-Ramp Widening"]:
            Weaving_Volume_Model_20peak += (PerPeakADT * ADT20NB) * (PerWeaveNB - PerTruckNB) * TMS_value

        # Second condition
        if ProjType == "Auxiliary Lane":
            Weaving_Volume_Model_20peak += RampVolP * PeakLngthNB

        # Third condition
        if ProjType in ["HOV Connector", "HOV Drop Ramp"]:
            Weaving_Volume_Model_20peak += PerWeaveNB * HOVvolNB * PeakLngthNB

        # Update the widget with the calculated value
        weaving_volume_year20peak_modelcalc_widget.value = round(Weaving_Volume_Model_20peak, 0)

        
    # Link the update function to changes in relevant widgets
    projectinfo_widgets.ADT_20NB_widget.observe(update_weaving_year20peak_volume, names='value')
    projectinfo_widgets.ADT_20NB_widget.observe(update_weaving_year20peak_volume, names='value')
    projectinfo_widgets.percent_traffic_weave_no_build_widget.observe(update_weaving_year20peak_volume, names='value')
    projectinfo_widgets.percent_traffic_weave_build_widget.observe(update_weaving_year20peak_volume, names='value')
    projectinfo_widgets.percent_trucks_nobuild_widget.observe(update_weaving_year20peak_volume, names='value')
    projectinfo_widgets.hourly_ramp_volume_peak_widget.observe(update_weaving_year20peak_volume, names='value')
    projectinfo_widgets.peak_period_widget.observe(update_weaving_year20peak_volume, names='value')
    projectinfo_widgets.HOV_lane_nobuild_widget.observe(update_weaving_year20peak_volume, names='value')
    projectinfo_widgets.subcategory_dropdown.observe(update_weaving_year20peak_volume, names='value') 
        
 # Non-HOV PNV1NB update function (similar to PwV20NB)        
    def calculate_pwv20nb(change):
        try:
            val = float(weaving_volume_year20peak_userchanged_widget.value)
            if val >= 0:
                PWV20NB = val
            else:
                PWV20NB = weaving_volume_year20peak_modelcalc_widget.value
        except:
            PWV20NB = weaving_volume_year20peak_modelcalc_widget.value

        PWV20NB_widget.value = PWV20NB
        

    # Link the PNV1NB widget update to changes in Non-HOV Volume Peak User widget
    weaving_volume_year20peak_modelcalc_widget.observe(calculate_pwv20nb, names='value')
    weaving_volume_year20peak_userchanged_widget.observe(calculate_pwv20nb, names='value')    

    # Combine all the Non-HOV volume widgets into a horizontal layout for display
    Weaving_Volume_year20peak_widgets = widgets.HBox([weaving_volume_year20peak_modelcalc_widget, weaving_volume_year20peak_userchanged_widget, PWV20NB_widget, PWV20NB_explanation_widget])
        

    ###################################################################
    # Truck Volume (Calculated by Model)
    truck_volume_year20peak_modelcalc_widget = widgets.FloatText(
        value=0.0,  # Set initial value to 0 or any other valid integer
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
    def update_truck_peakyear20_volume(change=None):
        # Retrieve relevant widget values
        ProjType = projectinfo_widgets.subcategory_dropdown.value
        PeakLngthNB = projectinfo_widgets.peak_period_widget.value
        DepRate1 = projectinfo_widgets.departure_rate_forecast_year_no_build_widget.value
        ADT1NB = projectinfo_widgets.adt_base_year_no_build_widget.value
        ADT20NB = projectinfo_widgets.ADT_20NB_widget.value
        PerPeakADT = params.per_peak_adt
        PerTruckNB = projectinfo_widgets.percent_trucks_nobuild_widget.value
        TMSLookup = params.TMSLookup
        TMSAdj = params.tms_adj

        # Look up the TMS volume adjustment factor
        TMS_value = TMSAdj.get(TMSLookup, {}).get("VolumeWithout", 1)

        # Check if it's a Highway Rail Grade Crossing project
        if ProjType == "Hwy-Rail Grade Crossing":
            truck_volume = 0
        else:
            if ProjType == "Queuing":
                # Calculate the base truck volume for the "Queuing" project type
                numerator = PeakLngthNB * (DepRate1 - ADT1NB * (1 - PerPeakADT) / (24 - PeakLngthNB))
                denominator = ((ADT1NB / ADT20NB) * DepRate20 - ADT1NB * (1 - PerPeakADT) / (24 - PeakLngthNB))
                if denominator != 0:  # Prevent division by zero
                    base_volume = (numerator / denominator) * DepRate20
                else:
                    base_volume = 0  # If denominator is zero, set base_volume to 0
            else:
                base_volume = PerPeakADT * ADT20NB

            # Multiply by the truck percentage and TMS adjustment
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
        try:
            val = float(truck_volume_year20peak_userchanged_widget.value)
            if val >= 0:
                PTV20NB = val
            else:
                PTV20NB = truck_volume_year20peak_modelcalc_widget.value
        except:
            PTV20NB = truck_volume_year20peak_modelcalc_widget.value

        PTV20NB_widget.value = PTV20NB

    # Link the PNV1NB widget update to changes in Non-HOV Volume Peak User widget
    truck_volume_year20peak_modelcalc_widget.observe(calculate_ptv20nb, names='value')
    truck_volume_year20peak_userchanged_widget.observe(calculate_ptv20nb, names='value')    

    # Combine all the Non-HOV volume widgets into a horizontal layout for display
    Truck_Volume_year20peak_widgets = widgets.HBox([truck_volume_year20peak_modelcalc_widget, truck_volume_year20peak_userchanged_widget, PTV20NB_widget, PTV20NB_explanation_widget])
    
    ###################################################################
    # Non-HOV Speed widgets 
    nonhov_speed_year20peak_modelcalc_widget = widgets.FloatText(
        value=0.0,  # Set initial value to 0 or any other valid integer
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
    PNS20NB_widget = widgets.FloatText(
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
        # Accessing relevant widget values from the provided list
        ProjType = projectinfo_widgets.subcategory_dropdown.value
        PeakLngthNB = projectinfo_widgets.peak_period_widget.value
        DepRate1 = projectinfo_widgets.departure_rate_forecast_year_no_build_widget.value
        DepRate20 = projectinfo_widgets.departure_rate_forecast_year_build_widget.value
        ArrRate1 = projectinfo_widgets.arrival_rate_base_year_no_build_widget.value
        ArrRate20 = projectinfo_widgets.arrival_rate_base_year_build_widget.value
        ADT1NB = projectinfo_widgets.adt_base_year_no_build_widget.value
        FFSpeedNB = projectinfo_widgets.free_flow_speed_no_build_widget.value
        IRI20NB = projectinfo_widgets.iri_forecast_year_no_build_widget.value
        ImpactedNB = projectinfo_widgets.impacted_length_no_build_widget.value
        HOVLanesNB = projectinfo_widgets.hov_hot_lanes_no_build_widget.value
        GenLanesNB = projectinfo_widgets.general_traffic_lanes_no_build_widget.value
        MaxVC = params.MaxVC
        SpeedWeaveAdj = params.SpeedWeaveAdj
        SpeedPavAdj = params.SpeedPavAdj
        TMSAdj = params.tms_adj
        TMSLookup = params.TMSLookup
        TruckSpeed = projectinfo_widgets.truck_speed_widget.value
        PerPeakADT = params.per_peak_adt
        roadway_capacity_non_HOV = params.roadway_capacity_non_HOV
        PerWeaveNB = projectinfo_widgets.percent_traffic_weave_no_build_widget.value

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
                flow_sum = sum(traffic_volumes[1:]) if HOVLanesNB != 0 else sum(traffic_volumes)

                capacity_params = roadway_capacity_non_HOV["Non-HOV Lanes"]["No Build"]
                GenAlphaNB = capacity_params["GenAlphaNB"]
                GenBetaNB = capacity_params["GenBetaNB"]
                GenLaneCapNB = capacity_params["GenLaneCapNB"]
                TMS_value = TMSAdj.get(TMSLookup, {}).get("SpeedWithout", 1)

                volume_term = flow_sum / (GenLanesNB * GenLaneCapNB * PeakLngthNB)
                delay_speed = FFSpeedNB / (1 + GenAlphaNB * min(volume_term, MaxVC) ** GenBetaNB)
                base_speed = delay_speed * TMS_value

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
    projectinfo_widgets.ADT_20NB_widget.observe(update_nonhov_year20peak_speed, names='value')  # ADT20NB
    projectinfo_widgets.free_flow_speed_no_build_widget.observe(update_nonhov_year20peak_speed, names='value')  # FFSpeedNB
    projectinfo_widgets.impacted_length_no_build_widget.observe(update_nonhov_year20peak_speed, names='value')  # ImpactedNB
    projectinfo_widgets.general_traffic_lanes_no_build_widget.observe(update_nonhov_year20peak_speed, names='value')  # GenLanesNB
    projectinfo_widgets.hov_hot_lanes_no_build_widget.observe(update_nonhov_year20peak_speed, names='value')  # HOVLanesNB
    projectinfo_widgets.percent_traffic_weave_no_build_widget.observe(update_nonhov_year20peak_speed, names='value')  # PerWeaveNB
    projectinfo_widgets.iri_forecast_year_no_build_widget.observe(update_nonhov_year20peak_speed, names='value')  # IRI20NB
    projectinfo_widgets.percent_traffic_weave_no_build_widget.observe(update_nonhov_year20peak_speed, names='value')  # IRI20NB
    

        
    def calculate_pns20nb(change=None):
        try:
            val = float(nonhov_speed_year20peak_userchanged_widget.value)
            updated_speed = max(val, 5)
        except:
            updated_speed = max(nonhov_speed_year20peak_modelcalc_widget.value, 5)

        PNS20NB_widget.value = updated_speed

    nonhov_speed_year20peak_userchanged_widget.observe(calculate_pns20nb, names='value')
    nonhov_speed_year20peak_modelcalc_widget.observe(calculate_pns20nb, names='value')
    

    # Combine into layout
    NonHOV_Year20Peak_Speed_widgets = widgets.HBox([nonhov_speed_year20peak_modelcalc_widget, nonhov_speed_year20peak_userchanged_widget, PNS20NB_widget, PNS20NB_explanation_widget])
    
    ###################################################################        
     # HOV Speed widgets for Year 20
    hov_speed_year20peak_modelcalc_widget = widgets.FloatText(
        value=0.0,
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

    PHS20NB_widget = widgets.FloatText(
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
       # Get relevant widget values
        PHV20NB = PHV20NB_widget.value
        HOVLanesNB = projectinfo_widgets.hov_hot_lanes_no_build_widget.value
        PeakLngthNB = projectinfo_widgets.peak_period_widget.value
        FFSpeedNB = projectinfo_widgets.free_flow_speed_no_build_widget.value
        ImpactedNB = projectinfo_widgets.impacted_length_no_build_widget.value
        ADT1NB = projectinfo_widgets.adt_base_year_no_build_widget.value
        ArrRate1 = projectinfo_widgets.arrival_rate_base_year_no_build_widget.value
        ArrRate20 = projectinfo_widgets.arrival_rate_base_year_build_widget.value
        DepRate1 = projectinfo_widgets.departure_rate_forecast_year_no_build_widget.value
        DepRate20 = projectinfo_widgets.departure_rate_forecast_year_build_widget.value
        MaxVC = params.MaxVC
        IRI20NB = projectinfo_widgets.iri_forecast_year_no_build_widget.value
        SpeedPavAdj = params.SpeedPavAdj
        TMSAdj = params.tms_adj
        TMSLookup = params.TMSLookup
        SpeedWeaveAdj = params.SpeedWeaveAdj
        ProjType = projectinfo_widgets.subcategory_dropdown.value
        roadway_capacity = params.roadway_capacity
        
        # Grab HOV capacity parameters
        hov_capacity_params = roadway_capacity["HOV Lanes"]
        HOVAlpha = hov_capacity_params["HOVAlpha"]
        HOVBeta = hov_capacity_params["HOVBeta"]
        HOVLaneCap = hov_capacity_params["HOVLaneCap"]

        PHV20NB = PHV20NB_widget.value

        if PHV20NB == 0:
            hov_speed = 55.0

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
        
        
    def calculate_phs20nb(change=None):
        try:
            val = float(hov_speed_year20peak_userchanged_widget.value)
            updated_speed = max(val, 5)
        except:
            updated_speed = max(hov_speed_year20peak_modelcalc_widget.value, 5)

        PHS20NB_widget.value = updated_speed


    hov_speed_year20peak_userchanged_widget.observe(calculate_phs20nb, names='value')
    hov_speed_year20peak_modelcalc_widget.observe(calculate_phs20nb, names='value')

    # Combine into layout
    HOV_Year20Peak_Speed_widgets = widgets.HBox([hov_speed_year20peak_modelcalc_widget, hov_speed_year20peak_userchanged_widget, PHS20NB_widget, PHS20NB_explanation_widget])
    
    ###################################################################    
    # Weaving Speed widgets 
    weave_speed_year20peak_modelcalc_widget = widgets.FloatText(
        value=0.0,  # Set initial value to 0 or any other valid integer
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
    PWS20NB_widget = widgets.FloatText(
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
        # Retrieve relevant widget values
        PWV20NB = PWV20NB_widget.value
        PNS20NB = PNS20NB_widget.value
        PTV20NB = PTV20NB_widget.value
        ProjType = projectinfo_widgets.subcategory_dropdown.value
        NumDirections = projectinfo_widgets.one_two_way_widget.value
        PeakLngthNB = projectinfo_widgets.peak_period_widget.value
        FFSpeedNB = projectinfo_widgets.free_flow_speed_no_build_widget.value
        RampFFSpdNB = projectinfo_widgets.ramp_design_speed_no_build_widget.value
        SegmentNB = projectinfo_widgets.highway_segment_no_build_widget.value
        IRI20NB = projectinfo_widgets.iri_forecast_year_no_build_widget.value
        TMSAdj = params.tms_adj
        TMSLookup = params.TMSLookup
        SpeedPavAdj = params.SpeedPavAdj

        # Check if the value of PWV20NB is 0, return 55 if true
        if PWV20NB == 0:
            Year20PeakWeaveSpeed = 55.0
        else:
            # Check if the project type is Auxiliary Lane or Off-Ramp Widening
            if ProjType in ["Auxiliary Lane", "Off-Ramp Widening"]:
                # Exponential adjustment for PWV20NB, PTV20NB, NumDirections, and PeakLngthNB
                exp_factor = math.exp((PWV20NB + PTV20NB) / NumDirections / PeakLngthNB / 1000)

                # Segment length factor depending on project type
                ramp_term_factor = 1083 if ProjType == "Off-Ramp Widening" else SegmentNB * 5280
                ramp_term = 0.002 * ramp_term_factor * RampFFSpdNB / 1000

                # Main formula for base speed
                base_speed = FFSpeedNB - (FFSpeedNB - 42) * (0.321 + 0.0039 * exp_factor - ramp_term)

                # Adjusted speed with a factor of 1.1 as per formula
                adjusted_speed = 1.1 * base_speed

                # Apply TMS adjustment if applicable
                TMS_adj_factor = TMSAdj.get(TMSLookup, {}).get("SpeedWithout", 1)
                adjusted_speed *= TMS_adj_factor

                # Apply pavement adjustment if the project type is Pavement
                if ProjType == "Pavement":
                    closest_iri_key = min(SpeedPavAdj.keys(), key=lambda x: abs(x - IRI20NB))
                    speed_adj = SpeedPavAdj[closest_iri_key]["Auto"]
                    adjusted_speed *= speed_adj

                # Final bounded result, ensuring the speed is at least 5 and not more than PNS20NB
                Year20PeakWeaveSpeed = max(5, min(PNS20NB, adjusted_speed))
            else:
                # If not Auxiliary Lane or Off-Ramp Widening, simply return PNS20NB
                Year20PeakWeaveSpeed = PNS20NB

        # Update the widget with the calculated result
        weave_speed_year20peak_modelcalc_widget.value = round(Year20PeakWeaveSpeed, 1)

        
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
    
    
    def calculate_pws20nb(change=None):
        try:
            val = float(weave_speed_year20peak_userchanged_widget.value)
            updated_speed = max(val, 5)
        except:
            updated_speed = max(weave_speed_year20peak_modelcalc_widget.value, 5)

        PWS20NB_widget.value = updated_speed

    weave_speed_year20peak_userchanged_widget.observe(calculate_pws20nb, names='value')
    weave_speed_year20peak_modelcalc_widget.observe(calculate_pws20nb, names='value')
                        

    # Combine into layout for display
    Weave_Year20Peak_Speed_widgets = widgets.HBox([weave_speed_year20peak_modelcalc_widget, weave_speed_year20peak_userchanged_widget, PWS20NB_widget, PWS20NB_explanation_widget])

    ###################################################################
    # Truck Speed widgets 
    truck_speed_year20peak_modelcalc_widget = widgets.FloatText(
        value=0.0,  # Set initial value to 0 or any other valid integer
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
    PTS20NB_widget = widgets.FloatText(
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
        # Retrieve relevant widget values
        PTV20NB = PTV20NB_widget.value
        PWS20NB = PWS20NB_widget.value
        PNS20NB = PNS20NB_widget.value
        ProjType = projectinfo_widgets.subcategory_dropdown.value
        IRI20NB = projectinfo_widgets.iri_forecast_year_no_build_widget.value
        TruckSpeed = projectinfo_widgets.truck_speed_widget.value
        SpeedPavAdj = params.SpeedPavAdj

        # Check if PTV20NB is 0
        if PTV20NB == 0:
            truck_speed = 55.0
        else:
            base_speed = PWS20NB if ProjType in ["Auxiliary Lane", "Off-Ramp Widening"] else PNS20NB

            if ProjType == "Pavement":
                iri_keys = [k for k in SpeedPavAdj if k <= IRI20NB]
                closest_iri = max(iri_keys) if iri_keys else 0

                pavement_divisor = SpeedPavAdj[closest_iri]["Truck"]
                adjusted_speed = min(TruckSpeed, base_speed / pavement_divisor)
                pavement_multiplier = SpeedPavAdj[closest_iri]["Truck"]
                truck_speed = adjusted_speed * pavement_multiplier
            else:
                truck_speed = min(TruckSpeed, base_speed)

        # Update the widget with the calculated truck speed
        truck_speed_year20peak_modelcalc_widget.value = round(truck_speed, 1)



    # Add observers to trigger the function when relevant widget values change
    PTV20NB_widget.observe(update_year20peak_truck_speed, names='value')
    PWS20NB_widget.observe(update_year20peak_truck_speed, names='value')
    PNS20NB_widget.observe(update_year20peak_truck_speed, names='value')
    projectinfo_widgets.subcategory_dropdown.observe(update_year20peak_truck_speed, names='value')
    projectinfo_widgets.free_flow_speed_no_build_widget.observe(update_year20peak_truck_speed, names='value')
    projectinfo_widgets.iri_forecast_year_no_build_widget.observe(update_year20peak_truck_speed, names='value')
    projectinfo_widgets.truck_speed_widget.observe(update_year20peak_truck_speed, names='value')
    
    
    def calculate_pts20nb(change=None):
        try:
            val = float(truck_speed_year20peak_userchanged_widget.value)
            updated_speed = max(val, 5)
        except:
            updated_speed = max(truck_speed_year20peak_modelcalc_widget.value, 5)

        PTS20NB_widget.value = updated_speed


    # Link the function to the user input widget change
    truck_speed_year20peak_userchanged_widget.observe(calculate_pts20nb, names='value')
    truck_speed_year20peak_modelcalc_widget.observe(calculate_pts20nb, names='value')

    # Combine into layout for display
    Truck_Year20Peak_Speed_widgets = widgets.HBox([truck_speed_year20peak_modelcalc_widget, truck_speed_year20peak_userchanged_widget, PTS20NB_widget, PTS20NB_explanation_widget])
    
######################################################################################################################################################################
############################### NonPeak Period ###############################

    # Non-HOV Volume Year 20 Non-Peak widgets
    non_hov_vol_year20nonpeak_modelcalc_widget = widgets.FloatText(
        value=0.0,  # Set initial value to 0 or any other valid integer
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
        # Retrieve relevant widget values
        ProjType = projectinfo_widgets.subcategory_dropdown.value
        ArrRate20 = projectinfo_widgets.arrival_rate_base_year_build_widget.value
        DepRate1 = projectinfo_widgets.departure_rate_forecast_year_no_build_widget.value
        DepRate20 = projectinfo_widgets.departure_rate_forecast_year_build_widget.value
        NumTrain20 = projectinfo_widgets.NumTrain20_widget.value
        GateTime20 = projectinfo_widgets.GateTime20_widget.value
        ADT20NB = projectinfo_widgets.ADT_20NB_widget.value
        ADT1NB = projectinfo_widgets.adt_base_year_no_build_widget.value
        PerPeakADT = params.per_peak_adt
        PeakLngthNB = projectinfo_widgets.peak_period_widget.value
        PerTruckNB = projectinfo_widgets.percent_trucks_nobuild_widget.value
        AnnualFactor = params.AnnualFactor
        PerWeaveNB = projectinfo_widgets.percent_traffic_weave_no_build_widget.value

        if ProjType == "Hwy-Rail Grade Crossing":
            # Highway-rail formula
            NonHOV_year20nonpeak_Volume = (
                (ArrRate20 * GateTime20 / 60)
                / (1 - ArrRate20 / DepRate20)
                * NumTrain20 / AnnualFactor
                * (1 - PerTruckNB)
            )
        else:
            # Queuing or standard volume calculation
            if ProjType == "Queuing":
                numerator = PeakLngthNB * (DepRate1 - ADT1NB * (1 - PerPeakADT) / (24 - PeakLngthNB))
                denominator = ((ADT1NB / ADT20NB) * DepRate20 - ADT1NB * (1 - PerPeakADT) / (24 - PeakLngthNB))
                base_volume = ADT20NB - (numerator / denominator) * DepRate20
            else:
                base_volume = (1 - PerPeakADT) * ADT20NB

            # Post-calculation adjustment
            if ProjType in ["Auxiliary Lane", "Off-Ramp Widening"]:
                adjustment = 1 - PerWeaveNB
            else:
                adjustment = 1 - PerTruckNB

            NonHOV_year20nonpeak_Volume = base_volume * adjustment

        # Update the widget
        non_hov_vol_year20nonpeak_modelcalc_widget.value = round(NonHOV_year20nonpeak_Volume, 2)



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
    projectinfo_widgets.percent_traffic_weave_no_build_widget.observe(update_NonHOV_year20nonpeak_Volume, names='value')
        
        
    def calculate_nnv20nb(change):
        try:
            val = float(non_hov_vol_year20nonpeak_userchanged_widget.value)
            if val >= 0:
                NNV20NB = val
            else:
                NNV20NB = non_hov_vol_year20nonpeak_modelcalc_widget.value
        except:
            NNV20NB = non_hov_vol_year20nonpeak_modelcalc_widget.value

        NNV20NB_widget.value = NNV20NB

    # Link the function to the user input widget change
    non_hov_vol_year20nonpeak_userchanged_widget.observe(calculate_nnv20nb, names='value') 
    non_hov_vol_year20nonpeak_modelcalc_widget.observe(calculate_nnv20nb, names='value') 

    # Combine into layout for display
    Non_HOV_Vol_year20nonpeak_widgets = widgets.HBox([non_hov_vol_year20nonpeak_modelcalc_widget, non_hov_vol_year20nonpeak_userchanged_widget, NNV20NB_widget, NNV20NB_explanation_widget])

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
        # Retrieve relevant widget values
        ProjType = projectinfo_widgets.subcategory_dropdown.value
        PerPeakADT = params.per_peak_adt
        ADT20NB = projectinfo_widgets.ADT_20NB_widget.value
        PerWeaveNB = projectinfo_widgets.percent_traffic_weave_no_build_widget.value
        PerTruckNB = projectinfo_widgets.percent_trucks_nobuild_widget.value
        RampVolNP = projectinfo_widgets.hourly_ramp_volume_nonpeak_widget.value
        PeakLngthNB = projectinfo_widgets.peak_period_widget.value

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



    # Observers for weaving volume update — only required variables included
    projectinfo_widgets.subcategory_dropdown.observe(update_year20nonpeak_weaving_volume, names='value')  # ProjType
    projectinfo_widgets.ADT_20NB_widget.observe(update_year20nonpeak_weaving_volume, names='value')        # ADT20NB
    projectinfo_widgets.percent_trucks_nobuild_widget.observe(update_year20nonpeak_weaving_volume, names='value')  # PerTruckNB
    projectinfo_widgets.percent_traffic_weave_no_build_widget.observe(update_year20nonpeak_weaving_volume, names='value')  # PerWeaveNB
    projectinfo_widgets.hourly_ramp_volume_nonpeak_widget.observe(update_year20nonpeak_weaving_volume, names='value')  # RampVolNP
    projectinfo_widgets.peak_period_widget.observe(update_year20nonpeak_weaving_volume, names='value')  # PeakLngthNB

        
    def calculate_nwv20nb(change):
        try:
            val = float(weaving_vol_year20nonpeak_userchanged_widget.value)
            if val >= 0:
                NWV20NB = val
            else:
                NWV20NB = weaving_vol_year20nonpeak_modelcalc_widget.value
        except:
            NWV20NB = weaving_vol_year20nonpeak_modelcalc_widget.value

        NWV20NB_widget.value = NWV20NB

    # Link the function to the user input widget change
    weaving_vol_year20nonpeak_userchanged_widget.observe(calculate_nwv20nb, names='value')  

    # Combine into layout for display
    Weaving_Vol_year20nonpeak_widgets = widgets.HBox([weaving_vol_year20nonpeak_modelcalc_widget, weaving_vol_year20nonpeak_userchanged_widget, NWV20NB_widget, NWV20NB_explanation_widget])
    
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
        # Retrieve relevant widget values
        ProjType = projectinfo_widgets.subcategory_dropdown.value
        ArrRate20 = projectinfo_widgets.arrival_rate_base_year_build_widget.value
        DepRate20 = projectinfo_widgets.departure_rate_forecast_year_build_widget.value
        NumTrain20 = projectinfo_widgets.NumTrain20_widget.value
        GateTime20 = projectinfo_widgets.GateTime20_widget.value
        ADT20NB = projectinfo_widgets.ADT_20NB_widget.value
        ADT1NB = projectinfo_widgets.adt_base_year_no_build_widget.value
        PerPeakADT = params.per_peak_adt
        PeakLngthNB = projectinfo_widgets.peak_period_widget.value
        PerTruckNB = projectinfo_widgets.percent_trucks_nobuild_widget.value
        AnnualFactor = params.AnnualFactor

        # Calculate truck volume based on project type
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

        # Update the widget with the calculated truck volume
        Truck_Volume_year20nonpeak_modelcalc_widget.value = round(Truck_Volume_year20nonpeak, 2)



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
    Truck_Volume_year20nonpeak_modelcalc_widget.observe(calculate_ntv20nb, names='value')
    

    # Combine into layout for display
    Truck_Volume_year20nonpeak_widgets = widgets.HBox([Truck_Volume_year20nonpeak_modelcalc_widget, Truck_Volume_year20nonpeak_userchanged_widget, NTV20NB_widget, NTV20NB_explanation_widget])

    ###################################################

    # Non-HOV Speed Year 20 Non-Peak widgets
    nonhov_speed_year20nonpeak_modelcalc_widget = widgets.FloatText(
        value=0.0,
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
    NNS20NB_widget = widgets.FloatText(
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
        # Retrieve relevant widget values
        ProjType = projectinfo_widgets.subcategory_dropdown.value
        GenLanesNB = projectinfo_widgets.general_traffic_lanes_no_build_widget.value
        HOVLanesNB = projectinfo_widgets.hov_hot_lanes_no_build_widget.value
        PeakLngthNB = projectinfo_widgets.peak_period_widget.value
        FFSpeedNB = projectinfo_widgets.free_flow_speed_no_build_widget.value
        ADT1NB = projectinfo_widgets.adt_base_year_no_build_widget.value
        ADT20NB = projectinfo_widgets.ADT_20NB_widget.value
        DepRate1 = projectinfo_widgets.departure_rate_forecast_year_no_build_widget.value
        DepRate20 = projectinfo_widgets.departure_rate_forecast_year_build_widget.value
        MaxVC = params.MaxVC
        IdleSpeed = params.IdleSpeed
        SpeedWeaveAdj = params.SpeedWeaveAdj
        SpeedPavAdj = params.SpeedPavAdj
        IRI20NB = projectinfo_widgets.iri_forecast_year_no_build_widget.value
        roadway_capacity_non_HOV = params.roadway_capacity_non_HOV
        NNV20NB = NNV20NB_widget.value  
        NWV20NB = NWV20NB_widget.value  
        NTV20NB = NTV20NB_widget.value
        PerPeakADT = params.per_peak_adt

        # Retrieve capacity parameters
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
                speed = 55.0
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
    nonhov_speed_year20nonpeak_modelcalc_widget.observe(calculate_nns20nb, names='value')
    
    NonHOV_speed_year20nonpeak_widgets = widgets.HBox([ nonhov_speed_year20nonpeak_modelcalc_widget, nonhov_speed_year20nonpeak_userchanged_widget, NNS20NB_widget, NNS20NB_explanation_widget])
    

    ###################################################
    # Weaving Speed Year 20 Non-Peak widgets
    weave_speed_year20nonpeak_modelcalc_widget = widgets.FloatText(
        value=0.0,
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
        # Retrieve relevant widget values from project info
        ProjType = projectinfo_widgets.subcategory_dropdown.value
        FFSpeedNB = projectinfo_widgets.free_flow_speed_no_build_widget.value
        PeakLngthNB = projectinfo_widgets.peak_period_widget.value
        NWV20NB = NWV20NB_widget.value
        NTV20NB = NTV20NB_widget.value
        NumDirections = projectinfo_widgets.one_two_way_widget.value
        RampFFSpdNB = projectinfo_widgets.ramp_design_speed_no_build_widget.value
        SegmentNB = projectinfo_widgets.highway_segment_no_build_widget.value
        IRI20NB = projectinfo_widgets.iri_forecast_year_no_build_widget.value
        SpeedPavAdj = params.SpeedPavAdj
        SpeedWeaveAdj = params.SpeedWeaveAdj
        MaxVC = params.MaxVC
        NNS20NB = NNS20NB_widget.value

        if NWV20NB == 0:
            speed = 55
        elif ProjType in ["Auxiliary Lane", "Off-Ramp Widening"]:
            base_speed = FFSpeedNB - (FFSpeedNB - 42) * (
                0.321 + 0.0039 * math.exp(
                    (NWV20NB + NTV20NB) / NumDirections / (24 - PeakLngthNB) / 1000
                ) - 0.002 * ((1083 if ProjType == "Off-Ramp Widening" else SegmentNB * 5280) * RampFFSpdNB / 1000)
            )

            speed = min(NNS20NB, 1.1 * base_speed)

            # Pavement adjustment
            if ProjType == "Pavement":
                iri_key = min(SpeedPavAdj.keys(), key=lambda k: abs(k - IRI20NB))
                speed *= SpeedPavAdj.get(iri_key, {}).get("Auto", 1)

            speed = max(speed, 5)
        else:
            speed = NNS20NB

        weave_speed_year20nonpeak_modelcalc_widget.value = round(speed, 1)

  
    
    
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
            
    weave_speed_year20nonpeak_modelcalc_widget.observe(calculate_nws20nb, names='value')
    weave_speed_year20nonpeak_userchanged_widget.observe(calculate_nws20nb, names='value')
    

    Weave_Speed_year20nonpeak_widgets = widgets.HBox([weave_speed_year20nonpeak_modelcalc_widget, weave_speed_year20nonpeak_userchanged_widget, NWS20NB_widget,  NWS20NB_explanation_widget])

  ###################################################   
    # Truck Speed Year 20 Non-Peak widgets
    truck_speed_year20nonpeak_modelcalc_widget = widgets.FloatText(
        value=0.0,
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
        ProjType = projectinfo_widgets.subcategory_dropdown.value
        IdleSpeed = params.IdleSpeed
        TruckSpeed = projectinfo_widgets.truck_speed_widget.value
        NTV20NB = NTV20NB_widget.value
        NTS20NB = NTS20NB_widget.value
        NNS20NB = NNS20NB_widget.value
        IRI20NB = projectinfo_widgets.iri_forecast_year_no_build_widget.value
        SpeedPavAdj = params.SpeedPavAdj

        if ProjType == "Hwy-Rail Grade Crossing":
            speed = IdleSpeed
        elif NTV20NB == 0:
            speed = 55.0
        else:
            # Formula for truck speed calculation
            if ProjType in ["Auxiliary Lane", "Off-Ramp Widening"]:
                base_speed = min(
                    TruckSpeed,
                    NTS20NB if ProjType in ["Auxiliary Lane", "Off-Ramp Widening"] else NNS20NB
                )

                # Apply Pavement condition adjustment
                if ProjType == "Pavement":
                    iri_key = min(SpeedPavAdj.keys(), key=lambda k: abs(k - IRI20NB))
                    base_speed /= SpeedPavAdj.get(iri_key, {}).get("Auto", 1)
                    base_speed *= SpeedPavAdj.get(iri_key, {}).get("Truck", 1)

                speed = base_speed
            else:
                speed = NNS20NB  # Fallback for other project types

        truck_speed_year20nonpeak_modelcalc_widget.value = round(speed, 1)


    
            
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
    truck_speed_year20nonpeak_modelcalc_widget.observe(calculate_nts20nb, names='value')
    
    Truck_Speed_year20nonpeak_widgets = widgets.HBox([ truck_speed_year20nonpeak_modelcalc_widget, truck_speed_year20nonpeak_userchanged_widget, NTS20NB_widget, NTS20NB_explanation_widget])

    


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
        # Retrieve relevant project information parameters
        ProjType = projectinfo_widgets.subcategory_dropdown.value
        HOVvolB = projectinfo_widgets.HOV_lane_build_widget.value
        PeakLngthNB = projectinfo_widgets.peak_period_widget.value
        PerWeaveNB = projectinfo_widgets.percent_traffic_weave_no_build_widget.value

        if ProjType == "Hwy-Rail Grade Crossing":
            # For Hwy-Rail, HOV Volume is 0
            volume = 0
        else:
            # Formula for HOV Volume Year 1 Peak Build
            reduction_factor = (1 - PerWeaveNB) if ProjType in ["HOV Connector", "HOV Drop Ramp"] else 1
            volume = HOVvolB * PeakLngthNB * reduction_factor

        # Update the widget with the calculated result
        HOV_vol_year1peak_build_modelcalc_widget.value = round(volume, 2)


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
    HOV_vol_year1peak_build_modelcalc_widget.observe(calculate_phv1b, names='value')

    # Combine all widgets into a horizontal layout for HOV Volume
    HOV_Vol_year1peak_build_widgets = widgets.HBox([HOV_vol_year1peak_build_modelcalc_widget,  HOV_vol_year1peak_build_userchanged_widget, PHV1B_widget, PHV1B_explanation_widget])
    
    #########################################################################
    
    Non_HOV_vol_year1peak_build_modelcalc_widget = widgets.FloatText(
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
        ProjType = projectinfo_widgets.subcategory_dropdown.value
        ADT1B = projectinfo_widgets.adt_base_year_build_widget.value
        PerPeakADT = params.per_peak_adt
        PerWeaveB = projectinfo_widgets.percent_traffic_weave_build_widget.value
        PerTruckB = projectinfo_widgets.percent_trucks_build_widget.value
        TMSAdj = params.tms_adj  
        TMSLookup = params.TMSLookup  
        HOVvolB = projectinfo_widgets.HOV_lane_build_widget.value
        PeakLngthNB = projectinfo_widgets.peak_period_widget.value
        TPerPeak = projectinfo_widgets.TPerPeak_widget.value
        TPerHwy = projectinfo_widgets.TPerHwy_widget.value
        TAPT1B = projectinfo_widgets.TAPT1B_widget.value
        TAPT1NB = projectinfo_widgets.TAPT1NB_widget.value
        AVOPeakNB = projectinfo_widgets.AVO_traffic_P_no_build_widget.value
        AnnualFactor = params.AnnualFactor 

        # Default value for volume
        volume = 0

        # If ProjType is "Hwy-Rail Grade Crossing", set volume to 0 directly
        if ProjType == "Hwy-Rail Grade Crossing":
            volume = 0
        else:
            # Retrieve the TMS adjustments for the given TMSLookup (equivalent of VLOOKUP)
            TMS_value = TMSAdj.get(TMSLookup, {}).get("VolumeWith", 1)  # Directly access the dictionary for TMS adjustments

            # Non-HOV Volume Year 1 Peak Build formula:
            if ProjType in ["Auxiliary Lane", "Off-Ramp Widening"]:
                volume = (PerPeakADT * ADT1B) * (1 - PerWeaveB) * TMS_value
            else:
                volume = (PerPeakADT * ADT1B) * (1 - PerTruckB) * TMS_value

            # Subtract HOV volume and apply the other adjustments
            volume -= HOVvolB * PeakLngthNB

            # Additional adjustment for PassRail, LRT, or Bus project types
            if ProjType in ["Passenger Rail", "Light-Rail (LRT)", "Bus"]:
                volume -= (TPerPeak * TPerHwy * (TAPT1B - TAPT1NB)) / (AnnualFactor * AVOPeakNB)

        # Round and set the calculated volume value to the widget
        Non_HOV_vol_year1peak_build_modelcalc_widget.value = round(volume, 2)


    
    
    
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
    Non_HOV_vol_year1peak_build_modelcalc_widget.observe(calculate_pnv1b, names='value')

    # Combine all widgets into a horizontal layout for Non-HOV Volume
    Non_HOV_Vol_year1peak_build_widgets = widgets.HBox([Non_HOV_vol_year1peak_build_modelcalc_widget,  Non_HOV_vol_year1peak_build_userchanged_widget, PNV1B_widget, PNV1B_explanation_widget])
    
    
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
        ProjType = projectinfo_widgets.subcategory_dropdown.value
        ADT1B = projectinfo_widgets.adt_base_year_build_widget.value
        PerPeakADT = params.per_peak_adt
        PerWeaveB = projectinfo_widgets.percent_traffic_weave_build_widget.value
        PerTruckB = projectinfo_widgets.percent_trucks_build_widget.value
        TMSAdj = params.tms_adj 
        TMSLookup = params.TMSLookup
        HOVvolB = projectinfo_widgets.HOV_lane_build_widget.value
        PeakLngthNB = projectinfo_widgets.peak_period_widget.value
        RampVolP = projectinfo_widgets.hourly_ramp_volume_peak_widget.value
        PerWeaveNB = projectinfo_widgets.percent_traffic_weave_no_build_widget.value  # Added definition

        if ProjType == "Hwy-Rail Grade Crossing":
            volume = 0
        else:
            tms_adj_values = TMSAdj.get(TMSLookup, {"VolumeWith": 1})  # Safe fallback

            if ProjType in ["Auxiliary Lane", "Off-Ramp Widening"]:
                volume = (PerPeakADT * ADT1B) * (PerWeaveB - PerTruckB) * tms_adj_values["VolumeWith"]
            elif ProjType in ["HOV Connector", "HOV Drop Ramp"]:
                volume = PerWeaveNB * HOVvolB * PeakLngthNB
            else:
                volume = 0

            if ProjType == "Auxiliary Lane":
                volume += RampVolP * PeakLngthNB

            if ProjType in ["HOV Connector", "HOV Drop Ramp"]:
                volume += PerWeaveNB * HOVvolB * PeakLngthNB

        weaving_vol_year1peak_build_modelcalc_widget.value = round(volume, 2)



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
    weaving_vol_year1peak_build_modelcalc_widget.observe(calculate_pwv1b, names='value')

    # Combine all widgets into a horizontal layout for Weaving Volume
    Weaving_Vol_year1peak_build_widgets = widgets.HBox([ weaving_vol_year1peak_build_modelcalc_widget, weaving_vol_year1peak_build_userchanged_widget, PWV1B_widget, PWV1B_explanation_widget])
    
    
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
        ProjType = projectinfo_widgets.subcategory_dropdown.value
        ADT1B = projectinfo_widgets.adt_base_year_build_widget.value
        PerPeakADT = params.per_peak_adt
        PerTruckB = projectinfo_widgets.percent_trucks_build_widget.value
        TMSAdj = params.tms_adj  
        TMSLookup = params.TMSLookup  

        # Default value for volume
        volume = 0

        # If ProjType is "Hwy-Rail Grade Crossing", set volume to 0 directly
        if ProjType == "Hwy-Rail Grade Crossing":
            volume = 0
        else:
            # Retrieve the TMS adjustments for the given TMSLookup (equivalent of VLOOKUP)
            TMS_value = TMSAdj.get(TMSLookup, {}).get("VolumeWith", 1)  # Directly access the dictionary for TMS adjustments
            volume = (PerPeakADT * ADT1B) * PerTruckB * TMS_value

        # Round and set the calculated volume value to the widget
        truck_vol_year1peak_build_modelcalc_widget.value = round(volume, 2)

            
            
    projectinfo_widgets.adt_base_year_build_widget.observe(update_truck_year1peak_Build_volume, names='value')  # ADT1B
    projectinfo_widgets.percent_trucks_build_widget.observe(update_truck_year1peak_Build_volume, names='value')  # PerTruckB
    projectinfo_widgets.subcategory_dropdown.observe(update_truck_year1peak_Build_volume, names='value')
    
    
    def calculate_ptv1b(change):
        try:
            # Get the value from the user input widget
            user_value = truck_vol_year1peak_build_userchanged_widget.value

            # Validate that the user input is a non-negative number
            if isinstance(user_value, (int, float)) and user_value >= 0:
                # If the input is valid, use it
                PTV1B = user_value
            else:
                # Otherwise, use the model-calculated value
                PTV1B = truck_vol_year1peak_build_modelcalc_widget.value

            # Ensure the PTV1B value is non-negative and update the widget
            PTV1B_widget.value = round(max(PTV1B, 0), 2)

        except Exception:
            # If any error occurs, fall back to using the model-calculated value
            PTV1B_widget.value = round(max(truck_vol_year1peak_build_modelcalc_widget.value, 0), 2)



    # Watch user entry and update final PTV1B value
    truck_vol_year1peak_build_userchanged_widget.observe(calculate_ptv1b, names='value')
    truck_vol_year1peak_build_modelcalc_widget.observe(calculate_ptv1b, names='value')
    
    Truck_Vol_year1peak_build_widgets = widgets.HBox([
        truck_vol_year1peak_build_modelcalc_widget,
        truck_vol_year1peak_build_userchanged_widget,
        PTV1B_widget,
        PTV1B_explanation_widget
    ])




   #######################################################################
    # Non-HOV Speed (Calculated by Model)
    nonhov_speed_year1peak_build_modelcalc_widget = widgets.FloatText(
        value=0.0,  # Initial value
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
        # Project type and adjustments
        ProjType = projectinfo_widgets.subcategory_dropdown.value
        FFSpeedB = projectinfo_widgets.free_flow_speed_build_widget.value
        GenLanesB = projectinfo_widgets.general_traffic_lanes_build_widget.value
        PeakLngthNB = projectinfo_widgets.peak_period_widget.value
        MaxVC = params.MaxVC
        AnnualFactor = params.AnnualFactor
        TMSLookup = params.TMSLookup
        TMSAdj = params.tms_adj
        SpeedPavAdj = params.SpeedPavAdj
        SpeedWeaveAdj = params.SpeedWeaveAdj
        roadway_capacity_non_HOV = params.roadway_capacity_non_HOV

        # Inputs from widgets
        PHV1B = PHV1B_widget.value
        PNV1B = PNV1B_widget.value
        PWV1B = PWV1B_widget.value
        PTV1B = PTV1B_widget.value
        HOVLanesB = projectinfo_widgets.hov_hot_lanes_build_widget.value  # Assuming this is defined

        total_volume = PHV1B + PNV1B + PWV1B + PTV1B

        if total_volume == 0:
            NonHOVSpeed = 55.0
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

            # Free connector adjustment
            FreeConn = ProjType == "Freeway Connector"
            if FreeConn:
                speed *= SpeedWeaveAdj.get(PerWeaveB, {}).get("Freeway", 1)

            # HOV connector/drop adjustment
            HOVConn = ProjType == "HOV Connector"
            HOVDrop = ProjType == "HOV Drop Ramp"
            if HOVConn or HOVDrop:
                speed *= SpeedWeaveAdj.get(PerWeaveB, {}).get("HOV", 1)

            # Pavement adjustment
            Pavement = ProjType == "Pavement"
            if Pavement:
                closest_iri = min(SpeedPavAdj.keys(), key=lambda x: abs(x - IRI1B))
                speed *= SpeedPavAdj[closest_iri].get("Auto", 1)

            # Final speed, capped at FFSpeedB
            NonHOVSpeed = min(speed, FFSpeedB)

        # Update the widget with result
        nonhov_speed_year1peak_build_modelcalc_widget.value = round(NonHOVSpeed, 2)

    

    
    
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
            val = float(nonhov_speed_year1peak_build_userchanged_widget.value)
            updated_speed = max(val, 5)
        except:
            updated_speed = max(nonhov_speed_year1peak_build_modelcalc_widget.value, 5)

        PNS1B_widget.value = updated_speed


    # Link the function to user input widget change
    nonhov_speed_year1peak_build_userchanged_widget.observe(calculate_pns1b, names='value')
    nonhov_speed_year1peak_build_modelcalc_widget.observe(calculate_pns1b, names='value')

    # Combine widgets into layout for Non-HOV Speed Year 1 Peak Build
    NonHOV_Speed_Year1Peak_Build_Widgets = widgets.HBox([nonhov_speed_year1peak_build_modelcalc_widget,  nonhov_speed_year1peak_build_userchanged_widget, PNS1B_widget, PNS1B_explanation_widget])

   #######################################################################

    # Widget for HOV Speed (Calculated by Model)
    hov_speed_year1peak_build_modelcalc_widget = widgets.FloatText(
        value=0.0,
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
        MaxVC = params.MaxVC  
        FFSpeedB = projectinfo_widgets.free_flow_speed_build_widget.value  
        HOVLanesB = projectinfo_widgets.hov_hot_lanes_build_widget.value  
        PeakLngthNB = projectinfo_widgets.peak_period_widget.value  
        SpeedPavAdj = params.SpeedPavAdj  
        IRI1B = projectinfo_widgets.iri_base_year_build_widget.value
        roadway_capacity = params.roadway_capacity
        ProjType = projectinfo_widgets.subcategory_dropdown.value

        # Access HOV capacity values from the pre-defined roadway_capacity dictionary
        hov_capacity = roadway_capacity["HOV Lanes"]
        HOVLaneCap = hov_capacity["HOVLaneCap"]
        HOVAlpha = hov_capacity["HOVAlpha"]
        HOVBeta = hov_capacity["HOVBeta"]

        # Define PHV1B and PNS1B from user-modified widget values
        PHV1B = PHV1B_widget.value  
        PNS1B = PNS1B_widget.value  
        Pavement = ProjType == "Pavement"  # Check if project type is Pavement

        if PHV1B == 0:
            hov_build_peak_speed = 55
        elif HOVLanesB == 0:
            hov_build_peak_speed = PNS1B
        else:
            # Compute v/c ratio
            v_c_ratio = PHV1B / (HOVLanesB * HOVLaneCap * PeakLngthNB)
            min_vc = min(v_c_ratio, MaxVC)
            base_speed = FFSpeedB / (1 + HOVAlpha * (min_vc ** HOVBeta))

            # Pavement adjustment if project type is Pavement
            pavement_adj = 1
            if Pavement:
                closest_iri_key = min(SpeedPavAdj.keys(), key=lambda x: abs(x - IRI1B))
                pavement_adj = SpeedPavAdj[closest_iri_key]["Auto"]

            hov_build_peak_speed = base_speed * pavement_adj

        # Set the calculated speed in the output widget
        hov_speed_year1peak_build_modelcalc_widget.value = round(hov_build_peak_speed, 2)
        

            


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
            val = float(hov_speed_year1peak_build_userchanged_widget.value)
            updated_speed = max(val, 5)
        except:
            updated_speed = max(hov_speed_year1peak_build_modelcalc_widget.value, 5)

        PHS1B_widget.value = updated_speed
            

    # Link user override for PHS1B
    hov_speed_year1peak_build_userchanged_widget.observe(calculate_phs1b, names='value')
    hov_speed_year1peak_build_modelcalc_widget.observe(calculate_phs1b, names='value')

    # Combine all widgets into a horizontal layout for HOV Speed Year 1 Peak Build
    HOV_Speed_year1peak_build_widgets = widgets.HBox([
        hov_speed_year1peak_build_modelcalc_widget,
        hov_speed_year1peak_build_userchanged_widget,
        PHS1B_widget,
        PHS1B_explanation_widget
    ])

   #######################################################################

    weaving_speed_year1peak_build_modelcalc_widget = widgets.FloatText(
        value=0.0,
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
        ProjType = projectinfo_widgets.subcategory_dropdown.value
        NumDirections = projectinfo_widgets.one_two_way_widget.value
        PeakLngthNB = projectinfo_widgets.peak_period_widget.value
        SegmentB = projectinfo_widgets.highway_segment_build_widget.value
        RampFFSpdB = projectinfo_widgets.ramp_design_speed_build_widget.value
        FFSpeedB = projectinfo_widgets.free_flow_speed_build_widget.value
        TMSAdj = params.tms_adj
        TMSLookup = params.TMSLookup
        SpeedPavAdj = params.SpeedPavAdj
        IRI1B = projectinfo_widgets.iri_base_year_build_widget.value

        PWV1B = PWV1B_widget.value
        PTV1B = PTV1B_widget.value
        PNS1B = PNS1B_widget.value

        if PWV1B == 0:
            weave_speed = 55.0
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
                pavement_adj = SpeedPavAdj.get(closest_iri_key, {}).get("Auto", 1)

            # TMS Adjustment
            tms_adj = TMSAdj.get(TMSLookup, {}).get("SpeedWith", 1)

            # Final Speed
            final_speed = adjusted_speed * tms_adj * pavement_adj
            weave_speed = max(5, min(PNS1B, final_speed))
        else:
            weave_speed = PNS1B

        weaving_speed_year1peak_build_modelcalc_widget.value = round(weave_speed, 2)



    
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
            val = float(weaving_speed_year1peak_build_userchanged_widget.value)
            updated_speed = max(val, 5)
        except:
            updated_speed = max(weaving_speed_year1peak_build_modelcalc_widget.value, 5)

        PWS1B_widget.value = updated_speed
        
    


    weaving_speed_year1peak_build_userchanged_widget.observe(calculate_pws1b, names='value')
    weaving_speed_year1peak_build_modelcalc_widget.observe(calculate_pws1b, names='value')

    Weaving_Speed_year1peak_build_widgets = widgets.HBox([weaving_speed_year1peak_build_modelcalc_widget,  weaving_speed_year1peak_build_userchanged_widget, PWS1B_widget, PWS1B_explanation_widget])
    
   #######################################################################    
    truck_speed_year1peak_build_modelcalc_widget = widgets.FloatText(
        value=0.0,
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
        ProjType = projectinfo_widgets.subcategory_dropdown.value
        IRI1B = projectinfo_widgets.iri_base_year_build_widget.value
        TruckSpeed = projectinfo_widgets.truck_speed_widget.value
        SpeedPavAdj = params.SpeedPavAdj

        # Get widget values
        PTV1B = PTV1B_widget.value
        PWS1B = PWS1B_widget.value
        PNS1B = PNS1B_widget.value

        if PTV1B == 0:
            truck_speed = 55.0
        else:
            # Find the closest IRI key
            closest_iri_key = min(SpeedPavAdj.keys(), key=lambda x: abs(x - IRI1B))

            # Adjustments if ProjType is "Pavement"
            speed_adj_auto = SpeedPavAdj[closest_iri_key]["Auto"] if ProjType == "Pavement" else 1
            speed_adj_truck = SpeedPavAdj[closest_iri_key]["Truck"] if ProjType == "Pavement" else 1

            # Determine limit speed
            limit_speed = PWS1B if ProjType == "Auxiliary Lane" else PNS1B

            # Apply speed adjustments
            base_speed = min(TruckSpeed, limit_speed / speed_adj_auto)
            truck_speed = base_speed * speed_adj_truck

        truck_speed_year1peak_build_modelcalc_widget.value = round(truck_speed, 2)

            
        
    
    PTV1B_widget.observe(update_truck_year1peak_Build_speed, names='value')
    PWS1B_widget.observe(update_truck_year1peak_Build_speed, names='value')
    PNS1B_widget.observe(update_truck_year1peak_Build_speed, names='value')
    projectinfo_widgets.iri_base_year_build_widget.observe(update_truck_year1peak_Build_speed, names='value') #IRI1B
    projectinfo_widgets.subcategory_dropdown.observe(update_truck_year1peak_Build_speed, names='value') #ProjType
    projectinfo_widgets.truck_speed_widget.observe(update_truck_year1peak_Build_speed, names='value') #TruckSpeed 

            
    def calculate_pts1b(change):
        try:
            val = float(truck_speed_year1peak_build_userchanged_widget.value)
            updated_speed = max(val, 5)
        except:
            updated_speed = max(truck_speed_year1peak_build_modelcalc_widget.value, 5)

        PTS1B_widget.value = updated_speed
            
    truck_speed_year1peak_build_userchanged_widget.observe(calculate_pts1b, names='value')
    truck_speed_year1peak_build_modelcalc_widget.observe(calculate_pts1b, names='value')
    
    Truck_Speed_year1peak_build_widgets = widgets.HBox([truck_speed_year1peak_build_modelcalc_widget,  truck_speed_year1peak_build_userchanged_widget, PTS1B_widget, PTS1B_explanation_widget])
    
###################################################################################################################################################################
    # Create the Non-HOV Volume Build widget to display the calculated value
    Non_HOV_Vol_year1nonpeak_build_modelcalc_widget = widgets.FloatText(
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
    def update_NonHOV_year1nonpeak_build_Volume(change=None):
        # Project type and adjustments
        ProjType = projectinfo_widgets.subcategory_dropdown.value
        ArrRate1 = projectinfo_widgets.arrival_rate_base_year_no_build_widget.value
        GateTime1 = projectinfo_widgets.GateTime1_widget.value
        NumTrain1 = projectinfo_widgets.NumTrain1_widget.value
        AnnualFactor = params.AnnualFactor
        PerTruckNB = projectinfo_widgets.percent_trucks_nobuild_widget.value
        ADT20B = projectinfo_widgets.adt_20_year_build_widget.value
        ADT20NB = projectinfo_widgets.ADT_20NB_widget.value
        ADT1B = projectinfo_widgets.adt_base_year_build_widget.value
        PerPeakADT = params.per_peak_adt
        PerWeaveB = projectinfo_widgets.percent_traffic_weave_build_widget.value
        TPerPeak = projectinfo_widgets.TPerPeak_widget.value
        TPerHwy = projectinfo_widgets.TPerHwy_widget.value
        TAPT1B = projectinfo_widgets.TAPT1B_widget.value
        TAPT1NB = projectinfo_widgets.TAPT1NB_widget.value
        AVONonNB = projectinfo_widgets.AVO_traffic_NP_no_build_widget.value
        PerTruckB = projectinfo_widgets.percent_trucks_build_widget.value
        

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
    def calculate_nnv1b_build_nonpeak(change=None):
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
    Non_HOV_Vol_year1nonpeak_build_modelcalc_widget.observe(calculate_nnv1b_build_nonpeak, names='value')

    # Combine all widgets into a horizontal layout for Non-HOV Volume (Build)
    Non_HOV_vol_year1nonpeak_build_widgets = widgets.HBox([Non_HOV_Vol_year1nonpeak_build_modelcalc_widget,  Non_HOV_Vol_year1nonpeak_build_userchanged_widget, NNV1B_widget, NNV1B_explanation_widget])
    
    
    #######################################################################################################


    # Define widgets
    weaving_vol_year1nonpeak_build_modelcalc_widget = widgets.FloatText(
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
        ProjType = projectinfo_widgets.subcategory_dropdown.value
        PerPeakADT = params.per_peak_adt
        ADT1B = projectinfo_widgets.adt_base_year_build_widget.value
        PerWeaveB = projectinfo_widgets.percent_traffic_weave_build_widget.value
        PerTruckB = projectinfo_widgets.percent_trucks_build_widget.value
        RampVolNP = projectinfo_widgets.hourly_ramp_volume_nonpeak_widget.value
        PeakLngthNB = projectinfo_widgets.peak_period_widget.value

        # Initialize volume
        volume = 0

        if ProjType in ["Auxiliary Lane", "Off-Ramp Widening"]:
            volume = ((1 - PerPeakADT) * ADT1B) * (PerWeaveB - PerTruckB)

        # Add ramp volume contribution for Auxiliary Lane
        if ProjType == "Auxiliary Lane":
            volume += RampVolNP * (24 - PeakLngthNB)

        weaving_vol_year1nonpeak_build_modelcalc_widget.value = round(volume, 2)


    # Trigger updates based on used variables
    projectinfo_widgets.adt_base_year_build_widget.observe(update_weaving_year1nonpeak_Build_volume, names='value')  # ADT1B
    projectinfo_widgets.percent_traffic_weave_build_widget.observe(update_weaving_year1nonpeak_Build_volume, names='value')  # PerWeaveB
    projectinfo_widgets.percent_trucks_build_widget.observe(update_weaving_year1nonpeak_Build_volume, names='value')  # PerTruckB
    projectinfo_widgets.hourly_ramp_volume_peak_widget.observe(update_weaving_year1nonpeak_Build_volume, names='value')  # RampVolNP
    projectinfo_widgets.peak_period_widget.observe(update_weaving_year1nonpeak_Build_volume, names='value')  # PeakLngthNB


    # Function to calculate NWV1B (for user-modified values)
    def calculate_nwv1b(change=None):
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
    weaving_vol_year1nonpeak_build_modelcalc_widget.observe(calculate_nwv1b, names='value')

    # Combine all widgets into a horizontal layout for Weaving Volume
    Weaving_Vol_year1nonpeak_build_widgets = widgets.HBox([
        weaving_vol_year1nonpeak_build_modelcalc_widget,
        weaving_vol_year1nonpeak_build_userchanged_widget,
        NWV1B_widget,
        NWV1B_explanation_widget
    ])

    #######################################################################################################
    
    # Define widgets
    truck_vol_year1nonpeak_build_modelcalc_widget = widgets.FloatText(
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
        ProjType = projectinfo_widgets.subcategory_dropdown.value
        ArrRate1 = projectinfo_widgets.arrival_rate_base_year_no_build_widget.value
        GateTime1 = projectinfo_widgets.GateTime1_widget.value
        DepRate1 = projectinfo_widgets.departure_rate_forecast_year_no_build_widget.value
        NumTrain1 = projectinfo_widgets.NumTrain1_widget.value
        AnnualFactor = params.AnnualFactor
        PerTruckNB = projectinfo_widgets.percent_trucks_nobuild_widget.value
        ADT20B = projectinfo_widgets.adt_20_year_build_widget.value
        ADT20NB = projectinfo_widgets.ADT_20NB_widget.value
        PerPeakADT = params.per_peak_adt
        ADT1B = projectinfo_widgets.adt_base_year_build_widget.value
        PerTruckB = projectinfo_widgets.percent_trucks_build_widget.value

        if ProjType == "Hwy-Rail Grade Crossing":
            numerator = ArrRate1 * GateTime1 / 60
            denominator = 1 - (ArrRate1 / DepRate1) if DepRate1 != 0 else 1  # Prevent division by zero
            result = (
                numerator / denominator
                * (NumTrain1 / AnnualFactor)
                * PerTruckNB
                * ADT20B / ADT20NB if ADT20NB != 0 else 0
            )
        else:
            result = ((1 - PerPeakADT) * ADT1B) * PerTruckB

        truck_vol_year1nonpeak_build_modelcalc_widget.value = round(result, 0)

            

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
    truck_vol_year1nonpeak_build_modelcalc_widget.observe(calculate_ntv1b, names='value')
    
    Truck_Vol_year1nonpeak_build_widgets = widgets.HBox([
        truck_vol_year1nonpeak_build_modelcalc_widget,
        truck_vol_year1nonpeak_build_userchanged_widget,
        NTV1B_widget,
        NTV1B_explanation_widget
    ])

    
    #######################################################################################################

    # Model-calculated Non-HOV Speed (Non-Peak)
    nonhov_speed_year1nonpeak_build_modelcalc_widget = widgets.FloatText(
        value=0.0,
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
        ProjType = projectinfo_widgets.subcategory_dropdown.value
        FFSpeedB = projectinfo_widgets.free_flow_speed_build_widget.value
        PeakLngthNB = projectinfo_widgets.peak_period_widget.value
        GenLanesB = projectinfo_widgets.general_traffic_lanes_build_widget.value
        HOVLanesB = projectinfo_widgets.hov_hot_lanes_build_widget.value
        MaxVC = params.MaxVC
        SpeedWeaveAdj = params.SpeedWeaveAdj
        SpeedPavAdj = params.SpeedPavAdj
        IRI1B = projectinfo_widgets.iri_base_year_build_widget.value
        roadway_capacity_non_HOV = params.roadway_capacity_non_HOV

        # Volume values
        NNV1B = NNV1B_widget.value
        NWV1B = NWV1B_widget.value
        NTV1B = NTV1B_widget.value

        total_volume = NNV1B + NWV1B + NTV1B

        if ProjType == "Hwy-Rail Grade Crossing":
            NonHOVSpeed = FFSpeedB
        elif total_volume == 0:
            NonHOVSpeed = 55.0
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
    nonhov_speed_year1nonpeak_build_modelcalc_widget.observe(calculate_nns1b, names='value')
    
    NonHOV_Speed_Year1NonPeak_Build_Widgets = widgets.HBox([
        nonhov_speed_year1nonpeak_build_modelcalc_widget,
        nonhov_speed_year1nonpeak_build_userchanged_widget,
        NNS1B_widget,
        NNS1B_explanation_widget
    ])


    #######################################################################################################


    # Weaving Speed Year 1 Non-Peak Build Widgets

    weaving_speed_year1nonpeak_build_modelcalc_widget = widgets.FloatText(
        value=0.0,
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
        ProjType = projectinfo_widgets.subcategory_dropdown.value
        FFSpeedB = projectinfo_widgets.free_flow_speed_build_widget.value
        PeakLngthNB = projectinfo_widgets.peak_period_widget.value
        NumDirections = projectinfo_widgets.one_two_way_widget.value
        SegmentB = projectinfo_widgets.highway_segment_build_widget.value
        RampFFSpdB = projectinfo_widgets.ramp_design_speed_build_widget.value
        SpeedPavAdj = params.SpeedPavAdj
        IRI1B = projectinfo_widgets.iri_base_year_build_widget.value

        NWV1B = NWV1B_widget.value
        NTV1B = NTV1B_widget.value
        NNS1B = NNS1B_widget.value

        if NWV1B == 0:
            weave_speed = 55.0
        elif ProjType == "Auxiliary Lane":
            # Calculate exponential component for base speed adjustment
            exp_component = math.exp((NWV1B + NTV1B) / NumDirections / (24 - PeakLngthNB) / 1000)
            ramp_factor = 1083 if ProjType == "Off-Ramp Widening" else SegmentB * 5280
            ramp_effect = 0.002 * (ramp_factor * RampFFSpdB / 1000)

            base_speed = FFSpeedB - (FFSpeedB - 42) * (0.321 + 0.0039 * exp_component - ramp_effect)
            adjusted_speed = 1.1 * base_speed

            # Apply Pavement Adjustment if necessary
            pavement_adj = 1
            if ProjType == "Pavement":
                closest_iri_key = min(SpeedPavAdj.keys(), key=lambda x: abs(x - IRI1B))
                pavement_adj = SpeedPavAdj[closest_iri_key]["Auto"]

            # Calculate the final speed considering pavement adjustment
            final_speed = adjusted_speed * pavement_adj
            weave_speed = max(5, min(NNS1B, final_speed))

        else:
            weave_speed = NNS1B

        # Update the widget value with the calculated speed
        weaving_speed_year1nonpeak_build_modelcalc_widget.value = round(weave_speed, 2)




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
    weaving_speed_year1nonpeak_build_modelcalc_widget.observe(calculate_nws1b, names='value')

    # Combine widgets for layout
    Weaving_Speed_year1nonpeak_build_widgets = widgets.HBox([weaving_speed_year1nonpeak_build_modelcalc_widget, weaving_speed_year1nonpeak_build_userchanged_widget, NWS1B_widget, NWS1B_explanation_widget])


    #######################################################################################################
    # Truck Speed Year 1 Non-Peak Build Widgets

    truck_speed_year1nonpeak_build_modelcalc_widget = widgets.FloatText(
        value=0.0,
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
        # Retrieve necessary widget values
        NTV1B = NTV1B_widget.value
        NNS1B = NNS1B_widget.value
        NWS1B = NWS1B_widget.value
        ProjType = projectinfo_widgets.subcategory_dropdown.value
        FFSpeedB = projectinfo_widgets.free_flow_speed_build_widget.value
        TruckSpeed = projectinfo_widgets.truck_speed_widget.value
        IRI1B = projectinfo_widgets.iri_base_year_build_widget.value
        SpeedPavAdj = params.SpeedPavAdj

        # If ProjType is "Hwy-Rail Grade Crossing", set truck speed to Free Flow Speed
        if ProjType == "Hwy-Rail Grade Crossing":
            truck_speed = FFSpeedB
        elif NTV1B == 0:
            truck_speed = 55.0  # Default speed when there is no truck volume
        else:
            # For other project types, calculate the truck speed based on provided formulas
            if ProjType == "Auxiliary Lane":
                # For auxiliary lanes, the truck speed is based on a formula involving SpeedPavAdj
                truck_speed = min(
                    TruckSpeed,
                    max(NWS1B, NNS1B) / (SpeedPavAdj.get(IRI1B, {}).get("Auto", 1))
                )
            else:
                # For non-auxiliary lanes, calculate speed using the pavement adjustment factor
                truck_speed = min(
                    TruckSpeed,
                    max(NWS1B, NNS1B) / SpeedPavAdj.get(IRI1B, {}).get("Auto", 1)
                )

            # Apply additional pavement adjustments if the project type is "Pavement"
            if ProjType == "Pavement":
                closest_iri_key = min(SpeedPavAdj.keys(), key=lambda x: abs(x - IRI1B))
                pavement_adj = SpeedPavAdj[closest_iri_key].get("Truck", 1)
                truck_speed *= pavement_adj

        # Set the final truck speed in the widget, rounding to 2 decimal places
        truck_speed_year1nonpeak_build_modelcalc_widget.value = round(truck_speed, 2)




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
    truck_speed_year1nonpeak_build_modelcalc_widget.observe(calculate_nts1b, names='value')

    # Combine widgets for layout
    Truck_Speed_year1nonpeak_build_widgets = widgets.HBox([truck_speed_year1nonpeak_build_modelcalc_widget, truck_speed_year1nonpeak_build_userchanged_widget, NTS1B_widget, NTS1B_explanation_widget])

###################################################################################################################################################################

    # Create the HOV Volume widget to display the calculated value
    HOV_Vol_year20peak_build_modelcalc_widget = widgets.FloatText(
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
    def update_HOV_Year20Peak_Build_Volume(change=None):
        ProjType = projectinfo_widgets.subcategory_dropdown.value
        PeakLngthNB = projectinfo_widgets.peak_period_widget.value
        ADT1NB = projectinfo_widgets.adt_base_year_no_build_widget.value
        ADT20NB = projectinfo_widgets.adt_20_year_build_widget.value
        DepRate1 = projectinfo_widgets.departure_rate_forecast_year_no_build_widget.value
        DepRate20 = projectinfo_widgets.departure_rate_forecast_year_build_widget.value
        PerPeakADT = params.per_peak_adt
        PerWeaveNB = projectinfo_widgets.percent_traffic_weave_no_build_widget.value
        HOVvolB = projectinfo_widgets.HOV_lane_build_widget.value

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
        try:
            val = float(HOV_Vol_year20peak_build_userchanged_widget.value)
            if val >= 0:
                PHV20B = val
            else:
                PHV20B = HOV_Vol_year20peak_build_modelcalc_widget.value
        except:
            PHV20B = HOV_Vol_year20peak_build_modelcalc_widget.value

        PHV20B_widget.value = PHV20B

    # Link the PHV20B widget update to changes in HOV_Vol_peak_userchanged_widget
    HOV_Vol_year20peak_build_userchanged_widget.observe(calculate_phv20b, names='value')
    HOV_Vol_year20peak_build_modelcalc_widget.observe(calculate_phv20b, names='value')

    # Combine all widgets into a horizontal layout for HOV Volume
    HOV_vol_year20peak_build_widgets = widgets.HBox([HOV_Vol_year20peak_build_modelcalc_widget, HOV_Vol_year20peak_build_userchanged_widget, PHV20B_widget, PHV20B_widget, PHV20B_explanation_widget])

    
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
    def update_nonHOV_Year20Peak_Build_Volume(change=None):
        ProjType = projectinfo_widgets.subcategory_dropdown.value
        ADT20B = projectinfo_widgets.adt_20_year_build_widget.value
        ADT1NB = projectinfo_widgets.adt_base_year_no_build_widget.value
        ADT20NB = projectinfo_widgets.ADT_20NB_widget.value
        DepRate1 = projectinfo_widgets.departure_rate_forecast_year_no_build_widget.value
        DepRate20 = projectinfo_widgets.departure_rate_forecast_year_build_widget.value
        PeakLngthNB = projectinfo_widgets.peak_period_widget.value
        PerPeakADT = params.per_peak_adt
        PerWeaveB = projectinfo_widgets.percent_traffic_weave_build_widget.value
        PerTruckB = projectinfo_widgets.percent_trucks_build_widget.value
        HOVvolB = projectinfo_widgets.HOV_lane_build_widget.value
        TMSAdj = params.tms_adj
        TMSLookup = params.TMSLookup
        TAPT20B = projectinfo_widgets.TAPT20B_widget.value
        TAPT20NB = projectinfo_widgets.TAPT20NB_widget.value
        TPerPeak = projectinfo_widgets.TPerPeak_widget.value
        TPerHwy = projectinfo_widgets.TPerHwy_widget.value
        AnnualFactor = params.AnnualFactor
        AVOPeakNB = projectinfo_widgets.AVO_traffic_P_no_build_widget.value


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
                transit_deduction = (
                    TPerPeak * TPerHwy * (TAPT20B - TAPT20NB) /
                    AnnualFactor / AVOPeakNB
                )

            nonHOV_Volume_Year20Peak_Build_Model = (
                PerPeakADT * ADT20B *
                (1 - subtract_pct - hov_adjustment) *
                tms_factor -
                HOVvolB * PeakLngthNB -
                transit_deduction
            )

        nonHOV_Vol_year20peak_build_modelcalc_widget.value = round(nonHOV_Volume_Year20Peak_Build_Model, 2)


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
            val = float(nonHOV_Vol_year20peak_build_userchanged_widget.value)
            if val >= 0:
                PNV20B = val
            else:
                PNV20B = nonHOV_Vol_year20peak_build_modelcalc_widget.value
        except:
            PNV20B = nonHOV_Vol_year20peak_build_modelcalc_widget.value

        PNV20B_widget.value = PNV20B

    nonHOV_Vol_year20peak_build_userchanged_widget.observe(calculate_pnv20b, names='value')
    nonHOV_Vol_year20peak_build_modelcalc_widget.observe(calculate_pnv20b, names='value')

    # Combine into layout
    nonHOV_vol_year20peak_build_widgets = widgets.HBox([
        nonHOV_Vol_year20peak_build_modelcalc_widget,
        nonHOV_Vol_year20peak_build_userchanged_widget,
        PNV20B_widget,
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
        # Get the relevant project variables from the widgets
        ProjType = projectinfo_widgets.subcategory_dropdown.value
        PerPeakADT = params.per_peak_adt
        ADT20B = projectinfo_widgets.adt_20_year_build_widget.value
        PerWeaveB = projectinfo_widgets.percent_traffic_weave_build_widget.value
        PerTruckB = projectinfo_widgets.percent_trucks_build_widget.value
        RampVolP = projectinfo_widgets.hourly_ramp_volume_peak_widget.value
        PeakLngthNB = projectinfo_widgets.peak_period_widget.value
        HOVvolB = projectinfo_widgets.HOV_lane_build_widget.value
        PerWeaveNB = projectinfo_widgets.percent_traffic_weave_no_build_widget.value
        TMSAdj = params.tms_adj
        TMSLookup = params.TMSLookup

        weaving_volume = 0

        if ProjType in ["Auxiliary Lane", "Off-Ramp Widening"]:
            tms_factor = TMSAdj.get(TMSLookup, {}).get("VolumeWith", 1)
            weaving_volume += (PerPeakADT * ADT20B) * (PerWeaveB - PerTruckB) * tms_factor

        if ProjType == "Auxiliary Lane":
            weaving_volume += RampVolP * PeakLngthNB

        if ProjType in ["HOV Connector", "HOV Drop Ramp"]:
            weaving_volume += PerWeaveNB * HOVvolB * PeakLngthNB

        weaving_Vol_year20peak_build_modelcalc_widget.value = round(weaving_volume, 2)


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
            val = float(weaving_Vol_year20peak_build_userchanged_widget.value)
            if val >= 0:
                PWV20B = val
            else:
                PWV20B = weaving_Vol_year20peak_build_modelcalc_widget.value
        except:
            PWV20B = weaving_Vol_year20peak_build_modelcalc_widget.value

        PWV20B_widget.value = PWV20B

    weaving_Vol_year20peak_build_userchanged_widget.observe(calculate_pwv20b, names='value')
    weaving_Vol_year20peak_build_modelcalc_widget.observe(calculate_pwv20b, names='value')

    # Combine into layout
    Weaving_vol_year20peak_build_widgets = widgets.HBox([
        weaving_Vol_year20peak_build_modelcalc_widget,
        weaving_Vol_year20peak_build_userchanged_widget,
        PWV20B_widget,
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
        # Retrieve necessary project-specific values from widgets or parameters
        ProjType = projectinfo_widgets.subcategory_dropdown.value
        ADT20B = projectinfo_widgets.adt_20_year_build_widget.value
        PerPeakADT = params.per_peak_adt
        DepRate1 = projectinfo_widgets.departure_rate_forecast_year_no_build_widget.value
        DepRate20 = projectinfo_widgets.departure_rate_forecast_year_build_widget.value
        ADT1NB = projectinfo_widgets.adt_base_year_no_build_widget.value
        PeakLngthNB = projectinfo_widgets.peak_period_widget.value
        PerTruckB = projectinfo_widgets.percent_trucks_build_widget.value
        TMSAdj = params.tms_adj
        TMSLookup = params.TMSLookup

        if ProjType == "Hwy-Rail Grade Crossing":
            truck_volume = 0

        elif ProjType == "Queuing":
            numerator = ADT20B * DepRate20 * PeakLngthNB * (
                DepRate1 - ADT1NB * (1 - PerPeakADT) / (24 - PeakLngthNB)
            )
            denominator = (
                (ADT1NB / ADT20B * DepRate20 - ADT1NB * (1 - PerPeakADT) / (24 - PeakLngthNB))
                / ADT20B
            )
            truck_volume = numerator / denominator if denominator != 0 else 0

        else:
            tms_factor = TMSAdj.get(TMSLookup, {}).get("VolumeWith", 1)
            truck_volume = PerPeakADT * ADT20B * PerTruckB * tms_factor

        truck_Vol_year20peak_build_modelcalc_widget.value = round(truck_volume, 2)


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
            val = float(truck_Vol_year20peak_build_userchanged_widget.value)
            if val >= 0:
                PTV20B = val
            else:
                PTV20B = truck_Vol_year20peak_build_modelcalc_widget.value
        except:
            PTV20B = truck_Vol_year20peak_build_modelcalc_widget.value

        PTV20B_widget.value = PTV20B

    truck_Vol_year20peak_build_userchanged_widget.observe(calculate_ptv20b, names='value')
    truck_Vol_year20peak_build_modelcalc_widget.observe(calculate_ptv20b, names='value')

    # Combine into layout
    Truck_vol_year20peak_build_widgets = widgets.HBox([
        truck_Vol_year20peak_build_modelcalc_widget,
        truck_Vol_year20peak_build_userchanged_widget,
        PTV20B_widget,
        PTV20B_explanation_widget
    ])
    
    
    ####################################################################################################### 
    
    # Non-HOV Speed widgets for Year 20 Peak Build
    nonhov_speed_year20peak_build_modelcalc_widget = widgets.FloatText(
        value=0.0,  # Set initial value to 0 or any other valid integer
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
    PNS20B_widget = widgets.FloatText(
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
        # Extract inputs
        ProjType = projectinfo_widgets.subcategory_dropdown.value
        PeakLngthNB = projectinfo_widgets.peak_period_widget.value
        DepRate20 = projectinfo_widgets.departure_rate_forecast_year_build_widget.value
        ArrRate20 = projectinfo_widgets.arrival_rate_base_year_build_widget.value
        DepRate1 = projectinfo_widgets.departure_rate_forecast_year_no_build_widget.value
        ArrRate1 = projectinfo_widgets.arrival_rate_base_year_no_build_widget.value
        ADT1NB = projectinfo_widgets.adt_base_year_no_build_widget.value
        PerPeakADT = params.per_peak_adt
        ImpactedNB = projectinfo_widgets.impacted_length_no_build_widget.value
        FFSpeedNB = projectinfo_widgets.free_flow_speed_no_build_widget.value
        HOVLanesNB = projectinfo_widgets.hov_hot_lanes_no_build_widget.value
        FFSpeedB = projectinfo_widgets.free_flow_speed_build_widget.value
        GenLanesNB = projectinfo_widgets.general_traffic_lanes_no_build_widget.value
        MaxVC = params.MaxVC
        TMSAdj = params.tms_adj
        TMSLookup = params.TMSLookup
        IRI20B = projectinfo_widgets.iri_forecast_year_build_widget.value
        SpeedWeaveAdj = params.SpeedWeaveAdj
        PerWeaveB = projectinfo_widgets.percent_traffic_weave_build_widget.value
        SpeedPavAdj = params.SpeedPavAdj
        TruckSpeed = projectinfo_widgets.truck_speed_widget.value

        # Volumes: PHV, PNV, PWV, PTV
        volumes = [PHV20B_widget.value, 
                   PNV20B_widget.value, 
                   PWV20B_widget.value, 
                   PTV20B_widget.value]
        total_volume = sum(volumes)

        if total_volume == 0:
            nonhov_speed = 55.0
        else:
            cap = params.roadway_capacity_non_HOV["Non-HOV Lanes"]["Build"]
            GenAlphaB = cap["GenAlphaB"]
            GenBetaB = cap["GenBetaB"]
            GenLaneCapB = cap["GenLaneCapB"]

            if HOVLanesNB == 0:
                volume_sum = sum(volumes)
            else:
                volume_sum = sum(volumes[1:])  # Skip PHV if HOV lanes exist

            base_denom = GenLanesNB * GenLaneCapB * PeakLngthNB
            volume_ratio = volume_sum / base_denom if base_denom else float("inf")

            if ProjType == "Queuing":
                try:
                    numerator = DepRate1 - ADT1NB * (1 - PerPeakADT) / (24 - PeakLngthNB)
                    denominator = (
                        ADT1NB / ADT1NB * DepRate20 - ADT1NB * (1 - PerPeakADT) / (24 - PeakLngthNB)
                    )
                    queuing_term = numerator / denominator if denominator else 1
                except ZeroDivisionError:
                    queuing_term = 1
            else:
                queuing_term = 1

            speed_calc = FFSpeedB / (
                1 + GenAlphaB * min(volume_ratio * queuing_term, MaxVC) ** GenBetaB
            )

            # Apply TMS adjustment
            tms_adj_factor = TMSAdj.get(TMSLookup, {}).get(3, 1)
            speed_calc *= tms_adj_factor

            # Apply Freeway Connector adjustment
            if ProjType == "Freeway Connector":
                speed_calc *= SpeedWeaveAdj.get(PerWeaveB, {}).get(2, 1)

            # Apply HOV Connector or Drop Ramp adjustment
            if ProjType in ["HOV Connector", "HOV Drop Ramp"]:
                speed_calc *= SpeedWeaveAdj.get(PerWeaveB, {}).get(3, 1)

            # Apply pavement condition adjustment
            if ProjType == "Pavement":
                closest_iri = min(SpeedPavAdj, key=lambda x: abs(x - IRI20B))
                speed_calc *= SpeedPavAdj[closest_iri].get(2, 1)

            # Cap by free-flow speed
            nonhov_speed = min(speed_calc, FFSpeedB)

        # Output
        nonhov_speed_year20peak_build_modelcalc_widget.value = round(nonhov_speed, 1)



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


    def calculate_pns20b(change=None):
        # Access the user-modified value directly from the widget
        if isinstance(nonhov_speed_year20peak_build_userchanged_widget.value, (int, float)) and nonhov_speed_year20peak_build_userchanged_widget.value >= 0:
            updated_NonHOV_year20peak_speed = max(nonhov_speed_year20peak_build_userchanged_widget.value, 5)  # Ensure the speed is at least 5
        else:
            updated_NonHOV_year20peak_speed = max(nonhov_speed_year20peak_build_modelcalc_widget.value, 5)  # Use the model value if the user value is invalid

        # Update the value of PNS20B widget
        PNS20B_widget.value = updated_NonHOV_year20peak_speed


    nonhov_speed_year20peak_build_userchanged_widget.observe(calculate_pns20b, names='value')
    nonhov_speed_year20peak_build_modelcalc_widget.observe(calculate_pns20b, names='value')

    # Combine into layout
    NonHOV_Year20Peak_Build_Speed_widgets = widgets.HBox([nonhov_speed_year20peak_build_modelcalc_widget, nonhov_speed_year20peak_build_userchanged_widget, PNS20B_widget, PNS20B_explanation_widget])
    
     ####################################################################################################### 
    # HOV Speed widgets for Year 20 Peak Build
    hov_speed_year20peak_build_modelcalc_widget = widgets.FloatText(
        value=0.0,  # Set initial value to 0 or any other valid integer
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
    PHS20B_widget = widgets.FloatText(
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
        # Extracting necessary values for the formula
        PHV20B = PHV20B_widget.value
        PNS20B = PNS20B_widget.value
        roadway_capacity = params.roadway_capacity
        HOVLanesB = projectinfo_widgets.hov_hot_lanes_build_widget.value
        ProjType = projectinfo_widgets.subcategory_dropdown.value
        DepRate1 = projectinfo_widgets.departure_rate_forecast_year_no_build_widget.value
        ADT1NB = projectinfo_widgets.adt_base_year_no_build_widget.value
        ADT20NB = projectinfo_widgets.ADT_20NB_widget.value
        PerPeakADT = params.per_peak_adt
        PeakLngthNB = projectinfo_widgets.peak_period_widget.value
        DepRate20 = projectinfo_widgets.departure_rate_forecast_year_build_widget.value
        FFSpeedB = projectinfo_widgets.free_flow_speed_build_widget.value
        SpeedPavAdj = params.SpeedPavAdj
        IRI20B = projectinfo_widgets.iri_forecast_year_build_widget.value
        MaxVC = params.MaxVC
        hov_capacity_params = roadway_capacity["HOV Lanes"]
        HOVAlpha = hov_capacity_params["HOVAlpha"]
        HOVBeta = hov_capacity_params["HOVBeta"]
        HOVLaneCap = hov_capacity_params["HOVLaneCap"]
        
        # === HOV speed calculation ===
        if PHV20B == 0:
            hov_speed = 55.0  # If PHV20B is zero, use 55 miles/h
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


    # Link the update function to changes in relevant widgets
    PHV20B_widget.observe(update_hov_year20peak_build_speed, names='value')
    projectinfo_widgets.subcategory_dropdown.observe(update_hov_year20peak_build_speed, names='value')  # ProjType
    projectinfo_widgets.peak_period_widget.observe(update_hov_year20peak_build_speed, names='value')     # PeakLngthNB
    projectinfo_widgets.departure_rate_forecast_year_build_widget.observe(update_hov_year20peak_build_speed, names='value')  # DepRate20
    projectinfo_widgets.departure_rate_forecast_year_no_build_widget.observe(update_hov_year20peak_build_speed, names='value')  # DepRate1
    projectinfo_widgets.adt_base_year_no_build_widget.observe(update_hov_year20peak_build_speed, names='value')  # ADT1NB
    projectinfo_widgets.iri_forecast_year_no_build_widget.observe(update_hov_year20peak_build_speed, names='value')  # IRI20B
    

    def calculate_phs20b(change=None):
        # Access the user-modified value directly from the widget
        if isinstance(hov_speed_year20peak_build_userchanged_widget.value, (int, float)) and hov_speed_year20peak_build_userchanged_widget.value >= 0:
            updated_HOV_year20peak_speed = max(hov_speed_year20peak_build_userchanged_widget.value, 5)  # Ensure the speed is at least 5
        else:
            updated_HOV_year20peak_speed = max(hov_speed_year20peak_build_modelcalc_widget.value, 5)  # Use the model value if the user value is invalid

        # Update the value of PHS20B widget
        PHS20B_widget.value = updated_HOV_year20peak_speed

    hov_speed_year20peak_build_userchanged_widget.observe(calculate_phs20b, names='value')
    hov_speed_year20peak_build_modelcalc_widget.observe(calculate_phs20b, names='value')

    # Combine into layout
    HOV_Year20Peak_Build_Speed_widgets = widgets.HBox([hov_speed_year20peak_build_modelcalc_widget, hov_speed_year20peak_build_userchanged_widget, PHS20B_widget, PHS20B_explanation_widget])
      

     ####################################################################################################### 
    
    # Widgets for Build Speed Calculation
    weave_speed_year20peak_build_modelcalc_widget = widgets.FloatText(
        value=0.0,  # Set initial value to 0 or any other valid integer
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
    PWS20B_widget = widgets.FloatText(
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
        # Retrieve widget/input values
        PWV20B = PWV20B_widget.value  # PWV20B
        PTV20B = PTV20B_widget.value  # PTV20B
        PNS20B = PNS20B_widget.value  # PNS20B
        ProjType = projectinfo_widgets.subcategory_dropdown.value
        NumDirections = projectinfo_widgets.one_two_way_widget.value
        PeakLngthNB = projectinfo_widgets.peak_period_widget.value
        SegmentB = projectinfo_widgets.highway_segment_build_widget.value
        RampFFSpdB = projectinfo_widgets.ramp_design_speed_build_widget.value
        FFSpeedB = projectinfo_widgets.free_flow_speed_build_widget.value
        TMSAdj = params.tms_adj
        TMSLookup = params.TMSLookup
        SpeedPavAdj = params.SpeedPavAdj
        IRI20B = projectinfo_widgets.iri_forecast_year_build_widget.value

        if PWV20B == 0:
            Year20PeakBuildWeaveSpeed = 55.0

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
    weave_speed_year20peak_build_modelcalc_widget.observe(calculate_pws20b, names='value')

    # Combine into layout for display
    Weave_Year20Peak_Build_Speed_widgets = widgets.HBox([weave_speed_year20peak_build_modelcalc_widget, weave_speed_year20peak_build_userchanged_widget, PWS20B_widget, PWS20B_explanation_widget])

     #######################################################################################################  
    
    # Widgets for Build Truck Speed Calculation
    truck_speed_year20peak_build_modelcalc_widget = widgets.FloatText(
        value=0.0,  # Set initial value to 0 or any other valid integer
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
    PTS20B_widget = widgets.FloatText(
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
        # Retrieve relevant widget values
        PTV20B = PTV20B_widget.value  # PTV20B
        PNS20B = PNS20B_widget.value  # PNS20B
        PWS20B = PWS20B_widget.value  # PWS20B
        ProjType = projectinfo_widgets.subcategory_dropdown.value
        SpeedPavAdj = params.SpeedPavAdj
        IRI20B = projectinfo_widgets.iri_forecast_year_build_widget.value
        TruckSpeed = projectinfo_widgets.truck_speed_widget.value

        if PTV20B == 0:
            truck_speed_year20peak_build_modelcalc_widget.value = 55.0
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
    truck_speed_year20peak_build_modelcalc_widget.observe(calculate_pts20b, names='value')

    # Combine into layout for display
    Truck_Year20Peak_Build_Speed_widgets = widgets.HBox([truck_speed_year20peak_build_modelcalc_widget, truck_speed_year20peak_build_userchanged_widget, PTS20B_widget, PTS20B_explanation_widget])

    
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
    NNV20B_widget = widgets.IntText(
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
    
    
    def update_NonHOV_year20nonpeak_build_Volume(change=None):
        # === Define relevant variables from the universal list ===
        ProjType = projectinfo_widgets.subcategory_dropdown.value
        ArrRate20 = projectinfo_widgets.arrival_rate_base_year_build_widget.value
        GateTime20 = projectinfo_widgets.GateTime20_widget.value
        DepRate20 = projectinfo_widgets.departure_rate_forecast_year_build_widget.value
        NumTrain20 = projectinfo_widgets.NumTrain20_widget.value
        AnnualFactor = params.AnnualFactor
        PerTruckNB = projectinfo_widgets.percent_trucks_nobuild_widget.value
        ADT20B = projectinfo_widgets.adt_20_year_build_widget.value
        ADT20NB = projectinfo_widgets.ADT_20NB_widget.value
        PeakLngthNB = projectinfo_widgets.peak_period_widget.value
        DepRate1 = projectinfo_widgets.departure_rate_forecast_year_no_build_widget.value
        ADT1NB = projectinfo_widgets.adt_base_year_no_build_widget.value
        PerPeakADT = params.per_peak_adt
        PerWeaveB = projectinfo_widgets.percent_traffic_weave_build_widget.value
        PerTruckB = projectinfo_widgets.percent_trucks_build_widget.value
        TPerPeak = projectinfo_widgets.TPerPeak_widget.value
        TPerHwy = projectinfo_widgets.TPerHwy_widget.value
        TAPT20B = projectinfo_widgets.TAPT20B_widget.value
        TAPT20NB = projectinfo_widgets.TAPT20NB_widget.value
        AVONonNB = projectinfo_widgets.AVO_traffic_NP_no_build_widget.value

        # Hwy-Rail case
        if ProjType == "Hwy-Rail Grade Crossing":
            NonHOV_year20nonpeak_build_Volume = (
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
            NonHOV_year20nonpeak_build_Volume = numerator / denominator if denominator != 0 else 0

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
            NonHOV_year20nonpeak_build_Volume = base_volume * (1 - subtract_pct) - transit_deduction

        # Assign the result to the widget
        nonHOV_Vol_year20nonpeak_build_modelcalc_widget.value = round(NonHOV_year20nonpeak_build_Volume, 2)

            
            
    # Observer setup for NNV20B calculation based on relevant project widgets
    projectinfo_widgets.subcategory_dropdown.observe(update_NonHOV_year20nonpeak_build_Volume, names='value')  # ProjType
    projectinfo_widgets.arrival_rate_base_year_build_widget.observe(update_NonHOV_year20nonpeak_build_Volume, names='value')  # ArrRate20
    projectinfo_widgets.GateTime20_widget.observe(update_NonHOV_year20nonpeak_build_Volume, names='value')  # GateTime20
    projectinfo_widgets.departure_rate_forecast_year_build_widget.observe(update_NonHOV_year20nonpeak_build_Volume, names='value')  # DepRate20
    projectinfo_widgets.NumTrain20_widget.observe(update_NonHOV_year20nonpeak_build_Volume, names='value')  # NumTrain20
    projectinfo_widgets.percent_trucks_nobuild_widget.observe(update_NonHOV_year20nonpeak_build_Volume, names='value')  # PerTruckNB
    projectinfo_widgets.ADT_20NB_widget.observe(update_NonHOV_year20nonpeak_build_Volume, names='value')  # ADT20NB
    projectinfo_widgets.adt_20_year_build_widget.observe(update_NonHOV_year20nonpeak_build_Volume, names='value')  # ADT20B
    projectinfo_widgets.peak_period_widget.observe(update_NonHOV_year20nonpeak_build_Volume, names='value')  # PeakLngthNB
    projectinfo_widgets.departure_rate_forecast_year_no_build_widget.observe(update_NonHOV_year20nonpeak_build_Volume, names='value')  # DepRate1
    projectinfo_widgets.adt_base_year_no_build_widget.observe(update_NonHOV_year20nonpeak_build_Volume, names='value')  # ADT1NB
    projectinfo_widgets.percent_traffic_weave_build_widget.observe(update_NonHOV_year20nonpeak_build_Volume, names='value')  # PerWeaveB
    projectinfo_widgets.percent_trucks_build_widget.observe(update_NonHOV_year20nonpeak_build_Volume, names='value')  # PerTruckB
    projectinfo_widgets.TAPT20B_widget.observe(update_NonHOV_year20nonpeak_build_Volume, names='value')  # TAPT20B
    projectinfo_widgets.TAPT20NB_widget.observe(update_NonHOV_year20nonpeak_build_Volume, names='value')  # TAPT20NB
    projectinfo_widgets.TPerPeak_widget.observe(update_NonHOV_year20nonpeak_build_Volume, names='value')  # TPerPeak
    projectinfo_widgets.TPerHwy_widget.observe(update_NonHOV_year20nonpeak_build_Volume, names='value')  # TPerHwy
    projectinfo_widgets.AVO_traffic_NP_no_build_widget.observe(update_NonHOV_year20nonpeak_build_Volume, names='value')  # AVONonNB

   

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
    nonHOV_Vol_year20nonpeak_build_modelcalc_widget.observe(calculate_nnv20b, names='value')

    # Combine into layout for display
    NonHOV_Year20NonPeak_Build_Volume_widgets = widgets.HBox([
        nonHOV_Vol_year20nonpeak_build_modelcalc_widget,
        nonHOV_Vol_year20nonpeak_build_userchanged_widget,
        NNV20B_widget,
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
    NWV20B_widget = widgets.IntText(
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
    # Function to update Weaving Volume dynamically for Non-Peak Year 20
    def update_weaving_Year20NonPeak_Build_Volume(change):
        # === Define relevant variables from the universal list ===
        ProjType = projectinfo_widgets.subcategory_dropdown.value
        PerPeakADT = params.per_peak_adt
        ADT20B = projectinfo_widgets.adt_20_year_build_widget.value
        PerWeaveB = projectinfo_widgets.percent_traffic_weave_build_widget.value
        PerTruckB = projectinfo_widgets.percent_trucks_build_widget.value
        RampVolNP = projectinfo_widgets.hourly_ramp_volume_nonpeak_widget.value
        PeakLngthNB = projectinfo_widgets.peak_period_widget.value

        weaving_volume = 0 
        
        # Calculate the volume based on the formula
        if ProjType in ["Auxiliary Lane", "Off-Ramp Widening"]:
            weaving_volume += ((1 - PerPeakADT) * ADT20B) * (PerWeaveB - PerTruckB)

        if ProjType == "Auxiliary Lane":
            weaving_volume += RampVolNP * (24 - PeakLngthNB)

        weaving_Vol_year20nonpeak_build_modelcalc_widget.value = round(weaving_volume, 2)


    # Observer setup for Weaving Volume (Non-Peak Year 20)
    projectinfo_widgets.subcategory_dropdown.observe(update_weaving_Year20NonPeak_Build_Volume, names='value')  # ProjType
    projectinfo_widgets.adt_20_year_build_widget.observe(update_weaving_Year20NonPeak_Build_Volume, names='value')  # ADT20B
    projectinfo_widgets.percent_traffic_weave_build_widget.observe(update_weaving_Year20NonPeak_Build_Volume, names='value')  # PerWeaveB
    projectinfo_widgets.percent_trucks_build_widget.observe(update_weaving_Year20NonPeak_Build_Volume, names='value')  # PerTruckB
    projectinfo_widgets.hourly_ramp_volume_nonpeak_widget.observe(update_weaving_Year20NonPeak_Build_Volume, names='value')  # RampVolNP
    projectinfo_widgets.peak_period_widget.observe(update_weaving_Year20NonPeak_Build_Volume, names='value')  # PeakLngthNB


    # Final value widget logic for NWV20B
    def calculate_nwv20b(change=None):
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
    weaving_Vol_year20nonpeak_build_modelcalc_widget.observe(calculate_nwv20b, names='value')
    
    # Combine into layout for display (Non-Peak Year 20)
    Weaving_vol_year20nonpeak_build_widgets = widgets.HBox([
        weaving_Vol_year20nonpeak_build_modelcalc_widget,
        weaving_Vol_year20nonpeak_build_userchanged_widget,
        NWV20B_widget,
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
    NTV20B_widget = widgets.IntText(
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
    def update_truck_Year20NonPeak_Build_Volume(change=None):
        # === Define relevant variables from the universal list ===
        ProjType = projectinfo_widgets.subcategory_dropdown.value
        ArrRate20 = projectinfo_widgets.arrival_rate_base_year_build_widget.value
        GateTime20 = projectinfo_widgets.GateTime20_widget.value
        DepRate20 = projectinfo_widgets.departure_rate_forecast_year_build_widget.value
        NumTrain20 = projectinfo_widgets.NumTrain20_widget.value
        AnnualFactor = params.AnnualFactor
        PerTruckNB = projectinfo_widgets.percent_trucks_nobuild_widget.value
        ADT20B = projectinfo_widgets.adt_20_year_build_widget.value
        ADT20NB = projectinfo_widgets.ADT_20NB_widget.value
        PeakLngthNB = projectinfo_widgets.peak_period_widget.value
        DepRate1 = projectinfo_widgets.departure_rate_forecast_year_no_build_widget.value
        ADT1NB = projectinfo_widgets.adt_base_year_no_build_widget.value
        PerPeakADT = params.per_peak_adt
        PerTruckB = projectinfo_widgets.percent_trucks_build_widget.value

        # Perform the calculation based on Project Type
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
        truck_Vol_year20nonpeak_build_modelcalc_widget.value = round(truck_volume, 2)  # Change here: Update widget value with calculated truck volume

    # Observer setup for non-peak truck volume
    projectinfo_widgets.subcategory_dropdown.observe(update_truck_Year20NonPeak_Build_Volume, names='value')  # ProjType
    projectinfo_widgets.adt_20_year_build_widget.observe(update_truck_Year20NonPeak_Build_Volume, names='value')  # ADT20B
    projectinfo_widgets.percent_trucks_build_widget.observe(update_truck_Year20NonPeak_Build_Volume, names='value')  # PerTruckB
    projectinfo_widgets.departure_rate_forecast_year_build_widget.observe(update_truck_Year20NonPeak_Build_Volume, names='value')  # DepRate20
    projectinfo_widgets.peak_period_widget.observe(update_truck_Year20NonPeak_Build_Volume, names='value')  # PeakLngthNB
    projectinfo_widgets.departure_rate_forecast_year_no_build_widget.observe(update_truck_Year20NonPeak_Build_Volume, names='value')  # DepRate1
    projectinfo_widgets.adt_base_year_no_build_widget.observe(update_truck_Year20NonPeak_Build_Volume, names='value')  # ADT1NB
    projectinfo_widgets.ADT_20NB_widget.observe(update_truck_Year20NonPeak_Build_Volume, names='value')  # ADT20NB
    projectinfo_widgets.arrival_rate_base_year_build_widget.observe(update_truck_Year20NonPeak_Build_Volume, names='value')
    projectinfo_widgets.GateTime20_widget.observe(update_truck_Year20NonPeak_Build_Volume, names='value')
    projectinfo_widgets.NumTrain20_widget.observe(update_truck_Year20NonPeak_Build_Volume, names='value')
    projectinfo_widgets.percent_trucks_nobuild_widget.observe(update_truck_Year20NonPeak_Build_Volume, names='value')
    projectinfo_widgets.adt_base_year_no_build_widget.observe(update_truck_Year20NonPeak_Build_Volume, names='value')
    

    # Final value widget logic for Non-Peak Truck Volume           
    def calculate_ntv20b(change):
        try:
            # Ensure user input is valid
            if isinstance(truck_Vol_year20nonpeak_build_userchanged_widget.value, (int, float)) and truck_Vol_year20nonpeak_build_userchanged_widget.value >= 0:
                NTV20B = max(float(truck_Vol_year20nonpeak_build_userchanged_widget.value), 0)  # Change here: Ensure user input is valid and non-negative
            else:
                NTV20B = max(truck_Vol_year20nonpeak_build_modelcalc_widget.value, 0)  # Change here: Fallback to model value if user input is invalid

            # Update the NTV widget with the final value
            NTV20B_widget.value = NTV20B
        except Exception:
            NTV20B_widget.value = max(truck_Vol_year20nonpeak_build_modelcalc_widget.value, 0)  # Change here: Default to model value on error

    # Link the function to the user-modified truck volume input widget
    truck_Vol_year20nonpeak_build_userchanged_widget.observe(calculate_ntv20b, names='value')  # Change here: Observe the user input for changes
    truck_Vol_year20nonpeak_build_modelcalc_widget.observe(calculate_ntv20b, names='value')  # Change here: Observe the model value for changes

    # Combine into layout for display
    Truck_vol_year20nonpeak_build_widgets = widgets.HBox([
        truck_Vol_year20nonpeak_build_modelcalc_widget,
        truck_Vol_year20nonpeak_build_userchanged_widget,
        NTV20B_widget,
        NTV20B_explanation_widget
    ])


     #######################################################################################################  
    # Non-HOV Speed widgets for Year 20 Non-Peak Build
    nonhov_speed_year20nonpeak_build_modelcalc_widget = widgets.FloatText(
        value=0.0,  # Set initial value to 0 or any other valid integer
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
    NNS20B_widget = widgets.FloatText(
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

        # === Define relevant variables from the universal list ===
        ProjType = projectinfo_widgets.subcategory_dropdown.value
        FFSpeedB = projectinfo_widgets.free_flow_speed_build_widget.value
        GenLanesB = projectinfo_widgets.general_traffic_lanes_build_widget.value
        HOVLanesB = projectinfo_widgets.hov_hot_lanes_build_widget.value
        PeakLngthNB = projectinfo_widgets.peak_period_widget.value
        DepRate1 = projectinfo_widgets.departure_rate_forecast_year_no_build_widget.value
        ADT1NB = projectinfo_widgets.adt_base_year_no_build_widget.value
        ADT20NB = projectinfo_widgets.ADT_20NB_widget.value
        DepRate20 = projectinfo_widgets.departure_rate_forecast_year_build_widget.value
        PerPeakADT = params.per_peak_adt
        PerWeaveB = projectinfo_widgets.percent_traffic_weave_build_widget.value
        SpeedWeaveAdj = params.SpeedWeaveAdj
        SpeedPavAdj = params.SpeedPavAdj
        IRI20B = projectinfo_widgets.iri_forecast_year_build_widget.value
        MaxVC = params.MaxVC
        roadway_capacity_non_HOV = params.roadway_capacity_non_HOV

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
            nonhov_speed = FFSpeedB  # No calculation needed
        else:
            if sum_all == 0:
                nonhov_speed = 55.0  # Default value
            else:
                volume_term = sum_all / ((GenLanesB + HOVLanesB) * GenLaneCapB * (24 - PeakLngthNB))

                # Queuing adjustment
                if ProjType == "Queuing":
                    try:
                        queuing_factor = (
                            (DepRate1 - ADT1NB * (1 - PerPeakADT) / (24 - PeakLngthNB)) /
                            ((ADT1NB / ADT20NB * DepRate20) - ADT1NB * (1 - PerPeakADT) / (24 - PeakLngthNB))
                        )
                    except ZeroDivisionError:
                        queuing_factor = float("inf")
                else:
                    queuing_factor = 1

                # Delay speed calculation
                delay_speed = FFSpeedB / (1 + GenAlphaB * min(volume_term * queuing_factor, MaxVC) ** GenBetaB)
                nonhov_speed = delay_speed

                # Adjustments for specific project types
                if ProjType == "Freeway Connector":
                    nonhov_speed *= SpeedWeaveAdj.get(PerWeaveB, {"Freeway": 1.0})["Freeway"]

                if ProjType in ["HOV Connector", "HOV Drop Ramp"]:
                    nonhov_speed *= SpeedWeaveAdj.get(PerWeaveB, {"HOV": 1.0})["HOV"]

                # Pavement adjustment
                if ProjType == "Pavement":
                    closest_iri_key = min(SpeedPavAdj.keys(), key=lambda x: abs(x - IRI20B))
                    nonhov_speed *= SpeedPavAdj[closest_iri_key]["Auto"]

        # Update the widget with the final calculated speed value
        nonhov_speed_year20nonpeak_build_modelcalc_widget.value = round(nonhov_speed, 1)



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


    def calculate_nns20b(change=None):
        # Access the user-modified value directly from the widget
        if isinstance(nonhov_speed_year20nonpeak_build_userchanged_widget.value, (int, float)) and nonhov_speed_year20nonpeak_build_userchanged_widget.value >= 0:
            updated_NonHOV_year20nonpeak_speed = max(nonhov_speed_year20nonpeak_build_userchanged_widget.value, 5)  # Ensure the speed is at least 5
        else:
            updated_NonHOV_year20nonpeak_speed = max(nonhov_speed_year20nonpeak_build_modelcalc_widget.value, 5)  # Use the model value if the user value is invalid

        # Update the value of NNS20B widget
        NNS20B_widget.value = updated_NonHOV_year20nonpeak_speed
        

    # Link user-modified value to NNS20B calculation
    nonhov_speed_year20nonpeak_build_userchanged_widget.observe(calculate_nns20b, names='value')
    nonhov_speed_year20nonpeak_build_modelcalc_widget.observe(calculate_nns20b, names='value')
    

    # Combine into layout
    NonHOV_Year20NonPeak_Build_Speed_widgets = widgets.HBox([nonhov_speed_year20nonpeak_build_modelcalc_widget, nonhov_speed_year20nonpeak_build_userchanged_widget, NNS20B_widget, NNS20B_explanation_widget])

    
     #######################################################################################################     
    # Widgets for Non-Peak Weaving Speed Calculation (Non-Peak Build)
    weave_speed_year20nonpeak_build_modelcalc_widget = widgets.FloatText(
        value=0.0,  # Set initial value to 0 or any other valid integer
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
    NWS20B_widget = widgets.FloatText(
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
        # === Define relevant variables from the universal list ===
        ProjType = projectinfo_widgets.subcategory_dropdown.value
        NumDirections = projectinfo_widgets.one_two_way_widget.value
        PeakLngthNB = projectinfo_widgets.peak_period_widget.value
        SegmentB = projectinfo_widgets.highway_segment_build_widget.value
        FFSpeedB = projectinfo_widgets.free_flow_speed_build_widget.value
        RampFFSpdB = projectinfo_widgets.ramp_design_speed_build_widget.value
        SpeedPavAdj = params.SpeedPavAdj
        IRI20B = projectinfo_widgets.iri_forecast_year_build_widget.value

        # Retrieve widget/input values
        NWV20B = NWV20B_widget.value  # NWV20B
        NTV20B = NTV20B_widget.value  # NTV20B
        NNS20B = NNS20B_widget.value  # NNS20B

        if NWV20B == 0:
            # If NWV20B is zero, use the default value of 55
            Year20NonPeakBuildWeaveSpeed = 55.0
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
    weave_speed_year20nonpeak_build_modelcalc_widget.observe(calculate_nws20b, names='value')

    # Combine into layout for display
    Weave_Year20NonPeak_Build_Speed_widgets = widgets.HBox([
        weave_speed_year20nonpeak_build_modelcalc_widget,
        weave_speed_year20nonpeak_build_userchanged_widget,
        NWS20B_widget,
        NWS20B_explanation_widget
    ])
    
     #######################################################################################################  
        
    # Widgets for Non-Peak Truck Speed Calculation
    truck_speed_year20nonpeak_build_modelcalc_widget = widgets.FloatText(
        value=0.0,  # Set initial value to 0 or any other valid integer
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
    NTS20B_widget = widgets.FloatText(
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
        # === Define relevant variables from the universal list ===
        ProjType = projectinfo_widgets.subcategory_dropdown.value
        IRI20B = projectinfo_widgets.iri_forecast_year_build_widget.value
        TruckSpeed = projectinfo_widgets.truck_speed_widget.value
        FFSpeedB = projectinfo_widgets.free_flow_speed_build_widget.value
        SpeedPavAdj = params.SpeedPavAdj

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
            truck_speed_year20nonpeak_build_modelcalc_widget.value = 55.0
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
    truck_speed_year20nonpeak_build_modelcalc_widget.observe(calculate_nts20b, names='value')
    

    # Combine into layout for display
    Truck_Year20NonPeak_Build_Speed_widgets = widgets.HBox([truck_speed_year20nonpeak_build_modelcalc_widget, truck_speed_year20nonpeak_build_userchanged_widget, NTS20B_widget,  NTS20B_explanation_widget])

##############################################################################################################################################################################################################   

    RADataAvail_widget = widgets.Dropdown(
        options=['Yes', 'No'],
        value='No',  
        description='Detailed Information on Ramp and Arterial Inputs Available:',
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )
    
    SegmentR_widget = widgets.IntText(
        value=0,
        description="Aggregate Segment Length in miles (All Ramps):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )
    
    SegmentA_widget = widgets.IntText(
        value=0,
        description="Aggregate Arterial Length in miles (All Ramps):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )
    
    # Widgets for Aggregate Ramp Volume - Year 1 No-Build (Calculated by Model)
    agg_ramp_vol_year1_nobuild_userentered_widget = widgets.IntText(
        value=0,  # Set initial value to 0 or any valid integer
        description="Aggregate Ramp Volume (User Entered):",
        disabled=False,  # Make it read-only
        layout=common_layout,
        style={'description_width': 'initial'}
    )


    # Used for Project Evaluation — defaults to modelcalc value unless user changes
    PRV1NB_widget = widgets.IntText(
        value=agg_ramp_vol_year1_nobuild_userentered_widget.value,  # Initially set to calculated value
        description="Aggregate Ramp Volume (Used for Proj Eval):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )
    
    # Explanation input for user changes
    PRV1NB_source_widget = widgets.Text(
        value=None,
        description="Source/Notes:",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )
    
    # Combine into layout for display
    Agg_ramp_vol_year1_nobuild_widgets = widgets.HBox([agg_ramp_vol_year1_nobuild_userentered_widget, PRV1NB_widget, PRV1NB_source_widget])

  
    # Function to calculate PRV1NB from user entry or default to 0
    def calculate_prv1nb(change):
        try:
            user_val = int(agg_ramp_vol_year1_nobuild_userentered_widget.value)
            used_val = user_val if user_val >= 0 else 0
        except (ValueError, TypeError):
            used_val = 0  # If not a valid number, use 0

        PRV1NB_widget.value = used_val

    # Attach the function to observe changes in user input
    agg_ramp_vol_year1_nobuild_userentered_widget.observe(calculate_prv1nb, names='value')

 #######################################################################################################  
    # User-entered average arterial volume (read-only)
    avg_arterial_vol_year1_nobuild_userentered_widget = widgets.IntText(
        value=0,
        description="Avg. Arterial Volume (User Entered):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Used for Project Evaluation — initially set to modelcalc value
    PAV1NB_widget = widgets.IntText(
        value=avg_arterial_vol_year1_nobuild_userentered_widget.value,  # Starts with calculated value
        description="Avg. Arterial Volume (Used for Proj Eval):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )
    
    # Function to compute the project evaluation value from user-entered avg arterial volume
    def calculate_pav1nb(change):
        try:
            user_val = int(avg_arterial_vol_year1_nobuild_userentered_widget.value)
            used_val = user_val if user_val >= 0 else 0
        except (ValueError, TypeError):
            used_val = 0

        PAV1NB_widget.value = used_val

    # Trigger function on user input change
    avg_arterial_vol_year1_nobuild_userentered_widget.observe(calculate_pav1nb, names='value')
    
    # Explanation input for user changes for PAV1NB
    PAV1NB_source_widget = widgets.Text(
        value=None,
        description="Source/Notes:",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Combine the widgets into layout for display for PAV1NB
    Avg_arterial_vol_year1_nobuild_widgets = widgets.HBox([avg_arterial_vol_year1_nobuild_userentered_widget, PAV1NB_widget, PAV1NB_source_widget])

    
 #######################################################################################################  

    # User-changed ramp speed (editable)
    avg_ramp_speed_year1_nobuild_userchanged_widget = widgets.IntText(
        value=0,
        description="Avg. Ramp Speed (User Changed):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Used for Project Evaluation — initially set to modelcalc value
    PRS1NB_widget = widgets.IntText(
        value=avg_ramp_speed_year1_nobuild_userchanged_widget.value,  # Starts with calculated value
        description="Avg. Ramp Speed (Used for Proj Eval):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )
    
    def calculate_prs1nb(change):
        try:
            IdleSpeed = params.IdleSpeed
            
            user_val = int(avg_ramp_speed_year1_nobuild_userchanged_widget.value)
            used_val = max(user_val, IdleSpeed) if user_val >= 0 else IdleSpeed
        except (ValueError, TypeError):
            used_val = IdleSpeed  # Fall back to IdleSpeed if invalid

        PRS1NB_widget.value = used_val

    # Attach the observer
    avg_ramp_speed_year1_nobuild_userchanged_widget.observe(calculate_prs1nb, names='value')

    # Explanation input for user changes for PAV1NB
    PRS1NB_source_widget = widgets.Text(
        value=None,
        description="Source/Notes:",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Combine the widgets into layout for display for PAV1NB
    Avg_ramp_speed_year1_nobuild_widgets = widgets.HBox([avg_ramp_speed_year1_nobuild_userchanged_widget, PRS1NB_widget, PRS1NB_source_widget])

 #######################################################################################################  

    # User-changed arterial speed input
    avg_arterial_speed_year1_nobuild_userchanged_widget = widgets.IntText(
        value=0,
        description="Avg. Arterial Speed (User Changed):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Used for Project Evaluation — initially set to modelcalc value
    PAS1NB_widget = widgets.IntText(
        value=avg_arterial_speed_year1_nobuild_userchanged_widget.value,  # Default to model value
        description="Avg. Arterial Speed (Used for Proj Eval):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )
    
    def calculate_pas1nb(change):
        try:
            IdleSpeed = params.IdleSpeed
            
            user_val = int(avg_arterial_speed_year1_nobuild_userchanged_widget.value)
            used_val = max(user_val, IdleSpeed) if user_val >= 0 else IdleSpeed
        except (ValueError, TypeError):
            used_val = IdleSpeed  # Fallback to IdleSpeed if invalid

        PAS1NB_widget.value = used_val

    # Observe and link the calculation to user input
    avg_arterial_speed_year1_nobuild_userchanged_widget.observe(calculate_pas1nb, names='value')
    
    # Explanation input for user changes for PAV1NB
    PAS1NB_source_widget = widgets.Text(
        value=None,
        description="Source/Notes:",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Combine the widgets into layout for display for PAV1NB
    Avg_arterial_speed_year1_nobuild_widgets = widgets.HBox([avg_arterial_speed_year1_nobuild_userchanged_widget, PAS1NB_widget, PAS1NB_source_widget])


    #######################################################################################################

    # Widgets for Aggregate Ramp Volume - Year 20 No-Build (Calculated by Model)
    agg_ramp_vol_year20_nobuild_userentered_widget = widgets.IntText(
        value=0,  # Set initial value to 0 or any valid integer
        description="Aggregate Ramp Volume (User Entered):",
        disabled=False,  # Make it read-only
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Used for Project Evaluation — defaults to modelcalc value unless user changes
    PRV20NB_widget = widgets.IntText(
        value=agg_ramp_vol_year20_nobuild_userentered_widget.value,  # Initially set to calculated value
        description="Aggregate Ramp Volume (Used for Proj Eval):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Explanation input for user changes
    PRV20NB_source_widget = widgets.Text(
        value=None,
        description="Source/Notes:",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Combine into layout for display for PAV20NB
    Agg_ramp_vol_year20_nobuild_widgets = widgets.HBox([agg_ramp_vol_year20_nobuild_userentered_widget, PRV20NB_widget, PRV20NB_source_widget])

    # Function to calculate PRV20NB from user entry or default to 0
    def calculate_prv20nb(change):
        try:
            user_val = int(agg_ramp_vol_year20_nobuild_userentered_widget.value)
            used_val = user_val if user_val >= 0 else 0
        except (ValueError, TypeError):
            used_val = 0  # If not a valid number, use 0

        PRV20NB_widget.value = used_val

    # Attach the function to observe changes in user input
    agg_ramp_vol_year20_nobuild_userentered_widget.observe(calculate_prv20nb, names='value')

    #######################################################################################################

    # User-entered average arterial volume (read-only)
    avg_arterial_vol_year20_nobuild_userentered_widget = widgets.IntText(
        value=0,
        description="Avg. Arterial Volume (User Entered):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Used for Project Evaluation — initially set to modelcalc value
    PAV20NB_widget = widgets.IntText(
        value=avg_arterial_vol_year20_nobuild_userentered_widget.value,  # Starts with calculated value
        description="Avg. Arterial Volume (Used for Proj Eval):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Function to compute the project evaluation value from user-entered avg arterial volume
    def calculate_pav20nb(change):
        try:
            user_val = int(avg_arterial_vol_year20_nobuild_userentered_widget.value)
            used_val = user_val if user_val >= 0 else 0
        except (ValueError, TypeError):
            used_val = 0

        PAV20NB_widget.value = used_val

    # Trigger function on user input change
    avg_arterial_vol_year20_nobuild_userentered_widget.observe(calculate_pav20nb, names='value')

    # Explanation input for user changes for PAV20NB
    PAV20NB_source_widget = widgets.Text(
        value=None,
        description="Source/Notes:",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Combine the widgets into layout for display for PAV20NB
    Avg_arterial_vol_year20_nobuild_widgets = widgets.HBox([avg_arterial_vol_year20_nobuild_userentered_widget, PAV20NB_widget, PAV20NB_source_widget])

    #######################################################################################################

    # User-changed ramp speed (editable)
    avg_ramp_speed_year20_nobuild_userchanged_widget = widgets.IntText(
        value=0,
        description="Avg. Ramp Speed (User Changed):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Used for Project Evaluation — initially set to modelcalc value
    PRS20NB_widget = widgets.IntText(
        value=avg_ramp_speed_year20_nobuild_userchanged_widget.value,  # Starts with calculated value
        description="Avg. Ramp Speed (Used for Proj Eval):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    def calculate_prs20nb(change):
        try:
            IdleSpeed = params.IdleSpeed

            user_val = int(avg_ramp_speed_year20_nobuild_userchanged_widget.value)
            used_val = max(user_val, IdleSpeed) if user_val >= 0 else IdleSpeed
        except (ValueError, TypeError):
            used_val = IdleSpeed  # Fall back to IdleSpeed if invalid

        PRS20NB_widget.value = used_val

    # Attach the observer
    avg_ramp_speed_year20_nobuild_userchanged_widget.observe(calculate_prs20nb, names='value')

    # Explanation input for user changes for PRS20NB
    PRS20NB_source_widget = widgets.Text(
        value=None,
        description="Source/Notes:",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Combine the widgets into layout for display for PRS20NB
    Avg_ramp_speed_year20_nobuild_widgets = widgets.HBox([avg_ramp_speed_year20_nobuild_userchanged_widget, PRS20NB_widget, PRS20NB_source_widget])

    #######################################################################################################

    # User-changed arterial speed input
    avg_arterial_speed_year20_nobuild_userchanged_widget = widgets.IntText(
        value=0,
        description="Avg. Arterial Speed (User Changed):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Used for Project Evaluation — initially set to modelcalc value
    PAS20NB_widget = widgets.IntText(
        value=avg_arterial_speed_year20_nobuild_userchanged_widget.value,  # Default to model value
        description="Avg. Arterial Speed (Used for Proj Eval):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    def calculate_pas20nb(change):
        try:
            IdleSpeed = params.IdleSpeed

            user_val = int(avg_arterial_speed_year20_nobuild_userchanged_widget.value)
            used_val = max(user_val, IdleSpeed) if user_val >= 0 else IdleSpeed
        except (ValueError, TypeError):
            used_val = IdleSpeed  # Fallback to IdleSpeed if invalid

        PAS20NB_widget.value = used_val

    # Observe and link the calculation to user input
    avg_arterial_speed_year20_nobuild_userchanged_widget.observe(calculate_pas20nb, names='value')

    # Explanation input for user changes for PAS20NB
    PAS20NB_source_widget = widgets.Text(
        value=None,
        description="Source/Notes:",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Combine the widgets into layout for display for PAS20NB
    Avg_arterial_speed_year20_nobuild_widgets = widgets.HBox([avg_arterial_speed_year20_nobuild_userchanged_widget, PAS20NB_widget, PAS20NB_source_widget])
    
     #########################################################################

    # Widgets for Aggregate Ramp Volume - Year 1 Build (Calculated by Model)
    agg_ramp_vol_year1_build_userentered_widget = widgets.IntText(
        value=0,  # Set initial value to 0 or any valid integer
        description="Aggregate Ramp Volume (User Entered):",
        disabled=False,  # Make it read-only
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Used for Project Evaluation — defaults to modelcalc value unless user changes
    PRV1B_widget = widgets.IntText(
        value=agg_ramp_vol_year1_build_userentered_widget.value,  # Initially set to calculated value
        description="Aggregate Ramp Volume (Used for Proj Eval):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Explanation input for user changes
    PRV1B_source_widget = widgets.Text(
        value=None,
        description="Source/Notes:",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Combine into layout for display
    Agg_ramp_vol_year1_build_widgets = widgets.HBox([agg_ramp_vol_year1_build_userentered_widget, PRV1B_widget, PRV1B_source_widget])

    # Function to calculate PRV1B from user entry or default to 0
    def calculate_prv1b(change):
        try:
            user_val = int(agg_ramp_vol_year1_build_userentered_widget.value)
            used_val = user_val if user_val >= 0 else 0
        except (ValueError, TypeError):
            used_val = 0  # If not a valid number, use 0

        PRV1B_widget.value = used_val

    # Attach the function to observe changes in user input
    agg_ramp_vol_year1_build_userentered_widget.observe(calculate_prv1b, names='value')

    #########################################################################

    # User-entered average arterial volume (read-only)
    avg_arterial_vol_year1_build_userentered_widget = widgets.IntText(
        value=0,
        description="Avg. Arterial Volume (User Entered):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Used for Project Evaluation — initially set to modelcalc value
    PAV1B_widget = widgets.IntText(
        value=avg_arterial_vol_year1_build_userentered_widget.value,  # Starts with calculated value
        description="Avg. Arterial Volume (Used for Proj Eval):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Function to compute the project evaluation value from user-entered avg arterial volume
    def calculate_pav1b(change):
        try:
            user_val = int(avg_arterial_vol_year1_build_userentered_widget.value)
            used_val = user_val if user_val >= 0 else 0
        except (ValueError, TypeError):
            used_val = 0

        PAV1B_widget.value = used_val

    # Trigger function on user input change
    avg_arterial_vol_year1_build_userentered_widget.observe(calculate_pav1b, names='value')

    # Explanation input for user changes for PAV1B
    PAV1B_source_widget = widgets.Text(
        value=None,
        description="Source/Notes:",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Combine the widgets into layout for display for PAV1B
    Avg_arterial_vol_year1_build_widgets = widgets.HBox([avg_arterial_vol_year1_build_userentered_widget, PAV1B_widget, PAV1B_source_widget])

    #########################################################################

    # User-changed ramp speed (editable)
    avg_ramp_speed_year1_build_userchanged_widget = widgets.IntText(
        value=0,
        description="Avg. Ramp Speed (User Changed):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Used for Project Evaluation — initially set to modelcalc value
    PRS1B_widget = widgets.IntText(
        value=avg_ramp_speed_year1_build_userchanged_widget.value,  # Starts with calculated value
        description="Avg. Ramp Speed (Used for Proj Eval):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    def calculate_prs1b(change):
        try:
            IdleSpeed = params.IdleSpeed

            user_val = int(avg_ramp_speed_year1_build_userchanged_widget.value)
            used_val = max(user_val, IdleSpeed) if user_val >= 0 else IdleSpeed
        except (ValueError, TypeError):
            used_val = IdleSpeed  # Fall back to IdleSpeed if invalid

        PRS1B_widget.value = used_val

    # Attach the observer
    avg_ramp_speed_year1_build_userchanged_widget.observe(calculate_prs1b, names='value')

    # Explanation input for user changes for PRS1B
    PRS1B_source_widget = widgets.Text(
        value=None,
        description="Source/Notes:",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Combine the widgets into layout for display for PRS1B
    Avg_ramp_speed_year1_build_widgets = widgets.HBox([avg_ramp_speed_year1_build_userchanged_widget, PRS1B_widget, PRS1B_source_widget])

    #########################################################################

    # User-changed arterial speed input
    avg_arterial_speed_year1_build_userchanged_widget = widgets.IntText(
        value=0,
        description="Avg. Arterial Speed (User Changed):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Used for Project Evaluation — initially set to modelcalc value
    PAS1B_widget = widgets.IntText(
        value=avg_arterial_speed_year1_build_userchanged_widget.value,  # Default to model value
        description="Avg. Arterial Speed (Used for Proj Eval):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    def calculate_pas1b(change):
        try:
            IdleSpeed = params.IdleSpeed

            user_val = int(avg_arterial_speed_year1_build_userchanged_widget.value)
            used_val = max(user_val, IdleSpeed) if user_val >= 0 else IdleSpeed
        except (ValueError, TypeError):
            used_val = IdleSpeed  # Fallback to IdleSpeed if invalid

        PAS1B_widget.value = used_val

    # Observe and link the calculation to user input
    avg_arterial_speed_year1_build_userchanged_widget.observe(calculate_pas1b, names='value')

    # Explanation input for user changes for PAS1B
    PAS1B_source_widget = widgets.Text(
        value=None,
        description="Source/Notes:",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Combine the widgets into layout for display for PAS1B
    Avg_arterial_speed_year1_build_widgets = widgets.HBox([avg_arterial_speed_year1_build_userchanged_widget, PAS1B_widget, PAS1B_source_widget])

    #########################################################################

    # Widgets for Aggregate Ramp Volume - Year 20 Build (Calculated by Model)
    agg_ramp_vol_year20_build_userentered_widget = widgets.IntText(
        value=0,  # Set initial value to 0 or any valid integer
        description="Aggregate Ramp Volume (User Entered):",
        disabled=False,  # Make it read-only
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Used for Project Evaluation — defaults to modelcalc value unless user changes
    PRV20B_widget = widgets.IntText(
        value=agg_ramp_vol_year20_build_userentered_widget.value,  # Initially set to calculated value
        description="Aggregate Ramp Volume (Used for Proj Eval):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Explanation input for user changes
    PRV20B_source_widget = widgets.Text(
        value=None,
        description="Source/Notes:",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Combine into layout for display for PAV20B
    Agg_ramp_vol_year20_build_widgets = widgets.HBox([agg_ramp_vol_year20_build_userentered_widget, PRV20B_widget, PRV20B_source_widget])

    # Function to calculate PRV20B from user entry or default to 0
    def calculate_prv20b(change):
        try:
            user_val = int(agg_ramp_vol_year20_build_userentered_widget.value)
            used_val = user_val if user_val >= 0 else 0
        except (ValueError, TypeError):
            used_val = 0  # If not a valid number, use 0

        PRV20B_widget.value = used_val

    # Attach the function to observe changes in user input
    agg_ramp_vol_year20_build_userentered_widget.observe(calculate_prv20b, names='value')

    #########################################################################

    # User-entered average arterial volume (read-only)
    avg_arterial_vol_year20_build_userentered_widget = widgets.IntText(
        value=0,
        description="Avg. Arterial Volume (User Entered):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Used for Project Evaluation — initially set to modelcalc value
    PAV20B_widget = widgets.IntText(
        value=avg_arterial_vol_year20_build_userentered_widget.value,  # Starts with calculated value
        description="Avg. Arterial Volume (Used for Proj Eval):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Function to compute the project evaluation value from user-entered avg arterial volume
    def calculate_pav20b(change):
        try:
            user_val = int(avg_arterial_vol_year20_build_userentered_widget.value)
            used_val = user_val if user_val >= 0 else 0
        except (ValueError, TypeError):
            used_val = 0

        PAV20B_widget.value = used_val

    # Trigger function on user input change
    avg_arterial_vol_year20_build_userentered_widget.observe(calculate_pav20b, names='value')

    # Explanation input for user changes for PAV20B
    PAV20B_source_widget = widgets.Text(
        value=None,
        description="Source/Notes:",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Combine the widgets into layout for display for PAV20B
    Avg_arterial_vol_year20_build_widgets = widgets.HBox([avg_arterial_vol_year20_build_userentered_widget, PAV20B_widget, PAV20B_source_widget])

    #########################################################################

    # User-changed ramp speed (editable)
    avg_ramp_speed_year20_build_userchanged_widget = widgets.IntText(
        value=0,
        description="Avg. Ramp Speed (User Changed):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Used for Project Evaluation — initially set to modelcalc value
    PRS20B_widget = widgets.IntText(
        value=avg_ramp_speed_year20_build_userchanged_widget.value,  # Starts with calculated value
        description="Avg. Ramp Speed (Used for Proj Eval):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    def calculate_prs20b(change):
        try:
            IdleSpeed = params.IdleSpeed

            user_val = int(avg_ramp_speed_year20_build_userchanged_widget.value)
            used_val = max(user_val, IdleSpeed) if user_val >= 0 else IdleSpeed
        except (ValueError, TypeError):
            used_val = IdleSpeed  # Fall back to IdleSpeed if invalid

        PRS20B_widget.value = used_val

    # Attach the observer
    avg_ramp_speed_year20_build_userchanged_widget.observe(calculate_prs20b, names='value')

    # Explanation input for user changes for PRS20B
    PRS20B_source_widget = widgets.Text(
        value=None,
        description="Source/Notes:",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Combine the widgets into layout for display for PRS20B
    Avg_ramp_speed_year20_build_widgets = widgets.HBox([avg_ramp_speed_year20_build_userchanged_widget, PRS20B_widget, PRS20B_source_widget])

    #########################################################################

    # User-changed arterial speed input
    avg_arterial_speed_year20_build_userchanged_widget = widgets.IntText(
        value=0,
        description="Avg. Arterial Speed (User Changed):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Used for Project Evaluation — initially set to modelcalc value
    PAS20B_widget = widgets.IntText(
        value=avg_arterial_speed_year20_build_userchanged_widget.value,  # Default to model value
        description="Avg. Arterial Speed (Used for Proj Eval):",
        disabled=True,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    def calculate_pas20b(change):
        try:
            IdleSpeed = params.IdleSpeed

            user_val = int(avg_arterial_speed_year20_build_userchanged_widget.value)
            used_val = max(user_val, IdleSpeed) if user_val >= 0 else IdleSpeed
        except (ValueError, TypeError):
            used_val = IdleSpeed  # Fallback to IdleSpeed if invalid

        PAS20B_widget.value = used_val

    # Observe and link the calculation to user input
    avg_arterial_speed_year20_build_userchanged_widget.observe(calculate_pas20b, names='value')

    # Explanation input for user changes for PAS20B
    PAS20B_source_widget = widgets.Text(
        value=None,
        description="Source/Notes:",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Combine the widgets into layout for display for PAS20B
    Avg_arterial_speed_year20_build_widgets = widgets.HBox([avg_arterial_speed_year20_build_userchanged_widget, PAS20B_widget, PAS20B_source_widget])

    
    
##############################################################################################################################################################################################################  

    HOVtrips_year1_nobuild_peak_widget = widgets.IntText(
        value=0,
        description="HOV Annual Person Trips (No Build):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    HOVtrips_year1_build_peak_widget = widgets.IntText(
        value=0,
        description="HOV Annual Person Trips (Build):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )
    
    # Combine the widgets into layout for display 
    Annual_person_trips_year1_peak_HOV_widgets = widgets.HBox([HOVtrips_year1_nobuild_peak_widget, HOVtrips_year1_build_peak_widget])

    NonHOVtrips_year1_nobuild_peak_widget = widgets.IntText(
        value=0,
        description="Non-HOV Annual Person Trips (No Build):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    NonHOVtrips_year1_build_peak_widget = widgets.IntText(
        value=0,
        description="Non-HOV Annual Person Trips (Build):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    PNT1Ind_widget = widgets.IntText(
        value=0,
        description="Non-HOV Annual Person Trips (Induced):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )
    
    # Combine the widgets into layout for display 
    Annual_person_trips_year1_peak_NonHOV_widgets = widgets.HBox([NonHOVtrips_year1_nobuild_peak_widget, NonHOVtrips_year1_build_peak_widget, PNT1Ind_widget])

    TruckTrips_year1_nobuild_peak_widget = widgets.IntText(
        value=0,
        description="Truck Annual Trips (No Build):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    TruckTrips_year1_build_peak_widget = widgets.IntText(
        value=0,
        description="Truck Annual Trips (Build):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    PTT1Ind_widget = widgets.IntText(
        value=0,
        description="Truck Annual Trips (Induced):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )
    
    # Combine the widgets into layout for display 
    Annual_person_trips_year1_peak_Truck_widgets = widgets.HBox([TruckTrips_year1_nobuild_peak_widget, TruckTrips_year1_build_peak_widget, PTT1Ind_widget])

    NonHOVtrips_year1_nobuild_widget = widgets.IntText(
        value=0,
        description="Non-HOV Annual Person Trips (No Build):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    NonHOVtrips_year1_build_widget = widgets.IntText(
        value=0,
        description="Non-HOV Annual Person Trips (Build):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    NNT1Ind_widget = widgets.IntText(
        value=0,
        description="Non-HOV Annual Person Trips (Induced):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )
    
    # Combine the widgets into layout for display 
    Annual_person_trips_year1_nonpeak_nonHOV_widgets = widgets.HBox([NonHOVtrips_year1_nobuild_widget, NonHOVtrips_year1_build_widget, NNT1Ind_widget])

    TruckTrips_year1_nobuild_widget = widgets.IntText(
        value=0,
        description="Truck Annual Trips (No Build):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    TruckTrips_year1_build_widget = widgets.IntText(
        value=0,
        description="Truck Annual Trips (Build):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    NTT1Ind_widget = widgets.IntText(
        value=0,
        description="Truck Annual Trips (Induced):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )
    
    # Combine the widgets into layout for display 
    Annual_person_trips_year1_nonpeak_Truck_widgets = widgets.HBox([TruckTrips_year1_nobuild_widget, TruckTrips_year1_build_widget, NTT1Ind_widget])

    TotalTrips_year1_nobuild_widget = widgets.IntText(
        value=0,
        description="Total Annual Trips (No Build):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    TotalTrips_year1_build_widget = widgets.IntText(
        value=0,
        description="Total Annual Trips (Build):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    TotalTrips_year1_induced_widget = widgets.IntText(
        value=0,
        description="Total Annual Trips (Induced):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )
    
    # Combine the widgets into layout for display 
    Annual_person_trips_year1_nonpeak_TotalTrips_widgets = widgets.HBox([TotalTrips_year1_nobuild_widget, TotalTrips_year1_build_widget, TotalTrips_year1_induced_widget])

    HOVtrips_year20_nobuild_peak_widget = widgets.IntText(
        value=0,
        description="HOV Annual Person Trips (No Build):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    HOVtrips_year20_build_peak_widget = widgets.IntText(
        value=0,
        description="HOV Annual Person Trips (Build):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Combine the widgets into layout for display 
    Annual_person_trips_year20_peak_HOV_widgets = widgets.HBox([HOVtrips_year20_nobuild_peak_widget, HOVtrips_year20_build_peak_widget])

    NonHOVtrips_year20_nobuild_peak_widget = widgets.IntText(
        value=0,
        description="Non-HOV Annual Person Trips (No Build):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    NonHOVtrips_year20_build_peak_widget = widgets.IntText(
        value=0,
        description="Non-HOV Annual Person Trips (Build):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    PNT20Ind_widget = widgets.IntText(
        value=0,
        description="Non-HOV Annual Person Trips (Induced):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Combine the widgets into layout for display 
    Annual_person_trips_year20_peak_NonHOV_widgets = widgets.HBox([NonHOVtrips_year20_nobuild_peak_widget, NonHOVtrips_year20_build_peak_widget, PNT20Ind_widget])

    TruckTrips_year20_nobuild_peak_widget = widgets.IntText(
        value=0,
        description="Truck Annual Trips (No Build):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    TruckTrips_year20_build_peak_widget = widgets.IntText(
        value=0,
        description="Truck Annual Trips (Build):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    PTT20Ind_widget = widgets.IntText(
        value=0,
        description="Truck Annual Trips (Induced):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Combine the widgets into layout for display 
    Annual_person_trips_year20_peak_Truck_widgets = widgets.HBox([TruckTrips_year20_nobuild_peak_widget, TruckTrips_year20_build_peak_widget, PTT20Ind_widget])

    NonHOVtrips_year20_nobuild_widget = widgets.IntText(
        value=0,
        description="Non-HOV Annual Person Trips (No Build):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    NonHOVtrips_year20_build_widget = widgets.IntText(
        value=0,
        description="Non-HOV Annual Person Trips (Build):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    NNT20Ind_widget = widgets.IntText(
        value=0,
        description="Non-HOV Annual Person Trips (Induced):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Combine the widgets into layout for display 
    Annual_person_trips_year20_nonpeak_nonHOV_widgets = widgets.HBox([NonHOVtrips_year20_nobuild_widget, NonHOVtrips_year20_build_widget, NNT20Ind_widget])

    TruckTrips_year20_nobuild_widget = widgets.IntText(
        value=0,
        description="Truck Annual Trips (No Build):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    TruckTrips_year20_build_widget = widgets.IntText(
        value=0,
        description="Truck Annual Trips (Build):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    NTT20Ind_widget = widgets.IntText(
        value=0,
        description="Truck Annual Trips (Induced):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Combine the widgets into layout for display 
    Annual_person_trips_year20_nonpeak_Truck_widgets = widgets.HBox([TruckTrips_year20_nobuild_widget, TruckTrips_year20_build_widget, NTT20Ind_widget])

    TotalTrips_year20_nobuild_widget = widgets.IntText(
        value=0,
        description="Total Annual Trips (No Build):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    TotalTrips_year20_build_widget = widgets.IntText(
        value=0,
        description="Total Annual Trips (Build):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    TotalTrips_year20_induced_widget = widgets.IntText(
        value=0,
        description="Total Annual Trips (Induced):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    # Combine the widgets into layout for display 
    Annual_person_trips_year20_nonpeak_TotalTrips_widgets = widgets.HBox([TotalTrips_year20_nobuild_widget, TotalTrips_year20_build_widget, TotalTrips_year20_induced_widget])

    
    
    
 




       
    # Highway Speed and Volume Inputs Section
    
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
            'widgets': [Non_HOV_Vol_year20nonpeak_widgets, Weaving_Vol_year20nonpeak_widgets, Truck_Volume_year20nonpeak_widgets, NonHOV_speed_year20nonpeak_widgets, Weave_Speed_year20nonpeak_widgets, Truck_Speed_year20nonpeak_widgets],
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
            'widgets': [HOV_vol_year20peak_build_widgets, nonHOV_vol_year20peak_build_widgets, Weaving_vol_year20peak_build_widgets, Truck_vol_year20peak_build_widgets, HOV_Year20Peak_Build_Speed_widgets, NonHOV_Year20Peak_Build_Speed_widgets, Weave_Year20Peak_Build_Speed_widgets, Truck_Year20Peak_Build_Speed_widgets ],
            'info_texts': highway_speed_and_volume_input_info[:8]
        },
        {
            'subtitle': 'Year 20 - Non-Peak Period',  
            'widgets': [NonHOV_Year20NonPeak_Build_Volume_widgets, Weaving_vol_year20nonpeak_build_widgets, Truck_vol_year20nonpeak_build_widgets, NonHOV_Year20NonPeak_Build_Speed_widgets, Weave_Year20NonPeak_Build_Speed_widgets, Truck_Year20NonPeak_Build_Speed_widgets ],
            'info_texts': highway_speed_and_volume_input_info[8:14]
        }
    ]
         

    
    ramp_and_arterial_input_subsections = [
        {
            'subtitle': 'Aggregate Segment Length', 
            'widgets': [
                RADataAvail_widget,
                SegmentR_widget,
                SegmentA_widget
            ],
            'info_texts': ramp_and_arterial_input_info[:3]
        },
        
        {
            'subtitle': 'No Build (Year 1 - Peak Period)', 
            'widgets': [
                Agg_ramp_vol_year1_nobuild_widgets,
                Avg_arterial_vol_year1_nobuild_widgets,
                Avg_ramp_speed_year1_nobuild_widgets,
                Avg_arterial_speed_year1_nobuild_widgets
            ],
            'info_texts': ramp_and_arterial_input_info[3:6]
        },
        {
            'subtitle': 'No Build (Year 20 - Peak Period)', 
            'widgets': [
                Agg_ramp_vol_year20_nobuild_widgets,
                Avg_arterial_vol_year20_nobuild_widgets,
                Avg_ramp_speed_year20_nobuild_widgets,
                Avg_arterial_speed_year20_nobuild_widgets
            ],
            'info_texts': ramp_and_arterial_input_info[3:6]
        },
        {
            'subtitle': 'Build (Year 1 - Peak Period)',  
            'widgets': [
                Agg_ramp_vol_year1_build_widgets,
                Avg_arterial_vol_year1_build_widgets,
                Avg_ramp_speed_year1_build_widgets,
                Avg_arterial_speed_year1_build_widgets
            ],
            'info_texts': ramp_and_arterial_input_info[3:6]
        },
        {
            'subtitle': 'Build (Year 20 - Peak Period)',   
            'widgets': [
                Agg_ramp_vol_year20_build_widgets,
                Avg_arterial_vol_year20_build_widgets,
                Avg_ramp_speed_year20_build_widgets,
                Avg_arterial_speed_year20_build_widgets
            ],
            'info_texts': ramp_and_arterial_input_info[3:6]
        }
    ]
    
    annual_person_trips_subsections = [
     
        {
            'subtitle': 'Year 1 - Peak Period', 
            'widgets': [
                Annual_person_trips_year1_peak_HOV_widgets, 
                Annual_person_trips_year1_peak_NonHOV_widgets,
                Annual_person_trips_year1_peak_Truck_widgets
            ],
            'info_texts': annual_person_trips_info[:1]
        },
        {
            'subtitle': 'Year 1 - Non-Peak Period', 
            'widgets': [
                Annual_person_trips_year1_nonpeak_nonHOV_widgets,
                Annual_person_trips_year20_peak_Truck_widgets                
            ],
            'info_texts': annual_person_trips_info[:1]
        },  
        {
            'subtitle': 'Year 1 - Total', 
            'widgets': [
                Annual_person_trips_year1_nonpeak_TotalTrips_widgets
            ],
            'info_texts':annual_person_trips_info[:1]
        },
        
        {
            'subtitle': 'Year 20 - Peak Period', 
            'widgets': [
                Annual_person_trips_year20_peak_HOV_widgets, 
                Annual_person_trips_year20_peak_NonHOV_widgets,
                Annual_person_trips_year20_peak_Truck_widgets
            ],
            'info_texts': annual_person_trips_info[:1]
        },
        {
            'subtitle': 'Year 20 - Non-Peak Period', 
            'widgets': [
                Annual_person_trips_year20_nonpeak_nonHOV_widgets,
                Annual_person_trips_year20_nonpeak_Truck_widgets                
            ],
            'info_texts': annual_person_trips_info[:1]
        },  
        {
            'subtitle': 'Year 20 - Total', 
            'widgets': [
                Annual_person_trips_year20_nonpeak_TotalTrips_widgets
            ],
            'info_texts': annual_person_trips_info[:1]
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
    
    ramp_and_arterial_input_section = create_section_with_subsections(
        ramp_and_arterial_input_title,
        ramp_and_arterial_input_subtitle,
        subsections=ramp_and_arterial_input_subsections
    )
    
    annual_person_trips_section = create_section_with_subsections(
        annual_person_trips_title,
        annual_person_trips_subtitle,
        subsections=annual_person_trips_subsections
    )


    
    
    

    
    

    # Non-HOV Volume Widget
    
    
    all_sections = widgets.VBox([highway_speed_and_volume_input_nobuild_section, highway_speed_and_volume_input_build_section, ramp_and_arterial_input_section, annual_person_trips_section])

    
    display(all_sections)
    
    
    
    
    
    