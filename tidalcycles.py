import os
import sublime
import sublime_plugin


sessionName = 'tidal'


class TidalEvalCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for selectionRegion in self.view.sel():
			lineRegion = self.view.line(selectionRegion)
			line = self.view.substr(lineRegion)
			print(line)

			# get surrounding lines, to evaluate entire block
			lines = [line]
			while True:
				a = lineRegion.a
				b = lineRegion.b
				if not (a == 0 or lines[0] == ''):
					lineRegion.a = a - 1
				if not (b >= self.view.size() - 1 or lines[-1] == ''):
					lineRegion.b = b + 1
				if lineRegion.a == a and lineRegion.b == b:
					break
				s = self.view.substr(lineRegion)
				lines = s.splitlines()
				if lines[0] == '' and lines[-1] == '':
					break
			lines = [l for l in lines if l != '']
			print(lines)

			code = line.replace('"', '\\\"')
			if len(lines) > 1:
				lines = [
					*lines
				]
				# TODO: evaluate multiple lines
				# code = 
				pass
			os.system(
				'tmux send-keys -t "{}" "{}" C-m \\;'.format(
					sessionName, code
				)
			)
