# 2025-07-29

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.6686   |       1.05818  |   0.101101 |
| solution-aron-mark |     4.69879  |       0.146809 |   0.23458  |
| solution-pl        |     0.499684 |       0.148291 |   0.236241 |
| solution-1-flask   |     0.505245 |       1.00809  |   0.261569 |
| solution-1         |     8.14665  |       1e-06    |   0.655842 |
| solution-2         |     0.490858 |       0.593057 |   1.88778  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.497677 |       0.151711 |   0.363528 |
| solution-aron-mark |     0.503961 |       0.153727 |   0.369805 |
| solution-flask     |     0.502324 |       1.0083   |   0.38091  |
| solution-1-flask   |     0.505802 |       1.00839  |   0.800944 |
| solution-2         |     0.496862 |       0.508697 |   2.68981  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.494632 |       0.158487 |    1.08399 |
| solution-aron-mark |     0.514442 |       0.160376 |    1.10487 |
| solution-flask     |     0.495559 |       1.00836  |    1.58341 |
| solution-1-flask   |     0.503342 |       1.00836  |    5.70836 |
| solution-2         |     0.491484 |       0.554572 |  175.064   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.50048  |       0.186417 |    3.18578 |
| solution-pl        |     0.49567  |       0.185953 |    3.18601 |
| solution-flask     |     0.498743 |       1.00847  |    5.07023 |