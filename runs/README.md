# 2025-11-21

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.52627  |       1.07762  |   0.100918 |
| solution-pl        |     0.4681   |       0.162753 |   0.244347 |
| solution-aron-mark |     0.617573 |       0.201671 |   0.246424 |
| solution-1-flask   |     0.48124  |       1.00819  |   0.265105 |
| solution-1         |     9.35004  |       1e-06    |   0.736578 |
| solution-2         |     6.01877  |       0.658485 |   1.19283  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.470506 |       0.160228 |   0.367509 |
| solution-flask     |     0.470298 |       1.0084   |   0.371592 |
| solution-aron-mark |     0.471111 |       0.158345 |   0.371942 |
| solution-1-flask   |     0.477186 |       1.00814  |   0.794173 |
| solution-2         |     0.473925 |       0.50958  |   9.66326  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.468387 |       0.165317 |    1.06841 |
| solution-pl        |     0.466809 |       0.164363 |    1.07675 |
| solution-flask     |     0.466424 |       1.00857  |    1.56633 |
| solution-1-flask   |     0.472906 |       1.00853  |    5.55379 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.465502 |       0.197619 |    3.24632 |
| solution-aron-mark |     0.467853 |       0.195757 |    3.27459 |
| solution-flask     |     0.471874 |       1.00849  |    5.19327 |