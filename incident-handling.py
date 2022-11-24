from typing import List
from healthChecker import HealthCheck
from projectSettings import ProjectSettings
import sys


def healthCheckGithubLabels(url: str, repo: str, serviceName: str, labels: List[str]):
    print(
        f"## INPUTS:\n# url: {url}\n# repository: {repo}\n# serviceName: {serviceName}\n# labels: {labels}\n##")
    config = ProjectSettings()
    hc = HealthCheck(config=config, repo=repo)
    hc.httpStatusCheckWithGithubLabels(serviceName, url, labels)


helpText = '''
Usage: python incident-handling.py <url to check httpStatus> <repository to manage issues> <label 1> ... <label n>
'''.format()

if __name__ == "__main__":
    if(len(sys.argv) == 4):
        print(helpText)
        exit(1)

    url = sys.argv[1]
    repo = sys.argv[2]
    serviceName = sys.argv[3]
    labels = sys.argv[4]

    labels = labels.split(",")

    healthCheckGithubLabels(url, repo, serviceName, labels)
