# Python Regex to parse apart android user agent device name
(?P&lt;browser&gt;Android) (?P&lt;major_version&gt;\d*)\.(?P&lt;minor_version&gt;\d*);[^;]*;(?P&lt;device&gt;[ \w]+) Build\/
