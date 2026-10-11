# 2026-10-11

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.65921  |       1.0539   |   0.119673 |
| solution-aron-mark |     7.34568  |       0.190085 |   0.253477 |
| solution-pl        |     0.466329 |       0.175041 |   0.263024 |
| solution-1-flask   |     0.45746  |       1.00855  |   0.265582 |
| solution-1         |     9.73337  |       1e-06    |   0.636102 |
| solution-2         |     0.435244 |       0.642949 |   1.93628  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.448807 |       1.00868  |   0.237302 |
| solution-pl        |     0.439399 |       0.168186 |   0.39462  |
| solution-aron-mark |     0.43386  |       0.168274 |   0.396005 |
| solution-1-flask   |     0.444816 |       1.00874  |   0.836519 |
| solution-2         |     0.430802 |       0.50707  |   7.7421   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.425448 |       1.00878  |    1.04161 |
| solution-pl        |     0.426511 |       0.172332 |    1.18965 |
| solution-aron-mark |     0.424696 |       0.173891 |    1.19299 |
| solution-1-flask   |     0.440699 |       1.00879  |    5.58857 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.426552 |       0.19961  |    3.56621 |
| solution-aron-mark |     0.430495 |       0.200777 |    3.69421 |
| solution-flask     |     0.434397 |       1.00873  |    4.3833  |