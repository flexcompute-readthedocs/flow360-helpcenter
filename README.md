# Actual README for the helpcenter repo

## Actions performed before deployment

To comply with bothe vuepress and myst + sphinx renderers, some specific macros are removed using the `clear_myst_toctrees.py` script. 
Those include:
* actual toctrees looking like:
```md
```markdown
```{toctree}
:hidden:
:maxdepth: 3
path/to/your/file1.md
path/to/your/file2.md
```
```
```

* stable references to sections: `(reference-name)=`