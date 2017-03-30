# PROTECTING YOUR ONLINE PRIVACY: How to establish a secure socks proxy through Columbia's UNIX server
### Stephan S. Dalal --- March 2017

### Fellow Lions, you may not be surprised that Columbia hosts some of the most powerful UNIX stacks on the planet.  The School uses these computer resources for research, crunching very large numbers, and other related tasks.  What you may be surprised to learn is that all Columbia students have access to the server, for life.  Here's quick guide for how to set-up your own secure connection to the internet, that will protect your privacy by encrypting your HTTP traffic for every webservice you visit on the web.  In practical terms, this means your ISP will not be able to view your browsing history.  This guide is for Windows users.  An OSX guide is coming soon.  Always know what you're doing.  I take no responsibility for any computer mishaps.  If you follow this guide, you should not run into any issues.

## Task 1: Install Putty

* (1) Download Putty, which is a free software available here: https://the.earth.li/~sgtatham/putty/latest/w64/putty-64bit-0.68-installer.msi
* (2) Install Putty on your computer.  When it's finished installing, search for 'Putty'.  Here is what the icon looks like: https://upload.wikimedia.org/wikipedia/commons/b/b6/PuTTY_icon_128px.png.
* (3) Open Putty.  Should should see this window: https://en.wikipedia.org/wiki/PuTTY#/media/File:PuTTY_Ubuntu.png (note, this is the view if you're using Linux.  Don't worry about not seeing the Terminal (black window). 

### Subtask for Setting up Putty
* Under "Host Name" type:
```sh
cunix.cc.columbia.edu
```
* Under "Port" type:
```sh
22
```
* Under "Saved Sessions, which should be blank, type:
```sh
CUNIX-PRIVATE
```
* Then, click "Save"
* Notice the menu to the left. Scroll down and expand "SSH".  Then, click on "Tunnels"
* In "Source Port," type: 7070
* In "Destination," type: D
* Select "Dynamic" and "Auto"
* Click Add (you should now see D7070 inside the application window box)
* To back to the left menu; scroll back up to "Session"
* Click Save (again)

You now should have a saved profile for your secure connection to the CUNIX servers.

## Task 2: Connect to CUNIX

* With Putty Open, click on your newly created CUNIX-PRIVATE profile so it is highlighted in blue
* Then Click Load (a black terminal window should now appear)
* If this is your first time connecting, you may get a message asking you if you want to connect.  You should respond "Yes"
* You should then be prompted for your login, like this:
```sh
login as: yourUNI
```
* Do not enter @columbia.edu.  Your login name is just your uni.
* You will then be prompted for a password, like this:
```sh
uniID@cunix.cc.columbia.edu's password: [enter your password] [then hit "Enter"]
```
* NOTE: as you type your password, you WILL NOT see any characters.  This is a security feature of the secure shell you are using
* You should now see a welcome message that reads:
```sh
Last login: Mon Mar 13 22:07:00 2017 from xxx.xxx.xxx.xxx
-bash-4.1$
```
* If you see this, congrats!  You are now logged into the CUNIX server.  Let's try to send a command to the server just to make sure
* Type the following:
```sh
-bash-4.1$ pwd
```
* You should see what is called the Present Working Directory (pwd), which is your current location in the CUNIX universe.
* Want a more interesting command?  Type:
```sh
-bash-4.1$ who
```
* You should now have a listing of every other Lion who is currently logged in
* Want to clear your screen? Type:
```sh
-bash-4.1$ clear
```
* Now that your connection has been opened, you should minimize Putty (BUT KEEP THE TERMINAL OPEN TO MAINTAIN THE CONNECTION)
* On to Task 3

## Task 3: Configure Web browser

I will assume you are using Chrome, since a good majority of the world uses Chrome.  Future iterations of this guide will have instructions for FireFox, but the instructions are pretty similar.

* Open Chrome, and go to settings, and then select "show advanced settings"
* Find "Change Proxy Settings" under the "Network Sub-menu"
* Under "Connections," at the bottom, click "LAN Settings"
* A new window should pop-up
* At the bottom, put a check mark next to "Use a proxy server for your LAN (These settings will ....)
* Then Click "Advanced" (but it's not really advanced, I promise)
* Notice the "Socks:" field? Type: 
```sh
Socks: localhost
```
* Enter the port number (quiz: do you remember it?)
```sh
Port: 7070
```
* Then Click "OK"
* Then Click "OK" (again)


## Task 3: Verify your secure IP Address

```sh
>>ssh uniID@cunix.cc.columbia.edu -D 7070
>>login as: uniID
>>uniID@cunix.cc.columbia.edu's password:
>>Last login: Mon Mar 13 21:31:10 2017 from 64.94.31.206
-bash-4.1$ #note the "$" symbol means you have accessed the server and are now sitting in your personal directory
$ ls # to list your files (there may be none)
$ mkdir [name of some folder]
$ ls # you should now see [name of some folder]
``` 
