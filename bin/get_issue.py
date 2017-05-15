#! /usr/bin/env python3.6


""" 
Extract articles from a Docker weekly html file to dump as JSON. 

Done to automate as much of the content parsing as possible.
"""

import json
import re
from typing import List, Set

import click
import requests
from bs4 import BeautifulSoup

from dw.models import Contributor, Article, Issue


def _clean_link_text(link_text: str) -> str:
    return re.sub(r'\s+', ' ', str(link_text).strip()).replace('\\n', '').replace('\\t', '').replace('\\r', '')


def get_articles(soup: BeautifulSoup) -> List[Article]:
    # This is pretty dumb and simple code to parse articles.
    # It's meant to just scrape links as best it can, then have the results checked by a human.
    articles: List[Article] = []
    added_article_titles: Set[str] = set()

    for parent in set([a.parent for a in soup.find_all('a')]):
        links = None
        while parent is not None:
            links = parent.find_all('a')
            # Each article is in the format <a/> by|with <a/> so if not two links, not valid
            # This doesn't guarantee we won't grab other content, but it's a start.
            if 'by' not in parent.text or len(links) != 2:
                parent = parent.parent
            else:
                break

        if parent is None or links is None:
            continue

        contributor = Contributor(name=_clean_link_text(links[1].string), url=links[1].get('href'))

        title = _clean_link_text(links[0].string)
        url = links[0].get('href')

        if title in added_article_titles:
            continue

        articles.append(
            Article(title=title, url=url, contributors=[contributor])
        )
        added_article_titles.add(title)

    return articles


@click.command()
@click.option('--number', required=True, type=int, help='The issue number.')
def main(number: int, ):
    issues = json.load(open('data/issues/index.json', 'r'))
    issue: Issue = None

    for issue in issues:
        if issue['number'] is number:
            issue = Issue(
                number=issue['number'],
                date=issue['date'],
                url=issue['url']
            )
            break

    if issue is None:
        click.echo('error: Unable to find issue number {}'.format(number))
        raise click.Abort()

    html = requests.get(issue.url).text
    soup: BeautifulSoup = BeautifulSoup(html, 'html.parser')
    issue.articles += get_articles(soup)

    click.echo(json.dumps(issue.__dict__(), indent=2))


if __name__ == '__main__':
    main()
