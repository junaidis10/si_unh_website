
import requests
import time

def check_sinta(sinta_id):
    url = f"https://sinta.kemdiktisaintek.go.id/authors/profile/{sinta_id}?view=googlescholar"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    start_time = time.time()
    try:
        print(f"Requesting {url}...")
        response = requests.get(url, headers=headers, timeout=10)
        end_time = time.time()
        print(f"Status Code: {response.status_code}")
        print(f"Time Taken: {end_time - start_time:.2f} seconds")
        if response.status_code == 200:
            print("Content Length:", len(response.text))
            if "ar-list-item" in response.text:
                print("Found ar-list-item in response!")
            else:
                print("ar-list-item NOT found in response.")
        else:
            print("Response text snippet:", response.text[:200])
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_sinta("6020586")
