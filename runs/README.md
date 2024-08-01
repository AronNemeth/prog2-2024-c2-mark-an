# 2024-08-01

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.26025  |       1.10123  |   0.089437 |
| solution-pl        |     1.88303  |       0.104118 |   0.168673 |
| solution-aron-mark |     0.558128 |       0.102554 |   0.172143 |
| solution-1-flask   |     0.567846 |       1.00908  |   0.258624 |
| solution-1         |     7.86299  |       1e-06    |   0.665468 |
| solution-2         |     4.53872  |       0.602617 |   0.871305 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.551042 |       1.00928  |   0.221354 |
| solution-aron-mark |     0.553859 |       0.104496 |   0.288522 |
| solution-pl        |     0.55718  |       0.10318  |   0.291782 |
| solution-1-flask   |     0.558341 |       1.00886  |   0.774363 |
| solution-2         |     0.552203 |       0.47572  |   3.34645  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.55463  |       1.00927  |   0.893608 |
| solution-pl        |     0.553855 |       0.112991 |   1.0211   |
| solution-aron-mark |     0.563449 |       0.111831 |   1.02781  |
| solution-1-flask   |     0.557888 |       1.00914  |   5.53409  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.5533   |       1.00909  |    4.16634 |
| solution-aron-mark |     0.551061 |       0.146951 |    4.27946 |
| solution-pl        |     0.55353  |       0.155412 |    4.28554 |