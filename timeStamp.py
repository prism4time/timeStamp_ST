
from datetime import datetime
import sublime
import sublime_plugin

class TimestampCommand(sublime_plugin.TextCommand):

	def run(self,edit):
		current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		self.view.insert(edit,self.view.sel()[0].begin(),current_time)


		