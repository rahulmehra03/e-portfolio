import requests
from twilio.rest import Client

# Twilio credentials
TWILIO_SID = 'AC23c2198f7a07fafed659375c8cf92ed9'
TWILIO_AUTH_TOKEN = 'd7048ca21aa9d76e6cd5d4438074752c'
TWILIO_PHONE_NUMBER = 'your_twilio_phone_number'
YOUR_PHONE_NUMBER = '07494423331'

# Ambee API details
AMBE_API_KEY = '2aa51da911fe9616cc78a459d247ca5bc7cb183df78989ae5a833a4df7c3aa29'
LATITUDE = '53.3638'  # Latitude for Widnes, England
LONGITUDE = '-2.7286'  # Longitude for Widnes, England

# Define high pollen count threshold
HIGH_POLLEN_THRESHOLD = 1

def get_pollen_count():
    url = f'https://api.ambeedata.com/latest/pollen/by-lat-lng?lat={LATITUDE}&lng={LONGITUDE}'
    headers = {
        'x-api-key': AMBE_API_KEY,
        'Content-type': 'application/json'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(data)  # Print the entire response to inspect its structure
        pollen_count = data['data'][0]['Count']
        return pollen_count
    else:
        print(f"Error: Unable to fetch data. Status code: {response.status_code}")
        return None

def send_alert(pollen_count):
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=f"The pollen count is {pollen_count} today Rahul. Take your medicine.",
        from_=TWILIO_PHONE_NUMBER,
        to=YOUR_PHONE_NUMBER
    )
    print(f"Alert sent: {message.sid}")

def send_alert2(pollen_count):
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=f"The pollen count is {pollen_count} today Rahul . You should be fine :)",
        from_=TWILIO_PHONE_NUMBER,
        to=YOUR_PHONE_NUMBER
    )
    print(f"Alert sent: {message.sid}")

def main():
    pollen_count = get_pollen_count()
    if pollen_count is not None:
        if pollen_count > HIGH_POLLEN_THRESHOLD:
            send_alert(pollen_count)
        else:
            send_alert2(pollen_count)

if __name__ == "__main__":
    main()
