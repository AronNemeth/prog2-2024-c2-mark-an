# 2025-05-04

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.06459  |       1.17498  |   0.083487 |
| solution-pl        |     5.59172  |       0.12286  |   0.190803 |
| solution-aron-mark |     0.471521 |       0.121303 |   0.194355 |
| solution-1-flask   |     0.469464 |       1.00861  |   0.272023 |
| solution-2         |     0.466439 |       0.706984 |   0.797903 |
| solution-1         |     7.41329  |       1e-06    |   0.825339 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.47191  |       0.125532 |   0.293236 |
| solution-aron-mark |     0.4919   |       0.126364 |   0.2952   |
| solution-flask     |     0.463533 |       1.00913  |   0.299864 |
| solution-1-flask   |     0.48171  |       1.00882  |   0.783443 |
| solution-2         |     0.465842 |       0.515634 |   1.75368  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.469959 |       0.12833  |   0.892893 |
| solution-pl        |     0.472566 |       0.13045  |   0.894326 |
| solution-flask     |     0.463216 |       1.00924  |   1.2358   |
| solution-1-flask   |     0.474894 |       1.00886  |   5.34017  |
| solution-2         |     0.459972 |       0.560984 |  24.995    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.467856 |       0.162889 |    2.80615 |
| solution-pl        |     0.465731 |       0.164138 |    2.83966 |
| solution-flask     |     0.462336 |       1.00868  |    4.19186 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.4621   |       0.264291 |    15.9405 |
| solution-aron-mark |     0.466403 |       0.2646   |    16.3215 |