# 2025-03-30

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.504638 |       1.00891  |   0.082148 |
| solution-aron-mark |     1.89513  |       0.120611 |   0.184509 |
| solution-pl        |     0.532358 |       0.126887 |   0.185478 |
| solution-1-flask   |     5.28106  |       1.11941  |   0.270513 |
| solution-1         |     7.58859  |       1e-06    |   0.831737 |
| solution-2         |     0.504926 |       0.781638 |   1.13397  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.507244 |       0.11937  |   0.29091  |
| solution-pl        |     0.503546 |       0.121115 |   0.292365 |
| solution-flask     |     0.50478  |       1.00861  |   0.300607 |
| solution-1-flask   |     0.513644 |       1.00919  |   0.791695 |
| solution-2         |     0.507862 |       0.496321 |   3.55074  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.504051 |       0.126827 |   0.898408 |
| solution-aron-mark |     0.508775 |       0.126928 |   0.900959 |
| solution-flask     |     0.504851 |       1.01207  |   1.25608  |
| solution-1-flask   |     0.52185  |       1.00883  |   5.62833  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.507973 |       0.157172 |    2.82346 |
| solution-pl        |     0.50883  |       0.157183 |    2.82408 |
| solution-flask     |     0.507303 |       1.00877  |    4.27995 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.505613 |       0.266069 |    16.0948 |
| solution-aron-mark |     0.514076 |       0.270991 |    16.5261 |