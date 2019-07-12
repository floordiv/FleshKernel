import log
import settings
import memory
import kernel
import threading
from func import broadcast

"""
co-core should handle memory, multi-threading and audit of the system (security subsystem, detects injections and 
rebindings)

how to sync threads? This is the problem of co-core. I think, it should handle all the inputs and outputs. But
idk how to handle two or more inputs at the same time and how to print info from other apps

also the problem is to handle prints - but this is more much easier. I should focus at the problem of handling inputs
"""



