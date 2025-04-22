class parameters:
    def __init__(self):
        # General Economic Parameters
        self.discount_rate = 0.04
        
        # Travel Time Parameters
        self.WageStatewide = 37.00  # Statewide Average Hourly Wage ($/hr)
        self.WageTruck = 25.66  # Truck Average Hourly Wage ($/hr)
        self.FringeTruck = 12.76  # Truck Benefits and Costs ($/hr)
        self.ValTimeOVFactor = 2  # Out-of-Vehicle Travel (times)
        self.ValTimeIMFactor = 3  # Incident-Related Travel (times)
        self.TTUprater = 0.0 / 100  # Travel Time Uprater (annual increase in percentage)
        
        # Accident Cost Parameters
        self.FatValue = 10436547  # Cost of a Fatality ($/event)
        self.InjAValue = 2750899  # Cost of Level A (Severe) Injury ($/event)
        self.InjBValue = 324424  # Cost of Level B (Moderate) Injury ($/event)
        self.InjCValue = 174936  # Cost of Level C (Minor) Injury ($/event)
        self.NoInjValue = 12026  # Cost of Property Damage ($/event)
        self.CATravTrend = 764512  # Freeway Travel Trend in million vehicle-miles (mil veh-mi)
        self.FatCount = 4390  # Number of Fatal Crashes
        self.InjCount = 218217  # Number of Injury Crashes
        self.NoInjCount = 445612  # Number of Property Damage Only (PDO) Crashes
        self.NonFwyAccRate = 0.87	# Statewide non freeway crashes per mil veh-mi

        
        # Vehicle Operating Cost Parameters
        self.FuelPriceAuto = 3.81  # Automobile Fuel Price (regular unleaded) ($/gal)
        self.FuelPriceTruck = 3.87  # Truck Fuel Price (diesel) ($/gal)
        self.SalesTaxGasState = 0.0225  # State Sales Tax (gasoline) (%)
        self.SalesTaxDieselState = 0.13  # State Sales Tax (diesel) (%)
        self.SalesTaxLocal = 0.005  # Average Local Sales Tax (%)
        self.ExciseTaxGasFed = 0.183  # Federal Fuel Excise Tax (gasoline) ($/gal)
        self.ExciseTaxDieselFed = 0.243  # Federal Fuel Excise Tax (diesel) ($/gal)
        self.ExciseTaxGasState = 0.511  # State Fuel Excise Tax (gasoline) ($/gal)
        self.ExciseTaxDieselState = 0.389  # State Fuel Excise Tax (diesel) ($/gal)
        self.NonFuelAuto = 0.356  # Automobile Non-Fuel Cost per Mile ($/mi)
        self.NonFuelTruck = 0.440  # Truck Non-Fuel Cost per Mile ($/mi)
        self.IdleSpeed = 5  # Idling Speed for Operating Costs and Emissions (mph) 
        
        # Highway Operations Parameters
        self.MaxVC = 1.56  # Maximum Volume/Capacity Ratio (unitless)
        self.AnnualFactor = 365  # Days per year (unitless)
        self.roadway_capacity = {
            "Freeway": {"alpha": 0.20, "beta": 10, "capacity_vphpl": 2000, "DepRateFwy": 1800},
            "Expressway": {"alpha": 0.20, "beta": 10, "capacity_vphpl": 2000, "DepRateExp": 1800},
            "Conventional Highway": {"alpha": 0.05, "beta": 10, "capacity_vphpl": 800, "DepRateConv": 1400},
            "HOV Lanes": {"HOVAlpha": 0.55, "HOVBeta": 8, "HOVLaneCap": 1600, "departure_rate_vphpl": None}  # HOV has no departure rate
        }
        
        self.roadway_capacity_non_HOV = {
            "Non-HOV Lanes": {
                "No Build": {"GenAlphaNB": 0.20, "GenBetaNB": 10, "GenLaneCapNB": 2000},
                "Build": {"GenAlphaB": 0.20, "GenBetaB": 10, "GenLaneCapB": 2000}
            }
        }
        

        # Active Transportation Parameters
        self.CycleDays = 365  # days  # Number of days cycling is done in a year
        self.WalkDays = 365  # days  # Number of days walking is done in a year
        self.SchDays = 180  # days  # Number of school days in a year
        self.VehSpeed = 25  # mph  # Average vehicle speed (miles per hour)
        self.VehOcc = 1.51  # persons / veh  # Average vehicle occupancy (persons per vehicle)
        self.CycSpeed = 8.70  # mph  # Average cycling speed (miles per hour)
        self.PedSpeed = 3.30  # mph  # Average walking speed (miles per hour)
        self.RTCycNB = 2.23  # trips  # Number of unlinked cycling trips made per day
        self.RTPedNB = 2.10  # trips  # Number of unlinked pedestrian trips made per day
        self.DivCycAutoNB = 0.50  # assumption (50%)  # Percentage of cyclists diverted from personal vehicles
        self.DivPedAutoNB = 0.50  # assumption (50%)  # Percentage of pedestrians diverted from personal vehicles
        self.ValTimeAT = 16.45  # $/hr/per adult  # The value of time for adults when using active transportation ($/hour per adult)
        self.ValTimeChild = 16.45  # $/hr/per child  # The value of time for children when using active transportation ($/hour per child)
        self.CLASS1MRS = 0.57  # Unitless  # Class I facility quality preference factor
        self.CLASS2MRS = 0.49  # Unitless  # Class II facility quality preference factor
        self.CLASS3MRS = 0.92  # Unitless  # Class III facility quality preference factor
        self.CLASS4MRS = 0.49  # Unitless  # Class IV facility quality preference factor (assumed same as Class II)
        self.StreetLightingValue = 0.110  # $/mi  # Value for street lighting per mile of walking path ($/mile)
        self.CurbLevelValue = 0.078  # $/mi  # Value for curb level (smoothness) per mile of walking path ($/mile)
        self.CrowdingValue = 0.055  # $/mi  # Value for crowding per mile of walking path ($/mile)
        self.PavementEvennessValue = 0.026  # $/mi  # Value for pavement evenness per mile of walking path ($/mile)
        self.InformationPanelsValue = 0.026  # $/mi  # Value for information panels along walking paths ($/mile)
        self.BenchesValue = 0.017  # $/mi  # Value for benches along walking paths ($/mile)
        self.DirectionalSignageValue = 0.017  # $/mi  # Value for directional signage along walking paths ($/mile)
        self.AnnSickDays = 3.50  # days/yr  # Average number of sick days employees take per year
        self.PerSickDaysLeave = 0.66  # %  # Percentage of sick days covered by short-term sick leave
        self.PerSickDaysRed = 0.06  # %  # Percentage reduction in sick days when active at least 30 minutes per day
        self.PerCycRiskRed = 0.045  # 4.5% reduction per 365 annual cycling miles  # Percentage reduction in mortality due to cycling
        self.PerPedRiskRed = 0.09  # 9.0% reduction per 365 annual walking miles  # Percentage reduction in mortality due to walking
        self.MortRateCyc = 252  # #/100,000 people  # Mortality rate for cycling (aged 20-64)
        self.MortRatePed = 392  # #/100,000 people  # Mortality rate for walking (aged 20-74)
        
        #Pavement Parameters
        # Pavement Condition Lookup Table (PaveDet) 
        self.pave_det = {
            0: {"Year20Light": 125, "Year20Medium": 150, "Year20Heavy": 350},
            25: {"Year20Light": 150, "Year20Medium": 200, "Year20Heavy": 500},
            50: {"Year20Light": 175, "Year20Medium": 250, "Year20Heavy": 675},
            75: {"Year20Light": 200, "Year20Medium": 300, "Year20Heavy": 750},
            100: {"Year20Light": 275, "Year20Medium": 400, "Year20Heavy": 750},
            125: {"Year20Light": 325, "Year20Medium": 475, "Year20Heavy": 750},
            150: {"Year20Light": 400, "Year20Medium": 575, "Year20Heavy": 750},
            175: {"Year20Light": 500, "Year20Medium": 700, "Year20Heavy": 750},
            200: {"Year20Light": 575, "Year20Medium": 750, "Year20Heavy": 750},
            225: {"Year20Light": 650, "Year20Medium": 750, "Year20Heavy": 750},
            250: {"Year20Light": 750, "Year20Medium": 750, "Year20Heavy": 750},
            275: {"Year20Light": 750, "Year20Medium": 750, "Year20Heavy": 750},
            300: {"Year20Light": 750, "Year20Medium": 750, "Year20Heavy": 750},
            325: {"Year20Light": 750, "Year20Medium": 750, "Year20Heavy": 750},
            350: {"Year20Light": 750, "Year20Medium": 750, "Year20Heavy": 750},
            375: {"Year20Light": 750, "Year20Medium": 750, "Year20Heavy": 750},
            400: {"Year20Light": 750, "Year20Medium": 750, "Year20Heavy": 750},
            425: {"Year20Light": 750, "Year20Medium": 750, "Year20Heavy": 750},
            450: {"Year20Light": 750, "Year20Medium": 750, "Year20Heavy": 750}
        }


#Parameter that needs further Calculations 
        # Calculate all the values once during initialization
        self.value_of_time_automobile = round(self.WageStatewide * 0.5 / 5, 2) * 5
        self.value_of_time_truck = round((self.WageTruck + self.FringeTruck) / 5, 2) * 5
        self.value_of_time_auto_and_truck_composite = round(
            (1.3 * self.value_of_time_automobile * 0.91 + self.value_of_time_truck * 0.09) / 5, 2
        ) * 5
        self.value_of_time_transit = round(self.WageStatewide * 0.5 / 5, 2) * 5
        self.fatality_crash_rate = round(self.FatCount / self.CATravTrend, 3)
        self.injury_crash_rate = round(self.InjCount / self.CATravTrend, 3)
        self.pdo_crash_rate = round(self.NoInjCount / self.CATravTrend, 3)
        self.fuel_auto = round((self.FuelPriceAuto / (1 + self.SalesTaxGasState + self.SalesTaxLocal) - 
                               self.ExciseTaxGasFed - self.ExciseTaxGasState) / 5, 2) * 5
        self.fuel_truck = round((self.FuelPriceTruck / (1 + self.SalesTaxDieselState) - 
                                 self.ExciseTaxDieselFed - self.ExciseTaxDieselState) / 5, 2) * 5
        self.per_peak_avg_hr = 0.081 
        self.per_peak_adt = 0.403 

        self.TMSLookup = "NoAdj"
        self.UserAdjInputs = "False"
        
<<<<<<< HEAD
        self.SpeedWeaveAdj = {
            0.000: {"Freeway": 1.000, "HOV": 1.000},
            0.002: {"Freeway": 0.982, "HOV": 0.988},
            0.004: {"Freeway": 0.964, "HOV": 0.976},
            0.006: {"Freeway": 0.945, "HOV": 0.964},
            0.008: {"Freeway": 0.927, "HOV": 0.952},
            0.010: {"Freeway": 0.909, "HOV": 0.939},
            0.012: {"Freeway": 0.891, "HOV": 0.927},
            0.014: {"Freeway": 0.873, "HOV": 0.915},
            0.016: {"Freeway": 0.855, "HOV": 0.903},
            0.018: {"Freeway": 0.836, "HOV": 0.891},
            0.020: {"Freeway": 0.789, "HOV": 0.879},
            0.022: {"Freeway": 0.747, "HOV": 0.867},
            0.024: {"Freeway": 0.706, "HOV": 0.855},
            0.026: {"Freeway": 0.664, "HOV": 0.842},
            0.028: {"Freeway": 0.623, "HOV": 0.817},
            0.030: {"Freeway": 0.581, "HOV": 0.789},
            0.032: {"Freeway": 0.540, "HOV": 0.761},
            0.034: {"Freeway": 0.498, "HOV": 0.734},
            0.036: {"Freeway": 0.476, "HOV": 0.706},
            0.038: {"Freeway": 0.473, "HOV": 0.678},
            0.040: {"Freeway": 0.471, "HOV": 0.650},
            0.042: {"Freeway": 0.468, "HOV": 0.623},
            0.044: {"Freeway": 0.466, "HOV": 0.595},
            0.046: {"Freeway": 0.463, "HOV": 0.567},
            0.048: {"Freeway": 0.460, "HOV": 0.540},
            0.050: {"Freeway": 0.458, "HOV": 0.512},
            0.052: {"Freeway": 0.455, "HOV": 0.484},
            0.054: {"Freeway": 0.453, "HOV": 0.476},
            0.056: {"Freeway": 0.453, "HOV": 0.474},
            0.058: {"Freeway": 0.453, "HOV": 0.473},
            0.060: {"Freeway": 0.453, "HOV": 0.471},
            0.062: {"Freeway": 0.453, "HOV": 0.469},
            0.064: {"Freeway": 0.453, "HOV": 0.467},
            0.066: {"Freeway": 0.453, "HOV": 0.466},
            0.068: {"Freeway": 0.453, "HOV": 0.464},
            0.070: {"Freeway": 0.453, "HOV": 0.462},
            0.072: {"Freeway": 0.453, "HOV": 0.460},
            0.074: {"Freeway": 0.453, "HOV": 0.459},
            0.076: {"Freeway": 0.453, "HOV": 0.457},
            0.078: {"Freeway": 0.453, "HOV": 0.455},
            0.080: {"Freeway": 0.453, "HOV": 0.453}
        }

        
=======
>>>>>>> 3ce506f0b22b27317d6525ffa8fe8b5e58771617
        #TMS Parameters
        self.tms_adj = {
            "AMoth": {"SpeedWithout": 1.02, "VolumeWithout": 0.95, "SpeedWith": 1.02, "VolumeWith": 0.95, "TT": -5.05, "VOC": 12.81, "Em": 1.37, "Benefit": 0.74},
            "AMsev": {"SpeedWithout": 1.53, "VolumeWithout": 0.94, "SpeedWith": 1.53, "VolumeWith": 0.94, "TT": 1.21, "VOC": 1.38, "Em": -0.37, "Benefit": 1.00},
            "IMoth": {"SpeedWithout": 0.88, "VolumeWithout": 1.18, "SpeedWith": 0.98, "VolumeWith": 0.96, "TT": 0.51, "VOC": 0.15, "Em": 0.06, "Benefit": 0.74},
            "IMsev": {"SpeedWithout": 1.01, "VolumeWithout": 0.97, "SpeedWith": 1.01, "VolumeWith": 0.95, "TT": 0.30, "VOC": 0.31, "Em": 0.30, "Benefit": 1.00},
            "NoAdj": {"SpeedWithout": 1.00, "VolumeWithout": 1.00, "SpeedWith": 1.00, "VolumeWith": 1.00, "TT": 0.00, "VOC": 0.00, "Em": 0.00, "Benefit": 1.00},
            "ORoth": {"SpeedWithout": 0.98, "VolumeWithout": 1.03, "SpeedWith": 1.00, "VolumeWith": 1.00, "TT": -0.07, "VOC": -0.03, "Em": -0.07, "Benefit": 0.00},
            "ORsev": {"SpeedWithout": 0.95, "VolumeWithout": 1.03, "SpeedWith": 1.00, "VolumeWith": 1.00, "TT": 0.00, "VOC": 0.00, "Em": 5.67, "Benefit": 0.00},
            "RMoth": {"SpeedWithout": 1.00, "VolumeWithout": 1.00, "SpeedWith": 1.03, "VolumeWith": 0.97, "TT": -0.07, "VOC": -0.03, "Em": -0.07, "Benefit": 1.00},
            "RMsev": {"SpeedWithout": 1.00, "VolumeWithout": 1.00, "SpeedWith": 1.05, "VolumeWith": 0.97, "TT": 0.00, "VOC": 0.00, "Em": 5.67, "Benefit": 1.00},
            "TIoth": {"SpeedWithout": 1.00, "VolumeWithout": 1.00, "SpeedWith": 1.02, "VolumeWith": 0.97, "TT": -0.11, "VOC": -0.12, "Em": -0.35, "Benefit": 1.00},
            "TIsev": {"SpeedWithout": 1.00, "VolumeWithout": 1.00, "SpeedWith": 1.01, "VolumeWith": 0.97, "TT": -0.39, "VOC": -0.39, "Em": -0.35, "Benefit": 1.00},
        }
<<<<<<< HEAD


        self.SpeedPavAdj = {
            0: {"Auto": 1.000, "Truck": 1.025},
            25: {"Auto": 1.000, "Truck": 1.025},
            50: {"Auto": 1.000, "Truck": 1.025},
            75: {"Auto": 1.000, "Truck": 1.025},
            100: {"Auto": 1.000, "Truck": 1.025},
            125: {"Auto": 1.000, "Truck": 1.025},
            150: {"Auto": 1.000, "Truck": 1.013},
            175: {"Auto": 1.000, "Truck": 1.000},
            200: {"Auto": 1.000, "Truck": 0.980},
            225: {"Auto": 1.000, "Truck": 0.949},
            250: {"Auto": 1.000, "Truck": 0.919},
            275: {"Auto": 0.991, "Truck": 0.890},
            300: {"Auto": 0.981, "Truck": 0.862},
            325: {"Auto": 0.971, "Truck": 0.834},
            350: {"Auto": 0.961, "Truck": 0.808},
            375: {"Auto": 0.952, "Truck": 0.782},
            400: {"Auto": 0.942, "Truck": 0.758},
            425: {"Auto": 0.932, "Truck": 0.734},
            450: {"Auto": 0.923, "Truck": 0.709}
        }
        
        self.transit_savings = {
            "Transit Vehicle Location (AVL)": {"AVLTTsaving": 0.15, "AVLCapSaving": 0.02, "AvlOMsaving": 0.08},
            "Transit Vehicle Signal Priority": {"SigTTsaving": 0.10},
            "Bus Rapid Transit (BRT)": {"BrtTTsaving": 0.29},
        }
=======
>>>>>>> 3ce506f0b22b27317d6525ffa8fe8b5e58771617
