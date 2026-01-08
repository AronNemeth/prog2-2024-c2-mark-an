# 2026-01-08

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.65492  |       1.04517  |   0.104935 |
| solution-pl        |     0.470609 |       0.164138 |   0.248013 |
| solution-aron-mark |     0.471505 |       0.161654 |   0.251269 |
| solution-1-flask   |     0.480379 |       1.00853  |   0.263505 |
| solution-1         |     8.08844  |       1e-06    |   0.771834 |
| solution-2         |     4.89168  |       0.836581 |   0.83896  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.479384 |       0.16657  |   0.374392 |
| solution-pl        |     0.475543 |       0.164291 |   0.381775 |
| solution-flask     |     0.474754 |       1.00873  |   0.385161 |
| solution-1-flask   |     0.498762 |       1.00882  |   0.802277 |
| solution-2         |     0.474204 |       0.521899 |   2.09964  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.484895 |       0.174043 |    1.10888 |
| solution-aron-mark |     0.487042 |       0.173965 |    1.11073 |
| solution-flask     |     0.468957 |       1.00867  |    1.59945 |
| solution-1-flask   |     0.486154 |       1.00877  |    5.58736 |
| solution-2         |     0.473741 |       0.567972 |   32.8396  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.469551 |       0.195648 |    3.51934 |
| solution-aron-mark |     0.480264 |       0.193328 |    3.5794  |
| solution-flask     |     0.484432 |       1.00857  |    5.11149 |