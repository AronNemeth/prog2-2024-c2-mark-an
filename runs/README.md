# 2025-12-08

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.24912  |       1.1314   |   0.103957 |
| solution-pl        |     0.958535 |       0.169401 |   0.250166 |
| solution-aron-mark |     0.960944 |       0.184674 |   0.260161 |
| solution-1-flask   |     0.951167 |       1.00854  |   0.27817  |
| solution-2         |     5.56013  |       0.990641 |   1.07217  |
| solution-1         |     9.18384  |       1e-06    |   1.10265  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.951456 |       1.00874  |   0.387043 |
| solution-pl        |     0.954919 |       0.174581 |   0.388426 |
| solution-aron-mark |     1.01092  |       0.189227 |   0.395714 |
| solution-1-flask   |     0.967385 |       1.00911  |   0.824724 |
| solution-2         |     0.946313 |       0.565419 |   3.0692   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.965684 |       0.178162 |    1.10464 |
| solution-pl        |     0.510729 |       0.185097 |    1.12367 |
| solution-flask     |     0.949935 |       1.00882  |    1.59208 |
| solution-1-flask   |     0.976192 |       1.00932  |    5.86226 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.498693 |       0.211811 |    3.86482 |
| solution-aron-mark |     0.524092 |       0.214058 |    4.04811 |
| solution-flask     |     0.528242 |       1.00857  |    5.43424 |