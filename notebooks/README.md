<br>

Thus far:

* [data.ipynb](https://colab.research.google.com/github/exhypotheses/credit/blob/develop/notebooks/data.ipynb)
* [embeddings.ipynb](https://colab.research.google.com/github/exhypotheses/credit/blob/develop/notebooks/embeddings.ipynb)

<br>
<br>

In relation to [data.ipynb](https://colab.research.google.com/github/exhypotheses/credit/blob/develop/notebooks/data.ipynb), edit the *help dictionary* such that

```
{'a name':
    {'source': the data file name, 
     'labels': [the list of target variables],
     'numeric': [the list of numeric fields], 
     'categoricalFields': [the list of categorical fields],
     'binaryFields': [the list of binary categorical fields], 
     'categoryGroups':  {'field name': [list of discrete choices], ...}
    }}
```

becomes

```
    {'a name':
    {'source': the data file name, 
     'target': [the list of target variables],
     'numeric': [the list of numeric fields], 
     'categoricalFields': [the list of categorical fields],
     'binaryCF': [the list of binary categorical fields],      
     'polytomousCF':  {'field name': [list of discrete choices], ...}
    }}
```

Note that categoryGroups/polytomousCF is a dictionary of polytomous categorical fields and their members.

<br>
<br>
<br>
<br>
