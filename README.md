# devlake-health-check

> Repository to handle health check and Github issue label management

## What it does?

1. Sends a GET requests to the given url, and checks if response code >= 200 and < 400
   1. true:
      1. check if there exists an issue with given labels
         1. true (meaning that the last run a issue was created and marked the service as down)
            1. close issue (mark service as up)
         2. false () # service is still up (previous check was also up)
   2. false:
      1. check if there exists an issue with given labels (last check was also status down)
         1. true:
            1. do nothing. no change in status
         2. false (last check yielded healthy / up)
            1. create issue for given repository and add given labels

## Usage

```
  - uses: skaugvoll-actions/devlake-health-check@v1.0.1-beta
    with:
      url: http://example.com
      repository: user|organization/repository
      serviceName: Arbitrary name
      labels: serviceName,label1,label2,...,labelN
    env:
      gh_token: ${{ secrets.GH_PAT }}
```

> labels:
>
> > Highly recommended to add serviceName as one of the labels
> >
> > Labels should create a unique set of label-combinations

> gh_token:
>
> > The GH_PAT should be a github token or PAT (personal access token) that has access to the given repository.
> >
> > If same repository as workflow, can use the automaticaly created github token that's allready available inside the workflow.
