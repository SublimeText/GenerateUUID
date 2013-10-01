# Generate UUID package for Sublime Text

Helper script to generate a UUID v4. Can be executed via keyboard shortcut `Ctrl+Shift+U` (or `Super+Shift+U` for OSX) and or via the menu item `Tools >> Packages >> Generate UUID v4`.

## Installation

The best way to install this bundle and keep up to date is to install it via [Package Control](https://sublime.wbond.net/installation). Once you have installed Package Control, open it via `Preferences >> Package Control` and click on `Package Control: Install Package`. Type `GenerateUUID` into the search box, then hit enter or click on the result to install.

### Using Git

If you are a git user, you can clone the repo directly into your `Packages` directory in the Sublime Text application settings area. Go to your Sublime Text `Packages` directory and clone the repository using the command below:

    git clone https://github.com/SublimeText/GenerateUUID "GenerateUUID"

### Download Manually

* Download the files using the GitHub .zip download option
* Unzip the files and rename the folder to `Generate UUID`
* Copy the folder to your Sublime Text `Packages` directory

## Preferences

To enable uppercase UUIDs, put the key `"uuid_uppercase": true` in your `Packages/User/Preferences.sublime-settings` file (accessible via the `Preferences >> Settings - User` menu option). If this key is not present, or is set to any other value, UUIDs will be generated in lowercase as before.
