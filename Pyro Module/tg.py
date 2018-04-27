
from __future__ import print_function

import math
import numpy as np

import mesh.patch as patch
from util import msg

def init_data(my_data, rp):
    """ initialize the incompressible Taylor-Green flow problem """

    msg.bold("initializing the incompressible Taylor-Green flow problem...")

    # make sure that we are passed a valid patch object
    if not isinstance(my_data, patch.CellCenterData2d):
        print(my_data.__class__)
        msg.fail("ERROR: patch invalid in tg.py")

    # get the velocities
    u = my_data.get_var("x-velocity")
    v = my_data.get_var("y-velocity")

    myg = my_data.grid

    if (myg.xmin != 0 or myg.xmax != 1 or
        myg.ymin != 0 or myg.ymax != 1):
        msg.fail("ERROR: domain should be a unit square")

    y_half = 0.5*(myg.ymin + myg.ymax)

    idx = myg.y2d <= myg.ymin + .02
    
    u[idx] = np.sin(2.0*math.pi*myg.x2d[idx])*np.cos(2.0*math.pi*myg.y2d[idx])

    v[:, :] = -np.cos(2.0*math.pi*myg.y2d)*np.sin(2.0*math.pi*myg.x2d)

def finalize():
    """ print out any information to the user at the end of the run """
pass
