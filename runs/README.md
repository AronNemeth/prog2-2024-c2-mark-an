# 2026-09-08

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.19849  |       1.191    |   0.11006  |
| solution-pl        |     2.90293  |       0.167567 |   0.241233 |
| solution-aron-mark |     0.435113 |       0.161543 |   0.247525 |
| solution-1-flask   |     0.448523 |       1.00858  |   0.265171 |
| solution-1         |     7.78903  |       1e-06    |   0.654284 |
| solution-2         |     4.5379   |       0.620227 |   1.37203  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.447675 |       0.156665 |   0.36792  |
| solution-pl        |     0.450852 |       0.163852 |   0.378617 |
| solution-flask     |     0.441782 |       1.00857  |   0.394647 |
| solution-1-flask   |     0.451816 |       1.0085   |   0.813426 |
| solution-2         |     0.449754 |       0.544267 |   4.99682  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.444378 |       0.166209 |    1.1078  |
| solution-pl        |     0.452803 |       0.166132 |    1.11146 |
| solution-flask     |     0.447366 |       1.00855  |    1.65514 |
| solution-1-flask   |     0.448353 |       1.00859  |    5.8947  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.443588 |       0.191148 |    3.76248 |
| solution-aron-mark |     0.45807  |       0.324104 |    3.81293 |
| solution-flask     |     0.47351  |       1.00859  |    5.50491 |