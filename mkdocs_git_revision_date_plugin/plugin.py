from os import environ

from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin
from mkdocs.utils import string_types
from jinja2 import Template
from .util import Util
from .filters import to_timeago


class GitRevisionDatePlugin(BasePlugin):
    config_scheme = (
        ('enabled_if_env', config_options.Type(string_types)),
        ('modify_md', config_options.Type(bool, default=True))
    )

    def __init__(self):
        self.enabled = True
        self.util = Util()

    def on_env(self, env, **kwargs) :
        env.filters['totimeago'] = to_timeago
        return env
        
    def on_config(self, config):
        env_name = self.config['enabled_if_env']
        if env_name:
            self.enabled = environ.get(env_name) == '1'
            if not self.enabled:
                print('PDF export is disabled (set environment variable %s to 1 to enable)' % env_name)
                return

    def on_page_markdown(self, markdown, page, config, files):
        if not self.enabled:
            return markdown

        revision_date = self.util.get_revision_date_for_file(page.file.abs_src_path)

        if not revision_date:
            from datetime import datetime
            revision_date = datetime.now().date()
            print('WARNING -  %s has no git logs, revision date defaulting to today\'s date' % page.file.src_path)

        page.meta['revision_date'] = revision_date

        if not self.config['modify_md']:
            return markdown

        if 'macros' in config['plugins']:
            keys = list(config['plugins'].keys())
            vals = list(config['plugins'].values())
            if keys.index('macros') > vals.index(self):
                new_markdown = '{{% set git_revision_date = \'{}\' %}}\n'.format(revision_date) + markdown
                return new_markdown
            else:
                print('WARNING - macros plugin must be placed AFTER the git-revision-date plugin. Skipping markdown modifications')
                return markdown
        else:
            md_template = Template(markdown)
            return md_template.render({'git_revision_date': revision_date})