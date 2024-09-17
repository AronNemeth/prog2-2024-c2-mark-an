# 2024-09-17

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.07293  |       1.0888   |   0.095631 |
| solution-pl        |     0.564781 |       0.104478 |   0.17323  |
| solution-aron-mark |     5.71017  |       0.106355 |   0.173345 |
| solution-1-flask   |     0.575284 |       1.00928  |   0.263851 |
| solution-1         |     7.62755  |       1e-06    |   0.596404 |
| solution-2         |     0.564971 |       0.574305 |   0.860683 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.556682 |       1.00898  |   0.217017 |
| solution-pl        |     0.56116  |       0.107413 |   0.286919 |
| solution-aron-mark |     0.586053 |       0.106894 |   0.287989 |
| solution-1-flask   |     0.570868 |       1.00874  |   0.774182 |
| solution-2         |     0.570089 |       0.497436 |  30.8726   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.56073  |       1.00928  |   0.875963 |
| solution-pl        |     0.560785 |       0.115776 |   0.990038 |
| solution-aron-mark |     0.567728 |       0.113504 |   1.05311  |
| solution-1-flask   |     0.562653 |       1.00946  |   5.51714  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.568179 |       1.00941  |    4.2454  |
| solution-aron-mark |     0.563132 |       0.142438 |    4.27897 |
| solution-pl        |     0.555217 |       0.144849 |    4.32724 |