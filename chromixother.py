# -*- coding: utf-8 -*-
from __future__ import unicode_literals
def download_show(id):
	"""
	Show the downloaded file in its folder in a file manager.
	Parameters
		integer	downloadId	
		The identifier for the downloaded file.
	"""
	line = "chrome.downloads.show {0}".format(id)


def download_open(id):
	"""
	Open the downloaded file now if the DownloadItem is complete; otherwise returns an error through runtime.lastError. Requires the "downloads.open" permission in addition to the "downloads" permission. An onChanged event will fire when the item is opened for the first time.
	Parameters
		integer	downloadId	
		The identifier for the downloaded file.
	"""
	line = "chrome.downloads.open"


def download_search():
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
	line = "chrome.downloads.search(object query)"
	opts = {}
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
