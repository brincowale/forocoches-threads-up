# Forocoches Threads UP
This script is designed to keep a thread more visible. Using spintax the script will change the word used to keep up the thread. To avoid flood or spam, only the last "UP" will remain on the thread, the old messages will be deleted after the new is published.

## Install
1. Install [Spintax](https://github.com/rexibit/spintax)
2. Edit config.json
3. Run up_threads.py

## Config file
The configuration file has three sections:

1. threads  
**name**: is not used, only for reference  
**last_post_id**: empty by default, is used by the script the first time a message was published on this thread  
**thread_id**: the id of the current thread  
**words_up_thread**: defines what group contains the used words  
**account**: the username of your account  

2. words_up_thread  
**default**: the default group of words in spintax format  

3. forocoches_accounts  
**username**: the key is your username, and the value is your password  

See config_example.json for reference.

 ## License
 The MIT License (MIT)

Copyright (c) <2016> <brincowale>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
