from dotenv import load_dotenv, load_dotenv, dotenv_values
from os import getenv


class ProjectSettings:
    def __init__(self):
        load_dotenv()  # load from .env. environment file and os-environment
        self.envFromFiles = {}

    def loadEnvFromFiles(self, files=["mysql.env", "gh.env"]):
        for f in files:
            self.envFromFiles = {**self.envFromFiles, **dotenv_values(f)}

    def getOsEnv(self, envVar):
        return getenv(envVar)

    def getFilesEnv(self, envVar):
        return self.envFromFiles.get(envVar)

    def getGhToken(self):
        token = None
        try:
            token = self.getOsEnv("gh_token")
            if(not token):
                try:
                    token = self.getFilesEnv("gh_token")
                except:
                    print("could not find 'gh_token'")
                    raise Exception(
                        "could not find gh_token in passed in env files")
        except Exception as e:
            print("Could not get gh_token from environment variables")
            exit(1)
        if(not token):
            print("Could not get gh_token from environment variables")
            exit(1)
        print("github token found")
        return token


if __name__ == "__main__":
    config = ProjectSettings()
