# 2025-10-18

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.41033  |       1.06309  |   0.099551 |
| solution-aron-mark |     0.485164 |       0.156053 |   0.240844 |
| solution-pl        |     4.35215  |       0.154401 |   0.243146 |
| solution-1-flask   |     0.492968 |       1.00815  |   0.264839 |
| solution-1         |     7.79414  |       1e-06    |   0.894231 |
| solution-2         |     0.488021 |       0.886432 |   1.54154  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.489167 |       0.154287 |   0.370804 |
| solution-flask     |     0.489881 |       1.00852  |   0.375295 |
| solution-aron-mark |     0.489987 |       0.156168 |   0.378512 |
| solution-1-flask   |     0.490674 |       1.00827  |   0.787459 |
| solution-2         |     0.484404 |       0.499165 |  12.1896   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.486766 |       0.166536 |    1.09563 |
| solution-aron-mark |     0.491768 |       0.16554  |    1.10125 |
| solution-flask     |     0.486696 |       1.00952  |    1.60715 |
| solution-1-flask   |     0.493876 |       1.00854  |    5.55463 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.494234 |       0.194643 |    3.31963 |
| solution-pl        |     0.487372 |       0.193202 |    3.32008 |
| solution-flask     |     0.485599 |       1.00836  |    5.12721 |