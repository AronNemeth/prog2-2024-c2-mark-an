# 2024-08-11

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.550338 |       1.0089   |   0.073768 |
| solution-aron-mark |     2.01869  |       0.101805 |   0.166336 |
| solution-pl        |     0.55362  |       0.102372 |   0.184114 |
| solution-1-flask   |     1.26114  |       1.06913  |   0.258462 |
| solution-1         |     7.6658   |       1e-06    |   0.57958  |
| solution-2         |     4.48019  |       0.517845 |   0.963362 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.548968 |       1.00925  |   0.223556 |
| solution-aron-mark |     0.549711 |       0.103035 |   0.28529  |
| solution-pl        |     0.555807 |       0.102165 |   0.285617 |
| solution-1-flask   |     0.557204 |       1.00881  |   0.766881 |
| solution-2         |     0.545846 |       0.472322 |   2.60633  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.548928 |       1.00915  |   0.891809 |
| solution-pl        |     0.549012 |       0.110438 |   0.983144 |
| solution-aron-mark |     0.547103 |       0.112533 |   0.985644 |
| solution-1-flask   |     0.559989 |       1.0092   |   5.50589  |
| solution-2         |     0.54854  |       0.516365 | 302.56     |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.549481 |       1.00904  |    4.15026 |
| solution-pl        |     0.550976 |       0.145076 |    4.2427  |
| solution-aron-mark |     0.549685 |       0.146764 |    4.27791 |