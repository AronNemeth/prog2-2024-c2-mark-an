# 2025-11-03

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.94682  |       1.29816  |   0.108685 |
| solution-aron-mark |     0.545872 |       0.193943 |   0.275396 |
| solution-pl        |     0.556067 |       0.193619 |   0.282496 |
| solution-1-flask   |     0.558903 |       1.0108   |   0.286187 |
| solution-1         |     8.80033  |       1e-06    |   0.672418 |
| solution-2         |     5.196    |       0.735602 |   2.23945  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.581325 |       0.194942 |   0.422848 |
| solution-pl        |     0.53828  |       0.198036 |   0.424415 |
| solution-flask     |     0.552544 |       1.01111  |   0.428353 |
| solution-1-flask   |     0.559944 |       1.0102   |   0.872749 |
| solution-2         |     0.533337 |       0.592456 |   3.72433  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.580776 |       0.200301 |    1.17788 |
| solution-aron-mark |     0.535614 |       0.203469 |    1.18229 |
| solution-flask     |     0.573096 |       1.01076  |    1.74095 |
| solution-1-flask   |     0.566951 |       1.01087  |    6.005   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.530239 |       0.230771 |    3.69041 |
| solution-aron-mark |     0.559893 |       0.235075 |    3.85468 |
| solution-flask     |     0.546144 |       1.0105   |    5.7471  |