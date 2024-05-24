from flask import Flask, render_template, request
import requests
from datetime import datetime, timedelta, timezone

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_schedule', methods=['POST'])
def get_schedule():

    base_url = f'https://api-v3.mbta.com/'
    api_key = '8023186685c54979aaba087928ff2554'

    if request.form['direction'] == 'outbound':
        #work
        direction_id = 0
        stop = 'place-mgngl'
        destination = 'Work'
    else:
        #home
        direction_id = 1
        stop='place-prmnl'
        destination='Home'
    
    params = {
        "filter[route_type]": 0,
        "filter[stop]": stop,
        "filter[route]": 'Green-E',
        "filter[direction_id]": direction_id,
        "sort" : 'departure_time',
        "api_key": api_key  
    }

    # The meaning of direction_id varies based on the route. You can programmatically get the direction names 
    # from /routes /data/{index}/attributes/direction_names or /routes/{id} /data/attributes/direction_names.

    # Make the API request
    print('Trying API request')
    try:
        response = requests.get(base_url + '/schedules', params=params)
    except:
        return 'Error occurred getting data from API but direction is: ' + request.form['direction']

    if response.status_code == 200:
        train_schedule = response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

    if train_schedule:
        next_trains = []
        
        for train in train_schedule['data']:
            current_time = datetime.now(timezone.utc)
            departure_time = datetime.fromisoformat(train['attributes']['departure_time'])
            time_diff = round((departure_time - current_time).total_seconds() / 60, 0)
            
            if 0 < time_diff < 60:
                print(f'Next train in {time_diff} minutes at {departure_time.strftime("%I:%M %p")}')
                next_trains.append(time_diff)
        
        return render_template('index.html', schedule=next_trains, destination=destination)
    else:
        print("Failed to retrieve train schedule.")


if __name__ == '__main__':
    app.run(debug=True)
