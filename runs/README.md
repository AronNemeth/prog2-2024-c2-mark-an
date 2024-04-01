# 2024-04-01

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.70421  |       1.07985  |   0.096984 |
| solution-pl        |     0.672501 |       0.111742 |   0.166818 |
| solution-aron-mark |     0.669509 |       0.111707 |   0.167829 |
| solution-1-flask   |     0.690012 |       1.00905  |   0.261413 |
| solution-1         |     9.09174  |       1e-06    |   0.803696 |
| solution-2         |     5.45489  |       0.640631 |   1.39568  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.662849 |       1.00906  |   0.17449  |
| solution-pl        |     0.67049  |       0.117116 |   0.259309 |
| solution-aron-mark |     0.677778 |       0.119721 |   0.272039 |
| solution-1-flask   |     0.683028 |       1.00934  |   0.787381 |
| solution-2         |     0.667977 |       0.451213 |   4.30508  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.690088 |       0.127277 |   0.81759  |
| solution-aron-mark |     0.68389  |       0.128129 |   0.818526 |
| solution-flask     |     0.698113 |       1.00932  |   0.925101 |
| solution-1-flask   |     0.706835 |       1.00894  |   5.60227  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.674632 |       0.157061 |    3.29787 |
| solution-aron-mark |     0.679572 |       0.154598 |    3.3153  |
| solution-flask     |     0.672948 |       1.009    |    5.61726 |