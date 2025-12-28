# 2025-12-28

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.81914  |       1.03326  |   0.095744 |
| solution-pl        |     0.474811 |       0.164524 |   0.245773 |
| solution-aron-mark |     0.476682 |       0.166422 |   0.245801 |
| solution-1-flask   |     0.491499 |       1.00827  |   0.258349 |
| solution-1         |     7.95461  |       1e-06    |   0.703941 |
| solution-2         |     4.772    |       0.650768 |   1.47035  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.478608 |       1.00835  |   0.362334 |
| solution-pl        |     0.48368  |       0.166509 |   0.365135 |
| solution-aron-mark |     0.481716 |       0.165394 |   0.369292 |
| solution-1-flask   |     0.478837 |       1.00843  |   0.798353 |
| solution-2         |     0.476233 |       0.512889 |  21.9371   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.480651 |       0.172385 |    1.06699 |
| solution-pl        |     0.476154 |       0.170746 |    1.07421 |
| solution-flask     |     0.476156 |       1.0085   |    1.56395 |
| solution-1-flask   |     0.479538 |       1.00847  |    5.61191 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.477723 |       0.192569 |    3.51788 |
| solution-pl        |     0.476224 |       0.194613 |    3.5457  |
| solution-flask     |     0.474281 |       1.00852  |    5.06935 |