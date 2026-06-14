# 2026-06-14

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.34222  |       1.13988  |   0.099931 |
| solution-1-flask   |     0.43988  |       1.00896  |   0.229518 |
| solution-aron-mark |     0.448685 |       0.153554 |   0.23041  |
| solution-pl        |     6.89238  |       0.175945 |   0.23304  |
| solution-1         |     8.04196  |       1e-06    |   0.610848 |
| solution-2         |     0.423658 |       0.7462   |   0.850456 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.444434 |       0.154531 |   0.354517 |
| solution-aron-mark |     0.434363 |       0.157759 |   0.361948 |
| solution-flask     |     0.437854 |       1.00897  |   0.389004 |
| solution-1-flask   |     0.436859 |       1.009    |   0.720095 |
| solution-2         |     0.445833 |       0.543267 |   4.57094  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.454751 |       0.159569 |    1.02764 |
| solution-aron-mark |     0.464202 |       0.171367 |    1.05252 |
| solution-flask     |     0.450939 |       1.0093   |    1.65206 |
| solution-1-flask   |     0.480332 |       1.00924  |    5.63455 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.47926  |       0.197507 |    4.14777 |
| solution-pl        |     0.481077 |       0.200929 |    4.26063 |
| solution-flask     |     0.470511 |       1.00919  |    5.80231 |