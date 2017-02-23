__author__ = 'rainsbp'

import webbrowser

from .Fusion360Utilities.Fusion360CommandBase import Fusion360CommandBase


# Main class for import command
class FusionStreetTeamCommand(Fusion360CommandBase):

    def __init__(self, cmd_def, debug):

        super().__init__(cmd_def, debug)

        self.url = cmd_def.get('url', 'http://www.autodesk.com/products/fusion-360/overview')

    # Executed on user pressing OK button
    def on_execute(self, command, command_inputs, args, input_values):

        # Launch web browser using user's default browser
        webbrowser.open(self.url)
