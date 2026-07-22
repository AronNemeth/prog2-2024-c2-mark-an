# 2026-07-22

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.35025  |       1.12465  |   0.109362 |
| solution-pl        |     0.467367 |       0.162119 |   0.252182 |
| solution-aron-mark |     0.457493 |       0.160377 |   0.25425  |
| solution-1-flask   |     0.469641 |       1.00874  |   0.265862 |
| solution-1         |     7.49722  |       1e-06    |   0.690845 |
| solution-2         |     4.68858  |       0.729177 |   1.27969  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.464001 |       0.159602 |   0.379448 |
| solution-pl        |     0.458945 |       0.161161 |   0.380701 |
| solution-flask     |     0.47096  |       1.00903  |   0.408134 |
| solution-1-flask   |     0.476971 |       1.0089   |   0.830977 |
| solution-2         |     0.468031 |       0.579483 |   2.79474  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.457329 |       0.170768 |    1.14359 |
| solution-aron-mark |     0.454404 |       0.164677 |    1.14502 |
| solution-flask     |     0.462613 |       1.0089   |    1.71436 |
| solution-1-flask   |     0.474318 |       1.00868  |    5.86119 |
| solution-2         |     0.465851 |       0.603498 |   38.5286  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.45619  |       0.190993 |    3.81947 |
| solution-aron-mark |     0.457904 |       0.188947 |    3.83509 |
| solution-flask     |     0.456469 |       1.00938  |    5.65371 |