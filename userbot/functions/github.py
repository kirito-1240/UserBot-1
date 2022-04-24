from github import Github

class GITAPP:
    def __init__(token, repo):
        g = Github(token)
        repo = g.get_repo(repo)
    def get_all_files
all_files = []
contents = repo.get_contents("")
while contents:
    file_content = contents.pop(0)
    if file_content.type == "dir":
        contents.extend(repo.get_contents(file_content.path))
    else:
        file = file_content
        all_files.append(str(file).replace('ContentFile(path="','').replace('")',''))

for file in glob.glob("./emojis/*"):

    with open(file, 'rb') as file:
        content = file.read()

    git_prefix = 'userbot/other/emojis'
    git_file = git_prefix + file.split("/")[-1]
    if git_file in all_files:
        contents = repo.get_contents(git_file)
        repo.update_file(contents.path, "committing files", content, contents.sha, branch="master")
        print(git_file + ' UPDATED')
    else:
        repo.create_file(git_file, "committing files", content, branch="master")
        print(git_file + ' CREATED')
