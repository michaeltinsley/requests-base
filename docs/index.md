# Requests Base Quickstart

<p align="center"><a href="/LICENSE"><img alt="MIT License" src="https://img.shields.io/badge/license-MIT-007EC7.svg?style=flat-square"></a> <a href="https://pypi.python.org/pypi/requests-base/"><img alt="PyPI" src="https://img.shields.io/pypi/v/requests-base.svg"></a></p>

Requests Base provides a single `BaseUrlSession` class, which allows a base URL to be set for a Requests Session. 

## Installation

### Install from [pypi](https://pypi.org/project/requests-base)

```bash
pip install requests-base
```

##  Using Requests Base

A Session with a URL that all requests will use as a base.

Let’s start by looking at an example:

```python
>>> from requests_base import BaseUrlSession
>>>
>>> session = BaseUrlSession(base_url="https://example.com/resource/")
>>> response = session.get('sub-resource/', params={'foo': 'bar'})
>>> print(response.request.url)
https://example.com/resource/sub-resource/?foo=bar
```

Our call to the `get` method will make a request to the URL passed in when we created the Session and the partial resource name we provide.

We implement this by overriding the `request` method so most uses of a Session are covered. (This, however, precludes the use of PreparedRequest objects).