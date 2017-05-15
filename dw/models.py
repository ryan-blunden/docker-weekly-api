from typing import List, Dict, Any


class Contributor:
    name: str
    url: str
    is_captain: bool

    def __init__(self, name: str, url: str, is_captain: bool = False):
        self.name = name
        self.url = url
        self.is_captain = is_captain

    def __repr__(self) -> str:
        return str(self.__dict__())

    def __dict__(self) -> Dict[str, Any]:
        return {
            'name': self.name,
            'url': self.url,
            'is_captain': self.is_captain
        }

    @classmethod
    def from_dict(cls, d):
        return cls(d['name'], d['url'], d.get('is_captain', False))


class Article:
    title: str
    url: str
    contributors: [Contributor]
    featured: bool

    def __init__(self, title: str, url: str, contributors: [Contributor], featured: bool = False):
        self.title = title
        self.url = url
        self.contributors = contributors
        self.featured = featured

        for contributor in contributors:
            if contributor.is_captain:
                self.featured = True
                break

    def __repr__(self) -> str:
        return str(self.__dict__())

    def __dict__(self) -> Dict[str, Any]:
        return {
            'title': self.title,
            'url': self.url,
            'featured': self.featured,
            'contributors': [contributor.__dict__() for contributor in self.contributors],
        }


class Issue:
    number: int
    date: str
    url: str
    articles: List[Article]
    count: int
    notes: str

    def __init__(self, number: int, date: str, url: str, articles: List[Article] = None):
        self.number = number
        self.date = date
        self.url = url
        self.articles = [] if articles is None else articles

        self.count = -1
        self.notes = ''

    def __dict__(self) -> Dict[str, Any]:
        return {
            'issue': self.number,
            'date': self.date,
            'url': self.url,
            'count': self.count,
            'notes': self.notes,
            'articles': [article.__dict__() for article in self.articles]
        }


class DockerCaptain:
    name: str
    avatar_url: str
    title: str
    bio: str
    links: Dict[str, str]

    def __init__(self, name: str, avatar_url: str, title: str, bio: str = '', links: Dict[str, str] = None):
        self.name = name
        self.avatar_url = avatar_url
        self.title = title
        self.bio = bio
        self.links = links if links is not None else {}

    def __repr__(self) -> str:
        return str(self.__dict__())

    def __dict__(self) -> Dict[str, Any]:
        return {
            'name': self.name,
            'avatar_url': self.avatar_url,
            'title': self.title,
            'bio': self.bio,
            'links': self.links
        }
