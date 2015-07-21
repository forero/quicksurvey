"""
A toolkit for simulating a survey with  multi-object spectrographs.
"""

__version__ = "0.1.dev1"

def version():
    """Return a version including a git revision string"""
    import os
    from os.path import dirname
    import subprocess
    
    gitdir = dirname(dirname(dirname(__file__)))+'/.git'
    os.environ['GIT_DIR'] = gitdir
    cmd = 'git rev-parse --short=6 HEAD'
    try:
        ver = subprocess.check_output(cmd.split())
        return __version__+'-'+ver.strip()
    except:
        return __version__

