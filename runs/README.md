# 2025-08-17

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.593    |       1.0386   |   0.104361 |
| solution-aron-mark |     4.95514  |       0.15969  |   0.244961 |
| solution-pl        |     0.499373 |       0.158998 |   0.249127 |
| solution-1-flask   |     0.506612 |       1.0085   |   0.2666   |
| solution-1         |     7.96476  |       1e-06    |   0.762116 |
| solution-2         |     0.502627 |       0.704911 |   0.839101 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.505869 |       0.159111 |   0.375847 |
| solution-pl        |     0.509231 |       0.163972 |   0.376542 |
| solution-flask     |     0.50458  |       1.00885  |   0.391233 |
| solution-1-flask   |     0.518111 |       1.00905  |   0.797805 |
| solution-2         |     0.505733 |       0.537672 |   3.04669  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.496005 |       0.165356 |    1.08337 |
| solution-pl        |     0.511381 |       0.16698  |    1.11061 |
| solution-flask     |     0.511569 |       1.00883  |    1.61974 |
| solution-1-flask   |     0.50553  |       1.00881  |    5.72107 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.491194 |       0.192058 |    3.30612 |
| solution-aron-mark |     0.502773 |       0.192656 |    3.31445 |
| solution-flask     |     0.50159  |       1.00859  |    5.19966 |