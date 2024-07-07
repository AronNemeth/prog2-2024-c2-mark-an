# 2024-07-07

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.508654 |       1.00919  |   0.092617 |
| solution-aron-mark |     6.14385  |       0.105098 |   0.170347 |
| solution-pl        |     0.503404 |       0.105332 |   0.171369 |
| solution-1-flask   |     1.19774  |       1.06167  |   0.305806 |
| solution-1         |     8.2662   |       1e-06    |   0.76132  |
| solution-2         |     0.504839 |       0.701877 |   1.24793  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.520872 |       1.00919  |   0.194283 |
| solution-pl        |     0.524551 |       0.104596 |   0.288658 |
| solution-aron-mark |     0.508527 |       0.10584  |   0.289297 |
| solution-1-flask   |     0.517234 |       1.00954  |   0.781005 |
| solution-2         |     0.51126  |       0.482632 |  12.692    |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.512199 |       1.0092   |   0.900585 |
| solution-aron-mark |     0.53264  |       0.115712 |   0.998285 |
| solution-pl        |     0.513484 |       0.11302  |   1.00213  |
| solution-1-flask   |     0.520407 |       1.00906  |   5.66626  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.510084 |       1.0094   |    4.19594 |
| solution-pl        |     0.503856 |       0.14697  |    4.33293 |
| solution-aron-mark |     0.513439 |       0.149176 |    4.34417 |