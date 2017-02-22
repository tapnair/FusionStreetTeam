__author__ = 'rainsbp'

import adsk.core
import adsk.fusion
import traceback

from .Fusion360Utilities import Fusion360Utilities as futil
from .Fusion360Utilities.Fusion360Utilities import get_app_objects
from .Fusion360Utilities.Fusion360CommandBase import Fusion360CommandBase


# Main class for import command
class SlicerImportCommand(Fusion360CommandBase):

    # Executed on user pressing OK button
    def on_execute(self, command, command_inputs, args, input_values):
        pass

# Define the user interface for the command
    def on_create(self, command, command_inputs):
        pass