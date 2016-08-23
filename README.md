# ical_dict

iCalDict is a Python library that converts a Calendar file (.ics) into a Dictionary object in Python.

### Usage

```python
# Import Library
from ical_dict import iCalDict

# Define optional key mapping
mapping = {
    "DTSTAMP":                              "dt_stamp",
    "DTSTART;TZID=America/New_York":        "dt_start",
    "DTEND;TZID=America/New_York":          "dt_end",
    ...
}

# Local File
file_name = 'events.ics'
converter = iCalDict(file_name, mapping)
print json.dumps(converter.convert())

# URL
url = 'http://25livepub.collegenet.com/calendars/NJIT_EVENTS.ics'
converter = iCalDict(url, mapping)
print json.dumps(converter.convert())
```

The constructor signature for `iCalDict` is as follows:

```python
def __init__(self, ics_file, mapping = {})
	...
```

Thus, `mapping` is an entirely optional value that converts your `.ics` file's keys into preferred keys.

### Example
The examples in the Usage section refer to the `events.ics` file in this repository. A sample output in JSON format is available in the `events.json` file in this repository. 

### TODO
All open items will be tracked via Issues. Have an enhancement idea, recognize a bug or want to contribute? Check out all of the Open Issues!

### LICENSE
MIT License
