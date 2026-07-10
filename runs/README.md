# 2026-07-10

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.61907  |       1.05142  |   0.108066 |
| solution-aron-mark |     0.423907 |       0.149771 |   0.235883 |
| solution-pl        |     7.83743  |       0.192184 |   0.23923  |
| solution-1-flask   |     0.434    |       1.00838  |   0.263865 |
| solution-1         |     8.50118  |       1e-06    |   0.714451 |
| solution-2         |     0.784499 |       0.697215 |   1.26551  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.45124  |       0.156641 |   0.394832 |
| solution-flask     |     0.427521 |       1.00844  |   0.407453 |
| solution-pl        |     0.433987 |       0.159446 |   0.460586 |
| solution-1-flask   |     0.436453 |       1.00835  |   0.831599 |
| solution-2         |     0.432423 |       0.504721 |   3.0053   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.434132 |       0.15689  |    1.14941 |
| solution-aron-mark |     0.426906 |       0.171037 |    1.17482 |
| solution-flask     |     0.439091 |       1.00856  |    1.73669 |
| solution-1-flask   |     0.434404 |       1.00829  |    5.69036 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.427379 |       0.183365 |    4.00461 |
| solution-pl        |     0.440579 |       0.189316 |    4.16187 |
| solution-flask     |     0.437345 |       1.00856  |    5.39781 |