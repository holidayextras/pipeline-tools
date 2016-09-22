### Pipeline Tools

The data pipeline project needs to distribute python tools across all its projects.
A simple solution is to create a tools package to be able to install into any project
by simply adding it into a requirements.txt file.

## Current tools
    - #Logging
    Be able to pass configs into this tool and instantiate a logger class with
    all the setup already taken care of