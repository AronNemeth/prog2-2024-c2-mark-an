# 2026-07-13

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.10246  |       1.07744  |   0.100823 |
| solution-pl        |     5.86963  |       0.187404 |   0.228787 |
| solution-1-flask   |     0.427558 |       1.00883  |   0.230811 |
| solution-aron-mark |     0.424459 |       0.150955 |   0.250894 |
| solution-1         |     7.76221  |       2e-06    |   0.679393 |
| solution-2         |     0.408277 |       0.797259 |   0.933333 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.423861 |       0.151026 |   0.344011 |
| solution-pl        |     0.445562 |       0.154185 |   0.348918 |
| solution-flask     |     0.419255 |       1.00895  |   0.39726  |
| solution-1-flask   |     0.425242 |       1.00889  |   0.725425 |
| solution-2         |     0.421986 |       0.493018 |   3.18817  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.428062 |       0.157358 |    1.0203  |
| solution-aron-mark |     0.425663 |       0.158093 |    1.02504 |
| solution-flask     |     0.424119 |       1.01127  |    1.63272 |
| solution-1-flask   |     0.425753 |       1.00881  |    5.70502 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.422499 |       0.183939 |    3.75606 |
| solution-aron-mark |     0.420782 |       0.181902 |    3.80343 |
| solution-flask     |     0.421706 |       1.00889  |    5.11861 |