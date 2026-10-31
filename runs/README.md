# 2026-10-31

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.459244 |       1.00925  |   0.095913 |
| solution-aron-mark |     2.30817  |       0.172962 |   0.257908 |
| solution-pl        |     0.448114 |       0.169885 |   0.258512 |
| solution-1-flask   |     1.19206  |       1.08916  |   0.274764 |
| solution-1         |     8.57628  |       1e-06    |   0.625984 |
| solution-2         |     4.70671  |       0.58348  |   0.838249 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.46437  |       1.00907  |   0.237832 |
| solution-aron-mark |     0.46487  |       0.181498 |   0.404666 |
| solution-pl        |     0.473765 |       0.183829 |   0.408984 |
| solution-1-flask   |     0.474032 |       1.00939  |   0.82762  |
| solution-2         |     0.477823 |       0.560027 |   4.21075  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.475122 |       1.00976  |    1.05273 |
| solution-aron-mark |     0.472441 |       0.184909 |    1.17442 |
| solution-pl        |     0.465427 |       0.186587 |    1.18547 |
| solution-1-flask   |     0.468361 |       1.00933  |    5.67301 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.475786 |       0.22263  |    3.83325 |
| solution-aron-mark |     0.454602 |       0.216122 |    3.8862  |
| solution-flask     |     0.456598 |       1.00885  |    4.88763 |