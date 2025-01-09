# 2025-01-09

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.89884  |       1.00883  |   0.104975 |
| solution-pl        |     0.543293 |       0.112845 |   0.193072 |
| solution-aron-mark |     0.543862 |       0.113851 |   0.19447  |
| solution-1-flask   |     5.3714   |       1.05379  |   0.276327 |
| solution-1         |     7.99289  |       1e-06    |   0.711848 |
| solution-2         |     0.542844 |       0.639412 |   0.990346 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.549665 |       0.115356 |   0.31901  |
| solution-pl        |     0.565023 |       0.113297 |   0.32123  |
| solution-flask     |     0.545695 |       1.009    |   0.488009 |
| solution-1-flask   |     0.578851 |       1.00918  |   0.798494 |
| solution-2         |     0.556635 |       0.53417  |   4.15207  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.572956 |       0.123624 |    1.06946 |
| solution-pl        |     0.546224 |       0.124401 |    1.08993 |
| solution-flask     |     0.541563 |       1.00917  |    2.19517 |
| solution-1-flask   |     0.554083 |       1.00999  |    5.7596  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.545028 |       0.148439 |    4.81404 |
| solution-pl        |     0.559574 |       0.152283 |    5.26484 |
| solution-flask     |     0.538918 |       1.00933  |    9.36014 |