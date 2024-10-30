# 2024-10-30

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.21012  |       1.08293  |   0.110597 |
| solution-aron-mark |     0.561435 |       0.10752  |   0.191215 |
| solution-pl        |     5.71742  |       0.109944 |   0.193421 |
| solution-1-flask   |     0.580421 |       1.00985  |   0.255501 |
| solution-1         |     7.62352  |       1e-06    |   0.852572 |
| solution-2         |     0.57502  |       0.711184 |   1.24713  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.58462  |       0.115166 |   0.305694 |
| solution-aron-mark |     0.560771 |       0.110977 |   0.340733 |
| solution-flask     |     0.562148 |       1.00883  |   0.480778 |
| solution-1-flask   |     0.571251 |       1.009    |   0.7674   |
| solution-2         |     0.572009 |       0.474792 |   3.41606  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.580742 |       0.11743  |    1.00917 |
| solution-pl        |     0.570145 |       0.116802 |    1.03713 |
| solution-flask     |     0.586299 |       1.00913  |    2.14004 |
| solution-1-flask   |     0.592172 |       1.00897  |    5.33149 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.568102 |       0.146206 |    4.44405 |
| solution-pl        |     0.567661 |       0.145164 |    4.5004  |
| solution-flask     |     0.561763 |       1.00963  |    8.45742 |