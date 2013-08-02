import sublime, sublime_plugin, os, time, re

class WM:
  def get_project_folder(window):
    project_folders = [] 
    if ( WM.has_project(window) ):
      for folder_data in window.project_data()["folders"]:
        project_folders.append(folder_data['path'])

    return project_folders

  def has_project(window):
    return window.project_data() != None

  def file_belongs_to_path(buffer, parent_folders, related_paths):
    file_in_project = False
    path = buffer.file_name()
    
    if ( path ):
      file_dir = os.path.dirname(path)
      if ( not file_dir in related_paths ):
        for folder in parent_folders:
          if ( file_dir.startswith(folder) ):
            related_paths.append(file_dir)
            file_in_project = True
            break
      else:
        file_in_project = True

    return file_in_project, related_paths

  def close_buffer(window, buffer):
    window.focus_view(buffer)
    window.run_command('close_file')


class lessTabsCommand(sublime_plugin.WindowCommand):
  def run(self):
    SETTINGS = sublime.load_settings("lessTabs.sublime-settings")
    modified_ls   = int(SETTINGS.get('modified_life_span'))
    accessed_ls   = int(SETTINGS.get('accessed_life_span'))

    now = time.time()
    active_view = sublime.active_window().active_view()

    for buffer in self.window.views():
      path = buffer.file_name()

      if (
        buffer != active_view
        and not buffer.is_loading()
        and not buffer.is_scratch()
        and not buffer.is_dirty()
        and path
        and os.path.exists(path)
        and now - os.path.getmtime(path) > modified_ls
        and now - os.path.getatime(path) > accessed_ls
      ):
        WM.close_buffer(self.window, buffer)


class lessTabsCloseProjectUnrelatedCommand(sublime_plugin.WindowCommand):
  def run(self):
  
    window = self.window

    if ( WM.has_project(window) ):
      related_paths = []
      project_folders = WM.get_project_folder(window)

      for buffer in window.views():
        file_in_project, related_paths = WM.file_belongs_to_path(buffer, project_folders, related_paths)

        if ( not file_in_project ):
          WM.close_buffer(window, buffer)
    else:
      sublime.status_message("Less Tabs : There is no open project.")


class lessTabsCloseDirUnrelatedCommand(sublime_plugin.WindowCommand):
  def run(self):
      self.window.show_input_panel("Directory of the tabs to keep open", "", self.on_done, None, None)

  def on_done(self, input):
    if ( os.path.exists(input) ):
      related_paths = []
      for buffer in self.window.views():
        file_in_dir, related_paths = WM.file_belongs_to_path(buffer, [input], related_paths)

        if ( not file_in_dir ):
          WM.close_buffer(self.window, buffer)
    else:
      sublime.error_message('Less Tabs : directory "'+input+'" not found.')
      self.window.run_command('less_tabs_close_dir_unrelated')


class lessTabsCloseFileDirUnrelatedCommand(sublime_plugin.WindowCommand):
  def run(self):
    window = self.window
    active_view = window.active_view()
    file_path = active_view.file_name()
    
    if ( file_path ):
      if ( file_path and os.path.exists(file_path) ):
        related_paths = []
        for buffer in window.views():
          file_in_dir, related_paths = WM.file_belongs_to_path(buffer, [os.path.dirname(file_path)], related_paths)

          if ( not file_in_dir ):
            WM.close_buffer(window, buffer)
      else:
        sublime.error_message('Less Tabs : file "'+file_path+'" not found.')
    else:
      sublime.error_message('Less Tabs : current tab doesn\'t exist on a physical drive.')


class lessTabsEvents(sublime_plugin.EventListener):
  def on_new(self, view):
    if ( sublime.load_settings("lessTabs.sublime-settings").get("close_on_open_new") ):
      sublime.active_window().run_command("less_tabs")
