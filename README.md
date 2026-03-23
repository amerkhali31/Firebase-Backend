Each directory under the Firebase directory represents a different firebase project.
Not yet used for firebase functions. For now, just CRUD on different databases.
Each directoryhas its own credentials json file that its respective main.py file will reference to connect the database.

# Top Level
- Project for MAGR
- Project for Dokkan
- General that contains generic firebase boilerplate

# MAGR
- Used to CRUD on the yearly prayer times
- https://www.islamicfinder.org/world/united-states/4907959/rockford-prayer-times/ is where prayer times come from
    - download yearly times
    - use pdf_utils to extract times