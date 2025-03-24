# 2025-03-24

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.535143 |       1.00875  |   0.084738 |
| solution-pl        |     0.527512 |       0.124048 |   0.189987 |
| solution-aron-mark |     1.78531  |       0.121637 |   0.190744 |
| solution-1-flask   |     4.95325  |       1.08801  |   0.267222 |
| solution-1         |     7.15067  |       1e-06    |   0.614714 |
| solution-2         |     0.518732 |       0.686415 |   0.926112 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.528676 |       0.12497  |   0.295214 |
| solution-pl        |     0.525736 |       0.123383 |   0.297154 |
| solution-flask     |     0.518765 |       1.00908  |   0.3447   |
| solution-1-flask   |     0.535017 |       1.00886  |   0.794435 |
| solution-2         |     0.526785 |       0.528086 |   2.71201  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.524416 |       0.130243 |   0.902441 |
| solution-pl        |     0.536752 |       0.130224 |   0.902699 |
| solution-flask     |     0.539051 |       1.00923  |   1.25892  |
| solution-1-flask   |     0.533365 |       1.00931  |   5.69307  |
| solution-2         |     0.519094 |       0.576379 |  40.2889   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.523205 |       0.16189  |    2.84683 |
| solution-aron-mark |     0.526318 |       0.163193 |    2.86597 |
| solution-flask     |     0.517688 |       1.00891  |    4.24908 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.517348 |       0.276352 |    16.6947 |
| solution-pl        |     0.513558 |       0.266162 |    16.7478 |