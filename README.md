# capital-time-api

# Capital Time API

Simple falsk based API deployed on GCP that returns the current local time and UTC offset for a given capital city

# Features

- Token-based authentication 
- Returns current time and UTC offset for supported capital cities
- Runs on public IP via GCP VM: public ip - 34.73.94.60

# Example Request 

- Bash: 
curl 'http://<<your-vm-external-ip>/api/time?city=London'   -H 'Authorization: Bearer supersecrettoken123'

- My Public IP
curl 'http://34.73.94.60:5000/api/time?city=Washington'   -H 'Authorization: Bearer supersecrettoken123'


# Output

{
  "city": "Washington",
  "local_time": "2025-04-20 22:07:08",
  "utc_offset": "UTC-04:00"
}

# Supported Cities

    "Washington",
    "London",
    "Tokyo",
    "Paris",
    "Delhi",
    "Canberra"





