import requests
from projectSettings import ProjectSettings
from githubWrapper import GithubWrapper


class HealthCheck:
    def __init__(self, config: ProjectSettings, repo: str = "user/repo"):
        self.config = config
        self.gh = GithubWrapper(config, repo)

    def _httpStatusCode(self, url):
        r = requests.get(url)
        print("Service status code: " + str(r.status_code))
        status = None
        if(r.status_code >= 200 and r.status_code < 400):
            status = 'up'
        else:
            status = 'down'
        return status

    def httpStatusCheckWithGithubLabels(self, serviceName, checkUrl, issueLabels):
        status = self._httpStatusCode(checkUrl)
        issue = self.gh.getIssueWithLabels(issueLabels)
        # status is down and previous status was up, since there are no open issues
        if(status == "down" and not issue):
            self.gh.createNewIssue(f"{serviceName}-incident", issueLabels)
            print("service is down, and incident is reported")
        # status is down and we have allready reported it
        elif(status == "down" and issue):
            print("No change in status. Service is still down and reported")
        # if status is up and there is a issue, that means can close the issue/incident, since service is not down anymore
        elif(status == "up" and issue):
            self.gh.updateIssue(issue.number, "close")
            print("service health is restored to healty, and incident is closed")
        # if status is up and there is no issue, do not create issue/incident
        elif(status == "up" and not issue):
            print("no change in status, service is up")
            pass
        else:
            raise Exception(
                "unknown status or issue/incident report not found")


if __name__ == "__main__":
    pass
