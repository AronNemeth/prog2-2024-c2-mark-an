# 2025-05-28

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.96649  |       1.00822  |   0.09709  |
| solution-pl        |     0.494762 |       0.146752 |   0.226352 |
| solution-aron-mark |     0.496271 |       0.146277 |   0.236347 |
| solution-1-flask   |     6.11738  |       1.08723  |   0.268053 |
| solution-1         |     7.89062  |       1e-06    |   0.699619 |
| solution-2         |     0.497742 |       0.63675  |   1.0172   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.557419 |       0.163672 |   0.368603 |
| solution-pl        |     0.522222 |       0.161597 |   0.372991 |
| solution-flask     |     0.492391 |       1.00844  |   0.375608 |
| solution-1-flask   |     0.500449 |       1.00811  |   0.796386 |
| solution-2         |     0.492523 |       0.500349 |   2.58764  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.499341 |       0.155587 |    1.04865 |
| solution-aron-mark |     0.505536 |       0.157053 |    1.05363 |
| solution-flask     |     0.504581 |       1.00848  |    1.53846 |
| solution-1-flask   |     0.566544 |       1.00899  |    5.57371 |
| solution-2         |     0.502822 |       0.55861  |   35.9803  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.495647 |       0.185262 |    3.16285 |
| solution-pl        |     0.503973 |       0.194372 |    3.17409 |
| solution-flask     |     0.506873 |       1.00848  |    5.04032 |