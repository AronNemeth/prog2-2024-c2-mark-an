# 2026-07-19

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.68979  |       1.07182  |   0.102199 |
| solution-1-flask   |     0.438493 |       1.00903  |   0.228997 |
| solution-pl        |     0.455943 |       0.151969 |   0.234181 |
| solution-aron-mark |     0.448451 |       0.160107 |   0.235576 |
| solution-1         |     7.80806  |       1e-06    |   0.652381 |
| solution-2         |     4.66798  |       0.718209 |   0.692437 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.451278 |       0.15312  |   0.35949  |
| solution-aron-mark |     0.461853 |       0.160371 |   0.360981 |
| solution-flask     |     0.430464 |       1.0111   |   0.396251 |
| solution-1-flask   |     0.435227 |       1.00907  |   0.738488 |
| solution-2         |     0.434619 |       0.527515 |   2.86604  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.431875 |       0.158771 |    1.03303 |
| solution-pl        |     0.435257 |       0.159442 |    1.06577 |
| solution-flask     |     0.433339 |       1.00919  |    1.66104 |
| solution-1-flask   |     0.443226 |       1.0091   |    5.77824 |
| solution-2         |     0.443765 |       0.573923 |   38.5758  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.446453 |       0.187532 |    4.04494 |
| solution-pl        |     0.432744 |       0.192398 |    4.15542 |
| solution-flask     |     0.43543  |       1.00911  |    5.42434 |