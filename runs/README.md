# 2025-02-11

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.538581 |       1.00872  |   0.079306 |
| solution-aron-mark |     0.529119 |       0.139565 |   0.203652 |
| solution-pl        |     1.73191  |       0.145508 |   0.208132 |
| solution-1-flask   |     4.92495  |       1.06348  |   0.262419 |
| solution-1         |     7.036    |       1e-06    |   0.607965 |
| solution-2         |     0.539902 |       0.513916 |   1.53658  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.527549 |       1.00857  |   0.292629 |
| solution-aron-mark |     0.527229 |       0.140964 |   0.306584 |
| solution-pl        |     0.526789 |       0.140834 |   0.30684  |
| solution-1-flask   |     0.535624 |       1.00864  |   0.803958 |
| solution-2         |     0.55411  |       0.486385 |   7.03796  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.534598 |       0.149409 |   0.905578 |
| solution-aron-mark |     0.529769 |       0.149225 |   1.0029   |
| solution-flask     |     0.525515 |       1.00866  |   1.25005  |
| solution-1-flask   |     0.533027 |       1.0088   |   5.66353  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.528177 |       0.176734 |    2.8311  |
| solution-pl        |     0.528822 |       0.175751 |    2.84049 |
| solution-flask     |     0.53661  |       1.00897  |    4.18621 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.529577 |       0.280303 |    17.3343 |
| solution-aron-mark |     0.5284   |       0.286828 |    19.1451 |