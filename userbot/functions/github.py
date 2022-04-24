import os
os.system("pip install PyGithub")
import glob
from github import Github
import Config

class GITAPP:
    def __init__(self):
        self.g = Github(Config.GIT_USERNAME, Config.GIT_PASSWORD)
        self.repo = self.g.get_repo(Config.REPO_NAME)

    def get_all_files(self, dir):
        if not dir.endswith("/"):
            dir = dir + "/"
        all_files = []
        for file in glob.glob((dir + "*")):
            if os.path.isfile(file):
                all_files.append(os.path.basename(file))  
        return all_files

    def create(self, oldfile, newfile):
        try:
            content = open(oldfile, "r").read()
        except:
            content = open(oldfile, "rb").read()
        try:
            self.repo.create_file(newfile, "creating file", content, branch="master")
            return True
        except:
            return False

    def update(self, oldfile, newfile):
        try:
            content = open(oldfile, "r").read()
        except:
            content = open(oldfile, "rb").read()
        try:
            contents = self.repo.get_contents(newfile)
            self.repo.update_file(contents.path, "updating file", content, contents.sha, branch="master")
            return True
        except:
            return False

    def delete(self, file):
        try:
            contents = self.repo.get_contents(file, ref="master")
            self.repo.delete_file(contents.path, "removing file", contents.sha, branch="master")
            return True
        except:
            return False
