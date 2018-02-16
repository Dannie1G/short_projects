

# Launches a map in the browser using an address from the
# command line or user input.

import webbrowser, sys


if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])

else:
    # Get address from user.
    address = input('What is the address?')

    
webbrowser.open('https://www.google.com/maps/place/' + address)

# TODO: Get address from clipboard.
