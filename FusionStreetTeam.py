# Author-Patrick Rainsberry
# Description-Application to help customers access Fusion Street Team Information


from .FusionStreetTeamCommand import FusionStreetTeamCommand


commands = []
cmd_definitions = []


# Define parameters for 1st command
cmd = {
    'cmd_name': 'Fusion Success Team Progression',
    'cmd_description': 'Fusion Success Team Progression',
    'cmd_id': 'cmdID_FT_Progression',
    'url': 'https://slack-files.com/T02NW42JD-F3ZRZB83Z-3cf6371435',
    'cmd_resources': './resources',
    'workspace': 'FusionSolidEnvironment',
    'toolbar_panel_id': 'SolidScriptsAddinsPanel',
    'add_to_drop_down': True,
    'drop_down_cmd_id': 'cmdID_FT_Drop',
    'drop_down_resources': './resources',
    'drop_down_name': 'Fusion Street Team',
    'is_promoted': True,
    'class': FusionStreetTeamCommand
}

cmd_definitions.append(cmd)

# Define parameters for 2nd command
cmd = {
    'cmd_name': 'Fusion Success Team Calendar',
    'cmd_description': 'Fusion Success Team Calendar',
    'url': 'https://calendly.com/street-team-members',
    'cmd_id': 'cmdID_FT_Calendar',
    'cmd_resources': './resources',
    'workspace': 'FusionSolidEnvironment',
    'toolbar_panel_id': 'SolidScriptsAddinsPanel',
    'add_to_drop_down': True,
    'drop_down_cmd_id': 'cmdID_FT_Drop',
    'drop_down_resources': './resources',
    'drop_down_name': 'Fusion Street Team',
    'is_promoted': True,

    'class': FusionStreetTeamCommand
}

cmd_definitions.append(cmd)

# Set to True to display various useful messages when debugging your app
debug = False


# Don't change anything below here:
for cmd_def in cmd_definitions:
    command = cmd_def['class'](cmd_def, debug)
    commands.append(command)


def run(context):
    for run_command in commands:
        run_command.on_run()


def stop(context):
    for stop_command in commands:
        stop_command.on_stop()
