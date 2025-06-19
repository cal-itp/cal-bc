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
########################################################################################
########################################################################################
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
    
############################################################################################
############################################################################################

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

    
#################################################################################
#################################################################################
#################################################################################
#################################################################################
""
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
    
    
    
    
    
    
