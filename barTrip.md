```python
import requests
import json

API_KEY= "EMPTY"
baseURL = "https://www.googleapis.com/qpxExpress/v1/trips/search?key="
URL = baseURL + API_KEY
print(URL)


flight = json.dumps({
  "request": {
    "slice": [
      {
        "origin": "JFK",
        "destination": "OLB",
        "date": "2017-07-28",
        "preferredCabin": "COACH",
        "permittedDepartureTime": {
          "earliestTime": "15:30",
          "latestTime": "23:59"
        }
      }
    ],
    "passengers": {
      "adultCount": 1,
      "infantInLapCount": 0,
      "infantInSeatCount": 0,
      "childCount": 0,
      "seniorCount": 0
    },
    "solutions": 20,
    "refundable": False
  }
})
header = {'Content-Type': 'application/json'}
response = requests.post(URL, data = flight, headers=header)
print(response.text)
```
