# 2024-09-30

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.96386  |       1.05051  |   0.082963 |
| solution-pl        |     0.567317 |       0.103373 |   0.178679 |
| solution-aron-mark |     2.12118  |       0.112131 |   0.186525 |
| solution-1-flask   |     0.586469 |       1.00852  |   0.270089 |
| solution-1         |     8.93289  |       1e-06    |   0.832884 |
| solution-2         |     4.97343  |       0.688942 |   1.11521  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.581816 |       1.00835  |   0.208592 |
| solution-pl        |     0.583315 |       0.104951 |   0.306923 |
| solution-aron-mark |     0.569856 |       0.103371 |   0.312353 |
| solution-1-flask   |     0.592271 |       1.00835  |   0.784973 |
| solution-2         |     0.57867  |       0.503689 |   4.83959  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.569597 |       1.00817  |   0.943154 |
| solution-aron-mark |     0.562524 |       0.110138 |   1.04411  |
| solution-pl        |     0.566573 |       0.111902 |   1.06374  |
| solution-1-flask   |     0.595288 |       1.00807  |   5.51661  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.564987 |       1.00836  |    4.23592 |
| solution-pl        |     0.560384 |       0.139551 |    4.51094 |
| solution-aron-mark |     0.576442 |       0.142284 |    4.57486 |