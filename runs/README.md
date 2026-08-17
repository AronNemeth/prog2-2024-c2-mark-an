# 2026-08-17

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     4.8727   |       1.18221  |   0.088231 |
| solution-pl        |     0.40945  |       0.145625 |   0.214985 |
| solution-aron-mark |     5.08817  |       0.145144 |   0.215704 |
| solution-1-flask   |     0.411923 |       1.00717  |   0.232532 |
| solution-1         |     9.32358  |       1e-06    |   0.814595 |
| solution-2         |     0.404239 |       0.712037 |   1.26403  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.402724 |       0.145904 |   0.324875 |
| solution-aron-mark |     0.405373 |       0.145043 |   0.329239 |
| solution-flask     |     0.404616 |       1.00743  |   0.383706 |
| solution-1-flask   |     0.411078 |       1.00758  |   0.708462 |
| solution-2         |     0.398935 |       0.50415  |   3.17057  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.403578 |       0.15362  |    1.06191 |
| solution-pl        |     0.402628 |       0.164163 |    1.06787 |
| solution-flask     |     0.411618 |       1.00766  |    1.66562 |
| solution-1-flask   |     0.412659 |       1.00717  |    5.95444 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.411757 |       0.174762 |    4.12987 |
| solution-aron-mark |     0.417929 |       0.178307 |    4.14723 |
| solution-flask     |     0.407526 |       1.0075   |    5.4273  |