# 2026-06-19

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.53465  |       1.04011  |   0.053037 |
| solution-1-flask   |     0.270179 |       1.00707  |   0.122417 |
| solution-pl        |     5.02836  |       0.114498 |   0.133637 |
| solution-aron-mark |     0.262587 |       0.09197  |   0.137512 |
| solution-1         |     5.4252   |       0        |   0.412859 |
| solution-2         |     0.276725 |       0.510614 |   0.558898 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.260232 |       0.091408 |   0.182592 |
| solution-pl        |     0.272781 |       0.098017 |   0.193073 |
| solution-flask     |     0.261881 |       1.00695  |   0.201616 |
| solution-1-flask   |     0.256746 |       1.00707  |   0.37667  |
| solution-2         |     0.259367 |       0.335354 |   6.03607  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.263499 |       0.095487 |   0.519129 |
| solution-aron-mark |     0.258112 |       0.103784 |   0.520463 |
| solution-flask     |     0.268997 |       1.00685  |   0.832255 |
| solution-1-flask   |     0.2655   |       1.00669  |   2.84653  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.264857 |       0.116052 |    2.08492 |
| solution-aron-mark |     0.274992 |       0.118612 |    2.13388 |
| solution-flask     |     0.282404 |       1.00707  |    2.75627 |
| solution-1-flask   |     0.268508 |       1.00725  |   24.4075  |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.263525 |       0.163251 |    12.1293 |
| solution-pl        |     0.25784  |       0.166533 |    12.2611 |
| solution-flask     |     0.254827 |       1.00684  |    14.2565 |