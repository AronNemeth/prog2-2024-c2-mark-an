# 2026-02-13

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.8304   |       1.1008   |   0.111008 |
| solution-pl        |     4.91316  |       0.153451 |   0.241884 |
| solution-aron-mark |     0.466084 |       0.151736 |   0.245138 |
| solution-1-flask   |     0.466912 |       1.00901  |   0.270333 |
| solution-1         |     8.45626  |       2e-06    |   0.710996 |
| solution-2         |     0.461371 |       0.643791 |   1.02378  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.471797 |       0.150691 |   0.384193 |
| solution-pl        |     0.480589 |       0.15659  |   0.3922   |
| solution-flask     |     0.475775 |       1.00929  |   0.407075 |
| solution-1-flask   |     0.469204 |       1.00892  |   0.817159 |
| solution-2         |     0.459596 |       0.536    |   2.71547  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.474878 |       0.158892 |    1.15046 |
| solution-pl        |     0.460311 |       0.158223 |    1.16991 |
| solution-flask     |     0.464025 |       1.00909  |    1.67756 |
| solution-1-flask   |     0.470345 |       1.00916  |    5.5806  |
| solution-2         |     0.456161 |       0.593397 |  307.111   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.464656 |       0.183952 |    4.00098 |
| solution-aron-mark |     0.461844 |       0.18644  |    4.0311  |
| solution-flask     |     0.473935 |       1.00916  |    5.47352 |