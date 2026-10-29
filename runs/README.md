# 2026-10-29

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.275928 |       1.00748  |   0.047972 |
| solution-1-flask   |     0.952263 |       1.16126  |   0.120722 |
| solution-pl        |     0.278341 |       0.105564 |   0.144636 |
| solution-aron-mark |     1.7643   |       0.109252 |   0.156122 |
| solution-1         |     4.60044  |       0        |   0.32455  |
| solution-2         |     3.46588  |       0.359998 |   0.629747 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.281613 |       1.00745  |   0.103014 |
| solution-pl        |     0.277843 |       0.108125 |   0.210022 |
| solution-aron-mark |     0.280963 |       0.111812 |   0.210554 |
| solution-1-flask   |     0.292992 |       1.00726  |   0.374953 |
| solution-2         |     0.281921 |       0.339957 |   1.33907  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.252865 |       1.007    |   0.45965  |
| solution-aron-mark |     0.265247 |       0.108849 |   0.536805 |
| solution-pl        |     0.259354 |       0.108486 |   0.564969 |
| solution-1-flask   |     0.256784 |       1.00709  |   2.76315  |
| solution-2         |     0.256183 |       0.358266 |  15.5949   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.253211 |       0.142121 |    1.90326 |
| solution-aron-mark |     0.260996 |       0.132514 |    1.90572 |
| solution-flask     |     0.260812 |       1.00711  |    2.1687  |
| solution-1-flask   |     0.268265 |       1.00733  |   24.249   |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.286683 |       0.199987 |    12.6781 |
| solution-aron-mark |     0.268735 |       0.233475 |    13.5963 |
| solution-flask     |     0.315888 |       1.00727  |    15.8642 |