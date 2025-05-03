# 2025-05-03

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.25648  |       1.09041  |   0.084673 |
| solution-pl        |     5.71551  |       0.121635 |   0.193718 |
| solution-aron-mark |     0.480904 |       0.120968 |   0.19486  |
| solution-1-flask   |     0.482131 |       1.00881  |   0.270966 |
| solution-1         |     8.03117  |       1e-06    |   0.603301 |
| solution-2         |     0.477373 |       0.553735 |   1.17418  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.469668 |       0.123121 |   0.295552 |
| solution-flask     |     0.468027 |       1.00862  |   0.296664 |
| solution-aron-mark |     0.469624 |       0.124249 |   0.29877  |
| solution-1-flask   |     0.481904 |       1.00904  |   0.793906 |
| solution-2         |     0.472967 |       0.526109 |   4.4741   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.472578 |       0.129154 |   0.886835 |
| solution-pl        |     0.470467 |       0.129895 |   0.891135 |
| solution-flask     |     0.464138 |       1.00909  |   1.238    |
| solution-1-flask   |     0.482017 |       1.00854  |   5.35478  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.46929  |       0.164048 |    2.82147 |
| solution-pl        |     0.479879 |       0.16082  |    2.834   |
| solution-flask     |     0.464206 |       1.00875  |    4.30714 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.473901 |       0.270928 |    16.6327 |
| solution-pl        |     0.471321 |       0.267749 |    16.6769 |