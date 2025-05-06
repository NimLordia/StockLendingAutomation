## This is a project to automate a manual, tedious task I have at work.

## It takes a list of customers IDs, and goes one by one, and opens each customer and checks if a certain checkbox is active or not.

# If yes, it unticks it and clicks ok for 2 alert boxes, then closes the client card and goes to the next client, otherwise, it will close the client card and go to the next client

# The user should supply an excel file with a list, and then click start in the GUI and then click on the backoffice window within 2 seconds

# The mouse positioning is automatic because the card is opened on the same place, and the check is for pixel color on a specific place.
# The test module is used to determine mouse location and pixel color in RGB. You can run it and then you have 5 seconds to check a specific location

# You can run pyinstaller --onefile --noconsole --name CheckboxAutomation gui_script.py to create an .exe file with GUI
