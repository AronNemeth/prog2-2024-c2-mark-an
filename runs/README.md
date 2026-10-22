# 2026-10-22

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.68775  |       1.14457  |   0.102703 |
| solution-pl        |     0.646821 |       0.173194 |   0.261907 |
| solution-1-flask   |     0.458699 |       1.00866  |   0.264519 |
| solution-aron-mark |     7.06577  |       0.27734  |   0.274204 |
| solution-1         |     9.72204  |       1e-06    |   0.962087 |
| solution-2         |     0.935333 |       0.982471 |   1.57136  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.456934 |       1.00852  |   0.242287 |
| solution-aron-mark |     0.451283 |       0.17794  |   0.39825  |
| solution-pl        |     0.465049 |       0.184639 |   0.412161 |
| solution-1-flask   |     0.468479 |       1.00879  |   0.818558 |
| solution-2         |     0.46189  |       0.546536 |   2.34416  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.4594   |       1.00934  |    1.06013 |
| solution-aron-mark |     0.458795 |       0.188264 |    1.17898 |
| solution-pl        |     0.46348  |       0.180831 |    1.18455 |
| solution-1-flask   |     0.470001 |       1.00906  |    5.79215 |
| solution-2         |     0.459009 |       0.591305 |  296.008   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.45165  |       0.20939  |    3.78608 |
| solution-aron-mark |     0.475715 |       0.207816 |    3.85102 |
| solution-flask     |     0.451974 |       1.00853  |    4.49936 |