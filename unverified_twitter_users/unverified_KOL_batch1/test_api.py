import requests
import json

def test_twitter_api():
    url = "https://api.twitterapi.io/twitter/user/info"
    headers = {"X-API-Key": "83b7557ef3eb4b35b5d4a8a320d45838"}
    params = {"userName": "Cupseyy"}
    
    try:
        response = requests.get(url, headers=headers, params=params)
        print(f"Status Code: {response.status_code}")
        print(f"Response Headers: {response.headers}")
        print(f"Response Text: {response.text}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"JSON Response: {json.dumps(data, indent=2)}")
        else:
            print(f"Error Response: {response.text}")
            
    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    test_twitter_api() 