# 2026-08-12

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.3584   |       1.0073   |   0.078854 |
| solution-1-flask   |     1.08756  |       1.08864  |   0.172971 |
| solution-pl        |     0.352753 |       0.172473 |   0.206774 |
| solution-aron-mark |     0.333276 |       0.150825 |   0.227968 |
| solution-1         |     6.22231  |       1e-06    |   0.566334 |
| solution-2         |     4.18032  |       0.7645   |   1.02962  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.332266 |       0.120782 |   0.276631 |
| solution-pl        |     0.332749 |       0.121969 |   0.280179 |
| solution-flask     |     0.335563 |       1.00744  |   0.303317 |
| solution-1-flask   |     0.338585 |       1.00738  |   0.562063 |
| solution-2         |     0.331509 |       0.398781 |   5.94201  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.333677 |       0.126776 |   0.807719 |
| solution-aron-mark |     0.339103 |       0.125202 |   0.814737 |
| solution-flask     |     0.335082 |       1.00776  |   1.28127  |
| solution-1-flask   |     0.339499 |       1.00746  |   4.42086  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.336806 |       0.259398 |    2.74224 |
| solution-pl        |     0.33881  |       0.144398 |    2.75514 |
| solution-flask     |     0.333881 |       1.00764  |    4.05294 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.333632 |       0.203497 |    15.621  |
| solution-pl        |     0.33426  |       0.21097  |    15.7444 |