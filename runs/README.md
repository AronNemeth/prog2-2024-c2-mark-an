# 2025-08-05

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.40538  |       1.31047  |   0.100246 |
| solution-pl        |     0.504029 |       0.151608 |   0.235682 |
| solution-aron-mark |     4.85978  |       0.157544 |   0.237597 |
| solution-1-flask   |     0.51788  |       1.00819  |   0.268075 |
| solution-1         |     7.74443  |       1e-06    |   0.699602 |
| solution-2         |     0.505051 |       0.627748 |   0.933266 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.504103 |       0.152941 |   0.362381 |
| solution-aron-mark |     0.518384 |       0.154082 |   0.366405 |
| solution-flask     |     0.502938 |       1.00824  |   0.377007 |
| solution-1-flask   |     0.521891 |       1.00863  |   0.794749 |
| solution-2         |     0.503327 |       0.509446 |   3.10044  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.511098 |       0.161483 |    1.064   |
| solution-pl        |     0.509007 |       0.158718 |    1.0652  |
| solution-flask     |     0.511899 |       1.00854  |    1.58175 |
| solution-1-flask   |     0.514012 |       1.00851  |    5.71634 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.512917 |       0.190884 |    3.22904 |
| solution-pl        |     0.499428 |       0.189044 |    3.26615 |
| solution-flask     |     0.511036 |       1.00841  |    5.13102 |