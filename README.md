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
  ctrl + cmd + k on OS X, or ctrl + alt + k on Windows
```

# Installation

### Package Control
Using [Package Control](http://wbond.net/sublime_packages/package_control), a
package manager for Sublime Text 2.

In ST2, press "cmd + shift + p" and then type "install".

Once you see "Package Control: Install Package", enter.

When the packages load, another selection window will appear. Type

BeautifyTex and enter. All done!

### Manual Installation

```bash
  cd "~/Library/Application Support/Sublime Text 2/Packages/"
  git clone git://github.com/ketan/BeautifyLatex.git
```
