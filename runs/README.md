# 2024-11-14

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.17323  |       1.14696  |   0.109129 |
| solution-pl        |     5.62086  |       0.107747 |   0.175099 |
| solution-aron-mark |     0.550913 |       0.104397 |   0.181558 |
| solution-1-flask   |     0.560427 |       1.00918  |   0.254898 |
| solution-1         |     7.60029  |       1e-06    |   0.675776 |
| solution-2         |     0.551909 |       0.570485 |   1.35572  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.555943 |       0.106285 |   0.295771 |
| solution-pl        |     0.574841 |       0.107696 |   0.297922 |
| solution-flask     |     0.554015 |       1.00891  |   0.482387 |
| solution-1-flask   |     0.556721 |       1.00936  |   0.780187 |
| solution-2         |     0.574409 |       0.49798  |   3.41818  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.553408 |       0.112587 |    1.00944 |
| solution-pl        |     0.562323 |       0.11256  |    1.04685 |
| solution-flask     |     0.552745 |       1.00882  |    2.17497 |
| solution-1-flask   |     0.55486  |       1.00899  |    5.40125 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.552721 |       0.14514  |    4.24598 |
| solution-pl        |     0.550519 |       0.145226 |    4.31438 |
| solution-flask     |     0.549605 |       1.00917  |    8.54685 |