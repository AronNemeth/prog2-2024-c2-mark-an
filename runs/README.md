# 2024-12-26

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.97153  |       1.00932  |   0.104157 |
| solution-pl        |     0.549977 |       0.111767 |   0.188148 |
| solution-aron-mark |     0.544795 |       0.112636 |   0.201583 |
| solution-1-flask   |     5.67778  |       1.08246  |   0.263406 |
| solution-1         |     7.95772  |       1e-06    |   0.751446 |
| solution-2         |     0.545311 |       0.626565 |   1.49678  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.532157 |       0.111723 |   0.320612 |
| solution-aron-mark |     0.552063 |       0.115424 |   0.324801 |
| solution-flask     |     0.55267  |       1.00936  |   0.489325 |
| solution-1-flask   |     0.557327 |       1.00899  |   0.823854 |
| solution-2         |     0.557011 |       0.486604 |   2.92568  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.534408 |       0.1172   |    1.07343 |
| solution-aron-mark |     0.544054 |       0.119783 |    1.07371 |
| solution-flask     |     0.548002 |       1.00888  |    2.21448 |
| solution-1-flask   |     0.563164 |       1.00912  |    5.9665  |
| solution-2         |     0.545731 |       0.539986 |   51.1287  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.550557 |       0.147485 |    4.66935 |
| solution-aron-mark |     0.588168 |       0.147767 |    4.68719 |
| solution-flask     |     0.533105 |       1.00921  |    8.93306 |