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

# Attach observers to all widgets
for widget in widget_triggers_volumes:
    widget.observe(calculate_average_volumes_highway, names='value')
for widget in widget_triggers_speed:
    widget.observe(calculate_average_speeds_highway, names='value')
    
    
################################ Travel Time Metrics Table #####################################
def get_grouped_highway_results():
    volume_results = calculate_average_volumes_highway(AnnualFactor)
    speed_results = calculate_average_speeds_highway(AnnualFactor)


    if volume_results and speed_results:
        # Convert to DataFrames
        df_volume = pd.DataFrame(volume_results)
        df_speed = pd.DataFrame(speed_results)

        # Merge all into one combined DataFrame
        df_combined = pd.merge(df_volume, df_speed, on="Combination", how="outer", suffixes=("_Volume", "_Speed"))

        # Split 'Combination' into components
        df_combined[['Period', 'Vehicle', 'Year']] = df_combined['Combination'].str.split('_', expand=True)

        # Clean 'Year' column (remove 'Year' text and convert to integer)
        df_combined['Year'] = df_combined['Year'].apply(lambda x: int(x.replace('Year', '')) if isinstance(x, str) else x)

        # Create a new column that holds only the year (optional, since 'Year' already does this)
        df_combined['Combination_YearOnly'] = df_combined['Year']


        # Define group for sorting (if needed later)
        df_combined['Group'] = df_combined['Period'].astype(str) + "_" + df_combined['Vehicle'].astype(str)

        # Final clean-up: keep only selected columns
        keep_columns = ['Combination',
            'Year', 'Group',
            'Avg_Vol_NoBuild', 'Avg_Vol_Build',
            'Avg_Speed_NoBuild', 'Avg_Speed_Build'
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


variable_names = ['Avg_Vol_NoBuild', 'Avg_Vol_Build', 'Avg_Speed_NoBuild', 'Avg_Speed_Build']

    
    
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

        # Create new column 'Combination' combining Group and Year
        group_result['Combination'] = group_result['Group'] + '_Year' + group_result['Year'].astype(str)

        all_group_trends.append(group_result)

    # Concatenate all groups
    final_df = pd.concat(all_group_trends, ignore_index=True)

    return final_df


final_trend_df = generate_trends_from_dataframe(df_combined, variable_names)
    
############################################################ Person Trips ############################################################

def calculate_person_trips_highway(final_trend_df):
    ProjType = projectinfo_widgets.subcategory_dropdown.value
    AVOHovNB = projectinfo_widgets.AVOHovNB_widget.value
    AVOHovB = projectinfo_widgets.AVOHovB_widget.value
    AVOPeakNB = projectinfo_widgets.AVO_traffic_P_no_build_widget.value
    AVOPeakB = projectinfo_widgets.AVO_traffic_P_build_widget.value
    AVONonNB = projectinfo_widgets.AVO_traffic_NP_no_build_widget.value
    AVONonB = projectinfo_widgets.AVO_traffic_NP_build_widget.value

    person_trip_results = []

    for _, row in final_trend_df.iterrows():
        combo = row['Combination']
        vol_nobuild = row.get('Avg_Vol_NoBuild', 0)
        vol_build = row.get('Avg_Vol_Build', 0)

        period, vehicle, year = combo.split('_')

        avo_nobuild = avo_build = 0

        if vehicle == 'HOV':
            avo_nobuild = AVOHovNB
            avo_build = AVOHovB
        elif vehicle in ['NonHOV', 'Ramp', 'Arterial']:
            if period == 'Peak':
                avo_nobuild = AVOPeakNB
                avo_build = AVOPeakB
            else:
                avo_nobuild = AVONonNB
                avo_build = AVONonB
        elif vehicle == 'Weaving':
            hov_condition = ProjType in ["HOV Connector", "HOV Drop Ramp"]
            if period == 'Peak':
                avo_nobuild = AVOHovNB if hov_condition else AVOPeakNB
                avo_build = AVOHovB if hov_condition else AVOPeakB
            else:
                avo_nobuild = AVOHovNB if hov_condition else AVONonNB
                avo_build = AVOHovB if hov_condition else AVONonB
        elif vehicle == 'Truck':
            avo_nobuild = 1
            avo_build = 1

        person_trips_nobuild = vol_nobuild * avo_nobuild if vol_nobuild else 0
        person_trips_build = vol_build * avo_build if vol_build else 0

        row_result = row.to_dict()
        row_result.update({
            'AnnualPersonTrips_NoBuild': person_trips_nobuild,
            'AnnualPersonTrips_Build': person_trips_build
        })

        person_trip_results.append(row_result)

    return pd.DataFrame(person_trip_results)


annual_person_trips = calculate_person_trips_highway(final_trend_df)

############################################################ Average Travel Time ############################################################

def calculate_average_travel_time(annual_person_trips):
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

    for _, row in annual_person_trips.iterrows():
        combo = row['Combination']
        speed_nobuild = row.get('Avg_Speed_NoBuild', 0)
        speed_build = row.get('Avg_Speed_Build', 0)

        period, vehicle, year = combo.split('_')

        travel_time_nobuild = "#N/A"
        travel_time_build = "#N/A"

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

        # Create a copy of the row as a dictionary
        row_result = row.to_dict()

        # Update with new travel time results
        row_result.update({
            'Avg_TravelTime_NoBuild': travel_time_nobuild,
            'Avg_TravelTime_Build': travel_time_build
        })

        # Append the updated row to the results list
        average_travel_time_results.append(row_result)

    # Convert the list of dicts into a DataFrame and return it
    return pd.DataFrame(average_travel_time_results)


# Call the function
average_traveltime_and_annual_persontrips = calculate_average_travel_time(annual_person_trips)

############################################################ Travel Time Benefits #############################################################################



    
    
    
    
# ################################ Widget Observers for Average Volume, Average Trips, Person Trips and Average Travel Time #####################################

# List of widgets to observe for both volume and speed (combining the existing ones)   
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
    


for widget in widget_triggers_persontrips:
    widget.observe(calculate_person_trips_highway, names='value')
for widget in widget_triggers_avgtraveltime:
    widget.observe(calculate_average_travel_time, names='value')
    







    

        
def traveltime_benefit():    
    def safe_float(val):
        try:
            return float(val)
        except (ValueError, TypeError):
            return 0
        
                
    # Fetch required values from widgets
    ProjType = projectinfo_widgets.subcategory_dropdown.value
    PerIndHOV = projectinfo_widgets.percent_induced_trip_widget.value
    PNT1Ind = modelinputs_widgets.PNT1Ind_widget.value
    PNT20Ind = modelinputs_widgets.PNT20Ind_widget.value
    PTT1Ind = modelinputs_widgets.PTT1Ind_widget.value
    PTT20Ind = modelinputs_widgets.PTT20Ind_widget.value
    NNT1Ind = modelinputs_widgets.NNT1Ind_widget.value
    NNT20Ind = modelinputs_widgets.NNT20Ind_widget.value
    NTT1Ind = modelinputs_widgets.NTT1Ind_widget.value
    NTT20Ind = modelinputs_widgets.NTT20Ind_widget.value
    TMSLookup = params.TMSLookup
    TMSAdj = params.tms_adj
    UserAdjInputs = params.UserAdjInputs
    Induced = params.Induced
    RADataAvail = modelinputs_widgets.RADataAvail_widget.value
    
    # Initialize existing_benefits for the sum for Arterial Ramp
    NonHOVexistingPeakTTBenefit = 0  # NonHOV Peak
    WeavingexistingPeakTTBenefit = 0  # Weaving Peak
    TruckexistingPeakTTBenefit = 0  # Truck Peak
    NonHOVinducedPeakTTBenefit = 0  # NonHOV Peak
    WeavinginducedPeakTTBenefit = 0  # Weaving Peak
    TruckinducedPeakTTBenefit = 0  # Truck Peak
    
    
    traveltime_benefit_results = []

    for _, row in average_traveltime_and_annual_persontrips.iterrows():
        row_result = row.to_dict()
        
        combo = row['Combination']
        avg_tt_nobuild = safe_float(row.get('Avg_TravelTime_NoBuild', 0))
        avg_tt_build = safe_float(row.get('Avg_TravelTime_Build', 0))
        annual_trips_nobuild = safe_float(row.get('AnnualPersonTrips_NoBuild', 0))
        annual_trips_build = safe_float(row.get('AnnualPersonTrips_Build', 0))

        period, vehicle, year = combo.split('_')

        travel_time_benefit_existing = 0
        travel_time_benefit_induced = 0

        if vehicle == 'HOV' and period == 'Peak':
            if ProjType in ['Truck Only Lane', 'Bypass', 'HOV-2 to HOV-3 Conv', 'HOT Lane Conversion', 'On-Ramp Widening', 'Ramp Metering', 'Ramp Metering Signal Coord', 'Incident Management', 'Traveler Information']:
                travel_time_benefit_existing = (
                    annual_trips_nobuild * avg_tt_nobuild - annual_trips_build * avg_tt_build
                )
            else:
                travel_time_benefit_existing = (
                    (avg_tt_nobuild - avg_tt_build) * min(annual_trips_nobuild, annual_trips_build)
                )

            if (
                annual_trips_build > annual_trips_nobuild
                and ProjType not in ['Truck Only Lane', 'Bypass', 'HOV-2 to HOV-3 Conv', 'HOT Lane Conversion', 'On-Ramp Widening', 'Ramp Metering', 'Ramp Metering Signal Coord', 'Incident Management', 'Traveler Information']
                and Induced == "Y"
            ):
                travel_time_benefit_induced = (
                    (avg_tt_nobuild - avg_tt_build)
                    * (annual_trips_build - annual_trips_nobuild)
                    * 0.5
                )
            else:
                travel_time_benefit_induced = 0

        elif vehicle == 'NonHOV' and period == 'Peak':
            if ProjType in ['Truck Only Lane', 'Bypass', 'HOV-2 to HOV-3 Conv', 'HOT Lane Conversion', 'On-Ramp Widening', 'Ramp Metering', 'Ramp Metering Signal Coord', 'Incident Management', 'Traveler Information']:
                base_benefit_existing = (
                    annual_trips_nobuild * avg_tt_nobuild - annual_trips_build * avg_tt_build
                )
            else:
                base_benefit_existing = (
                    (avg_tt_nobuild - avg_tt_build) * min(annual_trips_nobuild, annual_trips_build)
                )

            # Apply multiplier only if UserAdjInputs is the string "True"
            multiplier = TMSAdj.get(TMSLookup, {}).get('Em', 0) if UserAdjInputs == "True" else 1
            travel_time_benefit_existing = base_benefit_existing * multiplier

            # Assign value to (NonHOV Peak)
            NonHOVexistingPeakTTBenefit = travel_time_benefit_existing

            if (
                annual_trips_build > annual_trips_nobuild
                and ProjType not in ['Truck Only Lane', 'Bypass', 'HOV-2 to HOV-3 Conv', 'HOT Lane Conversion', 'On-Ramp Widening', 'Ramp Metering', 'Ramp Metering Signal Coord', 'Incident Management', 'Traveler Information']
                and Induced == "Y"
            ):
                base_benefit_induced = (
                    (avg_tt_nobuild - avg_tt_build)
                    * (annual_trips_build - annual_trips_nobuild)
                    * 0.5
                )

            elif ProjType in ['HOV-2 to HOV-3 Conv', 'HOT Lane Conversion']:

                year = combo.split('_')[-1]  # This will give 'Year1' or 'Year20'
                year_number = year.replace('Year', '')  # Extract '1' or '20' by removing 'Year'

                # Find the Peak_HOV row that matches the current year from the data
                peak_hov_row = next(
                    (row for row in average_travel_time if row['Combination'] == f'Peak_HOV_{year}'),
                    None
                )
                avg_tt_build_hov = peak_hov_row.get('Avg_TravelTime_Build', 0)

                # Calculate the induced benefit for Year 1 (base_benefit_induced_Year1)
                if year_number == '1':
                    base_benefit_induced = (
                        (avg_tt_nobuild - ((1 - PerIndHOV) * avg_tt_build + PerIndHOV * avg_tt_build_hov))
                        * PNT1Ind  # Directly using PNT1Ind for Year 1
                        * (-0.5 if Induced == "Y" else -1)
                    )
                    # Store the Year 1 value for later use in L55
                    base_benefit_induced_Year1 = base_benefit_induced
                # Calculate the induced benefit for Year 20 (base_benefit_induced_Year20)
                elif year_number == '20':
                    base_benefit_induced = (
                        (avg_tt_nobuild - ((1 - PerIndHOV) * avg_tt_build + PerIndHOV * avg_tt_build_hov))
                        * PNT20Ind  # Directly using PNT20Ind for Year 20
                        * (-0.5 if Induced == "Y" else -1)
                    )
                    # Store the Year 20 value for later use in L56
                    base_benefit_induced_Year20 = base_benefit_induced
                    
                else:  # For years 2 to 19, perform linear interpolation between Year 1 and Year 20
                    # Known values for years 1 and 20
                    years_known = np.array([1, 20])
                    benefits_known = np.array([base_benefit_induced_Year1, base_benefit_induced_Year20])

                    # Point at which we want to calculate the trend (for example, year_number is B58)
                    year_to_predict = int(year_number)

                    # Calculate the linear trend using NumPy's polyfit (linear regression)
                    slope, intercept = np.polyfit(years_known, benefits_known, 1)

                    # Now, calculate the interpolated value for the given year (B58)
                    interpolated_value = np.polyval([slope, intercept], year_to_predict)

                    # Final induced benefit using the interpolated value
                    base_benefit_induced = interpolated_value * (-0.5 if Induced == "Y" else -1)

                # Apply the multiplier if UserAdjInputs is True
                multiplier = TMSAdj.get(TMSLookup, {}).get('Em', 0) if UserAdjInputs == "True" else 1
                travel_time_benefit_induced = base_benefit_induced * multiplier

                # Assign value to (NonHOV Peak) for induced travel time benefit
                NonHOVinducedPeakTTBenefit = travel_time_benefit_induced


        elif vehicle == 'Weaving' and period == 'Peak':
            # Check if the project type is one of the special types
            if ProjType in ['Truck Only Lane', 'Bypass', 'HOV-2 to HOV-3 Conv', 'HOT Lane Conversion', 'On-Ramp Widening', 'Ramp Metering', 'Ramp Metering Signal Coord', 'Incident Management', 'Traveler Information']:
                # Calculate the base benefit for existing conditions
                base_benefit_existing = (
                    annual_trips_nobuild * avg_tt_nobuild - annual_trips_build * avg_tt_build
                )
            else:
                # Calculate base benefit when project type isn't one of the special cases
                base_benefit_existing = (
                    (avg_tt_nobuild - avg_tt_build) * min(annual_trips_nobuild, annual_trips_build)
                )

            # Apply multiplier only if UserAdjInputs is the string "True"
            multiplier = TMSAdj.get(TMSLookup, {}).get('Em', 0) if UserAdjInputs == "True" else 1
            travel_time_benefit_existing = base_benefit_existing * multiplier

            # Assign value to (Weaving)
            WeavingexistingPeakTTBenefit = travel_time_benefit_existing

            # If trips are greater in the build scenario and the project is not special, apply induced benefit
            if (
                annual_trips_build > annual_trips_nobuild
                and ProjType not in ['Truck Only Lane', 'Bypass', 'HOV-2 to HOV-3 Conv', 'HOT Lane Conversion', 'On-Ramp Widening', 'Ramp Metering', 'Ramp Metering Signal Coord', 'Incident Management', 'Traveler Information']
                and Induced == "Y"
            ):
                base_benefit_induced = (
                    (avg_tt_nobuild - avg_tt_build)
                    * (annual_trips_build - annual_trips_nobuild)
                    * 0.5
                )
            else:
                # If not induced or conditions are not met, set induced benefit to 0
                base_benefit_induced = 0

            # Apply multiplier only if UserAdjInputs is the string "True"
            travel_time_benefit_induced = base_benefit_induced * multiplier

            # Assign value to (Weaving)
            WeavinginducedPeakTTBenefit = travel_time_benefit_induced

        elif vehicle == 'Truck' and period == 'Peak':
            # Check if the project type is one of the special types
            if ProjType in ['Truck Only Lane', 'Bypass', 'HOV-2 to HOV-3 Conv', 'HOT Lane Conversion', 'On-Ramp Widening', 'Ramp Metering', 'Ramp Metering Signal Coord', 'Incident Management', 'Traveler Information']:
                # Calculate the base benefit for existing conditions
                base_benefit_existing = (
                    annual_trips_nobuild * avg_tt_nobuild - annual_trips_build * avg_tt_build
                )
            else:
                # Calculate base benefit when project type isn't one of the special cases
                base_benefit_existing = (
                    (avg_tt_nobuild - avg_tt_build) * min(annual_trips_nobuild, annual_trips_build)
                )

            # Apply multiplier only if UserAdjInputs is the string "True"
            multiplier = TMSAdj.get(TMSLookup, {}).get('Em', 0) if UserAdjInputs == "True" else 1
            travel_time_benefit_existing = base_benefit_existing * multiplier

            # Assign value to (NonHOV Peak)
            TruckexistingPeakTTBenefit = travel_time_benefit_existing

            if (
                annual_trips_build > annual_trips_nobuild
                and ProjType not in ['Truck Only Lane', 'Bypass', 'HOV-2 to HOV-3 Conv', 'HOT Lane Conversion', 'On-Ramp Widening', 'Ramp Metering', 'Ramp Metering Signal Coord', 'Incident Management', 'Traveler Information']
                and Induced == "Y"
            ):
                base_benefit_induced = (
                    (avg_tt_nobuild - avg_tt_build)
                    * (annual_trips_build - annual_trips_nobuild)
                    * 0.5
                )

            elif ProjType in ['HOV-2 to HOV-3 Conv', 'HOT Lane Conversion']:

                year = combo.split('_')[-1]  # This will give 'Year1' or 'Year20'
                year_number = year.replace('Year', '')  # Extract '1' or '20' by removing 'Year'

                # Find the Peak_HOV row that matches the current year from the data
                peak_hov_row = next(
                    (row for row in average_travel_time if row['Combination'] == f'Peak_HOV_{year}'),
                    None
                )
                avg_tt_build_hov = peak_hov_row.get('Avg_TravelTime_Build', 0)

                # Calculate the induced benefit for Year 1 (base_benefit_induced_Year1)
                if year_number == '1':
                    base_benefit_induced = (
                        (avg_tt_nobuild - ((1 - PerIndHOV) * avg_tt_build + PerIndHOV * avg_tt_build_hov))
                        * PTT1Ind 
                        * (-0.5 if Induced == "Y" else -1)
                    )
                    # Store the Year 1 value for later use in L55
                    base_benefit_induced_Year1 = base_benefit_induced
                # Calculate the induced benefit for Year 20 (base_benefit_induced_Year20)
                elif year_number == '20':
                    base_benefit_induced = (
                        (avg_tt_nobuild - ((1 - PerIndHOV) * avg_tt_build + PerIndHOV * avg_tt_build_hov))
                        * PTT20Ind 
                        * (-0.5 if Induced == "Y" else -1)
                    )
                    # Store the Year 20 value for later use in L56
                    base_benefit_induced_Year20 = base_benefit_induced
                    
                else:  # For years 2 to 19, perform linear interpolation between Year 1 and Year 20
                    # Known values for years 1 and 20
                    years_known = np.array([1, 20])
                    benefits_known = np.array([base_benefit_induced_Year1, base_benefit_induced_Year20])

                    # Point at which we want to calculate the trend (for example, year_number is B58)
                    year_to_predict = int(year_number)

                    # Calculate the linear trend using NumPy's polyfit (linear regression)
                    slope, intercept = np.polyfit(years_known, benefits_known, 1)

                    # Now, calculate the interpolated value for the given year (B58)
                    interpolated_value = np.polyval([slope, intercept], year_to_predict)

                    # Final induced benefit using the interpolated value
                    base_benefit_induced = interpolated_value * (-0.5 if Induced == "Y" else -1)

                # Apply the multiplier if UserAdjInputs is True
                multiplier = TMSAdj.get(TMSLookup, {}).get('Em', 0) if UserAdjInputs == "True" else 1
                travel_time_benefit_induced = base_benefit_induced * multiplier

                # Assign value to (NonHOV Peak) for induced travel time benefit
                TruckinducedPeakTTBenefit = travel_time_benefit_induced

            

        elif vehicle == 'Ramp' and period == 'Peak':
            if RADataAvail == "Y":
                travel_time_benefit_existing = (
                    (avg_tt_nobuild - avg_tt_build) * min(annual_trips_nobuild, annual_trips_build)
                )
            else:
                travel_time_benefit_existing = 0

            if (
                annual_trips_build > annual_trips_nobuild
                and RADataAvail == "Y"
                and Induced == "Y"
            ):
                travel_time_benefit_induced = (
                    (avg_tt_nobuild - avg_tt_build)
                    * (annual_trips_build - annual_trips_nobuild)
                    * 0.5
                )
            else:
                travel_time_benefit_induced = 0

        elif vehicle == 'Arterial' and period == 'Peak':
            if RADataAvail == "Y":
                travel_time_benefit_existing = (
                    (avg_tt_nobuild - avg_tt_build) * min(annual_trips_nobuild, annual_trips_build)
                )
            else:
                travel_time_benefit_existing = (NonHOVexistingPeakTTBenefit + WeavingexistingPeakTTBenefit + TruckexistingPeakTTBenefit) * TMSAdj.get(TMSLookup, {}).get('Benefit', 1)

            if (
                annual_trips_build > annual_trips_nobuild
                and RADataAvail == "Y"
                and Induced == "Y"
            ):
                travel_time_benefit_induced = (
                    (avg_tt_nobuild - avg_tt_build)
                    * (annual_trips_build - annual_trips_nobuild)
                    * 0.5
                )
            else:
                travel_time_benefit_induced = (NonHOVinducedPeakTTBenefit + WeavinginducedPeakTTBenefit + TruckinducedPeakTTBenefit) * TMSAdj.get(TMSLookup, {}).get('Benefit', 1)

        # NonPeak NonHOV
        elif vehicle == 'NonHOV' and period == 'NonPeak':
            if ProjType in ['Truck Only Lane', 'Bypass', 'HOV-2 to HOV-3 Conv', 'HOT Lane Conversion', 'On-Ramp Widening', 'Ramp Metering', 'Ramp Metering Signal Coord', 'Incident Management', 'Traveler Information']:
                travel_time_benefit_existing = (
                    annual_trips_nobuild * avg_tt_nobuild - annual_trips_build * avg_tt_build
                )
            else:
                travel_time_benefit_existing = (
                    (avg_tt_nobuild - avg_tt_build) * min(annual_trips_nobuild, annual_trips_build)
                )

            if (
                annual_trips_build > annual_trips_nobuild
                and ProjType not in ['Truck Only Lane', 'Bypass', 'HOV-2 to HOV-3 Conv', 'HOT Lane Conversion', 'On-Ramp Widening', 'Ramp Metering', 'Ramp Metering Signal Coord', 'Incident Management', 'Traveler Information']
                and Induced == "Y"
            ):
                travel_time_benefit_induced = (
                    (avg_tt_nobuild - avg_tt_build)
                    * (annual_trips_build - annual_trips_nobuild)
                    * 0.5
                )

            elif ProjType in ['HOV-2 to HOV-3 Conv', 'HOT Lane Conversion']:
                # Extract the year from the 'Combination' value (e.g., 'NonPeak_HOV_Year1' or 'NonPeak_HOV_Year20')
                year = combo.split('_')[-1]
                year_number = year.replace('Year', '')  # Extract '1' or '20' by removing 'Year'

                # Check if the year is 1, 20, or in between
                if year_number == '1':  
                    travel_time_benefit_induced = (
                        (avg_tt_nobuild - avg_tt_build) * NNT1Ind * (-0.5 if Induced == "Y" else -1)
                    )
                    # Store the Year 1 value for later interpolation
                    base_benefit_induced_Year1 = travel_time_benefit_induced

                elif year_number == '20':  # For Year 20, use NNT20Ind
                    travel_time_benefit_induced = (
                        (avg_tt_nobuild - avg_tt_build) * NNT20Ind * (-0.5 if Induced == "Y" else -1)
                    )
                    # Store the Year 20 value for later interpolation
                    base_benefit_induced_Year20 = travel_time_benefit_induced

                else:  # For years 2 to 19, perform linear interpolation between Year 1 and Year 20
                    # Known values for years 1 and 20
                    years_known = np.array([1, 20])
                    benefits_known = np.array([base_benefit_induced_Year1, base_benefit_induced_Year20])

                    # Point at which we want to calculate the trend (for example, year_number is B58)
                    year_to_predict = int(year_number)

                    # Calculate the linear trend using NumPy's polyfit (linear regression)
                    slope, intercept = np.polyfit(years_known, benefits_known, 1)

                    # Now, calculate the interpolated value for the given year
                    interpolated_value = np.polyval([slope, intercept], year_to_predict)

                    # Set the interpolated value as the induced benefit for the current year
                    travel_time_benefit_induced = interpolated_value

        # NonPeak Weaving
        elif vehicle == 'Weaving' and period == 'NonPeak':
            # Check if the project type is one of the special types
            if ProjType in ['Truck Only Lane', 'Bypass', 'HOV-2 to HOV-3 Conv', 'HOT Lane Conversion', 'On-Ramp Widening', 'Ramp Metering', 'Ramp Metering Signal Coord', 'Incident Management', 'Traveler Information']:
                # Calculate the base benefit for existing conditions
                travel_time_benefit_existing = (
                    annual_trips_nobuild * avg_tt_nobuild - annual_trips_build * avg_tt_build
                )
            else:
                # Calculate base benefit when project type isn't one of the special cases
                travel_time_benefit_existing = (
                    (avg_tt_nobuild - avg_tt_build) * min(annual_trips_nobuild, annual_trips_build)
                )

            if (
                annual_trips_build > annual_trips_nobuild
                and ProjType not in ['Truck Only Lane', 'Bypass', 'HOV-2 to HOV-3 Conv', 'HOT Lane Conversion', 'On-Ramp Widening', 'Ramp Metering', 'Ramp Metering Signal Coord', 'Incident Management', 'Traveler Information']
                and Induced == "Y"
            ):
                travel_time_benefit_induced = (
                    (avg_tt_nobuild - avg_tt_build)
                    * (annual_trips_build - annual_trips_nobuild)
                    * 0.5
                )
            else:
                # If not induced or conditions are not met, set induced benefit to 0
                travel_time_benefit_induced = 0

        # NonPeak Truck
        elif vehicle == 'Truck' and period == 'NonPeak':
            # Check if the project type is one of the special types
            if ProjType in ['Truck Only Lane', 'Bypass', 'HOV-2 to HOV-3 Conv', 'HOT Lane Conversion', 'On-Ramp Widening', 'Ramp Metering', 'Ramp Metering Signal Coord', 'Incident Management', 'Traveler Information']:
                # Calculate the base benefit for existing conditions
                travel_time_benefit_existing = (
                    annual_trips_nobuild * avg_tt_nobuild - annual_trips_build * avg_tt_build
                )
            else:
                # Calculate base benefit when project type isn't one of the special cases
                travel_time_benefit_existing = (
                    (avg_tt_nobuild - avg_tt_build) * min(annual_trips_nobuild, annual_trips_build)
                )

            if (
                annual_trips_build > annual_trips_nobuild
                and ProjType not in ['Truck Only Lane', 'Bypass', 'HOV-2 to HOV-3 Conv', 'HOT Lane Conversion', 'On-Ramp Widening', 'Ramp Metering', 'Ramp Metering Signal Coord', 'Incident Management', 'Traveler Information']
                and Induced == "Y"
            ):
                travel_time_benefit_induced = (
                    (avg_tt_nobuild - avg_tt_build)
                    * (annual_trips_build - annual_trips_nobuild)
                    * 0.5
                )

            elif ProjType in ['HOV-2 to HOV-3 Conv', 'HOT Lane Conversion']:
                # Extract the year from the 'Combination' value (e.g., 'NonPeak_HOV_Year1' or 'NonPeak_HOV_Year20')
                year = combo.split('_')[-1]
                year_number = year.replace('Year', '')  # Extract '1' or '20' by removing 'Year'

                # Calculate the induced benefit for Year 1 or Year 20
                if year_number == '1':  
                    travel_time_benefit_induced = (
                        (avg_tt_nobuild - avg_tt_build) * NTT1Ind * (-0.5 if Induced == "Y" else -1)
                    )
                    # Store the Year 1 value for later interpolation
                    base_benefit_induced_Year1 = travel_time_benefit_induced

                elif year_number == '20':  
                    travel_time_benefit_induced = (
                        (avg_tt_nobuild - avg_tt_build) * NTT20Ind * (-0.5 if Induced == "Y" else -1)
                    )
                    # Store the Year 20 value for later interpolation
                    base_benefit_induced_Year20 = travel_time_benefit_induced

                else:  # For years 2 to 19, perform linear interpolation between Year 1 and Year 20
                    # Known values for years 1 and 20
                    years_known = np.array([1, 20])
                    benefits_known = np.array([base_benefit_induced_Year1, base_benefit_induced_Year20])

                    # Point at which we want to calculate the trend (for example, year_number is B58)
                    year_to_predict = int(year_number)

                    # Calculate the linear trend using NumPy's polyfit (linear regression)
                    slope, intercept = np.polyfit(years_known, benefits_known, 1)

                    # Now, calculate the interpolated value for the given year
                    interpolated_value = np.polyval([slope, intercept], year_to_predict)

                    # Set the interpolated value as the induced benefit for the current year
                    travel_time_benefit_induced = interpolated_value


        # NonPeak Ramp
        elif vehicle == 'Ramp' and period == 'NonPeak':
            if RADataAvail == "Y":
                travel_time_benefit_existing = (
                    (avg_tt_nobuild - avg_tt_build) * min(annual_trips_nobuild, annual_trips_build)
                )
            else:
                travel_time_benefit_existing = 0

            if (
                annual_trips_build > annual_trips_nobuild
                and RADataAvail == "Y"
                and Induced == "Y"
            ):
                travel_time_benefit_induced = (
                    (avg_tt_nobuild - avg_tt_build)
                    * (annual_trips_build - annual_trips_nobuild)
                    * 0.5
                )
            else:
                travel_time_benefit_induced = 0

        # NonPeak Arterial
        elif vehicle == 'Arterial' and period == 'NonPeak':
            if RADataAvail == "Y":
                travel_time_benefit_existing = (
                    (avg_tt_nobuild - avg_tt_build) * min(annual_trips_nobuild, annual_trips_build)
                )
            else:
                travel_time_benefit_existing = (NonHOVexistingPeakTTBenefit + WeavingexistingPeakTTBenefit + TruckexistingPeakTTBenefit)* TMSAdj.get(TMSLookup, {}).get('Benefit', 1)

            if (
                annual_trips_build > annual_trips_nobuild
                and RADataAvail == "Y"
                and Induced == "Y"
            ):
                travel_time_benefit_induced = (
                    (avg_tt_nobuild - avg_tt_build)
                    * (annual_trips_build - annual_trips_nobuild)
                    * 0.5
                )                   
            else:
                travel_time_benefit_induced = (NonHOVinducedPeakTTBenefit + WeavinginducedPeakTTBenefit + TruckinducedPeakTTBenefit)* TMSAdj.get(TMSLookup, {}).get('Benefit', 1)


            # Add the calculated values to the results
        row_result.update({
            'ExistingBenefit': travel_time_benefit_existing,
            'InducedBenefit': travel_time_benefit_induced,
        })

        # Append updated row
        traveltime_benefit_results.append(row_result)

    return pd.DataFrame(traveltime_benefit_results)


traveltime_benefit = traveltime_benefit()






def get_grouped_travel_time_benefit_tables(df):
    # Define custom group order
    peak_order = ["Peak_HOV", "Peak_NonHOV", "Peak_Weaving", "Peak_Truck", "Peak_Ramp", "Peak_Arterial"]
    nonpeak_order = ["NonPeak_NonHOV", "NonPeak_Weaving", "NonPeak_Arterial"]
    custom_order = peak_order + nonpeak_order

    # Add temporary sort key for group order
    df['GroupOrder'] = df['Group'].apply(lambda x: custom_order.index(x) if x in custom_order else len(custom_order))

    # Add custom sorting for 'Year', where 1 and 20 should come first, then others in ascending order
    def custom_year_sort(year):
        if year == 1:
            return -1  # Make year 1 come first
        elif year == 20:
            return 0  # Make year 20 come second
        else:
            return year  # Keep the rest in ascending order

    # Sort by 'GroupOrder' first, then by custom year sorting
    df['YearSortOrder'] = df['Year'].apply(custom_year_sort)
    
    # Sort by the 'GroupOrder' and 'YearSortOrder', then drop helper columns
    df_sorted = df.sort_values(by=['GroupOrder', 'YearSortOrder']).drop(columns=['GroupOrder', 'Combination', 'YearSortOrder'])

    # Group by 'Group' and reset index for each group
    grouped_tables = {
        group: group_df.reset_index(drop=True)
        for group, group_df in df_sorted.groupby('Group')
    }

    # Display each group (you can adjust this to how you want to view it)
    for group, group_df in grouped_tables.items():
        print(f"Group: {group}")
        display(group_df)  # This will render it in Jupyter or IPython environments

    return grouped_tables




grouped_tables = get_grouped_travel_time_benefit_tables(traveltime_benefit)


    

     

