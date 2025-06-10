# 2025-06-10

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.88715  |       1.00845  |   0.098495 |
| solution-pl        |     0.496223 |       0.146841 |   0.23125  |
| solution-aron-mark |     0.49437  |       0.147846 |   0.233578 |
| solution-1-flask   |     5.23898  |       1.0767   |   0.263816 |
| solution-1         |     7.6592   |       1e-06    |   0.60688  |
| solution-2         |     0.495059 |       0.590068 |   0.982403 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.49266  |       0.148052 |   0.352547 |
| solution-aron-mark |     0.49417  |       0.149193 |   0.354371 |
| solution-flask     |     0.494603 |       1.00837  |   0.377078 |
| solution-1-flask   |     0.498779 |       1.00836  |   0.795537 |
| solution-2         |     0.499278 |       0.502698 |   2.79595  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.49431  |       0.15649  |    1.05646 |
| solution-pl        |     0.498044 |       0.155864 |    1.07903 |
| solution-flask     |     0.495843 |       1.00833  |    1.55215 |
| solution-1-flask   |     0.502212 |       1.00839  |    5.44142 |
| solution-2         |     0.493333 |       0.551073 |   31.821   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.496517 |       0.185332 |    3.18288 |
| solution-aron-mark |     0.493328 |       0.190121 |    3.26966 |
| solution-flask     |     0.492629 |       1.00829  |    5.00192 |