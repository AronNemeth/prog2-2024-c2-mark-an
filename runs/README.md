# 2026-11-05

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.34769  |       1.08892  |   0.098383 |
| solution-aron-mark |     6.01869  |       0.165805 |   0.248297 |
| solution-pl        |     0.413151 |       0.164051 |   0.252605 |
| solution-1-flask   |     0.420783 |       1.01073  |   0.2738   |
| solution-1         |     7.96069  |       1e-06    |   0.588935 |
| solution-2         |     0.40525  |       0.523824 |   0.939887 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.420515 |       1.01105  |   0.267965 |
| solution-pl        |     0.439853 |       0.172792 |   0.382523 |
| solution-aron-mark |     0.419013 |       0.166938 |   0.384742 |
| solution-1-flask   |     0.42176  |       1.01061  |   0.79345  |
| solution-2         |     0.413191 |       0.51253  |   2.85917  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.449452 |       1.0111   |    1.01853 |
| solution-aron-mark |     0.422545 |       0.179593 |    1.14657 |
| solution-pl        |     0.429481 |       0.180594 |    1.14831 |
| solution-1-flask   |     0.443401 |       1.0112   |    5.40914 |
| solution-2         |     0.425858 |       0.566413 |   46.9221  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.424815 |       0.209998 |    3.48178 |
| solution-pl        |     0.42763  |       0.207572 |    3.53343 |
| solution-flask     |     0.414444 |       1.01149  |    4.24415 |