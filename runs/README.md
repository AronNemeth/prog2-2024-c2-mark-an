# 2026-04-20

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.22442  |       1.04103  |   0.099906 |
| solution-pl        |     0.410626 |       0.145616 |   0.223718 |
| solution-1-flask   |     0.411753 |       1.00853  |   0.227233 |
| solution-aron-mark |     4.68183  |       0.150432 |   0.232703 |
| solution-1         |     7.91618  |       1e-06    |   0.59357  |
| solution-2         |     0.408271 |       0.551913 |   0.767363 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.40656  |       0.148417 |   0.345466 |
| solution-aron-mark |     0.409068 |       0.146285 |   0.346949 |
| solution-flask     |     0.406411 |       1.00861  |   0.3903   |
| solution-1-flask   |     0.414357 |       1.00871  |   0.717545 |
| solution-2         |     0.405466 |       0.494116 |   3.31386  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.406589 |       0.154363 |    1.01645 |
| solution-aron-mark |     0.420455 |       0.154086 |    1.03713 |
| solution-flask     |     0.409196 |       1.00876  |    1.62188 |
| solution-1-flask   |     0.409473 |       1.00876  |    5.56081 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.404868 |       0.178211 |    3.55901 |
| solution-aron-mark |     0.405628 |       0.176039 |    3.64141 |
| solution-flask     |     0.408623 |       1.00872  |    5.09933 |