#! /usr/bin/env python3.6

"""
Extract the list of Docker Captains from https://www.docker.com/community/docker-captains so they can be store in JSON
 locally. This is so we can then cross reference the article authors and mark their `Contributor` objects as captains. 
"""

# TODO: Re-do this with Selenium so I can scrape the bio text.
# TODO: Get the social links
import json
from typing import Dict, List, Any

import click
import requests
from bs4 import BeautifulSoup


class DockerCaptain:
    name: str
    avatar_url: str
    title: str

    def __init__(self, name: str, avatar_url: str, title: str):
        self.name = name
        self.avatar_url = avatar_url
        self.title = title

    def __repr__(self) -> str:
        return str(self.__dict__())

    def __dict__(self) -> Dict[str, Any]:
        return {
            'name': self.name,
            'avatar_url': self.avatar_url,
            'title': self.title
        }


@click.command()
def get_captains():
    html: str = requests.get('https://www.docker.com/community/docker-captains').text
    soup: BeautifulSoup = BeautifulSoup(html, 'html.parser')
    captains: List[DockerCaptain] = []

    for captain_soup in soup.select('#captians-container > ul > li'):
        captains.append(
            DockerCaptain(
                name=captain_soup.select('.name')[0].text,
                avatar_url=captain_soup.find('img')['src'],
                title=captain_soup.select('.job')[0].text
            )
        )

    click.echo(json.dumps([captain.__dict__() for captain in captains], indent=2))


if __name__ == '__main__':
    get_captains()
