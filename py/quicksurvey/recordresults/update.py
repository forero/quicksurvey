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

