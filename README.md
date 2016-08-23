# ical_dict

iCalDict is a Python library that converts a Calendar file (.ics) into a Dictionary object in Python.

### Usage

```python
# Import Library
from ical_dict import iCalDict

# Local File
converter = iCalDict('events.ics')
print json.dumps(converter.convert())

# URL
converter = iCalDict('http://25livepub.collegenet.com/calendars/NJIT_EVENTS.ics')
print json.dumps(converter.convert())
```

### Example
The examples in the Usage section refer to the `events.ics` file in this repository. A sample output in JSON format is available in the `events.json` file in this repository. 

### TODO
All open items will be tracked via Issues. Have an enhancement idea, recognize a bug or want to contribute? Check out all of the Open Issues!

### LICENSE
MIT License
