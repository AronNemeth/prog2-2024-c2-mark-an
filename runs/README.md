# 2026-01-13

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.11034  |       1.0695   |   0.104995 |
| solution-pl        |     0.491702 |       0.176658 |   0.249402 |
| solution-aron-mark |     0.94153  |       0.168457 |   0.250098 |
| solution-1-flask   |     0.909536 |       1.00842  |   0.2628   |
| solution-1         |     9.25714  |       1e-06    |   0.784096 |
| solution-2         |     5.20512  |       0.734112 |   1.72557  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.490833 |       0.169608 |   0.377989 |
| solution-pl        |     0.497158 |       0.168483 |   0.378443 |
| solution-flask     |     0.485481 |       1.00849  |   0.38572  |
| solution-1-flask   |     0.512856 |       1.00868  |   0.808191 |
| solution-2         |     0.474477 |       0.515913 |  12.3087   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.482946 |       0.174032 |    1.10552 |
| solution-pl        |     0.488731 |       0.172448 |    1.11329 |
| solution-flask     |     0.491373 |       1.00874  |    1.59139 |
| solution-1-flask   |     0.49746  |       1.00881  |    5.68441 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.47166  |       0.192765 |    3.63662 |
| solution-pl        |     0.476555 |       0.196989 |    3.77074 |
| solution-flask     |     0.48954  |       1.00869  |    5.20226 |