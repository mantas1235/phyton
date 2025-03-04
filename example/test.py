import requests

def get_photos():
    url = "https://jsonplaceholder.typicode.com/photos"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError if the status is not 200
        photos = response.json()
        return photos
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    photos_data = get_photos()
    if photos_data:
        # Display the first few photo records as an example
        for photo in photos_data[:5]:
            print(photo)