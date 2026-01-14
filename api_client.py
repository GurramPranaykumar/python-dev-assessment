import requests

def fetch_and_display_users(num_users):
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/users")
        response.raise_for_status()  # Raises an error if status is not 200

        users = response.json()

        if not isinstance(users, list):
            print("Unexpected JSON structure")
            return None

        for user in users[:num_users]:
            try:
                name = user["name"]
                email = user["email"]
                city = user["address"]["city"]
                print(f"Name: {name}\nEmail: {email}\nCity: {city}\n")
            except KeyError:
                print("Missing data in user entry. Skipping...\n")

    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return None
    except ValueError:
        print("Invalid JSON response")
        return None


# Example test calls
fetch_and_display_users(3)
fetch_and_display_users(15)