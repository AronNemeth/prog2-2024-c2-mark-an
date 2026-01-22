# 2026-01-22

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.10953  |       1.05476  |   0.101501 |
| solution-pl        |     0.917625 |       0.170789 |   0.249038 |
| solution-aron-mark |     0.925306 |       0.162249 |   0.250019 |
| solution-1-flask   |     0.930434 |       1.00831  |   0.266932 |
| solution-1         |     8.75941  |       2e-06    |   0.887088 |
| solution-2         |     5.18066  |       0.705763 |   1.07859  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.473482 |       0.164013 |   0.374231 |
| solution-pl        |     0.498952 |       0.165235 |   0.376013 |
| solution-flask     |     0.47432  |       1.00826  |   0.379362 |
| solution-1-flask   |     0.479634 |       1.00842  |   0.805257 |
| solution-2         |     0.474359 |       0.529424 |   3.48766  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.479767 |       0.169904 |    1.09449 |
| solution-pl        |     0.470897 |       0.165849 |    1.10674 |
| solution-flask     |     0.477506 |       1.00869  |    1.59748 |
| solution-1-flask   |     0.483815 |       1.00878  |    5.57102 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.475165 |       0.192327 |    3.49343 |
| solution-pl        |     0.464314 |       0.189605 |    3.5218  |
| solution-flask     |     0.472995 |       1.00877  |    5.09888 |