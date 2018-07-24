import os
import sublime
import sublime_plugin


sessionName = 'tidal'


class TidalEvalCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for selectionRegion in self.view.sel():
			lineRegion = self.view.line(selectionRegion)
			line = self.view.substr(lineRegion)

			def getStrippedLine(cursorAt):
				lineRegion = self.view.line(sublime.Region(cursorAt, cursorAt))
				return self.view.substr(lineRegion).strip()

			def startsWithWhitespace(s):
				return s.strip()[0] != s[0]

			# get surrounding lines, to evaluate entire block
			lines = [line]
			while True:
				a = lineRegion.a
				b = lineRegion.b
				if not (a == 0 or getStrippedLine(a - 1) == ''):
					lineRegion.a = a - 1
				if not (b >= self.view.size() - 1 or getStrippedLine(b + 1) == ''):
					lineRegion.b = b + 1
				if lineRegion.a == a and lineRegion.b == b:
					break
				s = self.view.substr(lineRegion)
				lines = s.splitlines()
				if lines[0] == '' and lines[-1] == '':
					break

			lines = [
				line.replace('"', '\\\"')
				for line in lines
				if line.strip() != ''
			]
			lines = [
				line if (startsWithWhitespace(line) or i == 0) else ' ; {}'.format(line)
				for i, line in list(enumerate(lines))
			]
			code = ''.join(lines)
			codes = [c.strip() for c in code.split(';')]
			print(codes)

			for c in codes:
				os.system(
					'tmux send-keys -t "{}" "{}" C-m \\;'.format(sessionName, c)
				)
