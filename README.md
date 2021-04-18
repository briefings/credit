
This is focused on Professor Dr. Hans Hofmann's [German Credit Data](https://archive.ics.uci.edu/ml/datasets/Statlog+%28German+Credit+Data%29)

<br>

### Development Notes

<br>

**Environment**

Refer to the [github.com/briefings/energy Development Notes](https://github.com/briefings/energy#development-notes), it outlines the
creation & usage of the environment `miscellaneous`, which is used by this repository also.

<br>

**Requirements**

```bash
    conda activate miscellaneous
    pip freeze -r docs/filter.txt > requirements.txt
```

whereby filter.txt does not include `python-graphviz`, `pywin32`, `nodejs`.  And, w.r.t. conventions

```bash
    pylint --generate-rcfile > .pylintrc
```

<br>
