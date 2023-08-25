import requests


# Usage example
owner = "BestFriend-Sweet"
repo = "gpt4all-large1"
branch = "main"
# path = ""


def get_file_list_from_github(owner, repo, path):
    api_url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"

    response = requests.get(api_url)
    response.raise_for_status()

    file_list = []
    for item in response.json():
        if item["type"] == "file":
            file_list.append(item["name"])

    return file_list


def download_file_from_github(owner, repo, branch, path):
    raw_url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{path}"

    file_response = requests.get(raw_url)
    file_response.raise_for_status()

    with open(path, "wb") as file:
        file.write(file_response.content)


file_list = get_file_list_from_github(owner, repo, "")


ind1 = int(input('Index1: '))
ind2 = int(input('Index2: '))

for path in file_list[ind1-1:ind2]:
    download_file_from_github(owner, repo, branch, path)
