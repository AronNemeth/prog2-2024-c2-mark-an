# 2025-12-11

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.22524  |       1.04946  |   0.10173  |
| solution-pl        |     0.472033 |       0.166237 |   0.245108 |
| solution-aron-mark |     0.487159 |       0.162631 |   0.246087 |
| solution-1-flask   |     0.488102 |       1.00827  |   0.273122 |
| solution-1         |     8.82858  |       1e-06    |   0.734311 |
| solution-2         |     5.75294  |       0.695137 |   1.0249   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.489762 |       0.164814 |   0.371544 |
| solution-flask     |     0.480879 |       1.0087   |   0.379762 |
| solution-pl        |     0.475757 |       0.1633   |   0.383156 |
| solution-1-flask   |     0.483612 |       1.00841  |   0.796337 |
| solution-2         |     0.493845 |       0.546033 |   3.2712   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.477399 |       0.172372 |    1.07083 |
| solution-pl        |     0.513272 |       0.179831 |    1.12421 |
| solution-flask     |     0.491656 |       1.00841  |    1.56556 |
| solution-1-flask   |     0.497273 |       1.00861  |    5.7378  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.480729 |       0.192624 |    3.57864 |
| solution-pl        |     0.504993 |       0.196909 |    3.69469 |
| solution-flask     |     0.51867  |       1.00858  |    5.09986 |