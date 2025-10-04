# 2025-10-04

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.45967  |       1.08374  |   0.102615 |
| solution-aron-mark |     0.482811 |       0.156082 |   0.241445 |
| solution-pl        |     0.487041 |       0.153063 |   0.24382  |
| solution-1-flask   |     0.490535 |       1.00905  |   0.269979 |
| solution-1         |     7.73042  |       1e-06    |   0.73475  |
| solution-2         |     4.35485  |       0.756653 |   0.863135 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.481858 |       0.1588   |   0.367776 |
| solution-pl        |     0.487433 |       0.1562   |   0.370543 |
| solution-flask     |     0.482957 |       1.0085   |   0.374725 |
| solution-1-flask   |     0.482323 |       1.00857  |   0.807648 |
| solution-2         |     0.488289 |       0.508662 |   5.44068  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.483089 |       0.162971 |    1.06728 |
| solution-aron-mark |     0.486945 |       0.164103 |    1.08088 |
| solution-flask     |     0.481541 |       1.00871  |    1.60235 |
| solution-1-flask   |     0.488389 |       1.00865  |    5.54601 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.484392 |       0.196506 |    3.24219 |
| solution-aron-mark |     0.48485  |       0.199394 |    3.24533 |
| solution-flask     |     0.487687 |       1.00843  |    5.098   |