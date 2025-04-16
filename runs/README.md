# 2025-04-16

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.507151 |       1.00935  |   0.08402  |
| solution-pl        |     0.513333 |       0.119362 |   0.184803 |
| solution-aron-mark |     1.78218  |       0.12075  |   0.193648 |
| solution-1-flask   |     4.78805  |       1.11113  |   0.269302 |
| solution-1         |     7.29947  |       1e-06    |   0.603302 |
| solution-2         |     0.508014 |       0.571481 |   1.16916  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.513205 |       0.122326 |   0.292471 |
| solution-aron-mark |     0.513309 |       0.121317 |   0.29275  |
| solution-flask     |     0.512606 |       1.00928  |   0.298044 |
| solution-1-flask   |     0.51245  |       1.00858  |   0.791241 |
| solution-2         |     0.507659 |       0.50964  |   3.41735  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.506495 |       0.128823 |    0.8913  |
| solution-pl        |     0.507496 |       0.127719 |    0.91141 |
| solution-flask     |     0.507388 |       1.00927  |    1.26995 |
| solution-1-flask   |     0.514539 |       1.00911  |    5.3488  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.511285 |       0.15701  |    2.8272  |
| solution-aron-mark |     0.516432 |       0.157585 |    2.86768 |
| solution-flask     |     0.511515 |       1.00897  |    4.23622 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.508443 |       0.268229 |    16.7057 |
| solution-aron-mark |     0.513825 |       0.265583 |    16.8384 |