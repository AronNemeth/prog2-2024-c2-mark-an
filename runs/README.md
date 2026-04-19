# 2026-04-19

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.12742  |       1.05105  |   0.105818 |
| solution-aron-mark |     4.74709  |       0.145296 |   0.232132 |
| solution-pl        |     0.411534 |       0.143528 |   0.233094 |
| solution-1-flask   |     0.416392 |       1.0082   |   0.267449 |
| solution-1         |     7.49233  |       1e-06    |   0.669684 |
| solution-2         |     0.411525 |       0.600386 |   1.41363  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.412395 |       0.146087 |   0.359909 |
| solution-aron-mark |     0.411549 |       0.147206 |   0.36325  |
| solution-flask     |     0.41053  |       1.00819  |   0.39948  |
| solution-1-flask   |     0.413586 |       1.00819  |   0.805336 |
| solution-2         |     0.406751 |       0.49652  |  13.2176   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.409492 |       0.151965 |    1.11479 |
| solution-aron-mark |     0.411672 |       0.151663 |    1.12054 |
| solution-flask     |     0.410627 |       1.00801  |    1.6716  |
| solution-1-flask   |     0.420123 |       1.00821  |    5.61802 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.408145 |       0.177679 |    3.76665 |
| solution-aron-mark |     0.412592 |       0.179288 |    3.79499 |
| solution-flask     |     0.406602 |       1.008    |    5.33858 |