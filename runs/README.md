# 2025-04-07

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.529781 |       1.00884  |   0.083754 |
| solution-aron-mark |     2.14013  |       0.122689 |   0.188274 |
| solution-pl        |     0.530497 |       0.123158 |   0.189142 |
| solution-1-flask   |     4.92886  |       1.06519  |   0.269547 |
| solution-1         |     7.34811  |       1e-06    |   0.615255 |
| solution-2         |     0.519022 |       0.631747 |   1.0971   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.512911 |       0.123356 |   0.292267 |
| solution-aron-mark |     0.521729 |       0.123739 |   0.298612 |
| solution-flask     |     0.516671 |       1.00898  |   0.299388 |
| solution-1-flask   |     0.52532  |       1.0091   |   0.797139 |
| solution-2         |     0.536557 |       0.539928 |   4.98652  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.509052 |       0.127276 |   0.910414 |
| solution-aron-mark |     0.521523 |       0.12947  |   0.928123 |
| solution-flask     |     0.514301 |       1.00869  |   1.26329  |
| solution-1-flask   |     0.518754 |       1.0089   |   5.72215  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.513587 |       0.160902 |    2.8475  |
| solution-pl        |     0.517221 |       0.158171 |    2.8719  |
| solution-flask     |     0.518728 |       1.009    |    4.26987 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.518182 |       0.268824 |    17.0018 |
| solution-pl        |     0.525664 |       0.276534 |    17.0806 |