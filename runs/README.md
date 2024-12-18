# 2024-12-18

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.0034   |       1.00845  |   0.104537 |
| solution-aron-mark |     0.52892  |       0.106577 |   0.183504 |
| solution-pl        |     0.548516 |       0.107515 |   0.184366 |
| solution-1-flask   |     5.11761  |       1.10933  |   0.264193 |
| solution-1         |     7.74933  |       1e-06    |   0.804068 |
| solution-2         |     0.525183 |       0.571992 |   1.07964  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.530923 |       0.109136 |   0.312716 |
| solution-pl        |     0.5388   |       0.113412 |   0.313987 |
| solution-flask     |     0.540034 |       1.00877  |   0.506167 |
| solution-1-flask   |     0.530894 |       1.00865  |   0.808542 |
| solution-2         |     0.52962  |       0.469323 |   3.78566  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.534712 |       0.116898 |    1.07139 |
| solution-aron-mark |     0.529347 |       0.11689  |    1.09091 |
| solution-flask     |     0.535523 |       1.00872  |    2.25036 |
| solution-1-flask   |     0.542657 |       1.00887  |    5.86581 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.53066  |       0.143092 |    4.32506 |
| solution-aron-mark |     0.533005 |       0.146677 |    4.59866 |
| solution-flask     |     0.521831 |       1.0085   |    8.90418 |