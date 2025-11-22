# 2025-11-22

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.82024  |       1.04418  |   0.099567 |
| solution-aron-mark |     0.474917 |       0.157285 |   0.240892 |
| solution-pl        |     0.476116 |       0.160744 |   0.248121 |
| solution-1-flask   |     0.476442 |       1.00818  |   0.26041  |
| solution-1         |     7.84331  |       1e-06    |   0.841591 |
| solution-2         |     4.79889  |       0.636361 |   1.21055  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.472593 |       0.158322 |   0.365502 |
| solution-pl        |     0.471528 |       0.164611 |   0.369035 |
| solution-flask     |     0.476924 |       1.00845  |   0.372345 |
| solution-1-flask   |     0.477403 |       1.00845  |   0.791432 |
| solution-2         |     0.467539 |       0.50578  |   8.47208  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.485909 |       0.171217 |    1.08744 |
| solution-aron-mark |     0.479396 |       0.165152 |    1.09459 |
| solution-flask     |     0.466688 |       1.00878  |    1.57655 |
| solution-1-flask   |     0.476831 |       1.00856  |    5.5759  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.469465 |       0.197228 |    3.20248 |
| solution-aron-mark |     0.469012 |       0.198101 |    3.20331 |
| solution-flask     |     0.470657 |       1.00861  |    5.09534 |