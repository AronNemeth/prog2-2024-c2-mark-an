# 2026-08-01

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.25856  |       1.00886  |   0.106822 |
| solution-aron-mark |     0.438012 |       0.155941 |   0.246827 |
| solution-pl        |     0.434785 |       0.159459 |   0.248142 |
| solution-1-flask   |     1.1429   |       1.06499  |   0.264461 |
| solution-1         |     7.48066  |       1e-06    |   0.678316 |
| solution-2         |     4.39717  |       0.693407 |   1.55227  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.436697 |       0.156929 |   0.386269 |
| solution-pl        |     0.439178 |       0.161734 |   0.386575 |
| solution-flask     |     0.435763 |       1.00928  |   0.409493 |
| solution-1-flask   |     0.437232 |       1.00874  |   0.82878  |
| solution-2         |     0.441717 |       0.525555 |   3.63613  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.436572 |       0.158443 |    1.14333 |
| solution-aron-mark |     0.443942 |       0.160134 |    1.16008 |
| solution-flask     |     0.431128 |       1.00905  |    1.71805 |
| solution-1-flask   |     0.440732 |       1.0097   |    5.84272 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.433995 |       0.184906 |    3.6454  |
| solution-aron-mark |     0.435053 |       0.187372 |    3.65132 |
| solution-flask     |     0.438837 |       1.00864  |    5.4137  |