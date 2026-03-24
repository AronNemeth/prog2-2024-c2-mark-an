# 2026-03-24

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.61886  |       1.24158  |   0.105373 |
| solution-pl        |     4.42711  |       0.148154 |   0.234298 |
| solution-aron-mark |     0.445455 |       0.147489 |   0.237602 |
| solution-1-flask   |     0.445027 |       1.00874  |   0.260479 |
| solution-1         |     7.43456  |       1e-06    |   0.735114 |
| solution-2         |     0.457681 |       0.671241 |   1.28719  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.44642  |       0.152014 |   0.372798 |
| solution-pl        |     0.446783 |       0.156744 |   0.372839 |
| solution-flask     |     0.446934 |       1.00886  |   0.393556 |
| solution-1-flask   |     0.448866 |       1.00883  |   0.849637 |
| solution-2         |     0.443236 |       0.507043 |   5.09437  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.441624 |       0.157444 |    1.12233 |
| solution-pl        |     0.445138 |       0.157552 |    1.12882 |
| solution-flask     |     0.443471 |       1.00914  |    1.67161 |
| solution-1-flask   |     0.448619 |       1.00905  |    5.59941 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.445622 |       0.179963 |    3.94995 |
| solution-pl        |     0.443044 |       0.183013 |    3.96084 |
| solution-flask     |     0.442072 |       1.00898  |    5.17609 |