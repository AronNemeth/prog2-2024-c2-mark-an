# 2025-08-03

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.46109  |       1.15793  |   0.097704 |
| solution-aron-mark |     4.55657  |       0.155413 |   0.233894 |
| solution-pl        |     0.511017 |       0.155489 |   0.235791 |
| solution-1-flask   |     0.519522 |       1.00819  |   0.263817 |
| solution-1         |     7.55809  |       1e-06    |   0.774248 |
| solution-2         |     0.511986 |       0.702494 |   2.07719  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.516735 |       0.155697 |   0.368176 |
| solution-aron-mark |     0.52507  |       0.160535 |   0.375316 |
| solution-flask     |     0.511303 |       1.00831  |   0.390608 |
| solution-1-flask   |     0.519768 |       1.00845  |   0.797369 |
| solution-2         |     0.515686 |       0.535336 |   2.96673  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.506973 |       0.160854 |    1.07982 |
| solution-aron-mark |     0.510284 |       0.16328  |    1.08209 |
| solution-flask     |     0.516226 |       1.00858  |    1.57011 |
| solution-1-flask   |     0.51508  |       1.00821  |    5.62084 |
| solution-2         |     0.499923 |       0.557241 |  169.209   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.505634 |       0.190835 |    3.25987 |
| solution-aron-mark |     0.511416 |       0.194724 |    3.29242 |
| solution-flask     |     0.500336 |       1.00834  |    5.11395 |