# 2025-01-01

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.82676  |       1.00877  |   0.103499 |
| solution-aron-mark |     0.527201 |       0.108101 |   0.183784 |
| solution-pl        |     0.527375 |       0.11035  |   0.190238 |
| solution-1-flask   |     4.77751  |       1.0773   |   0.264709 |
| solution-2         |     0.52795  |       0.598468 |   0.861578 |
| solution-1         |     7.42086  |       1e-06    |   0.899627 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.522328 |       0.109478 |   0.314029 |
| solution-aron-mark |     0.530811 |       0.109206 |   0.315697 |
| solution-flask     |     0.522222 |       1.00857  |   0.478034 |
| solution-1-flask   |     0.540511 |       1.00901  |   0.810647 |
| solution-2         |     0.522112 |       0.468338 |   2.43169  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.520873 |       0.116069 |    1.0641  |
| solution-aron-mark |     0.536557 |       0.11637  |    1.06502 |
| solution-flask     |     0.522883 |       1.00872  |    2.14346 |
| solution-1-flask   |     0.530739 |       1.00878  |    5.89264 |
| solution-2         |     0.528626 |       0.521044 |   46.2169  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.523643 |       0.149682 |    4.31439 |
| solution-pl        |     0.522807 |       0.143223 |    4.44594 |
| solution-flask     |     0.523266 |       1.0089   |    8.28468 |