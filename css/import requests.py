import requests

def finestFoodOutlet(city, votes):
    base_url = "https://jsonmock.hackerrank.com/api/food_outlets?"
    query = f"city={city}"
    
    results = []
    
    page = 1
    while True:
        url = f"{base_url}{query}&page={page}"
        response = requests.get(url)
        data = response.json()
        
        if "data" in data:
            results += data["data"]
        
        if page >= data["total_pages"]:
            break
        
        page += 1
    
    # Filter outlets with votes greater than or equal to the required minimum votes
    filtered_outlets = [outlet for outlet in results if outlet["user_rating"]["votes"] >= votes]
    
    # Find the finest food outlet with the highest rating and maximum vote count
    finest_outlet = max(filtered_outlets, key=lambda x: (x["user_rating"]["average_rating"], x["user_rating"]["votes"]))
    
    return finest_outlet["name"]

# Taking input from the user
city = input()
votes = int(input())

# Call the function and print the result
result = finestFoodOutlet(city, votes)
print(result)