# 2026-07-08

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.15162  |       1.07514  |   0.110146 |
| solution-pl        |     5.79359  |       0.184368 |   0.238775 |
| solution-aron-mark |     0.432187 |       0.151103 |   0.240896 |
| solution-1-flask   |     0.439477 |       1.00833  |   0.268412 |
| solution-1         |     7.44953  |       2e-06    |   0.831376 |
| solution-2         |     0.445677 |       0.834833 |   1.50787  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.433883 |       0.165821 |   0.37805  |
| solution-pl        |     0.429541 |       0.155625 |   0.378487 |
| solution-flask     |     0.427593 |       1.00845  |   0.395803 |
| solution-1-flask   |     0.43644  |       1.00854  |   0.819983 |
| solution-2         |     0.433127 |       0.532865 |   6.42751  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.432989 |       0.15938  |    1.13508 |
| solution-aron-mark |     0.441663 |       0.159312 |    1.14752 |
| solution-flask     |     0.430283 |       1.00874  |    1.73125 |
| solution-1-flask   |     0.443734 |       1.00858  |    5.77781 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.439447 |       0.183751 |    4.0967  |
| solution-aron-mark |     0.435114 |       0.184503 |    4.14448 |
| solution-flask     |     0.436805 |       1.00907  |    5.51884 |