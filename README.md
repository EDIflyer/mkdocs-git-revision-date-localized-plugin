[![Actions Status](https://github.com/timvink/mkdocs-git-revision-date-localized-plugin/workflows/pytest/badge.svg)](https://github.com/timvink/mkdocs-git-revision-date-localized-plugin/actions)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mkdocs-git-revision-date-localized-plugin)
![PyPI](https://img.shields.io/pypi/v/mkdocs-git-revision-date-localized-plugin)
![PyPI - Downloads](https://img.shields.io/pypi/dm/mkdocs-git-revision-date-localized-plugin)
[![codecov](https://codecov.io/gh/timvink/mkdocs-git-revision-date-localized-plugin/branch/master/graph/badge.svg)](https://codecov.io/gh/timvink/mkdocs-git-revision-date-localized-plugin)
![GitHub contributors](https://img.shields.io/github/contributors/timvink/mkdocs-git-revision-date-localized-plugin)
![PyPI - License](https://img.shields.io/pypi/l/mkdocs-git-revision-date-localized-plugin)

# mkdocs-git-revision-date-localized-plugin

[MkDocs](https://www.mkdocs.org/) plugin that enables displaying the date of the last git modification of a page. The plugin uses [babel](https://github.com/python-babel/babel/tree/master/babel) and [timeago.js](https://github.com/hustcc/timeago.js) to provide different localized date formats. Initial fork from [mkdocs-git-revision-date-plugin](https://github.com/zhaoterryy/mkdocs-git-revision-date-plugin).

![demo](https://github.com/timvink/mkdocs-git-revision-date-localized-plugin/raw/master/demo_screencast.gif)

(*Example when used together with the [mkdocs-material](https://github.com/squidfunk/mkdocs-material) theme*)

## Setup

Install the plugin using `pip3` with the following command:

```bash
pip3 install mkdocs-git-revision-date-localized-plugin
```

Next, add the following lines to your `mkdocs.yml`:

```yaml
plugins:
  - search
  - git-revision-date-localized
```

> If you have no `plugins` entry in your config file yet, you'll likely also want to add the `search` plugin. MkDocs enables it by default if there is no `plugins` entry set.

If you use the [mkdocs-material](https://squidfunk.github.io/mkdocs-material/) theme, you should already see the last revision on the bottom of your pages.

### Note when using build environments

This plugin needs access to the last commit that touched a specific file to be able to retrieve the date. By default many build environments only retrieve the last commit, which means you might need to:

<details>
  <summary>Change your CI settings</summary>
    <ul>
      <li>github actions: set <code>fetch_depth</code> to <code>0</code> (<a href="https://github.com/actions/checkout">docs</a>)</li>
      <li>gitlab runners: set <code>GIT_DEPTH</code> to <code>0</code> (<a href="https://docs.gitlab.com/ee/user/project/pipelines/settings.html#git-shallow-clone">docs</a>)</li>
      <li>bitbucket pipelines: set <code>clone: depth: full</code> (<a href="https://support.atlassian.com/bitbucket-cloud/docs/configure-bitbucket-pipelinesyml/">docs</a>)</li>
    </ul>
</details>


## Documentation

See [timvink.github.io/mkdocs-git-revision-date-localized-plugin](https://timvink.github.io/mkdocs-git-revision-date-localized-plugin/index.html).

## Contributing

Contributions are very welcome! Please read [CONTRIBUTING.md](https://github.com/timvink/mkdocs-git-revision-date-localized-plugin/blob/master/CONTRIBUTING.md) before putting in any work.
