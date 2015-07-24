import numpy as np

def find_available_targets(Fibers, TargetsTile):
    """
    Finds the IDs of the targets available to each fiber

    Args:
        Fibers (FocalPlaneFibers class object): fiber information
        TargetsTile (TargetTile class object): target information about all the 
             targets  in a given tile.
    Returns:
         Updates the .available_targets and .n_targets fields for each Fiber.
    Note:
    """

    for i in range(Fibers.n_fiber):
        x_pos = Fibers.x_focal[i]
        y_pos = Fibers.y_focal[i]
    
        patrol_radius = Fibers.positioner.R1 + Fibers.positioner.R2

        distance = np.sqrt((TargetsTile.x - x_pos)**2 + (TargetsTile.y - y_pos )**2)
        reachable = np.where(distance < patrol_radius)
        reachable = reachable[0]

        n_reachable = np.size(reachable)
        if(n_reachable>0):
            # The id's are sorted in increasing distance from fiber
            sort_id  = distance[reachable].argsort()
            Fibers.set_available(i, TargetsTile.id[reachable[sort_id]])
        else:
            Fibers.reset_available(i)            
    return 


def select_target(Fibers, TargetsTile, TargetsSurvey):
    """
    Using the information of available targets from a fiber
    sets the ID to be targetted.

    Args:
         Fibers (FocalPlaneFibers class object): fiber information
         TargetsTile (TargetTile class object): target information about all the 
             targets  in a given tile.
         TargetsSurvey (TargetSurvey class object): target information about the 
             results for all targets in the survey.
    Returns:
         Updates the .target field for each Fiber.
         Updates the .fiber field for each TargetsTile
    Note:
        TOWRITE
        - We do not use the information on different kinds of targets
        - We do not use any priority information
        - We do not check for positioner collision
        - We do not use information from the rest of the survey.
    """

    for i in range(Fibers.n_fiber):
        if(Fibers.n_targets[i]>0):
            target_array = Fibers.available_targets[i]
            target = target_array[0]
            Fibers.set_target(i, target)        
            TargetsTile.set_fiber(target, i)
    return 
