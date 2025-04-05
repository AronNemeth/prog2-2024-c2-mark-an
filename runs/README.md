# 2025-04-05

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.528794 |       1.00913  |   0.082965 |
| solution-aron-mark |     1.86853  |       0.125927 |   0.189525 |
| solution-pl        |     0.534486 |       0.121298 |   0.192655 |
| solution-1-flask   |     4.95217  |       1.05424  |   0.275568 |
| solution-1         |     7.48292  |       1e-06    |   0.717993 |
| solution-2         |     0.527717 |       0.627713 |   0.983735 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.535442 |       0.124259 |   0.292666 |
| solution-pl        |     0.544232 |       0.126711 |   0.297546 |
| solution-flask     |     0.533775 |       1.00925  |   0.303325 |
| solution-1-flask   |     0.59494  |       1.00887  |   0.846535 |
| solution-2         |     0.520916 |       0.518857 |   3.72189  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.548543 |       0.129638 |   0.913767 |
| solution-aron-mark |     0.545242 |       0.133578 |   0.914447 |
| solution-flask     |     0.533525 |       1.0091   |   1.28814  |
| solution-1-flask   |     0.527487 |       1.0091   |   5.9037   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.590882 |       0.160222 |    3.02821 |
| solution-aron-mark |     0.517829 |       0.168892 |    3.02822 |
| solution-flask     |     0.530871 |       1.00912  |    4.32334 |