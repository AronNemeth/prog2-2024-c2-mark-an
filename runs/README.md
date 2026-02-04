# 2026-02-04

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.05663  |       1.05329  |   0.104025 |
| solution-aron-mark |     0.466925 |       0.162117 |   0.249407 |
| solution-pl        |     0.456473 |       0.161794 |   0.252849 |
| solution-1-flask   |     0.472953 |       1.00836  |   0.263562 |
| solution-1         |     8.00979  |       1e-06    |   0.707803 |
| solution-2         |     5.52362  |       0.633619 |   1.14246  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.461576 |       0.169422 |   0.376725 |
| solution-aron-mark |     0.464861 |       0.166622 |   0.377722 |
| solution-flask     |     0.462873 |       1.00855  |   0.382226 |
| solution-1-flask   |     0.473519 |       1.0085   |   0.783684 |
| solution-2         |     0.458273 |       0.510683 |   4.35785  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.460558 |       0.172595 |    1.1198  |
| solution-pl        |     0.471287 |       0.172644 |    1.12286 |
| solution-flask     |     0.463544 |       1.00852  |    1.58615 |
| solution-1-flask   |     0.485029 |       1.00851  |    5.54425 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.464427 |       0.195672 |    3.80697 |
| solution-pl        |     0.460492 |       0.194435 |    3.8088  |
| solution-flask     |     0.462832 |       1.00868  |    5.0485  |