import sublime
import sublime_plugin
import uuid

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
        if prefix in ('uuid', 'uuid4'): # random
            val = uuid.uuid4()
        elif prefix == 'uuid1':         # host and current time
            val = uuid.uuid1()
        else:
            return []
        settings = sublime.load_settings('Preferences.sublime-settings')
        if settings.get('uuid_uppercase'):
            val = str(val).upper()
        return [(prefix, prefix, val)] if val else []
