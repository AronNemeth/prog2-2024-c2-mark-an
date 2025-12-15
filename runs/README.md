# 2025-12-15

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.88475  |       1.05457  |   0.099356 |
| solution-pl        |     0.488908 |       0.160568 |   0.246926 |
| solution-aron-mark |     0.47587  |       0.161456 |   0.248102 |
| solution-1-flask   |     0.485888 |       1.0082   |   0.272654 |
| solution-1         |     8.09505  |       1e-06    |   0.676242 |
| solution-2         |     4.90123  |       0.611439 |   1.29476  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.482688 |       0.168913 |   0.367218 |
| solution-pl        |     0.507641 |       0.176506 |   0.372704 |
| solution-flask     |     0.510155 |       1.0087   |   0.383458 |
| solution-1-flask   |     0.484665 |       1.00853  |   0.802954 |
| solution-2         |     0.470559 |       0.510853 |   3.54232  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.492145 |       0.173557 |    1.08543 |
| solution-aron-mark |     0.482184 |       0.173644 |    1.09653 |
| solution-flask     |     0.47574  |       1.00875  |    1.57905 |
| solution-1-flask   |     0.491539 |       1.00861  |    6.12695 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.470358 |       0.200943 |    3.536   |
| solution-pl        |     0.475234 |       0.193517 |    3.5621  |
| solution-flask     |     0.472746 |       1.0085   |    5.09731 |