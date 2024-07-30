# 2024-07-30

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.510824 |       1.00911  |   0.09593  |
| solution-aron-mark |     0.506956 |       0.102201 |   0.169516 |
| solution-pl        |     5.94184  |       0.107557 |   0.170201 |
| solution-1-flask   |     1.20918  |       1.04879  |   0.265477 |
| solution-1         |     7.8924   |       1e-06    |   0.605124 |
| solution-2         |     0.51077  |       0.526009 |   0.948649 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.510937 |       1.00898  |   0.190873 |
| solution-aron-mark |     0.51894  |       0.106414 |   0.286945 |
| solution-pl        |     0.523533 |       0.106772 |   0.288743 |
| solution-1-flask   |     0.534564 |       1.0089   |   0.770654 |
| solution-2         |     0.513492 |       0.483394 |  13.5645   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.52498  |       1.00908  |   0.892748 |
| solution-pl        |     0.541655 |       0.113144 |   0.990424 |
| solution-aron-mark |     0.50823  |       0.114381 |   0.993314 |
| solution-1-flask   |     0.535547 |       1.00924  |   5.61512  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.515177 |       1.00902  |    4.29895 |
| solution-aron-mark |     0.518051 |       0.148524 |    4.37978 |
| solution-pl        |     0.518634 |       0.150565 |    4.38659 |