# 2025-08-11

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.37677  |       1.26803  |   0.10153  |
| solution-aron-mark |     4.54352  |       0.151368 |   0.236115 |
| solution-pl        |     0.492218 |       0.19511  |   0.238065 |
| solution-1-flask   |     0.480893 |       1.00828  |   0.269277 |
| solution-1         |     7.48087  |       1e-06    |   0.693892 |
| solution-2         |     0.473208 |       0.6241   |   0.899885 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.476605 |       0.153634 |   0.363342 |
| solution-aron-mark |     0.48184  |       0.156378 |   0.369282 |
| solution-flask     |     0.472874 |       1.00843  |   0.379216 |
| solution-1-flask   |     0.482457 |       1.00846  |   0.797129 |
| solution-2         |     0.476545 |       0.504528 |   2.28748  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.477852 |       0.159733 |    1.07395 |
| solution-pl        |     0.477026 |       0.164214 |    1.07641 |
| solution-flask     |     0.474161 |       1.00849  |    1.58681 |
| solution-1-flask   |     0.480859 |       1.00845  |    5.65223 |
| solution-2         |     0.474072 |       0.557229 |   36.1025  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.475506 |       0.191439 |    3.2082  |
| solution-aron-mark |     0.482831 |       0.190897 |    3.22517 |
| solution-flask     |     0.487911 |       1.00848  |    5.09114 |