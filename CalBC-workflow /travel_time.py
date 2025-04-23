import pandas as pd
import ipywidgets as widgets
from IPython.display import display, clear_output

from parameters import parameters
params = parameters()

import projectinfo_widgets
import modelinputs_widgets


# Getting values used in all the functions 
AnnualFactor = params.AnnualFactor

######################################################################### HIGHWAY BENEFITS #########################################################################
############################################################ Average Volume ############################################################

def calculate_average_volumes_highway(AnnualFactor):
    # Define combinations
    periods = ['Peak', 'NonPeak']
    vehicle_types = ['HOV', 'NonHOV', 'Weaving', 'Truck', 'Ramp', 'Arterial']
    years = ['Year1', 'Year20']
    project_states = ['NoBuild', 'Build']

    # Build a dictionary of widget values
    volume_dict = {
        'PHV1NB': modelinputs_widgets.PHV1NB_widget.value,
        'PHV1B': modelinputs_widgets.PHV1B_widget.value,
        'PHV20NB': modelinputs_widgets.PHV20NB_widget.value,
        'PHV20B': modelinputs_widgets.PHV20B_widget.value,
        'PNV1NB': modelinputs_widgets.PNV1NB_widget.value,
        'PNV1B': modelinputs_widgets.PNV1B_widget.value,
        'PNV20NB': modelinputs_widgets.PNV20NB_widget.value,
        'PNV20B': modelinputs_widgets.PNV20B_widget.value,
        'PWV1NB': modelinputs_widgets.PWV1NB_widget.value,
        'PWV1B': modelinputs_widgets.PWV1B_widget.value,
        'PWV20NB': modelinputs_widgets.PWV20NB_widget.value,
        'PWV20B': modelinputs_widgets.PWV20B_widget.value,
        'PTV1NB': modelinputs_widgets.PTV1NB_widget.value,
        'PTV1B': modelinputs_widgets.PTV1B_widget.value,
        'PTV20NB': modelinputs_widgets.PTV20NB_widget.value,
        'PTV20B': modelinputs_widgets.PTV20B_widget.value,
        'PRV1NB': modelinputs_widgets.PRV1NB_widget.value,
        'PRV1B': modelinputs_widgets.PRV1B_widget.value,
        'PRV20NB': modelinputs_widgets.PRV20NB_widget.value,
        'PRV20B': modelinputs_widgets.PRV20B_widget.value,
        'PAV1NB': modelinputs_widgets.PAV1NB_widget.value,
        'PAV1B': modelinputs_widgets.PAV1B_widget.value,
        'PAV20NB': modelinputs_widgets.PAV20NB_widget.value,
        'PAV20B': modelinputs_widgets.PAV20B_widget.value,
        'NNV1NB': modelinputs_widgets.NNV1NB_widget.value,
        'NNV1B': modelinputs_widgets.NNV1B_widget.value,
        'NNV20NB': modelinputs_widgets.NNV20NB_widget.value,
        'NNV20B': modelinputs_widgets.NNV20B_widget.value,
        'NWV1NB': modelinputs_widgets.NWV1NB_widget.value,
        'NWV1B': modelinputs_widgets.NWV1B_widget.value,
        'NWV20NB': modelinputs_widgets.NWV20NB_widget.value,
        'NWV20B': modelinputs_widgets.NWV20B_widget.value,
        'NTV1NB': modelinputs_widgets.NTV1NB_widget.value,
        'NTV1B': modelinputs_widgets.NTV1B_widget.value,
        'NTV20NB': modelinputs_widgets.NTV20NB_widget.value,
        'NTV20B': modelinputs_widgets.NTV20B_widget.value,
    }

    all_combinations = []

    for period in periods:
        for vehicle in vehicle_types:
            if period == 'NonPeak' and vehicle in ['Ramp', 'HOV', 'Arterial']:
                continue
            for year in years:
                for state in project_states:
                    year_part = year.replace("Year", "")
                    state_part = 'NB' if state == 'NoBuild' else 'B'
                    volume_key = f"{period[:1]}{vehicle[:1]}V{year_part}{state_part}"

                    if volume_key in volume_dict:
                        average_volume = volume_dict[volume_key] * AnnualFactor
                        all_combinations.append({
                            'Combination': f"{period}_{vehicle}_{year}_{state}",
                            'AverageVolume': average_volume
                        })
                    else:
                        print(f"Warning: {volume_key} not found in widget values.")
    return all_combinations


# Call the function
average_volumes_highway = calculate_average_volumes_highway(AnnualFactor)



######################################################################### HIGHWAY BENEFITS #########################################################################
############################################################ Average Speed ############################################################

def calculate_average_speeds_highway(AnnualFactor):
    # Define combinations
    periods = ['Peak', 'NonPeak']
    vehicle_types = ['HOV', 'NonHOV', 'Weaving', 'Truck', 'Ramp', 'Arterial']
    years = ['Year1', 'Year20']
    project_states = ['NoBuild', 'Build']

    # Build a dictionary of widget values for speed (replacing 'V' with 'S')
    speed_dict = {
        'PHS1NB': modelinputs_widgets.PHS1NB_widget.value,
        'PHS1B': modelinputs_widgets.PHS1B_widget.value,
        'PHS20NB': modelinputs_widgets.PHS20NB_widget.value,
        'PHS20B': modelinputs_widgets.PHS20B_widget.value,
        'PNS1NB': modelinputs_widgets.PNS1NB_widget.value,
        'PNS1B': modelinputs_widgets.PNS1B_widget.value,
        'PNS20NB': modelinputs_widgets.PNS20NB_widget.value,
        'PNS20B': modelinputs_widgets.PNS20B_widget.value,
        'PWS1NB': modelinputs_widgets.PWS1NB_widget.value,
        'PWS1B': modelinputs_widgets.PWS1B_widget.value,
        'PWS20NB': modelinputs_widgets.PWS20NB_widget.value,
        'PWS20B': modelinputs_widgets.PWS20B_widget.value,
        'PTS1NB': modelinputs_widgets.PTS1NB_widget.value,
        'PTS1B': modelinputs_widgets.PTS1B_widget.value,
        'PTS20NB': modelinputs_widgets.PTS20NB_widget.value,
        'PTS20B': modelinputs_widgets.PTS20B_widget.value,
        'PRS1NB': modelinputs_widgets.PRS1NB_widget.value,
        'PRS1B': modelinputs_widgets.PRS1B_widget.value,
        'PRS20NB': modelinputs_widgets.PRS20NB_widget.value,
        'PRS20B': modelinputs_widgets.PRS20B_widget.value,
        'PAS1NB': modelinputs_widgets.PAS1NB_widget.value,
        'PAS1B': modelinputs_widgets.PAS1B_widget.value,
        'PAS20NB': modelinputs_widgets.PAS20NB_widget.value,
        'PAS20B': modelinputs_widgets.PAS20B_widget.value,
        'NNS1NB': modelinputs_widgets.NNS1NB_widget.value,
        'NNS1B': modelinputs_widgets.NNS1B_widget.value,
        'NNS20NB': modelinputs_widgets.NNS20NB_widget.value,
        'NNS20B': modelinputs_widgets.NNS20B_widget.value,
        'NWS1NB': modelinputs_widgets.NWS1NB_widget.value,
        'NWS1B': modelinputs_widgets.NWS1B_widget.value,
        'NWS20NB': modelinputs_widgets.NWS20NB_widget.value,
        'NWS20B': modelinputs_widgets.NWS20B_widget.value,
        'NTS1NB': modelinputs_widgets.NTS1NB_widget.value,
        'NTS1B': modelinputs_widgets.NTS1B_widget.value,
        'NTS20NB': modelinputs_widgets.NTS20NB_widget.value,
        'NTS20B': modelinputs_widgets.NTS20B_widget.value,
    }

    all_combinations = []

    for period in periods:
        for vehicle in vehicle_types:
            if period == 'NonPeak' and vehicle in ['Ramp', 'HOV', 'Arterial']:
                continue
            for year in years:
                for state in project_states:
                    year_part = year.replace("Year", "")
                    state_part = 'NB' if state == 'NoBuild' else 'B'
                    speed_key = f"{period[:1]}{vehicle[:1]}S{year_part}{state_part}"

                    if speed_key in speed_dict:
                        average_speed = round(speed_dict[speed_key], 1)
                        all_combinations.append({
                            'Combination': f"{period}_{vehicle}_{year}_{state}",
                            'AverageSpeed': average_speed
                        })
                    else:
                        print(f"Warning: {speed_key} not found in widget values.")

    return all_combinations


# Call the function for speed calculations
average_speeds_highway = calculate_average_speeds_highway(AnnualFactor)

def calculate_person_trips_highway(average_volumes_highway):
    ProjType = projectinfo_widgets.subcategory_dropdown.value
    AVOHovNB = projectinfo_widgets.AVOHovNB_widget.value
    AVOHovB = projectinfo_widgets.AVOHovB_widget.value
    AVOPeakNB = projectinfo_widgets.AVO_traffic_P_no_build_widget.value
    AVOPeakB = projectinfo_widgets.AVO_traffic_P_build_widget.value
    AVONonNB = projectinfo_widgets.AVO_traffic_NP_no_build_widget.value
    AVONonB = projectinfo_widgets.AVO_traffic_NP_build_widget.value
    
    
    person_trip_results = []

    for row in average_volumes_highway:
        combo = row['Combination']
        volume = row['AverageVolume']

        # Split the combination key into parts
        period, vehicle, year, state = combo.split('_')

        # Determine AVO based on rules
        if vehicle == 'HOV':
            avo = AVOHovNB if state == 'NoBuild' else AVOHovB

        elif vehicle in ['NonHOV', 'Ramp', 'Arterial']:
            if period == 'Peak':
                avo = AVOPeakNB if state == 'NoBuild' else AVOPeakB
            else:  # NonPeak
                avo = AVONonNB if state == 'NoBuild' else AVONonB

        elif vehicle == 'Weaving':
            hov_condition = ProjType in ["HOV Connector", "HOV Drop Ramp"]
            if period == 'Peak':
                avo = AVOHovNB if hov_condition and state == 'NoBuild' else (
                      AVOHovB if hov_condition else (
                      AVOPeakNB if state == 'NoBuild' else AVOPeakB))
            else:  # NonPeak
                avo = AVOHovNB if hov_condition and state == 'NoBuild' else (
                      AVOHovB if hov_condition else (
                      AVONonNB if state == 'NoBuild' else AVONonB))

        elif vehicle == 'Truck':
            avo = 1  # Person trips = volume for trucks

        else:
            print(f"Unknown vehicle type: {vehicle}")
            avo = 0

        person_trips = volume * avo

        person_trip_results.append({
            'Combination': combo,
            'AnnualPersonTrips': person_trips
        })

    return person_trip_results

annual_person_trips = calculate_person_trips_highway(average_volumes_highway)


def calculate_average_travel_time(average_speeds_highway):
    # Fetch required values from widgets
    ProjType = projectinfo_widgets.subcategory_dropdown.value
    ImpactedNB = projectinfo_widgets.impacted_length_no_build_widget.value
    ImpactedB = projectinfo_widgets.impacted_length_build_widget.value
    SegmentR = modelinputs_widgets.SegmentR_widget.value
    SegmentA = modelinputs_widgets.SegmentA_widget.value
    GateTime1 = projectinfo_widgets.GateTime1_widget.value

    # Safe division helper
    def safe_divide(numerator, denominator):
        return "#DIV/0!" if denominator == 0 else numerator / denominator

    # Results list
    average_travel_time_results = []

    # Iterate over the average speed results
    for row in average_speeds_highway:
        combo = row['Combination']
        speed = row['AverageSpeed']  

        period, vehicle, year, state = combo.split('_')

        # Apply travel time logic based on vehicle type and period
        if vehicle == 'HOV':
            if period == 'Peak':
                travel_time = safe_divide(ImpactedNB, speed) if state == 'NoBuild' else safe_divide(ImpactedB, speed)
            else:  
                continue

        elif vehicle == 'NonHOV':
            if period == 'Peak':
                travel_time = safe_divide(ImpactedNB, speed) if state == 'NoBuild' else safe_divide(ImpactedB, speed)
            else:  
                if ProjType == "Hwy-Rail Grade Crossing":
                    travel_time = GateTime1 / 60 / 2
                else:
                    travel_time = safe_divide(ImpactedNB, speed) if state == 'NoBuild' else safe_divide(ImpactedB, speed)

        elif vehicle == 'Weaving':
            travel_time = safe_divide(ImpactedNB, speed) if state == 'NoBuild' else safe_divide(ImpactedB, speed)

        elif vehicle == 'Truck':
            if period == 'Peak':
                travel_time = safe_divide(ImpactedNB, speed) if state == 'NoBuild' else safe_divide(ImpactedB, speed)
            else:
                if ProjType == "Hwy-Rail Grade Crossing":
                    travel_time = GateTime1 / 60 / 2
                else:
                    travel_time = safe_divide(ImpactedNB, speed) if state == 'NoBuild' else safe_divide(ImpactedB, speed)

        elif vehicle == 'Ramp':
            if period == 'Peak':
                travel_time = safe_divide(SegmentR, speed)
            else:
                continue

        elif vehicle == 'Arterial':
            if period == 'Peak':
                travel_time = safe_divide(SegmentA, speed)
            else:
                continue

        else:
            travel_time = "#N/A"

        average_travel_time_results.append({
            'Combination': combo,
            'AverageTravelTime': travel_time
        })

    return average_travel_time_results














# List of widgets to observe for both volume and speed (combining the existing ones)
widget_triggers_volumes = [
    modelinputs_widgets.PHV1NB_widget,
    modelinputs_widgets.PHV1B_widget,
    modelinputs_widgets.PHV20NB_widget,
    modelinputs_widgets.PHV20B_widget,
    modelinputs_widgets.PNV1NB_widget,
    modelinputs_widgets.PNV1B_widget,
    modelinputs_widgets.PNV20NB_widget,
    modelinputs_widgets.PNV20B_widget,
    modelinputs_widgets.PWV1NB_widget,
    modelinputs_widgets.PWV1B_widget,
    modelinputs_widgets.PWV20NB_widget,
    modelinputs_widgets.PWV20B_widget,
    modelinputs_widgets.PTV1NB_widget,
    modelinputs_widgets.PTV1B_widget,
    modelinputs_widgets.PTV20NB_widget,
    modelinputs_widgets.PTV20B_widget,
    modelinputs_widgets.PRV1NB_widget,
    modelinputs_widgets.PRV1B_widget,
    modelinputs_widgets.PRV20NB_widget,
    modelinputs_widgets.PRV20B_widget,
    modelinputs_widgets.PAV1NB_widget,
    modelinputs_widgets.PAV1B_widget,
    modelinputs_widgets.PAV20NB_widget,
    modelinputs_widgets.PAV20B_widget,
    modelinputs_widgets.NNV1NB_widget,
    modelinputs_widgets.NNV1B_widget,
    modelinputs_widgets.NNV20NB_widget,
    modelinputs_widgets.NNV20B_widget,
    modelinputs_widgets.NWV1NB_widget,
    modelinputs_widgets.NWV1B_widget,
    modelinputs_widgets.NWV20NB_widget,
    modelinputs_widgets.NWV20B_widget,
    modelinputs_widgets.NTV1NB_widget,
    modelinputs_widgets.NTV1B_widget,
    modelinputs_widgets.NTV20NB_widget,
    modelinputs_widgets.NTV20B_widget
]

widget_triggers_speed = [
    modelinputs_widgets.PHS1NB_widget,
    modelinputs_widgets.PHS1B_widget,
    modelinputs_widgets.PHS20NB_widget,
    modelinputs_widgets.PHS20B_widget,
    modelinputs_widgets.PNS1NB_widget,
    modelinputs_widgets.PNS1B_widget,
    modelinputs_widgets.PNS20NB_widget,
    modelinputs_widgets.PNS20B_widget,
    modelinputs_widgets.PWS1NB_widget,
    modelinputs_widgets.PWS1B_widget,
    modelinputs_widgets.PWS20NB_widget,
    modelinputs_widgets.PWS20B_widget,
    modelinputs_widgets.PTS1NB_widget,
    modelinputs_widgets.PTS1B_widget,
    modelinputs_widgets.PTS20NB_widget,
    modelinputs_widgets.PTS20B_widget,
    modelinputs_widgets.PRS1NB_widget,
    modelinputs_widgets.PRS1B_widget,
    modelinputs_widgets.PRS20NB_widget,
    modelinputs_widgets.PRS20B_widget,
    modelinputs_widgets.PAS1NB_widget,
    modelinputs_widgets.PAS1B_widget,
    modelinputs_widgets.PAS20NB_widget,
    modelinputs_widgets.PAS20B_widget,
    modelinputs_widgets.NNS1NB_widget,
    modelinputs_widgets.NNS1B_widget,
    modelinputs_widgets.NNS20NB_widget,
    modelinputs_widgets.NNS20B_widget,
    modelinputs_widgets.NWS1NB_widget,
    modelinputs_widgets.NWS1B_widget,
    modelinputs_widgets.NWS20NB_widget,
    modelinputs_widgets.NWS20B_widget,
    modelinputs_widgets.NTS1NB_widget,
    modelinputs_widgets.NTS1B_widget,
    modelinputs_widgets.NTS20NB_widget,
    modelinputs_widgets.NTS20B_widget
]
    
widget_triggers_persontrips = [    
    #PersonTrips-related widgets
    projectinfo_widgets.subcategory_dropdown,
    projectinfo_widgets.AVOHovNB_widget,
    projectinfo_widgets.AVOHovB_widget,
    projectinfo_widgets.AVO_traffic_P_no_build_widget,
    projectinfo_widgets.AVO_traffic_P_build_widget,
    projectinfo_widgets.AVO_traffic_NP_no_build_widget,
    projectinfo_widgets.AVO_traffic_NP_build_widget
    
]

widget_triggers_avgtraveltime =[
    projectinfo_widgets.subcategory_dropdown,
    projectinfo_widgets.impacted_length_no_build_widget,
    projectinfo_widgets.impacted_length_build_widget,
    modelinputs_widgets.SegmentR_widget,
    modelinputs_widgets.SegmentA_widget,
    projectinfo_widgets.GateTime1_widget,
]
    

# Attach observers to all widgets
for widget in widget_triggers_volumes:
    widget.observe(calculate_average_volumes_highway, names='value')
for widget in widget_triggers_speed:
    widget.observe(calculate_average_speeds_highway, names='value')
for widget in widget_triggers_persontrips:
    widget.observe(calculate_person_trips_highway, names='value')
for widget in widget_triggers_avgtraveltime:
    widget.observe(calculate_average_travel_time, names='value')
    

def update_combined_results(change=None):
        volume_results = calculate_average_volumes_highway(AnnualFactor)
        speed_results = calculate_average_speeds_highway(AnnualFactor)
        person_trips_results = calculate_person_trips_highway(volume_results)
        average_travel_time_results = calculate_average_travel_time(speed_results)

        if volume_results and speed_results and person_trips_results:
            # Combine into DataFrames and merge
            df_volume = pd.DataFrame(volume_results)
            df_speed = pd.DataFrame(speed_results)
            df_person_trips = pd.DataFrame(person_trips_results)
            df_average_travel_time = pd.DataFrame(average_travel_time_results)

            # Merge volume and speed first, adding suffixes
            df_combined = pd.merge(df_volume, df_speed, on="Combination", how="outer", suffixes=("_Volume", "_Speed"))

            # Merge person trips 
            df_combined = pd.merge(df_combined, df_person_trips, on="Combination", how="outer")
            
            #Merge average travel time
            df_combined = pd.merge(df_combined, df_average_travel_time, on="Combination", how="outer")

            # Display the combined table
            display(df_combined)  # This will show the table every time
        else:
            print("No results to display.")




def display_grouped_results_by_vehicle_period():
    volume_results = calculate_average_volumes_highway(AnnualFactor)
    speed_results = calculate_average_speeds_highway(AnnualFactor)
    person_trips_results = calculate_person_trips_highway(volume_results)
    average_travel_time_results = calculate_average_travel_time(speed_results)

    if volume_results and speed_results and person_trips_results:
        # Convert to DataFrames
        df_volume = pd.DataFrame(volume_results)
        df_speed = pd.DataFrame(speed_results)
        df_person_trips = pd.DataFrame(person_trips_results)
        df_average_travel_time = pd.DataFrame(average_travel_time_results)

        # Merge all into one combined DataFrame
        df_combined = pd.merge(df_volume, df_speed, on="Combination", how="outer", suffixes=("_Volume", "_Speed"))
        df_combined = pd.merge(df_combined, df_person_trips, on="Combination", how="outer")
        df_combined = pd.merge(df_combined, df_average_travel_time, on="Combination", how="outer")

        # Split Combination into components
        df_combined[['Period', 'Vehicle', 'Year', 'State']] = df_combined['Combination'].str.split('_', expand=True)
        df_combined['Period'] = pd.Categorical(df_combined['Period'], categories=['Peak', 'NonPeak'], ordered=True)
        
        # Create Group column
        df_combined['Group'] = df_combined['Period'].astype(str) + "_" + df_combined['Vehicle'].astype(str)

        # Display one table per group (e.g. Peak_HOV, NonPeak_Truck)
        for group_name, group_df in df_combined.groupby('Group'):
            print(f"--- {group_name} ---")
            display(group_df.drop(columns=['Period', 'Vehicle', 'Year', 'State', 'Group']))
            print("\n")

    else:
        print("No results to display.")


        
