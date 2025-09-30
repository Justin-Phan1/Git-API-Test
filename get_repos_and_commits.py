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

        commit_count = len(commits)
        result[repo_name] = commit_count
        
        print(f"Repo: {repo_name} Number of commits: {commit_count}")
        
    return result
