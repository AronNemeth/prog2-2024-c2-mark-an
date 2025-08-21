# 2025-08-21

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.94474  |       1.04469  |   0.103956 |
| solution-pl        |     0.492418 |       0.154158 |   0.242407 |
| solution-aron-mark |     4.95084  |       0.153302 |   0.244927 |
| solution-1-flask   |     0.500503 |       1.00835  |   0.265181 |
| solution-1         |     8.16011  |       1e-06    |   0.895661 |
| solution-2         |     0.731419 |       0.761059 |   1.15235  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.495947 |       0.158387 |   0.367564 |
| solution-pl        |     0.490399 |       0.154606 |   0.369328 |
| solution-flask     |     0.494195 |       1.00871  |   0.38076  |
| solution-1-flask   |     0.497729 |       1.00844  |   0.816337 |
| solution-2         |     0.494567 |       0.544804 |   2.63442  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.497844 |       0.165128 |    1.07762 |
| solution-pl        |     0.499202 |       0.167207 |    1.08333 |
| solution-flask     |     0.492381 |       1.00857  |    1.57112 |
| solution-1-flask   |     0.49725  |       1.00861  |    5.67478 |
| solution-2         |     0.497269 |       0.576077 |   37.8048  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.49022  |       0.191565 |    3.26183 |
| solution-aron-mark |     0.494249 |       0.192668 |    3.28917 |
| solution-flask     |     0.486671 |       1.00826  |    5.08805 |