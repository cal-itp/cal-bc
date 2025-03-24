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
            "Freeway": {"alpha": 0.20, "beta": 10, "capacity_vphpl": 2000, "departure_rate_vphpl": 1800},
            "Expressway": {"alpha": 0.20, "beta": 10, "capacity_vphpl": 2000, "departure_rate_vphpl": 1800},
            "Conventional Highway": {"alpha": 0.05, "beta": 10, "capacity_vphpl": 800, "departure_rate_vphpl": 1400},
            "HOV Lanes": {"alpha": 0.55, "beta": 8, "capacity_vphpl": 1600, "departure_rate_vphpl": None}  # HOV has no departure rate
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

    