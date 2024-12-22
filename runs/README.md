# 2024-12-22

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.9361   |       1.00886  |   0.106431 |
| solution-pl        |     0.533215 |       0.107748 |   0.185066 |
| solution-aron-mark |     0.534779 |       0.106458 |   0.187401 |
| solution-1-flask   |     5.64109  |       1.09974  |   0.267196 |
| solution-1         |     8.25138  |       1e-06    |   0.970342 |
| solution-2         |     0.530019 |       0.684747 |   1.0982   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.535458 |       0.110995 |   0.312914 |
| solution-pl        |     0.53058  |       0.114511 |   0.320054 |
| solution-flask     |     0.535002 |       1.00915  |   0.50179  |
| solution-1-flask   |     0.536061 |       1.00875  |   0.810205 |
| solution-2         |     0.536133 |       0.472139 |   4.33097  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.535364 |       0.115507 |    1.0806  |
| solution-pl        |     0.535294 |       0.115276 |    1.08561 |
| solution-flask     |     0.534776 |       1.00895  |    2.27901 |
| solution-1-flask   |     0.559471 |       1.01033  |    5.83627 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.53218  |       0.142996 |    4.28    |
| solution-aron-mark |     0.53363  |       0.144931 |    4.30789 |
| solution-flask     |     0.540882 |       1.00909  |    8.69798 |