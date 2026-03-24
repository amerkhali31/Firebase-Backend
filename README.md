Each directory under the Firebase directory represents a different firebase project.
Not yet used for firebase functions. For now, just CRUD on different databases.
Each directoryhas its own credentials json file that its respective main.py file will reference to connect the database.

# Top Level
- Project for MAGR
- Project for Dokkan
- General that contains generic firebase boilerplate

# MAGR
TO RUN:
1. download yearly prayer time pdf from islamicfinder. Grab the full year, not 12 individual months.
2. change the name of the downloads to be prayers_YEAR.pdf where YEAR is just YYYY of the year you are downloading for
3. in main.py, update the start and end date for clearing old prayer times and update the year variable to match YEAR
4. run source .venv/bin/activate
5. run python MAGR/src/main.py
6. Firebase should be the top level directory working out of

- Used to CRUD on the yearly prayer times
- https://www.islamicfinder.org/world/united-states/4907959/rockford-prayer-times/ is where prayer times come from