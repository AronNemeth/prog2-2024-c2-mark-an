# 2025-09-10

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.511397 |       1.00886  |   0.101604 |
| solution-aron-mark |     0.512672 |       0.158333 |   0.241128 |
| solution-pl        |     6.11615  |       0.331048 |   0.247909 |
| solution-1-flask   |     1.07722  |       1.05886  |   0.268454 |
| solution-1         |     7.67692  |       1e-06    |   0.741899 |
| solution-2         |     0.509436 |       0.71285  |   1.08321  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.514311 |       0.157868 |   0.370784 |
| solution-pl        |     0.50184  |       0.160129 |   0.373541 |
| solution-flask     |     0.482672 |       1.00839  |   0.389138 |
| solution-1-flask   |     0.503625 |       1.00854  |   0.811387 |
| solution-2         |     0.485948 |       0.507869 |   3.08159  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.496379 |       0.161579 |    1.08129 |
| solution-pl        |     0.500648 |       0.16436  |    1.11751 |
| solution-flask     |     0.495856 |       1.0084   |    1.62426 |
| solution-1-flask   |     0.48727  |       1.00875  |    5.7179  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.481147 |       0.190395 |    3.33317 |
| solution-aron-mark |     0.487748 |       0.204684 |    3.34647 |
| solution-flask     |     0.481984 |       1.00942  |    5.1599  |