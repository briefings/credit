<br>

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
<br>

### Encoding

  `dictionary = {`
      
        'e_chq_acc_status': {'A11': 0, 'A12': 1, 'A13': 2, 'A14': 3},    
        'credit_history': {'A30': 0, 'A31': 1, 'A32': 2, 'A33': 3, 'A34': 4},
        'purpose': {'A40': 0, 'A41': 1, 'A42': 2, 'A43': 3, 'A44': 4, 'A45': 5, 'A46': 6, 'A47': 7,
                    'A48': 8, 'A49': 9, 'A410': 10},    
        'savings_acc_class': {'A61': 0, 'A62': 1, 'A63': 2, 'A64': 3, 'A65': 4},    
        'curr_emp_class': {'A71': 0, 'A72': 1, 'A73': 2, 'A74': 3, 'A75': 4},    
        'sex_and_status': {'A91': 0, 'A92': 1, 'A93': 2, 'A94': 3, 'A95': 4},    
        'other_debtors_class': {'A101': 0, 'A102': 1, 'A103': 2},    
        'property': {'A121': 0, 'A122': 1, 'A123': 2, 'A124': 3},    
        'other_i_plans': {'A141': 0, 'A142': 1, 'A143': 2},    
        'housing': {'A151': 0, 'A152': 1, 'A153': 2},    
        'job': {'A171': 0, 'A172': 1, 'A173': 2, 'A174': 3},    
        'telephone': {'A191': 0, 'A192': 1},    
        'foreign_worker': {'A201': 1, 'A202': 0}
  
  `}`







