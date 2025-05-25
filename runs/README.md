# 2025-05-25

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.95132  |       1.0092   |   0.101689 |
| solution-aron-mark |     0.57588  |       0.168295 |   0.245313 |
| solution-pl        |     0.577017 |       0.170599 |   0.248567 |
| solution-1-flask   |     5.942    |       1.03511  |   0.276339 |
| solution-1         |     8.70422  |       1e-06    |   0.726478 |
| solution-2         |     0.580238 |       0.7368   |   1.65903  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.581957 |       0.179762 |   0.377724 |
| solution-pl        |     0.582219 |       0.179726 |   0.383938 |
| solution-flask     |     0.572361 |       1.00922  |   0.390354 |
| solution-1-flask   |     0.583185 |       1.00914  |   0.842636 |
| solution-2         |     0.563815 |       0.598412 |  12.5555   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.597925 |       0.185402 |    1.10533 |
| solution-pl        |     0.588287 |       0.176643 |    1.11535 |
| solution-flask     |     0.581367 |       1.00963  |    1.63786 |
| solution-1-flask   |     0.615356 |       1.0106   |    6.22223 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.575471 |       0.211612 |    4.05515 |
| solution-pl        |     0.583337 |       0.212563 |    4.10428 |
| solution-flask     |     0.573925 |       1.01027  |    5.95086 |