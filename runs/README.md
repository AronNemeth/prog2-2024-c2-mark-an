# 2025-06-22

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.494959 |       1.00844  |   0.100768 |
| solution-aron-mark |     5.54842  |       0.17629  |   0.236802 |
| solution-pl        |     0.487953 |       0.15051  |   0.240729 |
| solution-1-flask   |     1.07043  |       1.0692   |   0.267807 |
| solution-1         |     7.51863  |       1e-06    |   0.756674 |
| solution-2         |     0.498778 |       0.673339 |   0.913913 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.502891 |       0.151575 |   0.363288 |
| solution-aron-mark |     0.500695 |       0.151319 |   0.367831 |
| solution-flask     |     0.499686 |       1.00824  |   0.386697 |
| solution-1-flask   |     0.508499 |       1.00839  |   0.797792 |
| solution-2         |     0.497534 |       0.504441 |   3.17651  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.51388  |       0.158131 |    1.07593 |
| solution-pl        |     0.498301 |       0.158513 |    1.07943 |
| solution-flask     |     0.503222 |       1.00853  |    1.60499 |
| solution-1-flask   |     0.506696 |       1.00847  |    5.43081 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.495109 |       0.192404 |    3.24465 |
| solution-aron-mark |     0.504749 |       0.190739 |    3.27858 |
| solution-flask     |     0.496364 |       1.00843  |    5.15724 |