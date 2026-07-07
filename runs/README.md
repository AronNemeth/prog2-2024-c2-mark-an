# 2026-07-07

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.3307   |       1.08459  |   0.103209 |
| solution-1-flask   |     0.438423 |       1.00961  |   0.230564 |
| solution-pl        |     6.31171  |       0.171298 |   0.231029 |
| solution-aron-mark |     0.434105 |       0.152995 |   0.234776 |
| solution-1         |     7.77832  |       1e-06    |   0.575549 |
| solution-2         |     0.419245 |       0.649601 |   0.910541 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.433929 |       0.155273 |   0.35439  |
| solution-pl        |     0.439273 |       0.153662 |   0.363252 |
| solution-flask     |     0.435747 |       1.00924  |   0.388971 |
| solution-1-flask   |     0.435453 |       1.00922  |   0.725994 |
| solution-2         |     0.437976 |       0.50894  |   8.19985  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.431664 |       0.163664 |    1.0276  |
| solution-pl        |     0.429938 |       0.161507 |    1.04427 |
| solution-flask     |     0.437316 |       1.00956  |    1.65843 |
| solution-1-flask   |     0.437424 |       1.00952  |    5.75696 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.428551 |       0.186251 |    3.92398 |
| solution-pl        |     0.434482 |       0.187923 |    3.9316  |
| solution-flask     |     0.429679 |       1.00917  |    5.30664 |