import sublime_plugin
import uuid

class GenerateUuidCommand(sublime_plugin.TextCommand):
    """
    Generate a UUID version 4.

    Author: Eric Hamiter    
    Seealso: https://github.com/ehamiter/Sublime-Text-2-Plugins
    """
    def run(self, edit):
        u = str(uuid.uuid4())
        for r in self.view.sel():
            self.view.replace(edit, r, u)
