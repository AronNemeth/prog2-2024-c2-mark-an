# 2024-09-16

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.16187  |       1.06353  |   0.092002 |
| solution-aron-mark |     5.66474  |       0.104093 |   0.170307 |
| solution-pl        |     0.550457 |       0.104387 |   0.183612 |
| solution-1-flask   |     0.559474 |       1.00918  |   0.262453 |
| solution-1         |     7.44174  |       1e-06    |   0.592057 |
| solution-2         |     0.550168 |       0.500094 |   0.984594 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.555832 |       1.00915  |   0.22223  |
| solution-pl        |     0.552801 |       0.103296 |   0.296202 |
| solution-aron-mark |     0.547584 |       0.10445  |   0.30398  |
| solution-1-flask   |     0.565068 |       1.00913  |   0.77474  |
| solution-2         |     0.547984 |       0.476671 |   4.48092  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.549301 |       1.00916  |   0.904655 |
| solution-pl        |     0.551932 |       0.111569 |   0.984403 |
| solution-aron-mark |     0.549041 |       0.11141  |   0.989173 |
| solution-1-flask   |     0.556732 |       1.00927  |   5.5248   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.55402  |       0.144424 |    4.23051 |
| solution-aron-mark |     0.556524 |       0.14242  |    4.35076 |
| solution-flask     |     0.562356 |       1.00972  |    4.42214 |