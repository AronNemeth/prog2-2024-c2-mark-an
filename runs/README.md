# 2024-09-29

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.36642  |       1.06625  |   0.085351 |
| solution-aron-mark |     1.86332  |       0.101433 |   0.178876 |
| solution-pl        |     0.553589 |       0.103098 |   0.179117 |
| solution-1-flask   |     0.567392 |       1.00792  |   0.261238 |
| solution-1         |     7.66099  |       1e-06    |   0.587126 |
| solution-2         |     4.67803  |       0.539357 |   0.806233 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.55294  |       1.00848  |   0.20687  |
| solution-pl        |     0.55268  |       0.103317 |   0.306548 |
| solution-aron-mark |     0.563556 |       0.103223 |   0.312144 |
| solution-1-flask   |     0.564229 |       1.0082   |   0.784798 |
| solution-2         |     0.572288 |       0.477414 |   4.30888  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.554681 |       1.00816  |   0.942733 |
| solution-pl        |     0.567013 |       0.110124 |   1.04309  |
| solution-aron-mark |     0.556408 |       0.11254  |   1.04505  |
| solution-1-flask   |     0.56128  |       1.00807  |   5.39156  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.559295 |       1.00869  |    4.20431 |
| solution-aron-mark |     0.555808 |       0.152461 |    4.22932 |
| solution-pl        |     0.556636 |       0.137242 |    4.23292 |