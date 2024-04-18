# 2024-04-18

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.657731 |       1.00885  |   0.064002 |
| solution-aron-mark |     0.661863 |       0.110654 |   0.164296 |
| solution-pl        |     5.8076   |       0.111864 |   0.166554 |
| solution-1-flask   |     1.31514  |       1.05986  |   0.260012 |
| solution-1         |     7.86585  |       2e-06    |   0.595897 |
| solution-2         |     0.659154 |       0.416351 |   1.54368  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.659897 |       1.00892  |   0.160844 |
| solution-aron-mark |     0.655288 |       0.120528 |   0.258579 |
| solution-pl        |     0.661534 |       0.117677 |   0.258961 |
| solution-1-flask   |     0.668824 |       1.00936  |   0.798784 |
| solution-2         |     0.667313 |       0.42713  |   2.82118  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.660092 |       1.00897  |   0.689266 |
| solution-aron-mark |     0.660636 |       0.126266 |   0.828462 |
| solution-pl        |     0.667801 |       0.125723 |   0.847106 |
| solution-1-flask   |     0.67817  |       1.00917  |   5.53097  |
| solution-2         |     0.664095 |       0.487676 |  32.5378   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.668951 |       1.00927  |    2.46545 |
| solution-aron-mark |     0.660439 |       0.16256  |    3.27612 |
| solution-pl        |     0.660619 |       0.162634 |    3.30621 |

## Inputs: 1000000, Queries 1000

| solution       |   setup_time |   preproc_time |   run_time |
|:---------------|-------------:|---------------:|-----------:|
| solution-flask |     0.664538 |        1.00962 |     16.124 |