import requests

def getReposAndCommits(user):
    result = {}
    getrepos_url = "https://api.github.com/users/" + user + "/repos"
    repos_resp = requests.get(getrepos_url)
    repos = repos_resp.json()
    
    for repo in repos:
        repo_name = repo['name']
        getcommits_url = "https://api.github.com/repos/" + user + "/" + repo_name + "/commits"
        commits_resp = requests.get(getcommits_url)
        commits = commits_resp.json()
        num_commit = len(commits)
        result[repo_name] = num_commit
        print(f"Repo: {repo_name} Number of commits: {num_commit}")
    return result
