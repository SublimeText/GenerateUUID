import sublime
import sublime_plugin
import uuid

class GenerateUuidCommand(sublime_plugin.TextCommand):
    """
    Generate a UUID version 4.
    Plugin logic for the 'generate_uuid' command.
    Searches for "uuid_uppercase" setting in user preferences, capitalizes
    UUID if true.
    """

    def run(self, edit, short = False, single = False):
        for r, value in zip(self.view.sel(), self.generateUuids(short, single)):
            self.view.replace(edit, r, value)

    def generateUuids(self, short, single):
        settings = sublime.load_settings('Preferences.sublime-settings')
        uppercase = settings.get('uuid_uppercase')

        if single:
            value = self.newUuid(uppercase, short)
            while True:
                yield value
        else:
            while True:
                yield self.newUuid(uppercase, short)

    def newUuid(self, uppercase, short):
        value = str(uuid.uuid4())
        if uppercase:
            value = value.upper()
        if short:
            value = value.replace('-', '')
        return value

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
