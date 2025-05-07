# 2025-05-07

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.47142  |       1.0088   |   0.08581  |
| solution-pl        |     0.464108 |       0.119735 |   0.191103 |
| solution-aron-mark |     1.73965  |       0.121476 |   0.19659  |
| solution-1-flask   |     1.04793  |       1.04085  |   0.268619 |
| solution-1         |     7.57948  |       1e-06    |   0.691643 |
| solution-2         |     4.39098  |       0.675412 |   0.867911 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.46699  |       1.00906  |   0.300371 |
| solution-aron-mark |     0.49393  |       0.129709 |   0.303112 |
| solution-pl        |     0.477746 |       0.125977 |   0.303284 |
| solution-1-flask   |     0.492442 |       1.00888  |   0.785618 |
| solution-2         |     0.463309 |       0.523967 |   3.80253  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.486476 |       0.130829 |   0.900996 |
| solution-pl        |     0.479762 |       0.130374 |   0.90361  |
| solution-flask     |     0.468015 |       1.00907  |   1.26014  |
| solution-1-flask   |     0.478502 |       1.00911  |   5.55001  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.476006 |       0.166858 |    2.86506 |
| solution-aron-mark |     0.475381 |       0.164259 |    2.88892 |
| solution-flask     |     0.46336  |       1.00908  |    4.31455 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.472953 |       0.276929 |    16.0889 |
| solution-aron-mark |     0.482342 |       0.268021 |    16.6919 |