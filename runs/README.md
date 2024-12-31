# 2024-12-31

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.75524  |       1.0084   |   0.103989 |
| solution-pl        |     0.524307 |       0.109011 |   0.185484 |
| solution-aron-mark |     0.524865 |       0.111849 |   0.188155 |
| solution-1-flask   |     4.71808  |       1.0809   |   0.265628 |
| solution-1         |     7.27762  |       1e-06    |   0.590517 |
| solution-2         |     0.525286 |       0.514905 |   0.717702 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.527636 |       0.111571 |   0.316325 |
| solution-aron-mark |     0.526553 |       0.109289 |   0.316463 |
| solution-flask     |     0.529047 |       1.00866  |   0.480451 |
| solution-1-flask   |     0.53467  |       1.00885  |   0.804718 |
| solution-2         |     0.522504 |       0.47237  |   3.41123  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.542385 |       0.118387 |    1.08611 |
| solution-pl        |     0.526869 |       0.118034 |    1.09549 |
| solution-flask     |     0.525984 |       1.0089   |    2.12924 |
| solution-1-flask   |     0.534188 |       1.00876  |    5.84667 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.525977 |       0.144639 |    4.27399 |
| solution-aron-mark |     0.527649 |       0.144054 |    4.29386 |
| solution-flask     |     0.527635 |       1.00899  |    8.46266 |