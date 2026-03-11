# 2026-03-11

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.8161   |       1.09553  |   0.10671  |
| solution-pl        |     5.38513  |       0.1527   |   0.250798 |
| solution-aron-mark |     0.469411 |       0.15667  |   0.26561  |
| solution-1-flask   |     0.486501 |       1.00894  |   0.291558 |
| solution-1         |     8.47462  |       1e-06    |   0.723948 |
| solution-2         |     0.478936 |       0.703759 |   1.29797  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.492319 |       0.154141 |   0.398936 |
| solution-pl        |     0.487041 |       0.156366 |   0.402681 |
| solution-flask     |     0.478454 |       1.00924  |   0.436792 |
| solution-1-flask   |     0.492145 |       1.01111  |   0.829855 |
| solution-2         |     0.492239 |       0.580241 |   2.74862  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.465808 |       0.157439 |    1.11732 |
| solution-aron-mark |     0.461147 |       0.159941 |    1.13714 |
| solution-flask     |     0.46547  |       1.00907  |    1.62388 |
| solution-1-flask   |     0.462406 |       1.009    |    5.70695 |
| solution-2         |     0.457482 |       0.586765 |  298.754   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.467607 |       0.183029 |    4.06962 |
| solution-pl        |     0.463904 |       0.183447 |    4.13973 |
| solution-flask     |     0.473754 |       1.00947  |    5.37613 |