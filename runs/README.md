# 2024-07-19

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.08813  |       1.14129  |   0.092905 |
| solution-aron-mark |     0.498654 |       0.101199 |   0.167989 |
| solution-pl        |     5.78219  |       0.104096 |   0.16938  |
| solution-1-flask   |     0.508015 |       1.00903  |   0.257613 |
| solution-1         |     7.82761  |       1e-06    |   0.586373 |
| solution-2         |     0.49993  |       0.487396 |   0.892899 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.514456 |       1.00933  |   0.22339  |
| solution-pl        |     0.502297 |       0.104268 |   0.283154 |
| solution-aron-mark |     0.500268 |       0.102664 |   0.286624 |
| solution-1-flask   |     0.505815 |       1.00882  |   0.779064 |
| solution-2         |     0.499804 |       0.473952 |   3.42805  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.507454 |       1.00944  |   0.892376 |
| solution-aron-mark |     0.513524 |       0.112443 |   1.00028  |
| solution-pl        |     0.505546 |       0.113391 |   1.02453  |
| solution-1-flask   |     0.514013 |       1.0094   |   5.57028  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.507555 |       1.00892  |    4.3868  |
| solution-pl        |     0.501262 |       0.145479 |    4.39068 |
| solution-aron-mark |     0.498425 |       0.145929 |    4.3918  |