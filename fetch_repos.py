import requests
import json

USERNAME = "Evelinacb"  # Replace if your GitHub username is different

url = f"https://api.github.com/users/{USERNAME}/repos"

response = requests.get(url)
repos = response.json()

projects = []

for repo in repos:
    projects.append({
        "name": repo["name"],
        "description": repo["description"],
        "url": repo["html_url"]
    })

with open("projects.json", "w") as file:
    json.dump(projects, file, indent=4)

print("projects.json updated!")
