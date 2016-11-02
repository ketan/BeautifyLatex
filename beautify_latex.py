import os.path
import sublime, sublime_plugin, sys, re
import subprocess
import tempfile

class BeautifyLatexOnSave(sublime_plugin.EventListener):
  def on_pre_save(self, view):
    self.settings = sublime.load_settings('BeautifyLatex.sublime-settings')
    if self.settings.get('run_on_save'):
      view.run_command("beautify_latex", {"save": False, "error": False})

class BeautifyLatexCommand(sublime_plugin.TextCommand):
  def run(self, edit, error=True, save=True):
    self.load_settings()
    self.view.settings().set('translate_tabs_to_spaces', self.settings.get('translate_tabs_to_spaces'))
    self.view.settings().set('tab_size', self.settings.get('tab_size'))
    try:
      if self.is_latex_file():
        self.beautify_buffer(edit)
        if save and self.settings.get('save_on_beautify'):
          self.view.run_command('save')
      else:
        if error:
          raise Exception("This is not a Latex file.")
    except:
      msg = "Error: {0}".format(sys.exc_info()[1])
      sublime.error_message(msg)

  def beautify_buffer(self, edit):
    buffer_region = sublime.Region(0, self.view.size())
    buffer_text = self.view.substr(buffer_region)
    if buffer_text == "":
      return
    self.save_viewport_state()

    ext = os.path.splitext(self.view.file_name())[1]
    with tempfile.NamedTemporaryFile(delete=False,suffix=ext) as temp:
      try: 
          temp.write(buffer_text.encode("utf-8"))
          temp.flush()
          temp.close()
          beautified_buffer = self.pipe(self.cmd(temp.name))
          fix_lines = beautified_buffer.replace(os.linesep,'\n')
          self.check_valid_output(fix_lines)
          self.view.replace(edit, buffer_region, fix_lines)
      finally: 
          os.unlink(temp.name)
    self.reset_viewport_state()

  def check_valid_output(self, text):
    if text == "":
      msg = "invalid output. Check your latexindent settings"
      raise Exception(msg)

  def cmd(self, path = "-"):
    executable = self.which('latexindent.exe') or self.which('latexindent.pl')
    if not os.path.exists(executable):
      msg = "executable: '" + executable + "' not found."
      raise Exception(msg)

    return '"' + executable + '" "' + str(path) + '"'

  def finalize_output(self, text):
    lines = text.splitlines()
    finalized_output = "\n".join(lines)
    if self.view.settings().get("ensure_newline_at_eof_on_save") and not text.endswith("\n"):
      text += "\n"
    return finalized_output

  def load_settings(self):
    self.settings = sublime.load_settings('BeautifyLatex.sublime-settings')

  def save_viewport_state(self):
    self.previous_selection = [(region.a, region.b) for region in self.view.sel()]
    self.previous_position = self.view.viewport_position()

  def reset_viewport_state(self):
    self.view.set_viewport_position((0, 0,), False)
    self.view.set_viewport_position(self.previous_position, False)
    self.view.sel().clear()
    for a, b in self.previous_selection:
      self.view.sel().add(sublime.Region(a, b))

  def is_latex_file(self):
    file_patterns = self.settings.get('file_patterns') or ['\.tex']
    return self.match_pattern(file_patterns)

  def match_pattern(self, file_patterns):
    patterns = re.compile(r'\b(?:%s)\b' % '|'.join(file_patterns))
    return patterns.search(os.path.basename(self.view.file_name()))

  def pipe(self, cmd):
    cwd = os.path.dirname(self.view.file_name())
    beautifier = subprocess.Popen(cmd, shell=True, cwd=cwd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    out = beautifier.communicate(''.encode("utf-8"))[0]
    return out.decode('utf8')

  # http://stackoverflow.com/questions/377017/test-if-executable-exists-in-python/377028#377028
  def which(self,program):
    import os
    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None
