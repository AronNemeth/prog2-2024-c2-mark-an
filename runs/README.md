# 2025-08-30

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.467439 |       1.00823  |   0.096839 |
| solution-aron-mark |     0.45339  |       0.147132 |   0.229342 |
| solution-pl        |     5.45047  |       0.191599 |   0.229609 |
| solution-1-flask   |     1.0508   |       1.06549  |   0.248537 |
| solution-1         |     7.24486  |       1e-06    |   0.643066 |
| solution-2         |     0.475765 |       0.569705 |   1.5934   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.477257 |       0.150362 |   0.350416 |
| solution-aron-mark |     0.466172 |       0.1478   |   0.356749 |
| solution-flask     |     0.464526 |       1.00848  |   0.364787 |
| solution-1-flask   |     0.480928 |       1.0081   |   0.776846 |
| solution-2         |     0.461188 |       0.49929  |   3.83856  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.469653 |       0.158104 |    1.04354 |
| solution-pl        |     0.475246 |       0.15813  |    1.06432 |
| solution-flask     |     0.467766 |       1.00861  |    1.53227 |
| solution-1-flask   |     0.483864 |       1.00822  |    5.49356 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.472696 |       0.186534 |    3.14933 |
| solution-pl        |     0.466735 |       0.189829 |    3.16185 |
| solution-flask     |     0.469556 |       1.00905  |    4.93416 |