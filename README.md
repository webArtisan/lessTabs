#Less Tabs for sublime text 3

Are you tired of closing tabs manually ?

Do you want to close all old tabs with one command ?

After installing the plugin, press `ctrl + alt + c` and all the tabs that wasn't modified in the last 30 minutes (customize from settings) will be closed.

Files with unsaved changes will not be closed.

Files that were visited in the last minute will not be closed. (customize from settings)

##Installation
### Now available through [Package Control](http://wbond.net/sublime_packages/package_control)!
The easiest method is through [Package Control](http://wbond.net/sublime_packages/package_control). Open the command palette with <kbd>Ctrl</kbd><kbd>Shift</kbd><kbd>P</kbd> (Windows/Linux) or <kbd>⌘</kbd><kbd>Shift</kbd><kbd>P</kbd> (OSX) and type `pci` or `packconin` or whatever you like to get `Package Control: Install` showing. Click or hit <kbd>Enter</kbd>, type in `less` or `less tabs` ... and then hit <kbd>Enter</kbd>.

#### Manual install
Clone or download this repo to your **Packages** folder.

To easily open **Packages** folder, open sublime text then open the following menu `Preferences -> Browse Packages...`.

You can always clone the repo with git

    git clone git://github.com/webArtisan/lessTabs.git

##Usage

The default shortcut for closing tabs using lessTabs plugin is `ctrl + alt + c`.

There is also a command in the command palette `Less tabs: close old tabs`

##Features

- By setting the value of the setting value "close_on_open_new" to true, the plugin will execute the closing command when a new tab is opened.

- Close unrelated tabs to the open project.

- Close unrelated tabs to the directory of the current open tab (tab with focus).

- Close unrelated tabs to a user input directory.

##Stay tuned

I'm working on another package called **moreTabs**, that will help you open closed tabs in a much easier way.

##Credit
I got the idea at the first place from this plugin **TidyTabs** https://github.com/bradleyboy/TidyTabs-Sublime.

His plugin isn't sublime text 3 compatible so i made this one.

##License
<a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/"><img alt="Licence Creative Commons" style="border-width:0" src="http://i.creativecommons.org/l/by-sa/3.0/88x31.png" /></a>

&copy; 2012-2013 webArtisan <web.artisan89@gmail.com>.

This is free software. It is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/">Creative Commons Attribution-ShareAlike 3.0 Unported License</a>. Feel free to use this plugin in your own work. However, if you modify and/or redistribute it, please attribute me in some way, and distribute your work under this or a similar license. A shout-out would be appreciated.
