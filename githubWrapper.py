from github import Github
from typing import List
from projectSettings import ProjectSettings


class GithubWrapper:
    def __init__(self, config: ProjectSettings, repo: str, active: bool = True):
        self.active = active
        self.token = config.getGhToken()
        self._gh = Github(self.token)
        self.repo = self._gh.get_repo(repo)

    def _shouldExecute(self, fnc):
        if(not self.active):
            return
        return fnc()

    # TODO: use directive to wrap function, so that _shouldExecute runs before this
    def createNewIssue(self, title: str, labels: List[str]):
        issue = self.repo.create_issue(
            title=f"{title}",
            labels=labels
        )
        issueId = issue.number
        return issueId

    # TODO: use directive to wrap function, so that _shouldExecute runs before this
    def updateIssue(self, issueId: int, issueState: str):
        self.repo.get_issue(issueId).edit(state=issueState)

    def getIssueWithLabels(self, labels: List[str] = []):
        issues = self.repo.get_issues(labels=labels)
        for issue in issues:
            issueLabels = set([x.name for x in issue.labels])
            if set(labels) == issueLabels:
                return issue
        return None


if __name__ == "__main__":
    config = ProjectSettings()
    gh = GithubWrapper(config, repo="skaugvoll-actions/devlake-health-check")
    i = gh.getIssueWithLabels(["bug", "question"])
    print(i)
