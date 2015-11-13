# freeFlix
Watch movies with this simple Python client(only for OSX, can be easily modified to work on WIndows too). <br>

Before you get started, make sure you have VLC player installed. If you do not have VLC installed, go to <a href = "https://www.videolan.org/vlc/download-macosx.html"> this link </a>

To get started, simply download the repo(click on "download zip "), navigate to the folder via terminal and run these commands:<br>
Assuming it is downloaded in the Downloads directory, type these commands.

<i>cd ~/Downloads/freeFlix-master </i>

<i>sudo python get-pip.py </i>

Type your password. it will install a python pip program which lets you install other Python modules/libraries. Then,

<i>sudo pip install selenium </i>

<i>sudo pip install rottentomatoes </i>


and you should be all set



Now, the fun part,

run this command in your terminal

<i>python freeFlix.py skyfall </i>


and you should get a VLC window playing skyfall.

For other movies, simple replace skyfall with that movie name eg 
<i>python freeflix.py the dark knight </i>


<b> Also you can add subtitles easily to the streaming movie </b>

go to subscene.com and find the subtitle of that movie, download it, extract it and drag it to the player
