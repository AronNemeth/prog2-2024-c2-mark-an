# 2025-08-09

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.94464  |       1.07469  |   0.097754 |
| solution-aron-mark |     4.4147   |       0.149912 |   0.234566 |
| solution-pl        |     0.470242 |       0.158782 |   0.238569 |
| solution-1-flask   |     0.477587 |       1.00801  |   0.267914 |
| solution-1         |     7.83462  |       1e-06    |   0.697027 |
| solution-2         |     0.470002 |       0.61304  |   1.40357  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.471352 |       0.150651 |   0.360561 |
| solution-pl        |     0.480877 |       0.155223 |   0.365494 |
| solution-flask     |     0.483169 |       1.00837  |   0.371652 |
| solution-1-flask   |     0.487453 |       1.00838  |   0.801996 |
| solution-2         |     0.485157 |       0.497759 |  12.9145   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.478693 |       0.1601   |    1.07516 |
| solution-aron-mark |     0.493485 |       0.162473 |    1.07584 |
| solution-flask     |     0.486927 |       1.00835  |    1.58245 |
| solution-1-flask   |     0.484323 |       1.00841  |    5.65018 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.481354 |       0.190626 |    3.23835 |
| solution-aron-mark |     0.486896 |       0.190767 |    3.26084 |
| solution-flask     |     0.475175 |       1.00849  |    5.15278 |