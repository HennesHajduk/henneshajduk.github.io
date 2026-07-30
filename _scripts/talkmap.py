# Leaflet cluster map of talk locations
#
# Run this from the _talks/ directory, which contains .md files of all your
# talks. This scrapes the location YAML field from each .md file, geolocates it
# with geopy/Nominatim, and uses the getorg library to output data, HTML, and
# Javascript for a standalone cluster map. This is functionally the same as the
# #talkmap Jupyter notebook.
import frontmatter
import glob
import re
import time
import getorg
from geopy import Nominatim
from geopy.exc import GeocoderTimedOut

# Set the default timeout, in seconds
TIMEOUT = 5

# Nominatim's usage policy caps requests at 1/second
RATE_LIMIT_SECONDS = 1

# Collect the Markdown files
g = glob.glob("_talks/*.md")

# Prepare to geolocate
geocoder = Nominatim(user_agent="academicpages.github.io")
location_dict = {}
location = ""
permalink = ""
title = ""


def geocode_with_fallback(query, timeout):
    """Geocode, falling back to a shorter (less specific) query if no match is found."""
    time.sleep(RATE_LIMIT_SECONDS)
    result = geocoder.geocode(query, timeout=timeout)
    if result is None and "," in query:
        return geocode_with_fallback(query.split(",", 1)[1].strip(), timeout)
    return result

# Perform geolocation
for file in g:
    # Read the file
    data = frontmatter.load(file)
    data = data.to_dict()

    # Press on if the location is not present
    if 'location' not in data:
        continue

    # Prepare the description: title, month & year, exact city, and the
    # conference/institute (venue covers both "it was a conference" and
    # "for invited talks, the institute")
    title = data['title'].strip()
    venue = data['venue'].strip()
    location = data['location'].strip()
    city = data.get('city', location.split(',')[0]).strip()
    month_year = data['date'].strftime('%b %Y')
    description = f"<strong>{title}</strong><br>{month_year}<br>{venue}<br>{city}"
    if data.get('online'):
        description += "<br><em>(online)</em>"

    # Strip trailing "(online)"-style annotations before geocoding
    geocode_query = re.sub(r"\s*\([^)]*\)\s*$", "", location)

    # Geocode the location and report the status
    try:
        result = geocode_with_fallback(geocode_query, TIMEOUT)
        if result is None:
            print(f"Warning: no geocode match found for {geocode_query}, skipping pin")
            continue
        location_dict[description] = result
        print(description, result)
    except ValueError as ex:
        print(f"Error: geocode failed on input {geocode_query} with message {ex}")
    except GeocoderTimedOut as ex:
        print(f"Error: geocode timed out on input {geocode_query} with message {ex}")
    except Exception as ex:
        print(f"An unhandled exception occurred while processing input {geocode_query} with message {ex}")

# Save the map
m = getorg.orgmap.create_map_obj()
getorg.orgmap.output_html_cluster_map(location_dict, folder_name="_talkmap", hashed_usernames=False)
