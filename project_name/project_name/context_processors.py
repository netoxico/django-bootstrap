# coding: utf-8
from os import popen


def git(request):
    git_branch = popen('git rev-parse --abbrev-ref HEAD').readline().rstrip()
    git_commit = popen('git rev-parse HEAD').readline().rstrip()
    return {
        'GIT_BRANCH': git_branch,
        'GIT_COMMIT': git_commit
    }
