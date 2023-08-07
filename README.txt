Create a web-based music library for music directors to store 
title/composer/ensemble/performance dates
of purchased music selections for their ensemble.

TODO
    X- Create functionality of adding/searching new files

    X- For now, save to SQLite DB, if/when deployed use online subsciption DB

    X- Create HTML pages for adding/searching and search results for 
        every parameter
    X - Add functionality to edit files previously entered

    - Add functionality to accept searches that may not be capitalized
        and/or different date format
        X- DATE format in SQL? On webpage entry line
        - Include multiple dates saved so director can keep record?

    - Create registration page, add html registration page as homepage
        - Create a separate database that holds username/password for each user
        - Hash the password? Unhash/Compare on re-entry

    - Add CSS, images, make the whole thing look better

    X- Correct date search and input function so it only accepts MM/DD/YYYY

    X - Return multiple files if more than one matches search parameter


Create registration/login pages for music library

TODO
    Login
    X HTML for login page
    - When user inputs username/password, check against stored users in database
        - If user exists, send user to main.py for music_library
        - If user does not exist, send to registration page
    
    Registration
    X HTML for registration page
    - Input from user: username/password stored to 'registered_users' database
    - Hash the password when saving to database

When done with all this, integrate into the music_library code/templates folders

