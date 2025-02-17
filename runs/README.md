# 2025-02-17

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.521542 |       1.00895  |   0.079453 |
| solution-aron-mark |     0.525635 |       0.138694 |   0.201777 |
| solution-pl        |     1.78427  |       0.174776 |   0.201878 |
| solution-1-flask   |     5.48405  |       1.05609  |   0.266983 |
| solution-1         |     7.92786  |       1e-06    |   0.651982 |
| solution-2         |     0.528693 |       0.590938 |   0.78462  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.521651 |       1.00869  |   0.284358 |
| solution-aron-mark |     0.526121 |       0.14151  |   0.304071 |
| solution-pl        |     0.523555 |       0.139521 |   0.304314 |
| solution-1-flask   |     0.526287 |       1.00915  |   0.800397 |
| solution-2         |     0.522541 |       0.49335  |   4.30672  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.523655 |       0.148156 |   0.894808 |
| solution-aron-mark |     0.520291 |       0.146884 |   0.913535 |
| solution-flask     |     0.521387 |       1.00868  |   1.2184   |
| solution-1-flask   |     0.532683 |       1.00863  |   5.68668  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.526937 |       0.177833 |    2.80063 |
| solution-pl        |     0.521538 |       0.177688 |    2.83468 |
| solution-flask     |     0.522162 |       1.00907  |    4.18425 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.521318 |       0.279713 |    16.1876 |
| solution-pl        |     0.523084 |       0.275076 |    16.202  |