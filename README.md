# BeautifyLatex

Prettifies latex code using [latexindent.pl](https://github.com/cmhughes/latexindent.pl)

### Hooks

This package offers a pre-save hook, i.e., your latex files will be reformatted automatically before saving. To activate this feature, set:

```
  "run_on_save": true,
```


The sublime command "beautify_latex" performs a save after formatting. You can disable this default by setting:

```
  "save_on_beautify": false
```

You can change the file patterns handled by this plugin in the settings:

```
    "file_patterns": [ "\\.tex"],
```

### Tabs or Spaces

By default, Sublime does not translate tabs to spaces. If you wish to use tabs you will not need to change your settings. If you wish to use spaces, add the following setting.

```
"translate_tabs_to_spaces": true
```

### Key Binding

```
  ctrl + cmd + l on OS X, or ctrl + alt + l on Windows
```

# Installation

### Package Control
This package is a fork of [ketan/BeautifyLatex](https://github.com/ketan/BeautifyLatex), and the Sublime Text package has not been updated (as of Sep 6 2017). So you have to install the package manually.

### Manual Installation

**1. Navigate to the Sublime Text package directory**
```bash
  cd "~/Library/Application Support/Sublime Text 2/Packages/" # OS X (I think)
  cd "C:\Users\<username>\AppData\Roaming\Sublime Text 3\Packages" # (using Windows 10)
```
**2. Clone this repository**
```bash
  git clone https://github.com/flipphillips/BeautifyLatex.git
  ### Or ###
  git clone git@github.com:flipphillips/BeautifyLatex.git
```

**3. Restart Sublime Text**

### Note for Mac users
If you are using OS X El Capitan and get the following error 

    Error: can't specify None for path argument

while saving `tex` files, you may want to check the following things.

1. Do you have `latexindent`? This can be checked by typing `which latexindent` in the terminal. If you have `latexindent` installed, you shall get the following message telling you the directory, in which your `latexindent` resides.

        $ which latexindent
        /Library/TeX/texbin/latexindent

  If you do not have `latexindent` at all, you may consider upgrading your [`MacTeX`](http://tug.org/mactex/) or install `latexindent` manually. See CTAN page of `latexindent` [here](https://www.ctan.org/pkg/latexindent?lang=en).

2. Is your `latexindent` functional? To check this, go to the terminal, `cd` to the directory containing your `latexindent`, and type `perl latexindent`. If your `latexindent` is functional, you shall see its version information (see below).

        $ cd /Library/TeX/texbin/
        $ perl latexindent
        latexindent.pl version 2.1R
        usage: latexindent.pl [options] [file][.tex]
              -h  help (see the documentation for detailed instructions and examples)
              -o  output to another file; sample usage
                        latexindent.pl -o myfile.tex outputfile.tex
              -w  overwrite the current file- a backup will be made, but still be careful
              -s  silent mode- no output will be given to the terminal
              -t  tracing mode- verbose information given to the log file
              -l  use localSettings.yaml (assuming it exists in the directory of your file)
              -d  ONLY use defaultSettings.yaml, ignore ALL user files
              -c=cruft directory used to specify the location of backup files and indent.log

  Otherwise, you will see certain error message saying that `YAML::Tiny` (or some other components) was missing. To install these components, type the following lines in terminal (you may need to input your admin password).


        $ sudo cpan App::cpanminus
        $ sudo cpan YAML::Tiny
        $ sudo perl -MCPAN -e 'install "File::HomeDir"'


  After executing the above lines, check the availability of `latexindent` by typing `perl latexindent` again in the terminal.

3. Install [`Fix Mac Path`](https://packagecontrol.io/packages/Fix%20Mac%20Path) package and add the following line

        {
          "additional_path_items": ["/Library/TeX/texbin"]
        }

  in the `user` settings of `BeautifyLatex`. The string `"/Library/TeX/texbin"` is the directory containing your `latexindent`. Change it accordingly if you have a different directory.

4. If the problem has been solved, great! Otherwise (I mean you still saw `Error: can't specify None for path argument`), type the following line in terminal,
        
        $ sudo ln -s /Library/TeX/texbin/latexindent /Library/TeX/texbin/latexindent.pl
    
  which links `latexindent.pl` to `latexindent`. (It seems that by default `MacTeX` does not ship with `latexindent.pl`.) After linking, `BeautifyLatex` should run beautifully now.

As a reference, you may want to read this [thread](http://tex.stackexchange.com/questions/326600/use-latexindent-pl-with-beautifylatex-in-sublime-text/326619?noredirect=1#comment799934_326619) on tex.stackexchange.com.
