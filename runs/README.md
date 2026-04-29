# 2026-04-29

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.4856   |       1.10351  |   0.124475 |
| solution-pl        |     0.414951 |       0.146194 |   0.228188 |
| solution-aron-mark |     4.24729  |       0.145825 |   0.232889 |
| solution-1-flask   |     0.417407 |       1.00795  |   0.276007 |
| solution-1         |     7.41058  |       2e-06    |   0.986379 |
| solution-2         |     0.411281 |       0.927058 |   0.986561 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.415044 |       0.150525 |   0.361901 |
| solution-aron-mark |     0.427037 |       0.147795 |   0.364992 |
| solution-flask     |     0.414874 |       1.00825  |   0.402245 |
| solution-1-flask   |     0.418649 |       1.0083   |   0.809635 |
| solution-2         |     0.420722 |       0.512398 |   3.41805  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.413914 |       0.154423 |    1.07165 |
| solution-aron-mark |     0.415953 |       0.152625 |    1.07952 |
| solution-flask     |     0.414062 |       1.00829  |    1.62781 |
| solution-1-flask   |     0.42033  |       1.00817  |    5.62162 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.41877  |       0.178556 |    3.72882 |
| solution-pl        |     0.41816  |       0.178342 |    3.7454  |
| solution-flask     |     0.416143 |       1.00829  |    5.26604 |