#Author-Patrick Rainsberry
#Description-Application to help customers access Fusion Street Team Information

# Author-Patrick Rainsberry
# Description-testing top down workflow


from .TopDownProtoCommand import TopDownProtoCommand, TopDownProtoCommand2, TopDownProtoCommand3


commands = []
cmd_definitions = []


# Define parameters for 1st command #####
cmd = {
    'cmd_name': 'Create Component',
    'cmd_description': 'Testing Top Down Workflow',
    'cmd_resources': './resources',
    'cmd_id': 'cmdID_Demo_1',
    'workspace': 'FusionSolidEnvironment',
    'toolbar_panel_id': 'SolidScriptsAddinsPanel',
    'class': TopDownProtoCommand
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
