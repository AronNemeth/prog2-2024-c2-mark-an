# 2024-09-22

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.15842  |       1.11245  |   0.096184 |
| solution-aron-mark |     1.81866  |       0.101906 |   0.172359 |
| solution-pl        |     0.549126 |       0.100408 |   0.174276 |
| solution-1-flask   |     0.556849 |       1.00839  |   0.254733 |
| solution-1         |     7.42036  |       1e-06    |   0.774793 |
| solution-2         |     4.34545  |       0.666775 |   1.48603  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.55339  |       1.00882  |   0.203119 |
| solution-pl        |     0.563698 |       0.102891 |   0.302908 |
| solution-aron-mark |     0.567565 |       0.103047 |   0.30295  |
| solution-1-flask   |     0.562109 |       1.00827  |   0.785836 |
| solution-2         |     0.554292 |       0.488898 |   2.32926  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.550888 |       1.00836  |    0.91131 |
| solution-pl        |     0.550276 |       0.109474 |    1.02322 |
| solution-aron-mark |     0.555381 |       0.109636 |    1.02537 |
| solution-1-flask   |     0.558115 |       1.00774  |    5.39532 |
| solution-2         |     0.567444 |       0.53319  |   34.8378  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.547699 |       1.00827  |    4.10598 |
| solution-aron-mark |     0.552784 |       0.136527 |    4.15264 |
| solution-pl        |     0.561136 |       0.135486 |    4.23585 |