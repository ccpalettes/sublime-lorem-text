LoremText
=========
 
[LoremText 3](https://github.com/ccpalettes/sublime-lorem-text/tree/sublime-text-3-beta) is a plugin for
[sublime text 3](http://www.sublimetext.com/3) that creates random/fixed lorem
ipsum text. Lorem ipsum is commonly used as placeholder text before you have the
real meaningful content.

#### If you are using [sublime text 2](http://www.sublimetext.com), please visit [LoremText plugin for sublime text 2](https://github.com/ccpalettes/sublime-lorem-text).

Installation
------------

**Without Git:** [Download](https://github.com/ccpalettes/sublime-lorem-text/archive/sublime-text-3-beta.zip)
the latest source from GitHub and copy the folder to the Sublime Text "Packages"
directory.

**With Git:** Clone the repository to the Sublime Text "Packages" directory,
then switch to branch "sublime-text-3-beta":

    git clone https://github.com/ccpalettes/sublime-lorem-text.git
    git checkout sublime-text-3-beta

You can open the "Packages" directory by following the steps below:

* OS X: select menu entry `Sublime Text 3 -> Preferences -> Browse Packages...`
* Windows: select menu entry `Preferences -> Browse Packages...`
* Linux: select menu entry `Preferences -> Browse Packages...`

Usage
-----

There are a few ways to use the LoremText plugin.

* Just press the shortcut key (`alt+l` on all platforms) to insert some lorem
ipsum text.
* Type `lorem({word_count}, {paragraph_count})` in your file, make sure that the
input curosr is within the region of the `lorem{?, ?}` expression, then press
the shortcut key (`alt+l`). Parameter "word_count" represents how many paragraphs
to insert and parameter "paragraph_count" represents how many words that each
paragraph contains. For example, `lorem(100, 3)` means that it will create three
paragraphs of lorem ipsum text and each paragraph contains one hundred words.
Both the two parameters are optional, if you leave them empty, the plugin will
use default values that are configured in the settings file.
* Select menu entry `Edit -> Lorem Text...`, active the sub-menu commands.
* Go to Command Palette, find "Lorem Text" command.

Settings
--------

There are a number of settings available to customize the behavior of LoremText
and The default settings can be viewed by accessing the `Preferences > Package
Settings > LoremText > Settings – Default` menu entry. But make sure all
customized settings should be saved to Settings – User to prevent them from
being overridden during an upgrade.

- `default_paragraph_count` *(Number)* The default number of parapraphs to be
inserted.

- `default_word_count` *(Number)* The default number of words for each parapraph
to be inserted.

- `always_start_with_lorem_ipsum` *(Boolean)* If true, the generated text will
always starts with "Lorem ipsum".

- `generate_random_text` *(Boolean)* If true, it creates different random text
content every time, otherwise, it creates text from a fixed content every time
and the "always start with lorem ipsum" option will be forced enabled.

License
-------

The code is under MIT license:

Copyright (c) 2013

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.