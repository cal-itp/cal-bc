import pandas as pd
import numpy as np
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
                avg_vol_nobuild = None
                avg_vol_build = None
                for state in project_states:
                    year_part = year.replace("Year", "")
                    state_part = 'NB' if state == 'NoBuild' else 'B'
                    volume_key = f"{period[:1]}{vehicle[:1]}V{year_part}{state_part}"

                    if volume_key in volume_dict:
                        average_volume = volume_dict[volume_key] * AnnualFactor
                        if state == 'NoBuild':
                            avg_vol_nobuild = average_volume
                        else:
                            avg_vol_build = average_volume
                    else:
                        print(f"Warning: {volume_key} not found in widget values.")
                
                # Add to the list only if both values are found
                if avg_vol_nobuild is not None and avg_vol_build is not None:
                    all_combinations.append({
                        'Combination': f"{period}_{vehicle}_{year}",
                        'Avg_Vol_NoBuild': avg_vol_nobuild,
                        'Avg_Vol_Build': avg_vol_build
                    })

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
                avg_speed_nobuild = None
                avg_speed_build = None
                for state in project_states:
                    year_part = year.replace("Year", "")
                    state_part = 'NB' if state == 'NoBuild' else 'B'
                    speed_key = f"{period[:1]}{vehicle[:1]}S{year_part}{state_part}"

                    if speed_key in speed_dict:
                        average_speed = round(speed_dict[speed_key], 1)
                        if state == 'NoBuild':
                            avg_speed_nobuild = average_speed
                        else:
                            avg_speed_build = average_speed
                    else:
                        print(f"Warning: {speed_key} not found in widget values.")
                
                # Add to the list only if both values are found
                if avg_speed_nobuild is not None and avg_speed_build is not None:
                    all_combinations.append({
                        'Combination': f"{period}_{vehicle}_{year}",
                        'Avg_Speed_NoBuild': avg_speed_nobuild,
                        'Avg_Speed_Build': avg_speed_build
                    })

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
        vol_nobuild = row.get('Avg_Vol_NoBuild', 0)
        vol_build = row.get('Avg_Vol_Build', 0)

        period, vehicle, year = combo.split('_')  # We ignore the last 'state' part

        # Default AVO values
        avo_nobuild = avo_build = 0

        if vehicle == 'HOV':
            avo_nobuild = AVOHovNB
            avo_build = AVOHovB

        elif vehicle in ['NonHOV', 'Ramp', 'Arterial']:
            if period == 'Peak':
                avo_nobuild = AVOPeakNB
                avo_build = AVOPeakB
            else:  # NonPeak
                avo_nobuild = AVONonNB
                avo_build = AVONonB

        elif vehicle == 'Weaving':
            hov_condition = ProjType in ["HOV Connector", "HOV Drop Ramp"]
            if period == 'Peak':
                avo_nobuild = AVOHovNB if hov_condition else AVOPeakNB
                avo_build = AVOHovB if hov_condition else AVOPeakB
            else:  # NonPeak
                avo_nobuild = AVOHovNB if hov_condition else AVONonNB
                avo_build = AVOHovB if hov_condition else AVONonB

        elif vehicle == 'Truck':
            avo_nobuild = 1
            avo_build = 1

        else:
            print(f"Unknown vehicle type: {vehicle}")

        # Multiply volumes with AVO to get person trips
        person_trips_nobuild = vol_nobuild * avo_nobuild if vol_nobuild else 0
        person_trips_build = vol_build * avo_build if vol_build else 0

        person_trip_results.append({
            'Combination': combo,
            'AnnualPersonTrips_NoBuild': person_trips_nobuild,
            'AnnualPersonTrips_Build': person_trips_build
        })

    return person_trip_results


# Call the function
annual_person_trips = calculate_person_trips_highway(average_volumes_highway)



def calculate_average_travel_time(average_speeds_highway):
    # Fetch required values from widgets
    ProjType = projectinfo_widgets.subcategory_dropdown.value
    ImpactedNB = projectinfo_widgets.impacted_length_no_build_widget.value
    ImpactedB = projectinfo_widgets.impacted_length_build_widget.value
    SegmentR = modelinputs_widgets.SegmentR_widget.value
    SegmentA = modelinputs_widgets.SegmentA_widget.value
    GateTime1 = projectinfo_widgets.GateTime1_widget.value

    def safe_divide(numerator, denominator):
        return "#DIV/0!" if denominator == 0 else round(numerator / denominator, 2)

    average_travel_time_results = []

    for row in average_speeds_highway:
        combo = row['Combination']
        speed_nobuild = row.get('Avg_Speed_NoBuild', 0)
        speed_build = row.get('Avg_Speed_Build', 0)

        period, vehicle, year = combo.split('_')

        travel_time_nobuild = "#N/A"
        travel_time_build = "#N/A"

        # Travel time calculations
        if vehicle == 'HOV':
            if period == 'Peak':
                travel_time_nobuild = safe_divide(ImpactedNB, speed_nobuild)
                travel_time_build = safe_divide(ImpactedB, speed_build)

        elif vehicle == 'NonHOV':
            if period == 'Peak':
                travel_time_nobuild = safe_divide(ImpactedNB, speed_nobuild)
                travel_time_build = safe_divide(ImpactedB, speed_build)
            else:
                if ProjType == "Hwy-Rail Grade Crossing":
                    gate_time = GateTime1 / 60 / 2
                    travel_time_nobuild = gate_time
                    travel_time_build = gate_time
                else:
                    travel_time_nobuild = safe_divide(ImpactedNB, speed_nobuild)
                    travel_time_build = safe_divide(ImpactedB, speed_build)

        elif vehicle == 'Weaving':
            travel_time_nobuild = safe_divide(ImpactedNB, speed_nobuild)
            travel_time_build = safe_divide(ImpactedB, speed_build)

        elif vehicle == 'Truck':
            if period == 'Peak':
                travel_time_nobuild = safe_divide(ImpactedNB, speed_nobuild)
                travel_time_build = safe_divide(ImpactedB, speed_build)
            else:
                if ProjType == "Hwy-Rail Grade Crossing":
                    gate_time = GateTime1 / 60 / 2
                    travel_time_nobuild = gate_time
                    travel_time_build = gate_time
                else:
                    travel_time_nobuild = safe_divide(ImpactedNB, speed_nobuild)
                    travel_time_build = safe_divide(ImpactedB, speed_build)

        elif vehicle == 'Ramp':
            if period == 'Peak':
                travel_time_nobuild = safe_divide(SegmentR, speed_nobuild)
                travel_time_build = safe_divide(SegmentR, speed_build)

        elif vehicle == 'Arterial':
            if period == 'Peak':
                travel_time_nobuild = safe_divide(SegmentA, speed_nobuild)
                travel_time_build = safe_divide(SegmentA, speed_build)

        # Append result
        average_travel_time_results.append({
            'Combination': combo,
            'Avg_TravelTime_NoBuild': travel_time_nobuild,
            'Avg_TravelTime_Build': travel_time_build
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




# def display_grouped_results_by_vehicle_period():
#     volume_results = calculate_average_volumes_highway(AnnualFactor)
#     speed_results = calculate_average_speeds_highway(AnnualFactor)
#     person_trips_results = calculate_person_trips_highway(volume_results)
#     average_travel_time_results = calculate_average_travel_time(speed_results)

#     if volume_results and speed_results and person_trips_results:
#         # Convert to DataFrames
#         df_volume = pd.DataFrame(volume_results)
#         df_speed = pd.DataFrame(speed_results)
#         df_person_trips = pd.DataFrame(person_trips_results)
#         df_average_travel_time = pd.DataFrame(average_travel_time_results)

#         # Merge all into one combined DataFrame
#         df_combined = pd.merge(df_volume, df_speed, on="Combination", how="outer", suffixes=("_Volume", "_Speed"))
#         df_combined = pd.merge(df_combined, df_person_trips, on="Combination", how="outer")
#         df_combined = pd.merge(df_combined, df_average_travel_time, on="Combination", how="outer")

#         # Split Combination into components (Period, Vehicle, Year)
#         df_combined[['Period', 'Vehicle', 'Year']] = df_combined['Combination'].str.split('_', expand=True)

#         # Modify Combination to just include Year1 and Year20
#         df_combined['Combination'] = df_combined['Year']

#         # Custom group order
#         group_order = [
#             "Peak_HOV", "Peak_NonHOV", "Peak_Weaving", "Peak_Truck", "Peak_Ramp", "Peak_Arterial",
#             "NonPeak_NonHOV", "NonPeak_Weaving", "NonPeak_Truck"
#         ]

#         # Create Group column
#         df_combined['Group'] = df_combined['Period'].astype(str) + "_" + df_combined['Vehicle'].astype(str)

#         # Set Group as categorical and sort
#         df_combined['Group'] = pd.Categorical(df_combined['Group'], categories=group_order, ordered=True)
#         df_combined.sort_values(['Group', 'Year'], inplace=True)

#         # Display one table per group (e.g. Peak_HOV, NonPeak_Truck)
#         for group_name, group_df in df_combined.groupby('Group'):
#             print(f"--- {group_name} ---")

#             # Remove 'Year' suffix from Combination column (just keep the year value)
#             group_df['Year'] = group_df['Year'].apply(lambda x: int(x.replace('Year', '')) if isinstance(x, str) else x)

#             # Reorder columns to place 'Year' at the beginning
#             cols = ['Year'] + [col for col in group_df.columns if col != 'Year']
#             group_df = group_df[cols]
            
#             display(group_df.drop(columns=['Period', 'Vehicle', 'Group', 'Combination']))  # Drop columns we don't need
#             print("\n")

#     else:
#         print("No results to display.")

def get_grouped_highway_results():
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

        # Split Combination into components (Period, Vehicle, Year)
        df_combined[['Period', 'Vehicle', 'Year']] = df_combined['Combination'].str.split('_', expand=True)

        # Clean Year
        df_combined['Year'] = df_combined['Year'].apply(lambda x: int(x.replace('Year', '')) if isinstance(x, str) else x)

        # Reassign Combination to year only (if needed)
        df_combined['Combination'] = df_combined['Year']

        # Define group for sorting (if needed later)
        df_combined['Group'] = df_combined['Period'].astype(str) + "_" + df_combined['Vehicle'].astype(str)

        # Final clean-up: keep only selected columns
        keep_columns = [
            'Year', 'Group',
            'Avg_Vol_NoBuild', 'Avg_Vol_Build',
            'Avg_Speed_NoBuild', 'Avg_Speed_Build',
            'AnnualPersonTrips_NoBuild', 'AnnualPersonTrips_Build',
            'Avg_TravelTime_NoBuild', 'Avg_TravelTime_Build'
        ]
        df_combined = df_combined[keep_columns]

        return df_combined

    else:
        print("No results to display.")
        return None

df_combined = get_grouped_highway_results()   
    



def calculate_trend_for_variables(df, variable_name, group_name):
    """
    Calculates trend for a variable within a specific group, handling 'DIV0' as 0 for regression but preserving it in output.
    """

    # Filter by group
    group_df = df[df['Group'] == group_name]

    # Helper to safely convert to float (return 0 if 'DIV0', else float)
    def safe_float(val):
        try:
            return float(val)
        except:
            return 0.0

    # Extract original values for Year 1 and Year 20
    val1 = group_df.loc[group_df['Year'] == 1, variable_name].values[0]
    val20 = group_df.loc[group_df['Year'] == 20, variable_name].values[0]

    # Flags for DIV0 values
    val1_is_div = str(val1).strip().upper() == 'DIV0'
    val20_is_div = str(val20).strip().upper() == 'DIV0'

    # Convert to numeric for trend
    year_1_value = safe_float(val1)
    year_20_value = safe_float(val20)

    known_years = np.array([1, 20])
    known_values = np.array([year_1_value, year_20_value])

    # Perform regression
    coefficients = np.polyfit(known_years, known_values, 1)
    polynomial = np.poly1d(coefficients)

    # Predict for years 2 to 19
    predicted_years = np.arange(2, 20)
    predicted_values = polynomial(predicted_years)

    # Combine into full series
    all_years = np.concatenate(([1], predicted_years, [20]))
    all_values = np.concatenate(([year_1_value], predicted_values, [year_20_value]))

    # Reinsert 'DIV0'
    all_values = list(all_values)
    if val1_is_div:
        all_values[0] = 'DIV0'
    if val20_is_div:
        all_values[-1] = 'DIV0'

    # Build DataFrame
    df_trend = pd.DataFrame({
        'Year': all_years,
        'Group': group_name,
        variable_name: all_values
    })

    return df_trend


variable_names = ['Avg_Vol_NoBuild', 'Avg_Vol_Build', 'Avg_Speed_NoBuild', 'Avg_Speed_Build', 'AnnualPersonTrips_NoBuild', 'AnnualPersonTrips_Build', 'Avg_TravelTime_NoBuild', 'Avg_TravelTime_Build']
    
    
def generate_trends_from_dataframe(df, variable_names):
    all_group_trends = []

    for group in df['Group'].unique():
        group_trends = []

        for variable_name in variable_names:
            trend_df = calculate_trend_for_variables(df, variable_name, group)
            group_trends.append(trend_df)

        # Merge all variable trends for this group on Year and Group
        group_result = group_trends[0]
        for other_df in group_trends[1:]:
            group_result = pd.merge(group_result, other_df, on=['Year', 'Group'], how='outer')

        all_group_trends.append(group_result)

    # Concatenate all groups
    final_df = pd.concat(all_group_trends, ignore_index=True)

    return final_df



final_trend_df = generate_trends_from_dataframe(df_combined, variable_names)    
    
    
def display_grouped_tables(final_trend_df):
    if final_trend_df is None:
        print("Nothing to display.")
        return

    # Custom order for Peak and NonPeak groups
    peak_order = ["Peak_HOV", "Peak_NonHOV", "Peak_Weaving", "Peak_Truck", "Peak_Ramp", "Peak_Arterial"]
    nonpeak_order = ["NonPeak_NonHOV", "NonPeak_Weaving", "NonPeak_Arterial"]

    # Combine the two lists to define custom sorting order
    custom_order = peak_order + nonpeak_order

    # Sort the groups based on the custom order
    sorted_groups = sorted(final_trend_df['Group'].unique(), key=lambda x: custom_order.index(x) if x in custom_order else len(custom_order))

    for group_name in sorted_groups:
        # Filter the dataframe for each group
        group_df = final_trend_df[final_trend_df['Group'] == group_name]

        # Ensure Year 1 and Year 20 are at the top
        year_1_and_20 = group_df[group_df['Year'].isin([1, 20])]
        rest_of_years = group_df[~group_df['Year'].isin([1, 20])]

        # Sort the remaining years
        rest_of_years = rest_of_years.sort_values(by='Year')

        # Concatenate Year 1, Year 20 with the sorted remaining years
        group_df_sorted = pd.concat([year_1_and_20, rest_of_years])

        print(f"--- {group_name} ---")
        
        # Reorder to put Year at the beginning
        cols = ['Year'] + [col for col in group_df_sorted.columns if col not in ['Year', 'Period', 'Vehicle', 'Group', 'Combination']]
        group_df_sorted = group_df_sorted[cols]
                
        # Display the group DataFrame
        display(group_df)
        print("\n")

    
    
display_grouped_tables(final_trend_df)
     

