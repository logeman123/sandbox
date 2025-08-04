import json
import requests
import time

def get_profile_image(username, api_key):
    """
    Fetch profile image for a Twitter username using twitterapi.io
    """
    url = "https://api.twitterapi.io/twitter/user/info"
    headers = {"X-API-Key": api_key}
    params = {"userName": username}
    
    try:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            # Extract profile image URL from the response
            if 'data' in data and 'profilePicture' in data['data']:
                return data['data']['profilePicture']
        else:
            print(f"Error fetching profile for {username}: {response.status_code}")
    except Exception as e:
        print(f"Exception fetching profile for {username}: {e}")
    
    return None

def convert_batch_format(input_file, output_file):
    """
    Convert the batch data from the current format to the desired format.
    
    Current format:
    {
        "twitter_handle": "username",
        "wallet_address": "address",
        ...
    }
    
    Desired format:
    {
        "twitterUsername": "username",
        "walletAddress": "address",
        "profileImageUri": "image_url"
    }
    """
    TWITTER_API_KEY="83b7557ef3eb4b35b5d4a8a320d45838"
    
    # Read the input file
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    # Convert each record
    converted_data = []
    for i, record in enumerate(data):
        username = record.get("twitter_handle", "")
        wallet_address = record.get("wallet_address", "")
        
        print(f"Processing {i+1}/{len(data)}: {username}")
        
        # Get profile image
        profile_image = get_profile_image(username, TWITTER_API_KEY)
        
        converted_record = {
            "twitterUsername": username,
            "walletAddress": wallet_address,
            "profileImageUri": profile_image
        }
        converted_data.append(converted_record)
        
        # Add a small delay to avoid rate limiting
        time.sleep(0.1)
    
    # Write the converted data to output file
    with open(output_file, 'w') as f:
        json.dump(converted_data, f, indent=2)
    
    print(f"Converted {len(converted_data)} records from {input_file} to {output_file}")

if __name__ == "__main__":
    convert_batch_format("unverified_twitter_batch1.json", "converted_batch_with_images.json") 