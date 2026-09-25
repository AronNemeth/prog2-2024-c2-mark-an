# 2026-09-25

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.28253  |       1.04386  |   0.1094   |
| solution-pl        |     0.428335 |       0.163352 |   0.246387 |
| solution-aron-mark |     5.91475  |       0.179789 |   0.247111 |
| solution-1-flask   |     0.466275 |       1.00843  |   0.263218 |
| solution-1         |     8.15914  |       1e-06    |   0.735883 |
| solution-2         |     0.420796 |       0.697841 |   1.58198  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.449576 |       0.154942 |   0.378125 |
| solution-pl        |     0.445372 |       0.15942  |   0.385465 |
| solution-flask     |     0.437861 |       1.00858  |   0.400422 |
| solution-1-flask   |     0.441006 |       1.00845  |   0.806239 |
| solution-2         |     0.431132 |       0.508939 |  14.3234   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.433223 |       0.164009 |    1.15311 |
| solution-pl        |     0.429734 |       0.160265 |    1.16131 |
| solution-flask     |     0.43489  |       1.00866  |    1.6988  |
| solution-1-flask   |     0.442211 |       1.00877  |    5.84211 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.429253 |       0.185362 |    3.62837 |
| solution-aron-mark |     0.450162 |       0.191829 |    3.63555 |
| solution-flask     |     0.426752 |       1.00889  |    5.53579 |