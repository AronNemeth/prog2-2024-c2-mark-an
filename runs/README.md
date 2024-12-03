# 2024-12-03

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.11741  |       1.12531  |   0.112195 |
| solution-aron-mark |     0.564704 |       0.111801 |   0.183277 |
| solution-pl        |     5.65946  |       0.109008 |   0.192504 |
| solution-1-flask   |     0.585625 |       1.00943  |   0.256216 |
| solution-1         |     7.54818  |       1e-06    |   0.849814 |
| solution-2         |     0.555702 |       0.532644 |   1.31161  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.559045 |       0.110054 |   0.298727 |
| solution-pl        |     0.576726 |       0.111521 |   0.30527  |
| solution-flask     |     0.585807 |       1.0089   |   0.503271 |
| solution-1-flask   |     0.572521 |       1.00917  |   0.778133 |
| solution-2         |     0.575586 |       0.487864 |   6.87438  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.570113 |       0.116634 |    1.03324 |
| solution-pl        |     0.563263 |       0.117695 |    1.05267 |
| solution-flask     |     0.563621 |       1.00889  |    2.25862 |
| solution-1-flask   |     0.567998 |       1.00913  |    5.39802 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.556357 |       0.14963  |    4.31632 |
| solution-pl        |     0.556985 |       0.149339 |    4.4183  |
| solution-flask     |     0.554762 |       1.00917  |    8.54567 |