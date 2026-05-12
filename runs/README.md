# 2026-05-12

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.115    |       1.0554   |   0.1042   |
| solution-aron-mark |     5.3762   |       0.145183 |   0.239022 |
| solution-pl        |     0.420282 |       0.146248 |   0.247827 |
| solution-1-flask   |     0.417807 |       1.00802  |   0.266769 |
| solution-1         |     8.83968  |       1e-06    |   0.643153 |
| solution-2         |     0.41404  |       0.610672 |   1.40272  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.413092 |       0.150171 |   0.366094 |
| solution-aron-mark |     0.41149  |       0.14762  |   0.371145 |
| solution-flask     |     0.418407 |       1.00825  |   0.395302 |
| solution-1-flask   |     0.426386 |       1.00842  |   0.816934 |
| solution-2         |     0.41367  |       0.506989 |   4.22842  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.417139 |       0.151681 |    1.11449 |
| solution-aron-mark |     0.414528 |       0.160859 |    1.12332 |
| solution-flask     |     0.415169 |       1.00848  |    1.66927 |
| solution-1-flask   |     0.416064 |       1.00849  |    5.61365 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.414081 |       0.179399 |    3.81428 |
| solution-pl        |     0.425426 |       0.17772  |    3.82743 |
| solution-flask     |     0.41036  |       1.0084   |    5.32885 |