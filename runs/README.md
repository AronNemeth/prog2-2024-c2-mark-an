# 2024-07-24

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.511118 |       1.00957  |   0.097117 |
| solution-aron-mark |     0.510391 |       0.102999 |   0.169923 |
| solution-pl        |     6.0345   |       0.107866 |   0.170902 |
| solution-1-flask   |     1.14236  |       1.16738  |   0.26512  |
| solution-1         |     8.1709   |       1e-06    |   0.707398 |
| solution-2         |     0.513014 |       0.63876  |   0.898268 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.50376  |       1.00942  |   0.233766 |
| solution-pl        |     0.512495 |       0.104532 |   0.288766 |
| solution-aron-mark |     0.531027 |       0.108479 |   0.290486 |
| solution-1-flask   |     0.512088 |       1.00898  |   0.790617 |
| solution-2         |     0.524682 |       0.492012 |   2.86015  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.500686 |       1.00949  |   0.911817 |
| solution-pl        |     0.514929 |       0.11278  |   1.00754  |
| solution-aron-mark |     0.512529 |       0.113283 |   1.01058  |
| solution-1-flask   |     0.533008 |       1.00927  |   5.67624  |
| solution-2         |     0.52375  |       0.533411 |  48.532    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.496743 |       0.145959 |    4.39017 |
| solution-flask     |     0.51915  |       1.00954  |    4.5304  |
| solution-pl        |     0.51528  |       0.148131 |    4.75274 |