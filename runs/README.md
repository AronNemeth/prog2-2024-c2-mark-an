# 2025-09-07

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.496951 |       1.00939  |   0.097074 |
| solution-pl        |     5.84947  |       0.170029 |   0.235893 |
| solution-aron-mark |     0.478177 |       0.153377 |   0.239394 |
| solution-1-flask   |     1.29089  |       1.0651   |   0.282581 |
| solution-1         |     8.09253  |       1e-06    |   0.610125 |
| solution-2         |     0.509016 |       0.649246 |   1.68598  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.486273 |       0.155568 |   0.36461  |
| solution-aron-mark |     0.480353 |       0.155186 |   0.366622 |
| solution-flask     |     0.488649 |       1.00861  |   0.378024 |
| solution-1-flask   |     0.494492 |       1.00857  |   0.804233 |
| solution-2         |     0.488773 |       0.512748 |   4.26012  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.486844 |       0.162872 |    1.05825 |
| solution-pl        |     0.490604 |       0.163983 |    1.06051 |
| solution-flask     |     0.48594  |       1.00856  |    1.59579 |
| solution-1-flask   |     0.492464 |       1.00858  |    5.70063 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.480079 |       0.193363 |    3.29527 |
| solution-pl        |     0.488409 |       0.192202 |    3.30576 |
| solution-flask     |     0.483792 |       1.00852  |    5.15754 |