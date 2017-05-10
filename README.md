# Docker Weekly Data

Make the articles featured in Docker Weekly available via JSON and eventually, via a hosted service that can be consumed as an API.

## Why this was created

The motivation for building this was that the Docker Weekly (at time of creation, April 2017) was not being updated
to include the issues from 2017. This means that new subscribers had no way of seeing previous issues.

## What it does

All articles in each Docker Weekly issue from 2016 and 2017 have been parsed and put into the data directory.

Just `git clone` and inspect the `data` directory for the issue data.

## Why I felt it was important to make this data available

While Docker has gone through many rapid changes since its inception, many of the articles captured in the Docker weekly
articles arwe timeless as they focus on best practices and lessons learnt using Docker in production.

## TODO
 
- Create an nginx Dockerfile with routes so this can be run and data can be served up with URLs.
- Put an HTML front-end on the site using the data files and a static site generator.
- Tag each link with key words (e.g. `security`, `swarm`) to make the articles by themselves useful.
 
## Contributing

I would love help turning this into something more beneficial to the community. Pull requests are welcome.

Raise an issue if you want to suggest new, different or complimentary data to what's currently available.

Currently, you'll need a Python environment with version `3.6.x` installed, the easiest way of which to do this is, of
 course, to run it in a Docker container.
 
#  Where can I get more help, if I need it?

This project is in its infancy and exists as Open Source more for transparency reasons than anything else. As a result, it's not really yet ready for contributors, unless they're ok with the complete lack of documentation about how to get started.

But, this will change once the service is online, working and providing value. At that point, I'll switch gears and focus on how others can take this shell of an idea and turn into something great that hopefully, provides real value to the Docker community.
