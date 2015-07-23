import numpy as np

def find_available_targets(Fibers, Targets):
    """
    Finds the IDs of the targets available to each fiber

    Args:
        Fibers (FocalPlaneFibers class object): fiber information
        Targets (TargetTile class object): target information about all the 
             targets  in a given tile.
    Returns:
         Updates the .available_targets and .n_targets fields for each Fiber.
    Note:
    """

    for i in range(Fibers.n_fiber):
        x_pos = Fibers.x_focal[i]
        y_pos = Fibers.y_focal[i]
    
        patrol_radius = Fibers.positioner.R1 + Fibers.positioner.R2

        distance = np.sqrt((Targets.x - x_pos)**2 + (Targets.y - y_pos )**2)
        reachable = np.where(distance < patrol_radius)
        reachable = reachable[0]

        n_reachable = np.size(reachable)
        if(n_reachable>0):
            # The id's are sorted in increasing distance from fiber
            sort_id  = distance[reachable].argsort()
            Fibers.set_available(i, reachable[sort_id])
        else:
            Fibers.reset_available(i)            
    return 


def select_target(Fibers, Targets):
    """
    Using the information of available targets from a fiber, 
    sets the ID to be targetted.

    Args:
         Fibers (FocalPlaneFibers class object): fiber information
         Targets (TargetTile class object): target information about all the 
             targets  in a given tile.
    
    Returns:
         Updates the .target field for each Fiber.

    Note:
        - We do not use the information on different kinds of targets
        - We do not use any priority information
        - We do not chec for positioner collision
    """

    for i in range(Fibers.n_fiber):
        if(Fibers.n_targets[i]>0):
            target_array = Fibers.available_targets[i]
            target = target_array[0]
            Fibers.set_target(i, target)        
    return 
