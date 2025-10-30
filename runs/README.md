# 2025-10-30

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.79563  |       1.06852  |   0.104614 |
| solution-aron-mark |     0.495147 |       0.156073 |   0.249482 |
| solution-pl        |     0.510595 |       0.167176 |   0.254594 |
| solution-1-flask   |     0.495808 |       1.00811  |   0.275113 |
| solution-1         |     7.7407   |       1e-06    |   0.826644 |
| solution-2         |     4.77591  |       0.737948 |   0.970365 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.498764 |       0.164927 |   0.378014 |
| solution-flask     |     0.502994 |       1.00841  |   0.386746 |
| solution-aron-mark |     0.499516 |       0.19275  |   0.397682 |
| solution-1-flask   |     0.501603 |       1.0087   |   0.817504 |
| solution-2         |     0.520159 |       0.537591 |   3.9324   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.495051 |       0.167684 |    1.081   |
| solution-pl        |     0.51592  |       0.171024 |    1.08623 |
| solution-flask     |     0.502067 |       1.00838  |    1.58773 |
| solution-1-flask   |     0.505997 |       1.0087   |    5.85998 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.504176 |       0.199862 |    3.35417 |
| solution-pl        |     0.497651 |       0.2021   |    3.46046 |
| solution-flask     |     0.498047 |       1.00863  |    5.25429 |