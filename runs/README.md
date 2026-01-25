# 2026-01-25

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.8736   |       1.04677  |   0.101157 |
| solution-aron-mark |     0.467889 |       0.167889 |   0.241527 |
| solution-pl        |     0.466852 |       0.162117 |   0.242192 |
| solution-1-flask   |     0.496582 |       1.00982  |   0.268245 |
| solution-1         |     8.06321  |       1e-06    |   0.595405 |
| solution-2         |     4.99578  |       0.641457 |   1.05665  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.463272 |       0.161147 |   0.365708 |
| solution-pl        |     0.467286 |       0.162592 |   0.368335 |
| solution-flask     |     0.461754 |       1.00842  |   0.377506 |
| solution-1-flask   |     0.476628 |       1.00849  |   0.793741 |
| solution-2         |     0.461881 |       0.503053 |   4.11817  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.4646   |       0.167036 |    1.06497 |
| solution-pl        |     0.466854 |       0.166414 |    1.07533 |
| solution-flask     |     0.461149 |       1.0084   |    1.57493 |
| solution-1-flask   |     0.473874 |       1.00822  |    5.55893 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.465286 |       0.191505 |    3.46506 |
| solution-aron-mark |     0.467594 |       0.191798 |    3.50307 |
| solution-flask     |     0.467202 |       1.0084   |    5.08225 |