import os
import sublime
import sublime_plugin


sessionName = 'tidal'


class TidalEvalCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():
			line = self.view.line(region)
			lineContents = self.view.substr(line)
			cmd = 'tmux send-keys -t "{}" "{}" C-m'.format(
				sessionName, 
				lineContents.replace('"', '\\\"')
			)
			os.system(cmd)
