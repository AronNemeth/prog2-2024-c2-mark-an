# 2024-05-09

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.705453 |       1.00894  |   0.075686 |
| solution-pl        |     6.34312  |       0.124471 |   0.179406 |
| solution-aron-mark |     0.673085 |       0.11926  |   0.181267 |
| solution-1-flask   |     1.35141  |       1.08989  |   0.259052 |
| solution-1         |     8.39564  |       1e-06    |   0.600525 |
| solution-2         |     0.679596 |       0.440784 |   1.3061   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.688673 |       1.00949  |   0.167366 |
| solution-pl        |     0.683085 |       0.129706 |   0.277858 |
| solution-aron-mark |     0.687336 |       0.129358 |   0.278244 |
| solution-1-flask   |     0.705988 |       1.00947  |   0.797327 |
| solution-2         |     0.678717 |       0.441896 |   6.60766  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.679173 |       1.00929  |   0.717166 |
| solution-pl        |     0.684353 |       0.136343 |   0.833112 |
| solution-aron-mark |     0.700944 |       0.139827 |   0.833498 |
| solution-1-flask   |     0.695301 |       1.0096   |   5.5144   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.687809 |       1.00927  |    2.58579 |
| solution-pl        |     0.685173 |       0.175054 |    2.74945 |
| solution-aron-mark |     0.696578 |       0.175647 |    2.76973 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.683534 |       0.294079 |    19.981  |
| solution-flask     |     0.705329 |       1.01017  |    20.1014 |
| solution-pl        |     0.69631  |       0.304044 |    20.5834 |