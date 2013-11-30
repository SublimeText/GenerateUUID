import sublime
import sublime_plugin
import uuid
import re


class GenerateUuidCommand(sublime_plugin.TextCommand):
    """
    Generate a UUID version 4.
    Plugin logic for the 'generate_uuid' command.
    Searches for "uuid_uppercase" setting in user preferences, capitalizes
    UUID if true. - author Matt Morrison mattdmo@pigimal.com

    Author: Eric Hamiter
    Seealso: https://github.com/ehamiter/Sublime-Text-2-Plugins
    """
    def run(self, edit):
        for r in self.view.sel():
            settings = sublime.load_settings('Preferences.sublime-settings')
            if settings.get('uuid_uppercase'):
                value = str(uuid.uuid4()).upper()
            else:
                value = str(uuid.uuid4())

            self.view.replace(edit, r, value)

class GenerateShortUuidCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for r in self.view.sel():
            settings = sublime.load_settings('Preferences.sublime-settings')
            if settings.get('uuid_uppercase'):
                value = str(uuid.uuid4()).upper()
            else:
                value = str(uuid.uuid4())

            self.view.replace(edit, r, re.sub('-', '', value))

class GenerateUuidListenerCommand(sublime_plugin.EventListener):
    """
    Expand 'uuid' and 'uuid4' to a random uuid (uuid4) and
    'uuid1' to a uuid based on host and current time (uuid1).
    Searches for "uuid_uppercase" setting in user preferences, capitalizes
    UUID if true. - author Matt Morrison mattdmo@pigimal.com

    Author: Rob Cowie
    Seealso: https://github.com/SublimeText/GenerateUUID/issues/1
    """
    def on_query_completions(self, view, prefix, locations):
        uuid_prefix = ''
        _prefix = prefix
        if prefix[:2] == '0x':
            uuid_prefix = '0x'
            prefix = prefix[2:]

        if prefix in ('uuid', 'uuid4'):  # random
            val = str(uuid.uuid4())
        elif prefix == 'uuid1':          # host and current time
            val = str(uuid.uuid1())
        elif prefix == 'uuid1s':
            val = re.sub('-', '', str(uuid.uuid1()))
        elif prefix == 'uuids':
            val = re.sub('-', '', str(uuid.uuid4()))
        else:
            return []

        settings = sublime.load_settings('Preferences.sublime-settings')
        if settings.get('uuid_uppercase'):
            val = val.upper()
        
        return [(_prefix, _prefix, uuid_prefix+val)] if val else []
