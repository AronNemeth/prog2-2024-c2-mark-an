# 2026-08-25

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.10341  |       1.34235  |   0.105599 |
| solution-pl        |     0.423091 |       0.160481 |   0.236368 |
| solution-aron-mark |     4.60458  |       0.152573 |   0.240172 |
| solution-1-flask   |     0.432756 |       1.00826  |   0.268881 |
| solution-1         |     7.67792  |       1e-06    |   0.649456 |
| solution-2         |     0.42409  |       0.653225 |   0.909086 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.422598 |       0.162167 |   0.367149 |
| solution-pl        |     0.420698 |       0.155022 |   0.37065  |
| solution-flask     |     0.421429 |       1.00831  |   0.400088 |
| solution-1-flask   |     0.423834 |       1.00817  |   0.820706 |
| solution-2         |     0.420261 |       0.502058 |   4.59073  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.435066 |       0.16444  |    1.12013 |
| solution-aron-mark |     0.422772 |       0.160041 |    1.13122 |
| solution-flask     |     0.421816 |       1.00854  |    1.64607 |
| solution-1-flask   |     0.426199 |       1.00842  |    5.76839 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.420355 |       0.18316  |    3.47502 |
| solution-aron-mark |     0.425124 |       0.185473 |    3.51285 |
| solution-flask     |     0.434727 |       1.00834  |    5.3053  |