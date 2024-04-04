# 2024-04-04

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.94971  |       1.07055  |   0.066663 |
| solution-pl        |     0.663102 |       0.111818 |   0.16477  |
| solution-aron-mark |     0.66316  |       0.108034 |   0.165194 |
| solution-1-flask   |     0.673722 |       1.0086   |   0.263314 |
| solution-1         |     8.15761  |       1e-06    |   0.613589 |
| solution-2         |     4.78314  |       0.417794 |   1.28969  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.656235 |       1.00916  |   0.163502 |
| solution-pl        |     0.683227 |       0.117358 |   0.257046 |
| solution-aron-mark |     0.698431 |       0.119131 |   0.259227 |
| solution-1-flask   |     0.687535 |       1.00912  |   0.787105 |
| solution-2         |     0.663362 |       0.431474 |  11.2995   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.66914  |       0.124748 |   0.830814 |
| solution-pl        |     0.676112 |       0.125232 |   0.841752 |
| solution-flask     |     0.678368 |       1.00878  |   0.948515 |
| solution-1-flask   |     0.681181 |       1.00897  |   5.56509  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.666414 |       0.155711 |    3.33376 |
| solution-pl        |     0.665619 |       0.157968 |    3.37424 |
| solution-flask     |     0.673176 |       1.0088   |    5.39411 |