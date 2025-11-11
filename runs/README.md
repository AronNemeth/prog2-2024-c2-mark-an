# 2025-11-11

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.82072  |       1.05247  |   0.101995 |
| solution-pl        |     0.485529 |       0.162951 |   0.253505 |
| solution-aron-mark |     0.494819 |       0.165079 |   0.254257 |
| solution-1-flask   |     0.511457 |       1.00811  |   0.270454 |
| solution-1         |     8.96287  |       1e-06    |   0.865334 |
| solution-2         |     5.38846  |       0.772089 |   0.972147 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.485668 |       1.00844  |   0.372933 |
| solution-aron-mark |     0.477474 |       0.163202 |   0.381543 |
| solution-pl        |     0.518477 |       0.167599 |   0.382297 |
| solution-1-flask   |     0.502957 |       1.00879  |   0.820751 |
| solution-2         |     0.479188 |       0.527428 |   2.79343  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.475427 |       0.169005 |    1.06495 |
| solution-pl        |     0.476763 |       0.168493 |    1.06559 |
| solution-flask     |     0.486326 |       1.0086   |    1.5744  |
| solution-1-flask   |     0.477807 |       1.00848  |    5.64084 |
| solution-2         |     0.498664 |       0.594435 |   52.6539  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.480693 |       0.199635 |    3.28677 |
| solution-aron-mark |     0.486146 |       0.199688 |    3.32093 |
| solution-flask     |     0.483105 |       1.00874  |    5.20381 |