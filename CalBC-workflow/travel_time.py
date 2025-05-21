import pandas as pd
import numpy as np
import ipywidgets as widgets
from ipywidgets import interact
from IPython.display import display, clear_output, HTML


pd.set_option('display.max_columns', None)  
pd.set_option('display.width', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.float_format', '{:.2f}'.format)




from parameters import parameters
params = parameters()

import projectinfo_widgets
import modelinputs_widgets

common_layout = widgets.Layout(
    width='450px', 
    background_color='#CCFFCC',  # Background color for all widgets
    padding='5px',
    border='2px solid gray'  # Border color and thickness
)


# Getting values used in all the functions 
AnnualFactor = params.AnnualFactor
variable_names = ['Avg_Vol_NoBuild', 'Avg_Vol_Build', 'Avg_Speed_NoBuild', 'Avg_Speed_Build']


total_tt_benefit_widget = widgets.FloatText(
    value=0,
    description='Total Travel Time Benefit ($):',
    layout = common_layout,
    style={'description_width': 'initial'},
    disabled=False
)

# Display everything together
display(total_tt_benefit_widget)


        
def calculate_combined_average(AnnualFactor):    
    global df_combined 
    
    # Define combinations
    periods = ['Peak', 'NonPeak']
    vehicle_types = ['HOV', 'NonHOV', 'Weaving', 'Truck', 'Ramp', 'Arterial']
    years = ['Year1', 'Year20']
    project_states = ['NoBuild', 'Build']

    # Build a dictionary of widget values for volume (from your existing code)
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

    # Build a dictionary of widget values for speed (same as before)
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

    # Loop through periods, vehicle types, and years
    for period in periods:
        for vehicle in vehicle_types:
            if period == 'NonPeak' and vehicle in ['Ramp', 'HOV', 'Arterial']:
                continue
            for year in years:
                avg_vol_nobuild = None
                avg_vol_build = None
                avg_speed_nobuild = None
                avg_speed_build = None

                for state in project_states:
                    year_part = year.replace("Year", "")
                    state_part = 'NB' if state == 'NoBuild' else 'B'

                    # For volume calculation
                    volume_key = f"{period[:1]}{vehicle[:1]}V{year_part}{state_part}"
                    vol_value = volume_dict.get(volume_key, 0) or 0
                    avg_vol = vol_value * AnnualFactor

                    # For speed calculation
                    speed_key = f"{period[:1]}{vehicle[:1]}S{year_part}{state_part}"
                    speed_value = speed_dict.get(speed_key, 0) or 0
                    avg_speed = round(speed_value, 1)

                    if state == 'NoBuild':
                        avg_vol_nobuild = avg_vol
                        avg_speed_nobuild = avg_speed
                    else:
                        avg_vol_build = avg_vol
                        avg_speed_build = avg_speed

                # Append combined result to all_combinations
                all_combinations.append({
                    'Combination': f"{period}_{vehicle}_{year}",
                    'Avg_Vol_NoBuild': avg_vol_nobuild if avg_vol_nobuild is not None else 0,
                    'Avg_Vol_Build': avg_vol_build if avg_vol_build is not None else 0,
                    'Avg_Speed_NoBuild': avg_speed_nobuild if avg_speed_nobuild is not None else 0,
                    'Avg_Speed_Build': avg_speed_build if avg_speed_build is not None else 0
                })

    # Create a DataFrame from the combined results
    df_combined = pd.DataFrame(all_combinations)

    # Extract 'Period', 'Vehicle', 'Year' from 'Combination'
    df_combined[['Period', 'Vehicle', 'Year']] = df_combined['Combination'].str.split('_', expand=True)
    
    
    # Create a 'Group' column
    df_combined['Group'] = df_combined['Period'] + '_' + df_combined['Vehicle']
    
    # Convert 'Year' from 'Year1'/'Year20' to integer (1/20)
    df_combined['Year'] = df_combined['Year'].str.replace('Year', '').astype(int)
    
    # Drop columns we no longer need
    df_combined.drop(columns=['Period', 'Vehicle'], inplace=True)

    return df_combined


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


def calculate_person_trips_highway(final_trend_df):
    ProjType = projectinfo_widgets.subcategory_dropdown.value
    AVOHovNB = projectinfo_widgets.AVOHovNB_widget.value
    AVOHovB = projectinfo_widgets.AVOHovB_widget.value
    AVOPeakNB = projectinfo_widgets.AVO_traffic_P_no_build_widget.value
    AVOPeakB = projectinfo_widgets.AVO_traffic_P_build_widget.value
    AVONonNB = projectinfo_widgets.AVO_traffic_NP_no_build_widget.value
    AVONonB = projectinfo_widgets.AVO_traffic_NP_build_widget.value

    # Initialize empty columns
    final_trend_df['AnnualPersonTrips_NoBuild'] = 0
    final_trend_df['AnnualPersonTrips_Build'] = 0

    for idx, row in final_trend_df.iterrows():
        group = row['Group']
        period, vehicle = group.split('_')
        vol_nobuild = row.get('Avg_Vol_NoBuild', 0)
        vol_build = row.get('Avg_Vol_Build', 0)

        # Default AVOs
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
            else:
                avo_nobuild = AVOHovNB if hov_condition else AVONonNB
                avo_build = AVOHovB if hov_condition else AVONonB

        elif vehicle == 'Truck':
            avo_nobuild = avo_build = 1

        else:
            print(f"Unknown vehicle type: {vehicle}")

        # Calculate person trips
        person_trips_nobuild = vol_nobuild * avo_nobuild if vol_nobuild else 0
        person_trips_build = vol_build * avo_build if vol_build else 0

        # Store in the DataFrame
        final_trend_df.at[idx, 'AnnualPersonTrips_NoBuild'] = person_trips_nobuild
        final_trend_df.at[idx, 'AnnualPersonTrips_Build'] = person_trips_build

    return final_trend_df


def calculate_average_travel_time(final_trend_df):
    # Widget values
    ProjType = projectinfo_widgets.subcategory_dropdown.value
    ImpactedNB = projectinfo_widgets.impacted_length_no_build_widget.value
    ImpactedB = projectinfo_widgets.impacted_length_build_widget.value
    SegmentR = modelinputs_widgets.SegmentR_widget.value
    SegmentA = modelinputs_widgets.SegmentA_widget.value
    GateTime1 = projectinfo_widgets.GateTime1_widget.value

    def safe_divide(numerator, denominator):
        return "#DIV/0!" if denominator == 0 else numerator / denominator

    # Initialize empty columns
    final_trend_df['Avg_TravelTime_NoBuild'] = None
    final_trend_df['Avg_TravelTime_Build'] = None

    # Iterate and populate
    for idx, row in final_trend_df.iterrows():
        group = row['Group']
        year = row['Year']
        period, vehicle = group.split('_')
        speed_nobuild = row.get('Avg_Speed_NoBuild', 0)
        speed_build = row.get('Avg_Speed_Build', 0)

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

        # Assign directly into the DataFrame
        final_trend_df.at[idx, 'Avg_TravelTime_NoBuild'] = travel_time_nobuild
        final_trend_df.at[idx, 'Avg_TravelTime_Build'] = travel_time_build

    return final_trend_df


def traveltime_benefit(final_trend_df):    
    def safe_float(val):
        try:
            return float(val)
        except (ValueError, TypeError):
            return 0.0
        
    # Fetch required values from widgets
    ProjType = projectinfo_widgets.subcategory_dropdown.value
    PerIndHOV = projectinfo_widgets.percent_induced_trip_widget.value
    PNT1Ind = modelinputs_widgets.PNT1Ind_widget.value
    PNT20Ind = modelinputs_widgets.PNT20Ind_widget.value
    NNT1Ind = modelinputs_widgets.NNT1Ind_widget.value
    NNT20Ind = modelinputs_widgets.NNT20Ind_widget.value
    PTT1Ind = modelinputs_widgets.PTT1Ind_widget.value
    PTT20Ind = modelinputs_widgets.PTT20Ind_widget.value
    NTT1Ind = modelinputs_widgets.NTT1Ind_widget.value
    NTT20Ind = modelinputs_widgets.NTT20Ind_widget.value
    RADataAvail = modelinputs_widgets.RADataAvail_widget.value
    TMSLookup = params.TMSLookup
    TMSAdj = params.tms_adj
    UserAdjInputs = params.UserAdjInputs
    Induced = params.Induced
    
    NonHOVinducedPeakTTBenefit = 0
    WeavinginducedPeakTTBenefit = 0
    TruckinducedPeakTTBenefit = 0
    NonHOVexistingPeakTTBenefit = 0
    WeavingexistingPeakTTBenefit = 0
    TruckexistingPeakTTBenefit = 0 
    
    
    # Iterate through rows of final_trend_df and calculate the benefits
    for idx, row in final_trend_df.iterrows():
        combo = row['Group']
        period, vehicle = combo.split('_')  # Split to get period and vehicle
        year = row['Year']  # Year is directly from the 'Year' column
        
        avg_tt_nobuild = safe_float(row.get('Avg_TravelTime_NoBuild', 0))
        avg_tt_build = safe_float(row.get('Avg_TravelTime_Build', 0))
        annual_trips_nobuild = safe_float(row.get('AnnualPersonTrips_NoBuild', 0))
        annual_trips_build = safe_float(row.get('AnnualPersonTrips_Build', 0))

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

        if vehicle == 'NonHOV' and period == 'Peak':
            if ProjType in ['Truck Only Lane', 'Bypass', 'HOV-2 to HOV-3 Conv', 'HOT Lane Conversion', 'On-Ramp Widening', 'Ramp Metering', 'Ramp Metering Signal Coord', 'Incident Management', 'Traveler Information']:
                base_benefit_existing = (
                    annual_trips_nobuild * avg_tt_nobuild - annual_trips_build * avg_tt_build
                )
            else:
                base_benefit_existing = (
                    (avg_tt_nobuild - avg_tt_build) * min(annual_trips_nobuild, annual_trips_build)
                )

            # Apply multiplier if UserAdjInputs is the string "True"
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

                # Find the Peak_HOV row that matches the current year from the data
                peak_hov_row = next(
                    (row for row in final_trend_df if row['Group'] == 'Peak_HOV'),
                    None
                )
                avg_tt_build_hov = peak_hov_row.get('Avg_TravelTime_Build', 0)

                # Calculate the induced benefit for Year 1 (base_benefit_induced_Year1)
                if year == 1:
                    base_benefit_induced = (
                        (avg_tt_nobuild - ((1 - PerIndHOV) * avg_tt_build + PerIndHOV * avg_tt_build_hov))
                        * PNT1Ind  # Directly using PNT1Ind for Year 1
                        * (-0.5 if Induced == "Y" else -1)
                    )
                    # Store the Year 1 value for later use
                    base_benefit_induced_Year1 = base_benefit_induced
                # Calculate the induced benefit for Year 20 (base_benefit_induced_Year20)
                elif year == 20:
                    base_benefit_induced = (
                        (avg_tt_nobuild - ((1 - PerIndHOV) * avg_tt_build + PerIndHOV * avg_tt_build_hov))
                        * PNT20Ind  # Directly using PNT20Ind for Year 20
                        * (-0.5 if Induced == "Y" else -1)
                    )
                    # Store the Year 20 value for later use
                    base_benefit_induced_Year20 = base_benefit_induced

                else:  # For years 2 to 19, perform linear interpolation between Year 1 and Year 20
                    # Known values for years 1 and 20
                    years_known = np.array([1, 20])
                    benefits_known = np.array([base_benefit_induced_Year1, base_benefit_induced_Year20])

                    # Calculate the linear trend using NumPy's polyfit (linear regression)
                    slope, intercept = np.polyfit(years_known, benefits_known, 1)

                    # Now, calculate the interpolated value for the current year
                    interpolated_value = np.polyval([slope, intercept], year)

                    # Final induced benefit using the interpolated value
                    base_benefit_induced = interpolated_value * (-0.5 if Induced == "Y" else -1)

                # Apply the multiplier if UserAdjInputs is True
                multiplier = TMSAdj.get(TMSLookup, {}).get('Em', 0) if UserAdjInputs == "True" else 1
                travel_time_benefit_induced = base_benefit_induced * multiplier

                # Assign value to (NonHOV Peak) for induced travel time benefit
                NonHOVinducedPeakTTBenefit = travel_time_benefit_induced


        if vehicle == 'Weaving' and period == 'Peak':
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

        if vehicle == 'Truck' and period == 'Peak':
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

                # Find the Peak_HOV row that matches the current year from the data
                peak_hov_row = next(
                    (row for row in final_trend_df if row['Group'] == 'Peak_HOV'),
                    None
                )
                avg_tt_build_hov = peak_hov_row.get('Avg_TravelTime_Build', 0)

                # Calculate the induced benefit for Year 1 (base_benefit_induced_Year1)
                if year == 1:
                    base_benefit_induced = (
                        (avg_tt_nobuild - ((1 - PerIndHOV) * avg_tt_build + PerIndHOV * avg_tt_build_hov))
                        * PTT1Ind  # Directly using PNT1Ind for Year 1
                        * (-0.5 if Induced == "Y" else -1)
                    )
                    # Store the Year 1 value for later use
                    base_benefit_induced_Year1 = base_benefit_induced
                # Calculate the induced benefit for Year 20 (base_benefit_induced_Year20)
                elif year == 20:
                    base_benefit_induced = (
                        (avg_tt_nobuild - ((1 - PerIndHOV) * avg_tt_build + PerIndHOV * avg_tt_build_hov))
                        * PTT20Ind  # Directly using PNT20Ind for Year 20
                        * (-0.5 if Induced == "Y" else -1)
                    )
                    # Store the Year 20 value for later use
                    base_benefit_induced_Year20 = base_benefit_induced

                else:  # For years 2 to 19, perform linear interpolation between Year 1 and Year 20
                    # Known values for years 1 and 20
                    years_known = np.array([1, 20])
                    benefits_known = np.array([base_benefit_induced_Year1, base_benefit_induced_Year20])

                    # Calculate the linear trend using NumPy's polyfit (linear regression)
                    slope, intercept = np.polyfit(years_known, benefits_known, 1)

                    # Now, calculate the interpolated value for the current year
                    interpolated_value = np.polyval([slope, intercept], year)

                    # Final induced benefit using the interpolated value
                    base_benefit_induced = interpolated_value * (-0.5 if Induced == "Y" else -1)

                # Apply the multiplier if UserAdjInputs is True
                multiplier = TMSAdj.get(TMSLookup, {}).get('Em', 0) if UserAdjInputs == "True" else 1
                travel_time_benefit_induced = base_benefit_induced * multiplier

                # Assign value to (NonHOV Peak) for induced travel time benefit
                TruckinducedPeakTTBenefit = travel_time_benefit_induced

        if vehicle == 'Ramp' and period == 'Peak':
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

        if vehicle == 'Arterial' and period == 'Peak':
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
        if vehicle == 'NonHOV' and period == 'NonPeak':
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
                # Extract the year from the 'Year' value
                year = row['Year']

                if year == 1:
                    travel_time_benefit_induced = (
                        (avg_tt_nobuild - avg_tt_build) * NNT1Ind * (-0.5 if Induced == "Y" else -1)
                    )
                elif year == 20:
                    travel_time_benefit_induced = (
                        (avg_tt_nobuild - avg_tt_build) * NNT20Ind * (-0.5 if Induced == "Y" else -1)
                    )
                else:
                    # Compute the values needed for interpolation inline
                    benefit_year1 = (avg_tt_nobuild - avg_tt_build) * NNT1Ind * (-0.5 if Induced == "Y" else -1)
                    benefit_year20 = (avg_tt_nobuild - avg_tt_build) * NNT20Ind * (-0.5 if Induced == "Y" else -1)

                    travel_time_benefit_induced = np.interp(year, [1, 20], [benefit_year1, benefit_year20])


        # NonPeak Weaving
        if vehicle == 'Weaving' and period == 'NonPeak':
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
        if vehicle == 'Truck' and period == 'NonPeak':
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
                # Extract the year from the 'Year' value
                year = row['Year']

                if year == 1:
                    # Calculate the induced benefit for Year 1
                    travel_time_benefit_induced_Year1 = (
                        (avg_tt_nobuild - avg_tt_build) * NTT1Ind * (-0.5 if Induced == "Y" else -1)
                    )
                    travel_time_benefit_induced = travel_time_benefit_induced_Year1

                elif year == 20:
                    # Calculate the induced benefit for Year 20
                    travel_time_benefit_induced_Year20 = (
                        (avg_tt_nobuild - avg_tt_build) * NTT20Ind * (-0.5 if Induced == "Y" else -1)
                    )
                    travel_time_benefit_induced = travel_time_benefit_induced_Year20

                else:
                    # For years between 2 and 19, interpolate between Year 1 and Year 20 benefits
                    # Known values for Year 1 and Year 20
                    travel_time_benefit_induced_known = np.array([travel_time_benefit_induced_Year1, travel_time_benefit_induced_Year20])

                    # Known years for interpolation
                    years_known = np.array([1, 20])

                    # Calculate linear interpolation between Year 1 and Year 20 benefits
                    slope, intercept = np.polyfit(years_known, travel_time_benefit_induced_known, 1)

                    # Now, calculate the interpolated value for the current year
                    travel_time_benefit_induced = np.polyval([slope, intercept], year)


        # Assign the benefits to the row directly
        final_trend_df.at[idx, 'ExistingBenefit'] = travel_time_benefit_existing
        final_trend_df.at[idx, 'InducedBenefit'] = travel_time_benefit_induced

    # Return the updated DataFrame with benefits columns
    return final_trend_df


def add_dollar_calculated_column(final_trend_df):
    # Access the values from the params and projectinfo_widgets objects
    ValTimeAuto = params.ValTimeAuto
    TTUprater = params.TTUprater
    ValTimeIMFactor = params.ValTimeIMFactor
    Construct = projectinfo_widgets.construct_widget.value
    ProjType = projectinfo_widgets.subcategory_dropdown.value
    
    # Perform the calculation row-wise
    def calculate_new_column(row):
        # Sum of ExistingBenefit and InducedBenefit
        sum_benefits = row['ExistingBenefit'] + row['InducedBenefit']
        
        # Apply the calculation: Use ValTimeIMFactor if ProjType is 'Incident Management'
        factor_im = ValTimeIMFactor if ProjType == 'Incident Management' else 1
        
        # Apply the compound factor for the year (adjust for Construct value)
        year_factor = (1 + TTUprater) ** (row['Year'] + Construct - 1)
        
        # Calculate the result for the 'Constant Dollar' column
        result = sum_benefits * ValTimeAuto * factor_im * year_factor
        return result
    
    # Apply the calculation to each row and add the result as a new column named 'Constant Dollar'
    final_trend_df['Constant Dollar'] = final_trend_df.apply(calculate_new_column, axis=1)
    
    return final_trend_df  # Return the modified DataFrame




def add_discounted_value_column(df, value_column_name, output_column_name):
    Construct = projectinfo_widgets.construct_widget.value
    DiscRate = params.discount_rate
    
    def calculate_discounted_value(row):
        value = row[value_column_name]
        year = row['Year']
        discounted_value = value / ((1 + DiscRate) ** (year + Construct - 1))
        return discounted_value

    df[output_column_name] = df.apply(calculate_discounted_value, axis=1)
    return df

 

sum_by_year = None 

def sum_present_value_by_year(final_trend_df):
    global sum_by_year
    # Group by 'Year' and sum 'Present Value'
    sum_by_year = final_trend_df.groupby('Year')['Present Value'].sum().reset_index()
    sum_by_year = sum_by_year.rename(columns={'Present Value': 'Total Present Value'})
    
    # Calculate total
    total_value = sum_by_year['Total Present Value'].sum()
    
    # Add total row
    total_row = pd.DataFrame([{
        'Year': 'Total Travel Time Benefits',
        'Total Present Value': total_value
    }])
    sum_by_year = pd.concat([sum_by_year, total_row], ignore_index=True)
    
    return sum_by_year, total_value



def get_grouped_highway_results(final_trend_df):

    # Create 'Group' column if not already present
    final_trend_df['Group'] = final_trend_df['Group'].astype(str)  # ensure string for sorting

    # Define custom order for Group sorting
    group_order = [
        'Peak_HOV', 'Peak_NonHOV', 'Peak_Weaving', 'Peak_Truck',
        'Peak_Ramp', 'Peak_Arterial', 'NonPeak_NonHOV', 'NonPeak_Weaving', 'NonPeak_Truck'
    ]

    # Convert to categorical for sorting
    final_trend_df['Group'] = pd.Categorical(final_trend_df['Group'], categories=group_order, ordered=True)

    # Sort DataFrame by 'Group' and optionally 'Year' for readability
    final_trend_df.sort_values(by=['Group', 'Year'], inplace=True)

    # Display grouped results
    grouped = final_trend_df.groupby('Group')

    for group_name, group_df in grouped:
        print(f"\n--- Group: {group_name} ---")
        print(group_df)
        

    return final_trend_df



def main(change=None):
    df_combined = calculate_combined_average(AnnualFactor)
    final_trend_df = generate_trends_from_dataframe(df_combined, variable_names)
    final_trend_df = calculate_person_trips_highway(final_trend_df)
    final_trend_df = calculate_average_travel_time(final_trend_df)
    final_trend_df = traveltime_benefit(final_trend_df)
    final_trend_df = add_dollar_calculated_column(final_trend_df)
    final_trend_df = add_discounted_value_column(final_trend_df, value_column_name='Constant Dollar', output_column_name='Present Value')
    sum_by_year, total_value = sum_present_value_by_year(final_trend_df)
    total_tt_benefit_widget.value = total_value
    # calculate_benefit_cost_ratio(None, sum_by_year)
    
    
main(change=None)    

# List of all widgets (both for volumes and speeds)
widget_triggers = [
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
    modelinputs_widgets.NTV20B_widget,
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
    modelinputs_widgets.NTS20B_widget,
    projectinfo_widgets.subcategory_dropdown,
    projectinfo_widgets.AVOHovNB_widget,
    projectinfo_widgets.AVOHovB_widget,
    projectinfo_widgets.AVO_traffic_P_no_build_widget,
    projectinfo_widgets.AVO_traffic_P_build_widget,
    projectinfo_widgets.AVO_traffic_NP_no_build_widget,
    projectinfo_widgets.AVO_traffic_NP_build_widget,
    projectinfo_widgets.impacted_length_no_build_widget,
    projectinfo_widgets.percent_induced_trip_widget,
    modelinputs_widgets.PNT1Ind_widget,
    modelinputs_widgets.PNT20Ind_widget,
    modelinputs_widgets.RADataAvail_widget,
    projectinfo_widgets.construct_widget,
    projectinfo_widgets.impacted_length_no_build_widget,
    projectinfo_widgets.impacted_length_build_widget,
    modelinputs_widgets.SegmentR_widget,
    modelinputs_widgets.SegmentA_widget,
    projectinfo_widgets.GateTime1_widget
]

# Attach the observer to all widgets in the combined list
for widget in widget_triggers:
    widget.observe(main, names='value')


