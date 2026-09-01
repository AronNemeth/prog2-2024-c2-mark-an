# 2026-09-01

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     5.46262  |       1.15483  |   0.069601 |
| solution-1-flask   |     0.294438 |       1.00627  |   0.153893 |
| solution-pl        |     0.293542 |       0.105278 |   0.155075 |
| solution-aron-mark |     3.77117  |       0.111387 |   0.161357 |
| solution-1         |     6.12039  |       1e-06    |   0.497988 |
| solution-2         |     0.284121 |       0.681269 |   0.659833 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.290634 |       0.123714 |   0.248203 |
| solution-pl        |     0.292341 |       0.109422 |   0.2501   |
| solution-flask     |     0.315684 |       1.00583  |   0.29051  |
| solution-1-flask   |     0.297773 |       1.00615  |   0.47999  |
| solution-2         |     0.289123 |       0.354809 |   2.48734  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.329827 |       0.25122  |   0.803591 |
| solution-pl        |     0.323748 |       0.121302 |   0.824637 |
| solution-flask     |     0.289589 |       1.0062   |   1.37128  |
| solution-1-flask   |     0.299568 |       1.00625  |   4.02837  |
| solution-2         |     0.290272 |       0.409848 |  32.7275   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.33147  |       0.149635 |    3.29347 |
| solution-aron-mark |     0.290655 |       0.212022 |    3.51477 |
| solution-flask     |     0.292368 |       1.00625  |    4.12874 |