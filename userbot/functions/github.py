import os
os.system("pip install PyGithub")
import glob
from github import Github

class GITAPP:
    def __init__(self, token, repo):
        self.g = Github(token)
        self.repo = self.g.get_repo(repo)

    def get_all_files(self, dir):
        all_files = []
        for file in glob.glob(dir):
            if os.path.isfile(file):
                all_files.append(os.path.basename(file))  
        return all_files

    def create(self, oldfile, newfile):
        try:
            content = open(oldfile, "r").read()
        except:
            content = open(oldfile, "rb").read()
        self.repo.create_file(newfile, "creating file", content, branch="master")

    def update(self, oldfile, newfile):
        try:
            content = open(oldfile, "r").read()
        except:
            content = open(oldfile, "rb").read()
        contents = self.repo.get_contents(newfile)
        self.repo.update_file(contents.path, "updating file", content, contents.sha, branch="master")

    def delete(self, file):
        contents = self.repo.get_contents(file, ref="master")
        self.repo.delete_file(contents.path, "removing file", contents.sha, branch="master")
