import numpy as np

def assign_positioner(SinglePositioner, Targets):
    """
    Finds a target to assign to a positioner.

    Args:
        SinglePositioner (Positioner class object): central positioner 
             considered for the assignemtn.
        Targets (TargetTile class object): target information about all the 
             targets  in a given tile.
    Returns:
        [x_on_target, y_on_target]


    Note:
         Right now this version does not take into account:
         - Different priorities among different targets.
         - Information on previous observation of the Targets
         - Information about neighboring positioners (to check for collisions)
    """
    x_on_target = 0.0
    y_on_target = 0.0

    x_pos = SinglePositioner.offset_x
    y_pos = SinglePositioner.offset_y
    
    patrol_radius = SinglePositioner.R1 + SinglePositioner.R2


    distance = np.sqrt((Targets.x - x_pos)**2 + (Targets.x - y_pos )**2)
    reachable = np.where((distance < patrol_radius) & (Targets.fiber_id == -1))
    reachable = reachable[0]

    n_reachable = np.size(reachable)
    if (n_reachable):
        x_on_target = Targets.x[reachable[0]]
        y_on_target = Targets.y[reachable[0]]
        SinglePositioner.set_target(reachable[0])
        Targets.fiber_id[reachable[0]] = SinglePositioner.id
    else:
        x_on_target = x_pos
        y_on_target = y_pos

    SinglePositioner.set_available(reachable)
    
    return [x_on_target, y_on_target]
