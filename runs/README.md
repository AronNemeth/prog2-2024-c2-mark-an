# 2025-01-12

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.83994  |       1.00892  |   0.104363 |
| solution-pl        |     0.541859 |       0.113913 |   0.190202 |
| solution-aron-mark |     0.544661 |       0.112471 |   0.194004 |
| solution-1-flask   |     5.06756  |       1.08965  |   0.277431 |
| solution-1         |     7.35653  |       1e-06    |   0.609809 |
| solution-2         |     0.541507 |       0.583968 |   0.795079 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.541882 |       0.115219 |   0.319134 |
| solution-aron-mark |     0.54061  |       0.114632 |   0.320409 |
| solution-flask     |     0.543717 |       1.00895  |   0.48     |
| solution-1-flask   |     0.560394 |       1.01024  |   0.808254 |
| solution-2         |     0.538034 |       0.510319 |  12.7594   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.544941 |       0.122215 |    1.09057 |
| solution-pl        |     0.540838 |       0.120548 |    1.13454 |
| solution-flask     |     0.558364 |       1.00916  |    2.18049 |
| solution-1-flask   |     0.554608 |       1.00898  |    5.8128  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.539213 |       0.151344 |    4.87249 |
| solution-pl        |     0.548034 |       0.150727 |    4.92965 |
| solution-flask     |     0.54428  |       1.00883  |    8.9924  |