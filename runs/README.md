# 2025-12-12

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.68326  |       1.03554  |   0.09775  |
| solution-aron-mark |     0.475018 |       0.164598 |   0.243019 |
| solution-pl        |     0.496733 |       0.162744 |   0.248281 |
| solution-1-flask   |     0.47913  |       1.00811  |   0.263489 |
| solution-1         |     8.00727  |       1e-06    |   0.662422 |
| solution-2         |     4.77892  |       0.620872 |   1.55433  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.481011 |       0.167901 |   0.368384 |
| solution-flask     |     0.476267 |       1.00825  |   0.36867  |
| solution-pl        |     0.491984 |       0.164315 |   0.373318 |
| solution-1-flask   |     0.480999 |       1.0083   |   0.797388 |
| solution-2         |     0.472663 |       0.518985 |  14.5695   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.475086 |       0.169572 |    1.075   |
| solution-aron-mark |     0.473935 |       0.169836 |    1.07565 |
| solution-flask     |     0.474443 |       1.00848  |    1.56914 |
| solution-1-flask   |     0.481656 |       1.00836  |    5.55606 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.475155 |       0.194346 |    3.53565 |
| solution-pl        |     0.472417 |       0.203557 |    3.55265 |
| solution-flask     |     0.479207 |       1.0085   |    5.13926 |