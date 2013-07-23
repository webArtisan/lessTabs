import sublime, sublime_plugin, os, time

class lessTabsCommand(sublime_plugin.WindowCommand):
  def run(self):
    SETTINGS = sublime.load_settings("lessTabs.sublime-settings")
    modified_ls   = int(SETTINGS.get('modified_life_span'))
    accessed_ls   = int(SETTINGS.get('accessed_life_span'))

    now = time.time()

    for buffer in self.window.views():
      path = buffer.file_name()
      
      if (
        path
        and not buffer.is_scratch()
        and not buffer.is_dirty()
        and os.path.exists(path) == True
        and now - os.path.getmtime(path) > modified_ls
        and now - os.path.getatime(path) > accessed_ls
      ):
        self.window.focus_view(buffer)
        self.window.run_command('close_file')