# Protecting Your Privacy Online --- Connecting to a secured SOCKS proxy with your Columbia University ID
## stephan s. dalal --- March 2017

# Establishing a Connection to the Columbia Unix Servers

### Fellow Lions, you may not be surprised that Columbia hosts some of the most powerful UNIX stacks.  You may be surprised to know that every student enjoys lifetime (as of now) access to the UNIX stack.


(1) Download Putty, which is a free software available here: https://the.earth.li/~sgtatham/putty/latest/w64/putty-64bit-0.68-installer.msi

connect to the Unix Stack and instruct your computer to establish a secure socks proxy operating on port 7070, like this:

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
