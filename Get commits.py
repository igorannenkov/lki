from github import Github
from dateutil.parser import parse

gitHub = Github()
user_name = input("Имя пользователя GitHub: ")
repo_name = input(f"Наименование репозитория пользователя {user_name}: ")
branch_name = input(f"Наименование ветки репозитория {repo_name}: ")
required_date = parse(input("Дата начала ЧЧ.ММ.ГГГГ: "), ignoretz=True)
repo = gitHub.get_repo(f"{user_name}/{repo_name}")

commits = []

for commit in repo.get_commits():
    commit_date = parse(str(commit.commit.author.date), ignoretz=True)
    if required_date < commit_date:
       print(commit.sha, commit.author, commit.commit.author.date)
       commits.append(f"{commit.sha} {commit.author} {commit.commit.author.date}")

with open("commits.txt", "w", encoding="UTF-8") as file:
    for line in commits:
        file.write(line + "\n")

