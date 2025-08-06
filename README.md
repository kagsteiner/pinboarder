# pinboarder
Python tools to work on pinboard.in bookmarks

Over the years my pinboard.in account has become messy. The python scripts here help managing it. Should work for every pinboard user. Someday I might even add an UI or something.

*don't look at code quality*, I have not coded a single line; this was totally vibe coded with gemini cli. My handwritten code would, of course, be flawless. But I would never find time to do this hand-coded. The kind of stuff you get done with AIs because they are not important enough to you to spend real time on.

**Usage**
1. go to pinboard.in and copy your personal pinboard token into the clipboard.
2. create a .env file that contains
PINBOARD_TOKEN=<your token>
3. run the script of your choice, currently only 
python markdead.py
4. wait - for my 800 bookmarks it takes 15 minutes or so.
5. enjoy the freshly tagged bookmarks, search for !dead to see only living bookmarks.

**markdead.py**

Will read all your pinboard.in bookmarks, check the sites for being alive, and add a tag "dead" to them if they are not.

It passes browser parameters in a reasonable way to convince sites that it is a browser. If it fails and gets a "forbidden" HTTP status, it will consider the site alive.

After you have run the script, you can add "!dead" to the search in pinboard.in to only get living sites.

