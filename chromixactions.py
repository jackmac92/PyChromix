# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from dashtools import unixresults as nix
from time import sleep


def chromix_raw(cmd, response=True):
	final = "chromix raw {0}".format(cmd)
	result = nix.run(final)
	if response:
		if result:
			return json.loads(result)
		else:
			return 0
		
def format_cmd(line, opts):
	return "{0} '{1}'".format(line, json.dumps(opts))

def tab_get(tabId):
	line = "chrome.tabs.get"
	opts = {"tabId":str(tabId)}
	cmd = format_cmd(line, opts)
	return chromix_raw(cmd)

def tab_getCurrent():
	line ="chrome.tabs.query"
	opts = {}
	opts["currentWindow"] = True
	opts["active"] = True
	cmd = format_cmd(line, opts)
	return chromix_raw(cmd)[0]
def tab_create(url = None, windowId = None, index = None, active = False):	
	line = "chrome.tabs.create"
	opts = {}
	opts["url"]=url
	opts["active"]=active
	if windowId: opts["windowId"]=windowId
	if index: opts["index"]=index
	cmd = format_cmd(line, opts)
	return chromix_raw(cmd,response=False)

def tab_move(tabIds, windowId = None, index = None):
	"""

	object	moveProperties	
		integer	(optional) windowId	- Defaults to the window the tab is currently in.
		integer	index - The position to move the window to. -1 will place the tab at the end of the window.
	"""
	opts = {}
	if type(tabIds) == str or type(tabIds) == int:tabIds=[int(tabIds)]
	opts["tabIds"] = tabIds
	if index:
		opts['index'] = index
	else:
		opts['index'] = 0
	if windowId:
		opts['windowId'] = windowId
	# else:
	# 	opts['windowId'] = window_getCurrent()['id']
	line = "chrome.tabs.move"
	cmd = format_cmd(line, opts)
	print cmd
	return chromix_raw(cmd)

def tab_AllFromWindow():
	line = "chrome.tabs.query"
	opts = {}
	opts['currentWindow'] = True
	cmd = format_cmd(line, opts)
	result = chromix_raw(cmd)
	return [dict(i) for i in result]

def tab_remove(tabIds):
	if not type(tabIds) == list: tabIds=[tabIds]
	line = "chrome.tabs.remove"
	opts = {}
	opts["tabIds"] = tabIds
	cmd = format_cmd(line, opts)
	print cmd
	return chromix_raw(cmd)
def tab_removeCurrent():
	# url = tab_getCurrent()['url']
	# cmd = "chromix with {0} close".format(url)
	cmd = "chromix with current close"
	nix.run(cmd)



def tab_query(**kwargs):
	# active	= Whether the tabs are active in their windows.
	# pinned	= Whether the tabs are pinned.
	# highlighted	= Whether the tabs are highlighted.
	# currentWindow	= Whether the tabs are in the current window.
	# lastFocusedWindow	= Whether the tabs are in the last focused window.
	# status	= Whether the tabs have completed loading.
	# title	= Match page titles against a pattern.
	# string or array of string url	= Match tabs against one or more URL patterns. Note that fragment identifiers are not matched.
	# windowId	= The ID of the parent window, or windows.WINDOW_ID_CURRENT for the current window.
	# windowType	
	# The type of window the tabs are in.

	# 	query active:true
	# 	query windowId:windowId all
	opts = {}
	if kwargs:
		for k,v in kwargs.items():
			if not type(v) == bool and v[0].isdigit(): v = int(v)
			opts[k]=v
	line = "chrome.tabs.query"
	cmd = format_cmd(line, opts)
	return chromix_raw(cmd)

def tab_Listall():
	line = "chrome.tabs.query '{}'"
	cmd = line
	return chromix_raw(cmd)

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
def tab_LoadingPages():
	line = "chrome.tabs.query"
	opts = {"status":"loading"}
	cmd = format_cmd(line, opts)
	return chromix_raw(cmd)
def tab_executeScript(code):
	line = "chrome.tabs.executeScript"
	opts = {}
	opts["code"] = code
	cmd = format_cmd(line, opts)
	print cmd
	chromix_raw(cmd)

def window_get(windowId):
	"""Done"""
	line = "chrome.windows.get"
	opts = {}
	opts["windowId"] = windowId
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

def window_remove(windowId):
	line = "chrome.windows.remove"
	opts = {}
	opts["windowId"] = windowId
	cmd = format_cmd(line, opts)
	return chromix_raw(cmd)

def window_update(windowId, updateInfo):
	"""NOTE DONE DON'T CARE"""
	line = "chrome.windows.update"
	cmd = "{0} {1}".format(line)
	return chromix_raw(cmd)

def windowSave():
	options = window_getCurrent(withTabs=True)
	print options


def download_show(dlId):
	"""
	Show the downloaded file in its folder in a file manager.
	Parameters
		integer	downloadId	
		The identifier for the downloaded file.
	"""
	line = "chrome.downloads.show"
	opts = {}
	opts["downloadId"]=dlId
	cmd = format_cmd(line, opts)
	return chromix_raw(cmd)

def download_open(id):
	"""
	Open the downloaded file now if the DownloadItem is complete; otherwise returns an error through runtime.lastError. Requires the "downloads.open" permission in addition to the "downloads" permission. An onChanged event will fire when the item is opened for the first time.
	Parameters
		integer	downloadId	
		The identifier for the downloaded file.
	"""
	line = "chrome.downloads.open"


def download_search(**kwargs):
	"""
	query (array of string) - This array of search terms limits results to DownloadItem whose filename or url contain all of the search terms that do not begin with a dash '-' and none of the search terms that do begin with a dash.
	mime (string) - The file's MIME type.
	state (State) - Indicates whether the download is progressing, interrupted, or complete.
	exists (boolean) - Whether the downloaded file exists;
	filenameRegex (string) - Limits results to DownloadItem whose filename matches the given regular expression.
	urlRegex (string) - Limits results to DownloadItem whose url matches the given regular expression.
	orderBy (array of string) - Set elements of this array to DownloadItem properties in order to sort search results. For example, setting orderBy=['startTime'] sorts the DownloadItem by their start time in ascending order. To specify descending order, prefix with a hyphen: '-startTime'.
	fileSize (double) - Number of bytes in the whole file post-decompression, or -1 if unknown.
	totalBytes (double) - Number of bytes in the whole file, without considering file compression, or -1 if unknown.
	totalBytesGreater (double) - Limits results to DownloadItem whose totalBytes is greater than the given integer.
	totalBytesLess (double) - Limits results to DownloadItem whose totalBytes is less than the given integer.
	startedBefore (string) - Limits results to DownloadItem that started before the given ms since the epoch.
	endedBefore (string) - Limits results to DownloadItem that ended before the given ms since the epoch.
	startedAfter (string) - Limits results to DownloadItem that started after the given ms since the epoch.
	endedAfter (string) - Limits results to DownloadItem that ended after the given ms since the epoch.
	startTime (string) - The time when the download began in ISO 8601 format.
	endTime (string) - The time when the download ended in ISO 8601 format.
	limit (integer) - The maximum number of matching DownloadItem returned. Defaults to 1000. Set to 0 in order to return all matching DownloadItem. See search for how to page through results.
	id (integer) - The id of the DownloadItem to query.
	"""
	line = "chrome.downloads.search"
	opts = {}
	if kwargs:
		for k,v in kwargs.items():
			if not type(v) == bool and v[0].isdigit(): v = int(v)
			opts[k]=v
	cmd = format_cmd(line, opts)
	return chromix_raw(cmd)

def bookmarks_search(q=None):
	line = "chrome.bookmarks.search"
	opts = {}
	cmd  = format_cmd(line, opts)
	return chromix_raw(cmd) 
def bookmarks_getTree():
	cmd = "chrome.bookmarks.getTree"
	return chromix_raw(cmd)
def bookmarks_getRecent(n):
	line = "chrome.bookmarks.getRecent"
	opts = {}
	opts['numberOfItems'] = int(n)
def bookmarks_getChildren(id):
	line = "chrome.bookmarks.getChildren"
	opts = {}
	opts['id'] = id
	cmd = format_cmd(line, opts)
	return chromix_raw(cmd)
def bookmarks_remove(id):
	line = "chrome.bookmarks.remove"
	opts = {}
	opts['id'] = id
	cmd = format_cmd(line, opts)
	return chromix_raw(cmd)
def bookmarks_move(id):
	line = "chrome.bookmarks.move"
	opts = {}
	opts['id'] = id
	cmd = format_cmd(line, opts)
	return chromix_raw(cmd)
def bookmarks_get(id):
	line = "chrome.bookmarks.get"
	opts = {}
	opts['id'] = id
	cmd = format_cmd(line, opts)
	return chromix_raw(cmd)
	

# Special
# with
# without
# current/ other
# chrome/ normal

# pin/unpin
# url

# chromix with normal list

# chromix with "url" focus




if __name__ == '__main__':
	pass