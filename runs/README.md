# 2025-08-06

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.35423  |       1.04961  |   0.10168  |
| solution-pl        |     0.499081 |       0.156286 |   0.237982 |
| solution-aron-mark |     4.72619  |       0.160753 |   0.250624 |
| solution-1-flask   |     0.535008 |       1.00838  |   0.257586 |
| solution-1         |     8.43563  |       1e-06    |   0.686557 |
| solution-2         |     0.511676 |       0.630578 |   1.90665  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.506509 |       0.156357 |   0.371782 |
| solution-pl        |     0.518551 |       0.155698 |   0.373451 |
| solution-flask     |     0.510022 |       1.00847  |   0.381698 |
| solution-1-flask   |     0.526294 |       1.00852  |   0.812343 |
| solution-2         |     0.513708 |       0.524851 |   2.36045  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.508106 |       0.163602 |    1.08101 |
| solution-aron-mark |     0.521174 |       0.162801 |    1.08941 |
| solution-flask     |     0.525177 |       1.00872  |    1.61014 |
| solution-1-flask   |     0.507275 |       1.00851  |    5.69801 |
| solution-2         |     0.497677 |       0.571738 |  167.152   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.50898  |       0.190728 |    3.3371  |
| solution-pl        |     0.528361 |       0.196057 |    3.34996 |
| solution-flask     |     0.510876 |       1.00846  |    5.25886 |