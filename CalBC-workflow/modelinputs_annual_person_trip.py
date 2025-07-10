""
### Year 1 Peak ###
######################################### HOV Trips #######################################
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
########### function to update HOV Trips No Build ###############
def update_annualpersontrip_year1_peak_HOVtrips_nobuild(change):
    PeakLngthNB = projectinfo_widgets.peak_period_widget.value
    HOVvolNB = projectinfo_widgets.HOV_lane_nobuild_widget.value
    AVOHovNB = projectinfo_widgets.AVOHovNB_widget.value
    AnnualFactor = params.AnnualFactor
    annualpersontrip_year1_peak_HOVtrips_nobuild = PeakLngthNB*HOVvolNB*AVOHovNB*AnnualFactor
    HOVtrips_year1_nobuild_peak_widget.value = annualpersontrip_year1_peak_HOVtrips_nobuild
######### observe and update value to changes in user-modified value #########
projectinfo_widgets.peak_period_widget.observe(update_annualpersontrip_year1_peak_HOVtrips_nobuild, names='value')
projectinfo_widgets.HOV_lane_nobuild_widget.observe(update_annualpersontrip_year1_peak_HOVtrips_nobuild, names='value')
projectinfo_widgets.AVOHovNB_widget.observe(update_annualpersontrip_year1_peak_HOVtrips_nobuild, names='value')

########### function to update HOV Trips Build ###############
def update_annualpersontrip_year1_peak_HOVtrips_build(change):
    PeakLngthNB = projectinfo_widgets.peak_period_widget.value
    HOVvolB = projectinfo_widgets.HOV_lane_build_widget.value
    AVOHovB = projectinfo_widgets.AVOHovB_widget.value
    AnnualFactor = params.AnnualFactor
    annualpersontrip_year1_peak_HOVtrips_build = PeakLngthNB*HOVvolB*AVOHovB*AnnualFactor
    HOVtrips_year1_build_peak_widget.value = annual_persontrip_year1_peak_HOVtrips_build
############# observe and update value to changes in user-modified value #################
projectinfo_widgets.peak_period_widget.observe(update_annualpersontrip_year1_peak_HOVtrips_build, names='value')
projectinfo_widgets.HOV_lane_build_widget.observe(update_annualpersontrip_year1_peak_HOVtrips_build, names='value')
projectinfo_widgets.AVOHovB_widget.observe(update_annualpersontrip_year1_peak_HOVtrips_build, names='value')

### Year 1 Peak ###
########################################## NonHOV Trips ################################################
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
########### function to update Non-HOV Trips No Build ###############
def update_annualpersontrip_year1_peak_NonHOVtrips_nobuild(change):
    ProjType = projectinfo_widgets.subcategory_dropdown.value
    PerPeakADT = params.per_peak_adt
    ADT1NB = projectinfo_widgets.adt_base_year_no_build_widget.value
    PerTruckNB =  projectinfo_widgets.percent_trucks_nobuild_widget.value
    PeakLngthNB = projectinfo_widgets.peak_period_widget.value
    HOVvolNB = projectinfo_widgets.HOV_lane_nobuild_widget.value
    RampVolP =  projectinfo_widgets.hourly_ramp_volume_peak_widget.value
    AVOPeakNB = projectinfo_widgets.AVO_traffic_P_no_build_widget.value
    AnnualFactor = params.AnnualFactor
    if ProjType == "Auxiliary Lane":
                x = RampVolP*PeakLngthNB
            else:
                x = 0
    annualpersontrip_year1_peak_NonHOVtrips_nobuild = (PerPeakADT*ADT1NB*(1-PerTruckNB)-PeakLngthNB*HOVvolNB+x)*AVOPeakNB*AnnualFactor
    NonHOVtrips_year1_nobuild_peak_widget.value = annualpersontrip_year1_peak_NonHOVtrips_nobuild
######### observe and update value to changes in user-modified value #########
projectinfo_widgets.subcategory_dropdown.observe(update_annualpersontrip_year1_peak_NonHOVtrips_nobuild, names='value')
projectinfo_widgets.adt_base_year_no_build_widget.observe(update_annualpersontrip_year1_peak_NonHOVtrips_nobuild, names='value')
projectinfo_widgets.percent_trucks_nobuild_widget.observe(update_annualpersontrip_year1_peak_NonHOVtrips_nobuild, names='value')
projectinfo_widgets.peak_period_widget.observe(update_annualpersontrip_year1_peak_NonHOVtrips_nobuild, names='value')
projectinfo_widgets.HOV_lane_nobuild_widget.observe(update_annualpersontrip_year1_peak_NonHOVtrips_nobuild, names='value')
projectinfo_widgets.hourly_ramp_volume_peak_widget.observe(update_annualpersontrip_year1_peak_NonHOVtrips_nobuild, names='value')
projectinfo_widgets.AVO_traffic_P_no_build_widget.observe(update_annualpersontrip_year1_peak_NonHOVtrips_nobuild, names='value')

########### function to update Non-HOV Trips Build ###############
def update_annualpersontrip_year1_peak_NonHOVtrips_build(change):
    ProjType = projectinfo_widgets.subcategory_dropdown.value
    PerPeakADT = params.per_peak_adt
    ADT1B = projectinfo_widgets.adt_base_year_build_widget.value
    PerTruckB = projectinfo_widgets.percent_trucks_build_widget.value
    PeakLngthNB = projectinfo_widgets.peak_period_widget.value
    HOVvolB = projectinfo_widgets.HOV_lane_build_widget.value
    RampVolP =  projectinfo_widgets.hourly_ramp_volume_peak_widget.value
    AVOPeakB = projectinfo_widgets.AVO_traffic_P_build_widget.value
    AnnualFactor = params.AnnualFactor
    if ProjType == "Auxiliary Lane":
                x = RampVolP*PeakLngthNB
            else:
                x = 0
    annualpersontrip_year1_peak_NonHOVtrips_build = (PerPeakADT*ADT1B*(1-PerTruckB)-PeakLngthNB*HOVvolB+x)*AVOPeakB*AnnualFactor
    NonHOVtrips_year1_build_peak_widget.value = annualpersontrip_year1_peak_NonHOVtrips_build
######### observe and update value to changes in user-modified value #########
projectinfo_widgets.subcategory_dropdown.observe(update_annualpersontrip_year1_peak_NonHOVtrips_build, names='value')
projectinfo_widgets.adt_base_year_build_widget.observe(update_annualpersontrip_year1_peak_NonHOVtrips_build, names='value')
projectinfo_widgets.percent_trucks_build_widget.observe(update_annualpersontrip_year1_peak_NonHOVtrips_build, names='value')
projectinfo_widgets.peak_period_widget.observe(update_annualpersontrip_year1_peak_NonHOVtrips_build, names='value')
projectinfo_widgets.HOV_lane_build_widget.observe(update_annualpersontrip_year1_peak_NonHOVtrips_build, names='value')
projectinfo_widgets.hourly_ramp_volume_peak_widget.observe(update_annualpersontrip_year1_peak_NonHOVtrips_build, names='value')
projectinfo_widgets.AVO_traffic_P_build_widget.observe(update_annualpersontrip_year1_peak_NonHOVtrips_build, names='value')

### Year 1 Peak ###
######################################### Truck Trips #############################################
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
########### function to update Truck Trips No Build ###############
def update_annualpersontrip_year1_peak_TruckTrips_nobuild(change):
    PerPeakADT = params.per_peak_adt
    ADT1NB = projectinfo_widgets.adt_base_year_no_build_widget.value
    PerTruckNB = projectinfo_widgets.percent_trucks_nobuild_widget.value
    AnnualFactor = params.AnnualFactor
    annualpersontrip_year1_peak_TruckTrips_nobuild = PerPeakADT*ADT1NB*PerTruckNB*AnnualFactor
    TruckTrips_year1_nobuild_peak_widget.value = annualpersontrip_year1_peak_TruckTrips_nobuild
######### observe and update value to changes in user-modified value #########
projectinfo_widgets.adt_base_year_no_build_widget.observe(update_annualpersontrip_year1_peak_TruckTrips_nobuild, names='value')
projectinfo_widgets.percent_trucks_nobuild_widget.observe(update_annualpersontrip_year1_peak_TruckTrips_nobuild, names='value')

########### function to update Truck Trips Build ###############
def update_annualpersontrip_year1_peak_TruckTrips_build(change):
    PerPeakADT = params.per_peak_adt
    ADT1B = projectinfo_widgets.adt_base_year_build_widget.value
    PerTruckB = projectinfo_widgets.percent_trucks_build_widget.value
    AnnualFactor = params.AnnualFactor
    annualpersontrip_year1_peak_TruckTrips_build = PerPeakADT*ADT1B*PerTruckB*AnnualFactor
    
    TruckTrips_year1_build_peak_widget.value = annualpersontrip_year1_peak_TruckTrips_build
######### observe and update value to changes in user-modified value #########
projectinfo_widgets.adt_base_year_build_widget.observe(update_annualpersontrip_year1_peak_TruckTrips_build, names='value')
projectinfo_widgets.percent_trucks_build_widget.observe(update_annualpersontrip_year1_peak_TruckTrips_build, names='value')


### Year 1 NonPeak ###
########################################## NonHOV Trips ################################################
########################################################################################################
    NonHOVtrips_year1_nobuild_nonpeak_widget = widgets.IntText(
        value=0,
        description="Non-HOV Annual Person Trips (No Build):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    NonHOVtrips_year1_build_nonpeak_widget = widgets.IntText(
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
    
########### function to update Non-HOV Trips No Build ###############
def update_annualpersontrip_year1_nonpeak_NonHOVtrips_nobuild(change):
    ProjType = projectinfo_widgets.subcategory_dropdown.value
    PerPeakADT = params.per_peak_adt
    ADT1NB = projectinfo_widgets.adt_base_year_no_build_widget.value
    PerTruckNB =  projectinfo_widgets.percent_trucks_nobuild_widget.value
    RampVolNP = projectinfo_widgets.hourly_ramp_volume_nonpeak_widget.value
    PeakLngthNB = projectinfo_widgets.peak_period_widget.value
    AVONonNB = projectinfo_widgets.AVO_traffic_NP_no_build_widget.value
    AnnualFactor = params.AnnualFactor
    if ProjType == "Auxiliary Lane":
                x = RampVolNP*(24-PeakLngthNB)
            else:
                x = 0
    annualpersontrip_year1_nonpeak_NonHOVtrips_nobuild = ((1-PerPeakADT)*ADT1NB*(1-PerTruckNB)+x)*AVONonNB*AnnualFactor
    NonHOVtrips_year1_nobuild_nonpeak_widget.value = annualpersontrip_year1_nonpeak_NonHOVtrips_nobuild
######### observe and update value to changes in user-modified value #########
projectinfo_widgets.subcategory_dropdown.observe(update_annualpersontrip_year1_nonpeak_NonHOVtrips_nobuild, names='value')
projectinfo_widgets.adt_base_year_no_build_widget.observe(update_annualpersontrip_year1_nonpeak_NonHOVtrips_nobuild, names='value')
projectinfo_widgets.percent_trucks_nobuild_widget.observe(update_annualpersontrip_year1_nonpeak_NonHOVtrips_nobuild, names='value')
projectinfo_widgets.hourly_ramp_volume_nonpeak_widget.observe(update_annualpersontrip_year1_nonpeak_NonHOVtrips_nobuild, names='value')
projectinfo_widgets.peak_period_widget.observe(update_annualpersontrip_year1_nonpeak_NonHOVtrips_nobuild, names='value')
projectinfo_widgets.AVO_traffic_NP_no_build_widget.observe(update_annualpersontrip_year1_nonpeak_NonHOVtrips_nobuild, names='value')

########### function to update Non-HOV Trips Build ###############
def update_annualpersontrip_year1_nonpeak_NonHOVtrips_build(change):
    ProjType = projectinfo_widgets.subcategory_dropdown.value
    PerPeakADT = params.per_peak_adt
    ADT1B = projectinfo_widgets.adt_base_year_build_widget.value
    PerTruckB = projectinfo_widgets.percent_trucks_build_widget.value
    RampVolNP = projectinfo_widgets.hourly_ramp_volume_nonpeak_widget.value
    PeakLngthNB = projectinfo_widgets.peak_period_widget.value
    AVONonB = projectinfo_widgets.AVO_traffic_NP_build_widget.value
    AnnualFactor = params.AnnualFactor
    if ProjType == "Auxiliary Lane":
                x = RampVolNP*(24-PeakLngthNB)
            else:
                x = 0
    annualpersontrip_year1_nonpeak_NonHOVtrips_build = ((1-PerPeakADT)*ADT1B*(1-PerTruckB)+x)*AVONonB*AnnualFactor
    NonHOVtrips_year1_build_nonpeak_widget.value = annualpersontrip_year1_nonpeak_NonHOVtrips_build
######### observe and update value to changes in user-modified value #########
projectinfo_widgets.subcategory_dropdown.observe(update_annualpersontrip_year1_nonpeak_NonHOVtrips_build, names='value')
projectinfo_widgets.adt_base_year_build_widget.observe(update_annualpersontrip_year1_nonpeak_NonHOVtrips_build, names='value')
projectinfo_widgets.percent_trucks_build_widget.observe(update_annualpersontrip_year1_nonpeak_NonHOVtrips_build, names='value')
projectinfo_widgets.hourly_ramp_volume_nonpeak_widget.observe(update_annualpersontrip_year1_nonpeak_NonHOVtrips_build, names='value')
projectinfo_widgets.peak_period_widget.observe(update_annualpersontrip_year1_nonpeak_NonHOVtrips_build, names='value')
projectinfo_widgets.AVO_traffic_NP_build.observe(update_annualpersontrip_year1_nonpeak_NonHOVtrips_build, names='value')

    
### Year 1 NonPeak ###
########################################## Truck Trips ################################################
    TruckTrips_year1_nobuild_nonpeak_widget = widgets.IntText(
        value=0,
        description="Truck Annual Trips (No Build):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    TruckTrips_year1_build_nonpeak_widget = widgets.IntText(
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
    
########### function to update Truck Trips No Build ###############
def update_annualpersontrip_year1_nonpeak_TruckTrips_nobuild(change):
    PerPeakADT = params.per_peak_adt
    ADT1NB = projectinfo_widgets.adt_base_year_no_build_widget.value
    PerTruckNB = projectinfo_widgets.percent_trucks_nobuild_widget.value
    AnnualFactor = params.AnnualFactor
    annualpersontrip_year1_nonpeak_TruckTrips_nobuild = (1-PerPeakADT)*ADT1NB*PerTruckNB*AnnualFactor
    TruckTrips_year1_nobuild_nonpeak_widget.value = annualpersontrip_year1_nonpeak_TruckTrips_nobuild
    
######### observe and update value to changes in user-modified value #########
projectinfo_widgets.adt_base_year_no_build_widget.observe(update_annualpersontrip_year1_nonpeak_TruckTrips_nobuild, names='value')
projectinfo_widgets.percent_trucks_nobuild_widget.observe(update_annualpersontrip_year1_nonpeak_TruckTrips_nobuild, names='value')

########### function to update Truck Trips Build ###############
def update_annualpersontrip_year1_nonpeak_TruckTrips_build(change):
    PerPeakADT = params.per_peak_adt
    ADT1B = projectinfo_widgets.adt_base_year_build_widget.value
    PerTruckB = projectinfo_widgets.percent_trucks_build_widget.value
    AnnualFactor = params.AnnualFactor
    
    annualpersontrip_year1_nonpeak_TruckTrips_build = (1-PerPeakADT)*ADT1B*PerTruckB*AnnualFactor
    TruckTrips_year1_build_nonpeak_widget.value = annualpersontrip_year1_nonpeak_TruckTrips_build
######### observe and update value to changes in user-modified value #########
projectinfo_widgets.adt_base_year_build_widget.observe(update_annualpersontrip_year1_nonpeak_TruckTrips_build, names='value')
projectinfo_widgets.percent_trucks_build_widget.observe(update_annualpersontrip_year1_nonpeak_TruckTrips_build, names='value')

### Year 1 Total Trips ###
######################################################################################
######################################################################################
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
    
########### function to update Total Trips No Build ###############
def update_annualpersontrip_year1_TotalTrips_nobuild(change):
    HOVPNBY1 = HOVtrips_year1_nobuild_peak_widget.value
    NonHOVPNBY1 = NonHOVtrips_year1_nobuild_peak_widget.value
    TruckPNBY1 = TruckTrips_year1_nobuild_peak_widget.value
    NonHOVNPNBY1 = NonHOVtrips_year1_nobuild_nonpeak_widget.value
    TruckNPNBY1 = TruckTrips_year1_nobuild_nonpeak_widget.value
    annualpersontrip_year1_TotalTrips_nobuild = HOVPNBY1+NonHOVPNBY1+TruckPNBY1+NonHOVNPNBY1+TruckNPNBY1
    TotalTrips_year1_nobuild_widget.value = annualpersontrip_year1_TotalTrips_nobuild
######### observe and update value to changes in user-modified value #########
HOVtrips_year1_nobuild_peak_widget.observe(update_annualpersontrip_year1_TotalTrips_nobuild, names='value')
NonHOVtrips_year1_nobuild_peak_widget.observe(update_annualpersontrip_year1_TotalTrips_nobuild, names='value')
TruckTrips_year1_nobuild_peak_widget.observe(update_annualpersontrip_year1_TotalTrips_nobuild, names='value')
NonHOVtrips_year1_nobuild_nonpeak_widget.observe(update_annualpersontrip_year1_TotalTrips_nobuild, names='value')
TruckTrips_year1_nobuild_nonpeak_widget.observe(update_annualpersontrip_year1_TotalTrips_nobuild, names='value')
########### function to update Total Trips Build ###############
def update_annualpersontrip_year1_TotalTrips_build(change):
    HOVPBY1 = HOVtrips_year1_build_peak_widget.value
    NonHOVPBY1 = NonHOVtrips_year1_build_peak_widget.value
    TruckPBY1 = TruckTrips_year1_build_peak_widget.value
    NonHOVNPBY1 = NonHOVtrips_year1_build_nonpeak_widget.value
    TruckNPBY1 = TruckTrips_year1_build_nonpeak_widget.value
    annualpersontrip_year1_TotalTrips_build = HOVPBY1+NonHOVPBY1+TruckPBY1+NonHOVNPBY1+TruckNPBY1
    TotalTrips_year1_build_widget.value = annualpersontrip_year1_TotalTrips_build
######### observe and update value to changes in user-modified value #########
HOVtrips_year1_build_peak_widget.observe(update_annualpersontrip_year1_TotalTrips_build, names='value')
NonHOVtrips_year1_build_peak_widget.observe(update_annualpersontrip_year1_TotalTrips_build, names='value')
TruckTrips_year1_build_peak_widget.observe(update_annualpersontrip_year1_TotalTrips_build, names='value')
NonHOVtrips_year1_build_nonpeak_widget.observe(update_annualpersontrip_year1_TotalTrips_build, names='value')
TruckTrips_year1_build_nonpeak_widget.observe(update_annualpersontrip_year1_TotalTrips_build, names='value')
    
    
    
    
##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################

### Year 20 Peak ###
######################################### HOV Trips #######################################
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

########### function to update HOV Trips No Build ###############
def update_annualpersontrip_year20_peak_HOVtrips_nobuild(change):
    PeakLngthNB = projectinfo_widgets.peak_period_widget.value
    HOVvolNB = projectinfo_widgets.HOV_lane_nobuild_widget.value
    AVOHovNB = projectinfo_widgets.AVOHovNB_widget.value
    AnnualFactor = params.AnnualFactor
    annualpersontrip_year20_peak_HOVtrips_nobuild = PeakLngthNB*HOVvolNB*AVOHovNB*AnnualFactor
    HOVtrips_year20_nobuild_peak_widget.value = annualpersontrip_year20_peak_HOVtrips_nobuild
######### observe and update value to changes in user-modified value #########
projectinfo_widgets.peak_period_widget.observe(update_annualpersontrip_year20_peak_HOVtrips_nobuild, names='value')
projectinfo_widgets.HOV_lane_nobuild_widget.observe(update_annualpersontrip_year20_peak_HOVtrips_nobuild, names='value')
projectinfo_widgets.AVOHovNB_widget.observe(update_annualpersontrip_year20_peak_HOVtrips_nobuild, names='value')

########### function to update HOV Trips Build ###############
def update_annualpersontrip_year20_peak_HOVtrips_build(change):
    PeakLngthNB = projectinfo_widgets.peak_period_widget.value
    HOVvolB = projectinfo_widgets.HOV_lane_build_widget.value
    AVOHovB = projectinfo_widgets.AVOHovB_widget.value
    AnnualFactor = params.AnnualFactor
    annualpersontrip_year20_peak_HOVtrips_build = PeakLngthNB*HOVvolB*AVOHovB*AnnualFactor
    HOVtrips_year20_build_peak_widget.value = annual_persontrip_year20_peak_HOVtrips_build
############# observe and update value to changes in user-modified value #################
projectinfo_widgets.peak_period_widget.observe(update_annualpersontrip_year20_peak_HOVtrips_build, names='value')
projectinfo_widgets.HOV_lane_build_widget.observe(update_annualpersontrip_year20_peak_HOVtrips_build, names='value')
projectinfo_widgets.AVOHovB_widget.observe(update_annualpersontrip_year20_peak_HOVtrips_build, names='value')
    
### Year 20 Peak ###
######################################### NonHOV Trips #######################################
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
    
########### function to update Non-HOV Trips No Build ###############
def update_annualpersontrip_year20_peak_NonHOVtrips_nobuild(change):
    ProjType = projectinfo_widgets.subcategory_dropdown.value
    PerPeakADT = params.per_peak_adt
    ADT20NB = projectinfo_widgets.ADT_20NB_widget.value
    PerTruckNB =  projectinfo_widgets.percent_trucks_nobuild_widget.value
    PeakLngthNB = projectinfo_widgets.peak_period_widget.value
    HOVvolNB = projectinfo_widgets.HOV_lane_nobuild_widget.value
    RampVolP =  projectinfo_widgets.hourly_ramp_volume_peak_widget.value
    AVOPeakNB = projectinfo_widgets.AVO_traffic_P_no_build_widget.value
    AnnualFactor = params.AnnualFactor
    if ProjType == "Auxiliary Lane":
                x = RampVolP*PeakLngthNB
            else:
                x = 0
    annualpersontrip_year20_peak_NonHOVtrips_nobuild = (PerPeakADT*ADT20NB*(1-PerTruckNB)-PeakLngthNB*HOVvolNB+x)*AVOPeakNB*AnnualFactor
    NonHOVtrips_year20_nobuild_peak_widget.value = annualpersontrip_year20_peak_NonHOVtrips_nobuild
######### observe and update value to changes in user-modified value #########
projectinfo_widgets.subcategory_dropdown.observe(update_annualpersontrip_year20_peak_NonHOVtrips_nobuild, names='value')
projectinfo_widgets.adt_base_year_no_build_widget.observe(update_annualpersontrip_year20_peak_NonHOVtrips_nobuild, names='value')
projectinfo_widgets.percent_trucks_nobuild_widget.observe(update_annualpersontrip_year20_peak_NonHOVtrips_nobuild, names='value')
projectinfo_widgets.peak_period_widget.observe(update_annualpersontrip_year20_peak_NonHOVtrips_nobuild, names='value')
projectinfo_widgets.HOV_lane_nobuild_widget.observe(update_annualpersontrip_year20_peak_NonHOVtrips_nobuild, names='value')
projectinfo_widgets.hourly_ramp_volume_peak_widget.observe(update_annualpersontrip_year20_peak_NonHOVtrips_nobuild, names='value')
projectinfo_widgets.AVO_traffic_P_no_build_widget.observe(update_annualpersontrip_year20_peak_NonHOVtrips_nobuild, names='value')

########### function to update Non-HOV Trips Build ###############
def update_annualpersontrip_year20_peak_NonHOVtrips_build(change):
    ProjType = projectinfo_widgets.subcategory_dropdown.value
    PerPeakADT = params.per_peak_adt
    ADT20B = projectinfo_widgets.adt_20_year_build_widget.value
    PerTruckB = projectinfo_widgets.percent_trucks_build_widget.value
    PeakLngthNB = projectinfo_widgets.peak_period_widget.value
    HOVvolB = projectinfo_widgets.HOV_lane_build_widget.value
    RampVolP =  projectinfo_widgets.hourly_ramp_volume_peak_widget.value
    AVOPeakB = projectinfo_widgets.AVO_traffic_P_build_widget.value
    AnnualFactor = params.AnnualFactor
    if ProjType == "Auxiliary Lane":
                x = RampVolP*PeakLngthNB
            else:
                x = 0
    annualpersontrip_year20_peak_NonHOVtrips_build = (PerPeakADT*ADT20B*(1-PerTruckB)-PeakLngthNB*HOVvolB+x)*AVOPeakB*AnnualFactor
    NonHOVtrips_year20_build_peak_widget.value = annualpersontrip_year20_peak_NonHOVtrips_build
######### observe and update value to changes in user-modified value #########
projectinfo_widgets.subcategory_dropdown.observe(update_annualpersontrip_year20_peak_NonHOVtrips_build, names='value')
projectinfo_widgets.adt_base_year_build_widget.observe(update_annualpersontrip_year20_peak_NonHOVtrips_build, names='value')
projectinfo_widgets.percent_trucks_build_widget.observe(update_annualpersontrip_year20_peak_NonHOVtrips_build, names='value')
projectinfo_widgets.peak_period_widget.observe(update_annualpersontrip_year20_peak_NonHOVtrips_build, names='value')
projectinfo_widgets.HOV_lane_build_widget.observe(update_annualpersontrip_year20_peak_NonHOVtrips_build, names='value')
projectinfo_widgets.hourly_ramp_volume_peak_widget.observe(update_annualpersontrip_year20_peak_NonHOVtrips_build, names='value')
projectinfo_widgets.AVO_traffic_P_build_widget.observe(update_annualpersontrip_year20_peak_NonHOVtrips_build, names='value')

### Year 20 Peak ###
######################################### Truck Trips #######################################
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
    
########### function to update Truck Trips No Build ###############
def update_annualpersontrip_year20_peak_TruckTrips_nobuild(change):
    PerPeakADT = params.per_peak_adt
    ADT20NB = projectinfo_widgets.ADT_20NB_widget.value
    PerTruckNB = projectinfo_widgets.percent_trucks_nobuild_widget.value
    AnnualFactor = params.AnnualFactor
    annualpersontrip_year20_peak_TruckTrips_nobuild = PerPeakADT*ADT20NB*PerTruckNB*AnnualFactor
    TruckTrips_year20_nobuild_peak_widget.value = annualpersontrip_year20_peak_TruckTrips_nobuild
######### observe and update value to changes in user-modified value #########
projectinfo_widgets.adt_base_year_no_build_widget.observe(update_annualpersontrip_year20_peak_TruckTrips_nobuild, names='value')
projectinfo_widgets.percent_trucks_nobuild_widget.observe(update_annualpersontrip_year20_peak_TruckTrips_nobuild, names='value')

########### function to update Truck Trips Build ###############
def update_annualpersontrip_year20_peak_TruckTrips_build(change):
    PerPeakADT = params.per_peak_adt
    ADT20B = projectinfo_widgets.adt_20_year_build_widget.value
    PerTruckB = projectinfo_widgets.percent_trucks_build_widget.value
    AnnualFactor = params.AnnualFactor
    annualpersontrip_year20_peak_TruckTrips_build = PerPeakADT*ADT20B*PerTruckB*AnnualFactor
    TruckTrips_year20_build_peak_widget.value = annualpersontrip_year20_peak_TruckTrips_build
######### observe and update value to changes in user-modified value #########
projectinfo_widgets.adt_base_year_build_widget.observe(update_annualpersontrip_year20_peak_TruckTrips_build, names='value')
projectinfo_widgets.percent_trucks_build_widget.observe(update_annualpersontrip_year20_peak_TruckTrips_build, names='value')
    
### Year 20 NonPeak ###
######################################### NonHOV Trips #######################################
#################################################################################################
    NonHOVtrips_year20_nobuild_nonpeak_widget = widgets.IntText(
        value=0,
        description="Non-HOV Annual Person Trips (No Build):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    NonHOVtrips_year20_build_nonpeak_widget = widgets.IntText(
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
    
########### function to update Non-HOV Trips No Build ###############
def update_annualpersontrip_year20_nonpeak_NonHOVtrips_nobuild(change):
    ProjType = projectinfo_widgets.subcategory_dropdown.value
    PerPeakADT = params.per_peak_adt
    ADT20NB = projectinfo_widgets.ADT_20NB_widget.value
    PerTruckNB =  projectinfo_widgets.percent_trucks_nobuild_widget.value
    RampVolNP = projectinfo_widgets.hourly_ramp_volume_nonpeak_widget.value
    PeakLngthNB = projectinfo_widgets.peak_period_widget.value
    AVONonNB = projectinfo_widgets.AVO_traffic_NP_no_build_widget.value
    AnnualFactor = params.AnnualFactor
    if ProjType == "Auxiliary Lane":
                x = RampVolNP*(24-PeakLngthNB)
            else:
                x = 0
    annualpersontrip_year20_nonpeak_NonHOVtrips_nobuild = ((1-PerPeakADT)*ADT20NB*(1-PerTruckNB)+x)*AVONonNB*AnnualFactor
    NonHOVtrips_year20_nobuild_nonpeak_widget.value = annualpersontrip_year20_nonpeak_NonHOVtrips_nobuild
######### observe and update value to changes in user-modified value #########
projectinfo_widgets.subcategory_dropdown.observe(update_annualpersontrip_year20_nonpeak_NonHOVtrips_nobuild, names='value')
projectinfo_widgets.adt_base_year_no_build_widget.observe(update_annualpersontrip_year20_nonpeak_NonHOVtrips_nobuild, names='value')
projectinfo_widgets.percent_trucks_nobuild_widget.observe(update_annualpersontrip_year20_nonpeak_NonHOVtrips_nobuild, names='value')
projectinfo_widgets.hourly_ramp_volume_nonpeak_widget.observe(update_annualpersontrip_year20_nonpeak_NonHOVtrips_nobuild, names='value')
projectinfo_widgets.peak_period_widget.observe(update_annualpersontrip_year20_nonpeak_NonHOVtrips_nobuild, names='value')
projectinfo_widgets.AVO_traffic_NP_no_build_widget.observe(update_annualpersontrip_year20_nonpeak_NonHOVtrips_nobuild, names='value')

########### function to update Non-HOV Trips Build ###############
def update_annualpersontrip_year20_nonpeak_NonHOVtrips_build(change):
    ProjType = projectinfo_widgets.subcategory_dropdown.value
    PerPeakADT = params.per_peak_adt
    ADT20B = projectinfo_widgets.adt_20_year_build_widget.value
    PerTruckB = projectinfo_widgets.percent_trucks_build_widget.value
    RampVolNP = projectinfo_widgets.hourly_ramp_volume_nonpeak_widget.value
    PeakLngthNB = projectinfo_widgets.peak_period_widget.value
    AVONonB = projectinfo_widgets.AVO_traffic_NP_build_widget.value
    AnnualFactor = params.AnnualFactor
    if ProjType == "Auxiliary Lane":
                x = RampVolNP*(24-PeakLngthNB)
            else:
                x = 0
    annualpersontrip_year20_nonpeak_NonHOVtrips_build = ((1-PerPeakADT)*ADT20B*(1-PerTruckB)+x)*AVONonB*AnnualFactor
    NonHOVtrips_year20_build_nonpeak_widget.value = annualpersontrip_year20_nonpeak_NonHOVtrips_build
######### observe and update value to changes in user-modified value #########
projectinfo_widgets.subcategory_dropdown.observe(update_annualpersontrip_year20_nonpeak_NonHOVtrips_build, names='value')
projectinfo_widgets.adt_base_year_build_widget.observe(update_annualpersontrip_year20_nonpeak_NonHOVtrips_build, names='value')
projectinfo_widgets.percent_trucks_build_widget.observe(update_annualpersontrip_year20_nonpeak_NonHOVtrips_build, names='value')
projectinfo_widgets.hourly_ramp_volume_nonpeak_widget.observe(update_annualpersontrip_year20_nonpeak_NonHOVtrips_build, names='value')
projectinfo_widgets.peak_period_widget.observe(update_annualpersontrip_year20_nonpeak_NonHOVtrips_build, names='value')
projectinfo_widgets.AVO_traffic_NP_build.observe(update_annualpersontrip_year20_nonpeak_NonHOVtrips_build, names='value')
    
### Year 20 nonPeak ###
######################################### Truck Trips #######################################
    TruckTrips_year20_nobuild_nonpeak_widget = widgets.IntText(
        value=0,
        description="Truck Annual Trips (No Build):",
        disabled=False,
        layout=common_layout,
        style={'description_width': 'initial'}
    )

    TruckTrips_year20_build_nonpeak_widget = widgets.IntText(
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
    
########### function to update Truck Trips No Build ###############
def update_annualpersontrip_year20_nonpeak_TruckTrips_nobuild(change):
    PerPeakADT = params.per_peak_adt
    ADT20NB = projectinfo_widgets.ADT_20NB_widget.value
    PerTruckNB = projectinfo_widgets.percent_trucks_nobuild_widget.value
    AnnualFactor = params.AnnualFactor
    annualpersontrip_year20_nonpeak_TruckTrips_nobuild = (1-PerPeakADT)*ADT20NB*PerTruckNB*AnnualFactor
    TruckTrips_year20_nobuild_nonpeak_widget.value = annualpersontrip_year20_nonpeak_TruckTrips_nobuild
    
######### observe and update value to changes in user-modified value #########
projectinfo_widgets.adt_base_year_no_build_widget.observe(update_annualpersontrip_year20_nonpeak_TruckTrips_nobuild, names='value')
projectinfo_widgets.percent_trucks_nobuild_widget.observe(update_annualpersontrip_year20_nonpeak_TruckTrips_nobuild, names='value')

########### function to update Truck Trips Build ###############
def update_annualpersontrip_year20_nonpeak_TruckTrips_build(change):
    PerPeakADT = params.per_peak_adt
    ADT20B = projectinfo_widgets.adt_20_year_build_widget.value
    PerTruckB = projectinfo_widgets.percent_trucks_build_widget.value
    AnnualFactor = params.AnnualFactor
    
    annualpersontrip_year20_nonpeak_TruckTrips_build = (1-PerPeakADT)*ADT20B*PerTruckB*AnnualFactor
    TruckTrips_year20_build_nonpeak_widget.value = annualpersontrip_year20_nonpeak_TruckTrips_build
######### observe and update value to changes in user-modified value #########
projectinfo_widgets.adt_base_year_build_widget.observe(update_annualpersontrip_year20_nonpeak_TruckTrips_build, names='value')
projectinfo_widgets.percent_trucks_build_widget.observe(update_annualpersontrip_year20_nonpeak_TruckTrips_build, names='value')

### Year 20 Total Trips ###
######################################################################################################
######################################################################################################
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
    
########### function to update Total Trips No Build ###############
def update_annualpersontrip_year20_TotalTrips_nobuild(change):
    HOVPNBY20 = HOVtrips_year20_nobuild_peak_widget.value
    NonHOVPNBY20 = NonHOVtrips_year20_nobuild_peak_widget.value
    TruckPNBY20 = TruckTrips_year20_nobuild_peak_widget.value
    NonHOVNPNBY20 = NonHOVtrips_year20_nobuild_nonpeak_widget.value
    TruckNPNBY20 = TruckTrips_year20_nobuild_nonpeak_widget.value
    annualpersontrip_year20_TotalTrips_nobuild = HOVPNBY1+NonHOVPNBY1+TruckPNBY1+NonHOVNPNBY1+TruckNPNBY1
    TotalTrips_year20_nobuild_widget.value = annualpersontrip_year20_TotalTrips_nobuild
######### observe and update value to changes in user-modified value #########
HOVtrips_year20_nobuild_peak_widget.observe(update_annualpersontrip_year20_TotalTrips_nobuild, names='value')
NonHOVtrips_year20_nobuild_peak_widget.observe(update_annualpersontrip_year20_TotalTrips_nobuild, names='value')
TruckTrips_year20_nobuild_peak_widget.observe(update_annualpersontrip_year20_TotalTrips_nobuild, names='value')
NonHOVtrips_year20_nobuild_nonpeak_widget.observe(update_annualpersontrip_year20_TotalTrips_nobuild, names='value')
TruckTrips_year20_nobuild_nonpeak_widget.observe(update_annualpersontrip_year20_TotalTrips_nobuild, names='value')

########### function to update Total Trips Build ###############
def update_annualpersontrip_year20_TotalTrips_build(change):
    HOVPBY20 = HOVtrips_year20_build_peak_widget.value
    NonHOVPBY20 = NonHOVtrips_year20_build_peak_widget.value
    TruckPBY20 = TruckTrips_year20_build_peak_widget.value
    NonHOVNPBY20 = NonHOVtrips_year20_build_nonpeak_widget.value
    TruckNPBY20 = TruckTrips_year20_build_nonpeak_widget.value
    annualpersontrip_year20_TotalTrips_build = HOVPBY1+NonHOVPBY1+TruckPBY1+NonHOVNPBY1+TruckNPBY1
    TotalTrips_year20_build_widget.value = annualpersontrip_year20_TotalTrips_build
######### observe and update value to changes in user-modified value #########
HOVtrips_year20_build_peak_widget.observe(update_annualpersontrip_year20_TotalTrips_build, names='value')
NonHOVtrips_year20_build_peak_widget.observe(update_annualpersontrip_year20_TotalTrips_build, names='value')
TruckTrips_year20_build_peak_widget.observe(update_annualpersontrip_year20_TotalTrips_build, names='value')
NonHOVtrips_year20_build_nonpeak_widget.observe(update_annualpersontrip_year20_TotalTrips_build, names='value')
TruckTrips_year20_build_nonpeak_widget.observe(update_annualpersontrip_year20_TotalTrips_build, names='value')