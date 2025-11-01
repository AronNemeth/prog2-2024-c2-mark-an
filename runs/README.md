# 2025-11-01

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.3097   |       1.05861  |   0.099354 |
| solution-aron-mark |     0.921451 |       0.154824 |   0.240431 |
| solution-pl        |     0.46382  |       0.15896  |   0.244273 |
| solution-1-flask   |     0.863178 |       1.00821  |   0.264716 |
| solution-1         |     7.89798  |       1e-06    |   0.723033 |
| solution-2         |     5.00089  |       0.726428 |   1.18847  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.46545  |       0.159887 |   0.360327 |
| solution-aron-mark |     0.464377 |       0.160765 |   0.365651 |
| solution-flask     |     0.463105 |       1.00813  |   0.372623 |
| solution-1-flask   |     0.470628 |       1.00827  |   0.784111 |
| solution-2         |     0.464419 |       0.502129 |   3.28734  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.469502 |       0.16655  |    1.06086 |
| solution-aron-mark |     0.467927 |       0.164728 |    1.06427 |
| solution-flask     |     0.468872 |       1.00848  |    1.55876 |
| solution-1-flask   |     0.479046 |       1.00846  |    5.60742 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.46851  |       0.198174 |    3.17104 |
| solution-pl        |     0.467136 |       0.194508 |    3.17564 |
| solution-flask     |     0.464949 |       1.00848  |    5.0343  |