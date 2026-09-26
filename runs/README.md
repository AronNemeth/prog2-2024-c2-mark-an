# 2026-09-26

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.30518  |       1.05299  |   0.146045 |
| solution-aron-mark |     6.68086  |       0.180368 |   0.23648  |
| solution-pl        |     0.439681 |       0.155108 |   0.240465 |
| solution-1-flask   |     0.443758 |       1.00848  |   0.254024 |
| solution-1         |     7.76201  |       1e-06    |   0.60703  |
| solution-2         |     0.417953 |       0.694661 |   2.14947  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.429395 |       0.15866  |   0.373751 |
| solution-aron-mark |     0.451333 |       0.15915  |   0.379517 |
| solution-flask     |     0.426595 |       1.00835  |   0.393051 |
| solution-1-flask   |     0.439309 |       1.00819  |   0.813154 |
| solution-2         |     0.443437 |       0.516303 |   2.26513  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.427248 |       0.160882 |    1.1217  |
| solution-pl        |     0.431682 |       0.16384  |    1.12983 |
| solution-flask     |     0.42969  |       1.00882  |    1.63651 |
| solution-1-flask   |     0.434485 |       1.00876  |    5.78144 |
| solution-2         |     0.426579 |       0.563284 |   37.656   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.429743 |       0.184277 |    3.49352 |
| solution-aron-mark |     0.431792 |       0.182777 |    3.56206 |
| solution-flask     |     0.429639 |       1.00843  |    5.28673 |