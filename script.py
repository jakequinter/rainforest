import requests


def follow_url(url):
    while True:
        response = requests.get(url, headers={"Accept": "application/json"})
        data = response.json()

        if "message" in data and data["message"] == "This is not the end":
            print(f"Following URL: {data['follow']}")
            url = data["follow"]
        else:
            print("End of the sequence or different message encountered.")
            print(data)
            break


# Initial URL
initial_url = "https://www.letsrevolutionizetesting.com/challenge?id=756775492"
follow_url(initial_url)
