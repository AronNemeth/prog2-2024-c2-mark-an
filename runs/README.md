# 2026-04-01

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.4023   |       1.06696  |   0.101961 |
| solution-aron-mark |     0.41537  |       0.145962 |   0.228528 |
| solution-pl        |     4.32557  |       0.147489 |   0.230381 |
| solution-1-flask   |     0.414277 |       1.00805  |   0.257611 |
| solution-1         |     7.18668  |       1e-06    |   0.674512 |
| solution-2         |     0.408853 |       0.598452 |   1.26458  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.409276 |       0.146764 |   0.355459 |
| solution-pl        |     0.414759 |       0.146403 |   0.367171 |
| solution-flask     |     0.417617 |       1.00806  |   0.379794 |
| solution-1-flask   |     0.412011 |       1.00802  |   0.797435 |
| solution-2         |     0.410051 |       0.503168 |   2.83691  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.417518 |       0.153536 |    1.08791 |
| solution-aron-mark |     0.415447 |       0.15121  |    1.11496 |
| solution-flask     |     0.407964 |       1.00795  |    1.63684 |
| solution-1-flask   |     0.418164 |       1.00819  |    5.89163 |
| solution-2         |     0.409043 |       0.556934 |   31.398   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.412706 |       0.178238 |    3.97199 |
| solution-pl        |     0.402479 |       0.190882 |    4.19541 |
| solution-flask     |     0.428252 |       1.00873  |    5.21257 |