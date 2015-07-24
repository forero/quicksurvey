import numpy as np
from astropy.io import fits
from quicksurvey import util

def initialize_observation_files(tile_file_list):
    """
    Initializes all the files holding observational results.
    
    Args:
        tile_file_list (string): 1D array of filenames with tile by tile target information.
    Note:
        The outcome will be a set of files, tile by tile, holding the information from observations.
        Being the initialization, all the relevant information is set to the defaul values of the
        TargetsTile class.
    """
    n_tiles = len(tile_file_list)
    if(n_tiles>0):
        for tile_file in tile_file_list:
            target_tile_pack = util.TargetTile(tile_file)                   
            target_tile_pack.write_results_to_file(tile_file)
    return

def sync_observation_files(all_targets):
    """
    Syncs all the files holding observational results to increase the number of observations
    
    Args:
        all_targets (TargetSurvey class object): object summarizing the information for all targets
    """
    print("Starting to write results to files")
    # loop over each target and check whether it hass been assigned to a fiber.
    for i_target in range(all_targets.n_targets):
        for tile_file  in all_targets.tile_names[i_target]:
            results_file = tile_file.replace("Targets_Tile", "Results_Tile")
            f = fits.open(results_file, mode='update')

            tmp_id =  np.int_(f[1].data['TARGETID'])
            tmp_nobs =  f[1].data['NOBS']
            loc = np.where(tmp_id == all_targets.id[i_target])
            if(np.size(loc)!=0):
                tmp_nobs[loc[0]] = tmp_nobs[loc[0]] + 1
                         # TOWRITE: still have to make the update to ASSIGNEDTYPE and ASSIGNEDZ 
            else:
                raise ValueError('The target id %d in tile was not found in local list'%(all_targets.id[i_target]))
                    
            f.flush()
            f.close()
    return

def update_global_targets(all_targets, tile_targets):
    """
    Updates the array holding observational results to increase the number of observations
    
    Args:
        all_targets (TargetSurvey class object): object summarizing the information for all targets
        tile_targets (TargetTile class object): object summarizing the information for targets on a given tile.
    """

    # loop over each target and check whether it hass been assigned to a fiber.
    for i_target in range(tile_targets.n):
        if(tile_targets.fiber[i_target]!=-1):
            loc = np.where(all_targets.id == tile_targets.id[i_target])
            if(np.size(loc)!=0):
                loc = loc[0]
                all_targets.n_observed[loc] = all_targets.n_observed[loc] + 1
                # TOWRITE: still have to make the update to ASSIGNEDTYPE and ASSIGNEDZ 
            else:
                raise ValueError('The target id %d in tile was not found in general target list'%(tile_targets.id[i_target]))
    return


