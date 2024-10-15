# Django QR

<p align="center">
  <a href="https://github.com/abe-101/django-qr/actions/workflows/ci.yml?query=branch%3Amain">
    <img src="https://img.shields.io/github/actions/workflow/status/abe-101/django-qr/ci.yml?branch=main&label=CI&logo=github&style=flat-square" alt="CI Status" >
  </a>
  <a href="https://django-qr.readthedocs.io">
    <img src="https://img.shields.io/readthedocs/django-qr.svg?logo=read-the-docs&logoColor=fff&style=flat-square" alt="Documentation Status">
  </a>
  <a href="https://codecov.io/gh/abe-101/django-qr">
    <img src="https://img.shields.io/codecov/c/github/abe-101/django-qr.svg?logo=codecov&logoColor=fff&style=flat-square" alt="Test coverage percentage">
  </a>
</p>
<p align="center">
  <a href="https://python-poetry.org/">
    <img src="https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json" alt="Poetry">
  </a>
  <a href="https://github.com/astral-sh/ruff">
    <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json" alt="Ruff">
  </a>
  <a href="https://github.com/pre-commit/pre-commit">
    <img src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=flat-square" alt="pre-commit">
  </a>
</p>
<p align="center">
  <a href="https://pypi.org/project/django-qr/">
    <img src="https://img.shields.io/pypi/v/django-qr.svg?logo=python&logoColor=fff&style=flat-square" alt="PyPI Version">
  </a>
  <img src="https://img.shields.io/pypi/pyversions/django-qr.svg?style=flat-square&logo=python&amp;logoColor=fff" alt="Supported Python versions">
  <img src="https://img.shields.io/pypi/l/django-qr.svg?style=flat-square" alt="License">
</p>

---

**Documentation**: <a href="https://django-qr.readthedocs.io" target="_blank">https://django-qr.readthedocs.io </a>

**Source Code**: <a href="https://github.com/abe-101/django-qr" target="_blank">https://github.com/abe-101/django-qr </a>

---

Generate and manage QR codes that redirect to specific views in your Django project

## Installation

Install this via pip (or your favourite package manager):

`pip install django-qr`

Add the app to your `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    # ...
    "django_qr",
]
```

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- prettier-ignore-start -->
<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://www.habet.dev/"><img src="https://avatars.githubusercontent.com/u/82916197?v=4?s=80" width="80px;" alt="Abe Hanoka"/><br /><sub><b>Abe Hanoka</b></sub></a><br /><a href="https://github.com/abe-101/django-qr/commits?author=abe-101" title="Code">💻</a> <a href="#ideas-abe-101" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/abe-101/django-qr/commits?author=abe-101" title="Documentation">📖</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->
<!-- prettier-ignore-end -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!

## Credits

This package was created with
[Copier](https://copier.readthedocs.io/) and the
[browniebroke/pypackage-template](https://github.com/browniebroke/pypackage-template)
project template.
