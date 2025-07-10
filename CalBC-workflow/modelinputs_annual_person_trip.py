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

    
#########################################################
#########################################################
#########################################################
#########################################################
#########################################################

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
 



 ##############################################################################################
 ##############################################################################################
 ##############################################################################################
 ##############################################################################################
       
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
    
    
    