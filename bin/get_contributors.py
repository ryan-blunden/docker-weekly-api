#! /usr/bin/env python3.6

"""
Extract the list of Docker Captains from https://www.docker.com/community/docker-captains so they can be store in JSON
 locally. This is so we can then cross reference the article authors and mark their `Contributor` objects as captains. 
"""

# TODO: Re-do this with Selenium so I can scrape the bio text.
# TODO: Get the social links
import json
import os
import re
from typing import Dict, List

import click

ISSUE_FILE_REGEX = re.compile(r'^\d+\.json$')


@click.command()
def get_contributors():
    contributors: Dict[str, Dict] = {}
    issues_files: List[str] = [issue for issue in os.listdir('data/issues') if
                               re.match(ISSUE_FILE_REGEX, issue) is not None]

    captains: Dict[str, Dict] = {}
    with open('data/captains/index.json', 'r') as f:
        captains = {captain['name']: captain for captain in json.load(f)}

    for issue_file in issues_files:
        issue = None
        with open('data/issues/{}'.format(issue_file)) as f:
            issue = json.load(f)

        for article in issue['articles']:
            for contributor in article['contributors']:
                if captains.get(contributor['name']) is not None:
                    contributor['is_captain'] = True
                    contributor['captain_data'] = captains.get(contributor['name'])
                contributors[contributor['name']] = contributor

    click.echo(json.dumps([contributor for k, contributor in contributors.items()], indent=2))


if __name__ == '__main__':
    get_contributors()
