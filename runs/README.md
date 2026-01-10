# 2026-01-10

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.87905  |       1.07078  |   0.105922 |
| solution-aron-mark |     0.475359 |       0.165013 |   0.245674 |
| solution-pl        |     0.465296 |       0.162307 |   0.249178 |
| solution-1-flask   |     0.475302 |       1.0081   |   0.267487 |
| solution-1         |     8.01118  |       1e-06    |   0.698532 |
| solution-2         |     4.90439  |       0.670702 |   1.44033  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.470438 |       0.162553 |   0.37245  |
| solution-aron-mark |     0.470666 |       0.16261  |   0.374646 |
| solution-flask     |     0.474331 |       1.00855  |   0.380976 |
| solution-1-flask   |     0.478104 |       1.00863  |   0.794216 |
| solution-2         |     0.473191 |       0.509903 |   2.56763  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.478441 |       0.168606 |    1.09208 |
| solution-pl        |     0.472188 |       0.180563 |    1.1102  |
| solution-flask     |     0.469695 |       1.00851  |    1.58432 |
| solution-1-flask   |     0.469887 |       1.00852  |    5.54793 |
| solution-2         |     0.471505 |       0.567421 |  294.61    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.46967  |       0.193366 |    3.48646 |
| solution-aron-mark |     0.470114 |       0.192901 |    3.57411 |
| solution-flask     |     0.466651 |       1.00843  |    5.13907 |