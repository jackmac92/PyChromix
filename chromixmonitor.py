# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from time import sleep
from dashtools import unixresults as nix
from dashOBJ import chromixactions 
import json
import sys
from fuzzywuzzy import process
reload(sys)
sys.setdefaultencoding('utf8')
get_all_chrome = chromixactions.window_getAll_with_tabs
currentTab = chromixactions.tab_getCurrent

class ChromeWindow(object):
	"""docstring for ChromeWindow"""

	def __init__(self, chromixJson):
		super(ChromeWindow, self).__init__()
		self.id              = chromixJson['id']
		self.focused         = chromixJson['focused'] 
		self.state           = chromixJson['state'] 
		self.type            = chromixJson['type'] 
		self.incognito       = chromixJson['incognito'] 
		self.alwaysOnTop     = chromixJson['alwaysOnTop'] 
		self.window_geometry = [chromixJson['height'],chromixJson['width'],chromixJson['top'],chromixJson['left']]
		self.raw_tabs 		 = chromixJson['tabs']
		self.tabs     = {}
		for tabJson in self.raw_tabs:
			tabinfo = ChromeTab(tabJson)
			self.tabs[str(tabinfo.id)] = tabinfo

	def matchByTitle(self,comtitle):
		tmp = {}
		for tab in chromixactions.tab_query(active=True): tmp[tab['title']]=tab
		pick = tmp[process.extractOne(title, tmp.keys())[0]]['windowId']

		for win in get_all_chrome():
			if win['id'] == pick:
				return self.new(win)
	def __repr__(self):
		try:
			return "winId:{0} - #Tabs:{1}".format(self.id, len(self.tabs))
		except UnicodeEncodeError, e:
			source = unicode("windId:{0} - #Tabs:{1}".format(self.id, self.tabs), 'utf-8')
			return source


	def createTab(self, url = None, windowId = None, index = None, active = False):
		""" 
		windowId -- The window to create the new tab in. Defaults to the current window.
		index -- The position the tab should take in the window. The provided value will be clamped to between zero and the number of tabs in the window.
		url -- The URL to navigate the tab to initially. Fully-qualified URLs must include a scheme (i.e. 'http://www.google.com', not 'www.google.com'). Relative URLs will be relative to the current page within the extension. Defaults to the New Tab Page.
		active -- Whether the tab should become the active tab in the window. Does not affect whether the window is focused (see windows.update). Defaults to true.
		"""
		
		line = "chrome.tabs.create"
		opts = {}
		opts["url"]=url
		opts["active"]=active
		if windowId: opts["windowId"]=windowId
		if index: opts["index"]=index
		cmd = format_cmd(line, opts)
		return chromix_raw(cmd,response=False)
	def window_remove(windowId):
		line = "chrome.windows.remove"
		opts = {}
		opts["windowId"] = windowId
		cmd = format_cmd(line, opts)
		return chromix_raw(cmd)

	def resize():pass; 
	def get_active_tab():pass; 	
	def close(self):pass; 
	def minimize(self):pass; 

class ChromeTab(object):
	"""docstring for ChromeTab"""
	def __init__(self, chromixJson = None, tabID = None):
		super(ChromeTab, self).__init__()	
		self.id          = int(chromixJson['id'])
		self.windowId    = int(chromixJson['windowId'])
		self.index       = int(chromixJson['index'])
		self.title       = chromixJson['title']
		self.url         = chromixJson['url']
		self.active      = chromixJson['active']
		self.status      = chromixJson['status']
		self.selected    = chromixJson['selected']
		self.highlighted = chromixJson['highlighted']
		self.pinned      = chromixJson['pinned'] 
		self.incognito   = chromixJson['incognito']
		self.geometry    = [chromixJson['height'], chromixJson['width']]
	def close(self):
		cmd = "chrome.tabs.remove {0}".format(self.id)
		return chromix_raw(cmd, response=False)
	def move(self, index, windowId = None):
		opts = {}
		opts['index'] = index
		if windowId: opts['windowId'] = windowId
		line = "chrome.tabs.move {0}".format(self.id)
		cmd = format_cmd(line, opts)
		return chromix_raw(cmd)		
	def __repr__(self):
		return "tabId:{0} - Title:{1}".format(self.id, self.title[:25])
	def getByID(tabId):
		line = "chrome.tabs.get"
		opts = {"tabId":str(tabId)}
		cmd = format_cmd(line, opts)
		return chromix_raw(cmd)

	def tab_query(**kwargs):
		# active	= Whether the tabs are active in their windows. # pinned	= Whether the tabs are pinned. # highlighted	= Whether the tabs are highlighted. # currentWindow	= Whether the tabs are in the current window. # lastFocusedWindow	= Whether the tabs are in the last focused window. # status	= Whether the tabs have completed loading. # title	= Match page titles against a pattern. # string or array of string url	= Match tabs against one or more URL patterns. Note that fragment identifiers are not matched. # windowId	= The ID of the parent window, or windows.WINDOW_ID_CURRENT for the current window. # windowType	 # The type of window the tabs are in. # 	query active:true # 	query windowId:windowId a 
		opts = {}
		if kwargs:
			for k,v in kwargs.items():
				if not type(v) == bool and v[0].isdigit(): v = int(v)
				opts[k]=v
		line = "chrome.tabs.query"
		cmd = format_cmd(line, opts)
		return chromix_raw(cmd)

	def injectJavascript(self,code):
		line = "chrome.tabs.executeScript"
		opts = {}
		opts["code"] = code
		cmd = format_cmd(line, opts)
		chromix_raw(cmd)



def tab_LoadingPages():
	line = "chrome.tabs.query"
	opts = {"status":"loading"}
	cmd = format_cmd(line, opts)
	return chromix_raw(cmd)
def tab_AllPrevWindow():
	line = "chrome.tabs.query"
	id = window_getLastFocused()['id']
	opts = {"windowId":id}
	cmd = format_cmd(line, opts)
	return chromix_raw(cmd)
def window_get(windowId):
	"""Done"""
	line = "chrome.windows.get"
	opts = {}
	opts["windowId"] = windowId
	cmd = format_cmd(line, opts)
	return chromix_raw(cmd)
def window_getAll():
	"""Done"""
	cmd = "chrome.windows.getAll"
	return chromix_raw(cmd)
def window_getAll_with_tabs():
	"""Done"""
	line = "chrome.windows.getAll"
	opts = {}
	opts["populate"] = True
	cmd = format_cmd(line, opts)
	return chromix_raw(cmd)
def window_getCurrent(withTabs = False):
	"""Done"""
	line = "chrome.windows.getCurrent"
	if withTabs:
		opts = {}
		opts["populate"] = True
		cmd = format_cmd(line, opts)
	else:
		cmd = line
	return chromix_raw(cmd)
def window_getLastFocused():
	"""Done"""
	cmd = "chrome.windows.getLastFocused"
	return chromix_raw(cmd)
def window_create(**kwargs):
	"""Done"""
	line = "chrome.windows.create"
	if kwargs:
		opts = kwargs
		# for k,v in kwargs:
		# 	opts[k] = v
		cmd = format_cmd(line, opts)
	else:
		cmd = line
	return chromix_raw(cmd)

		
def format_cmd(line, opts):
	return "{0} '{1}'".format(line, json.dumps(opts))

def chromix_raw(cmd, response=True):
	final = "chromix raw {0}".format(cmd)
	print final
	result = nix.run(final)
	print result
	if response:
		if result:
			return json.loads(result)
		else:
			return 0

def modelCurrentChrome():
	result = []
	for x in get_all_chrome():
		win = ChromeWindow(x)
		result.append((win,win.tabs.values()))
	return result


if __name__ == '__main__':
	pass