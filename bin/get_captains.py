#! /usr/bin/env python3.6

"""
Extract the list of Docker Captains from https://www.docker.com/community/docker-captains so they can be store in JSON
 locally. This is so we can then cross reference the article authors and mark their `Contributor` objects as captains. 
"""

import json
from typing import List

import click
import requests
from bs4 import BeautifulSoup

from dw.models import DockerCaptain


@click.command()
def get_captains():
    html: str = requests.get('https://www.docker.com/community/docker-captains').text
    soup: BeautifulSoup = BeautifulSoup(html, 'html.parser')
    captains_soup = soup.select('#captians-container > ul > li')
    captains_bios = {
        bio_soup.select('.name')[0].text: bio_soup.find('p').text for bio_soup in soup.select('div.captian_info')
    }
    captains: List[DockerCaptain] = []

    for captain_soup in captains_soup:
        captains.append(
            DockerCaptain(
                name=captain_soup.select('.name')[0].text,
                avatar_url=captain_soup.find('img')['src'],
                title=captain_soup.select('.job')[0].text,
                bio=captains_bios[captain_soup.select('.name')[0].text],
                links={link['class'][0].split('_')[0]:link.find('a')['href'] for link in captain_soup.select('ul > li')}
            )
        )

    click.echo(json.dumps([captain.__dict__() for captain in captains], indent=2))


if __name__ == '__main__':
    get_captains()
