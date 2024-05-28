# 2024-05-28

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.57733  |       1.09018  |   0.076584 |
| solution-aron-mark |     6.01916  |       0.101036 |   0.158218 |
| solution-pl        |     0.66561  |       0.102224 |   0.160885 |
| solution-1-flask   |     0.687966 |       1.0093   |   0.261379 |
| solution-1         |     8.30297  |       1e-06    |   0.698622 |
| solution-2         |     0.654151 |       0.415227 |   1.15553  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.671517 |       1.00914  |   0.159526 |
| solution-aron-mark |     0.667665 |       0.103964 |   0.249286 |
| solution-pl        |     0.676894 |       0.106111 |   0.260942 |
| solution-1-flask   |     0.672688 |       1.00903  |   0.803367 |
| solution-2         |     0.666496 |       0.427514 |   2.79395  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.677591 |       1.00936  |   0.706071 |
| solution-aron-mark |     0.672825 |       0.11399  |   0.794503 |
| solution-pl        |     0.670096 |       0.115183 |   0.795305 |
| solution-1-flask   |     0.693625 |       1.00924  |   5.56327  |
| solution-2         |     0.672732 |       0.482528 | 166.926    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.670587 |       1.00912  |    2.48808 |
| solution-aron-mark |     0.669918 |       0.147868 |    2.59147 |
| solution-pl        |     0.66308  |       0.150331 |    2.59352 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.665149 |       1.00914  |    16.4898 |
| solution-pl        |     0.668243 |       0.275325 |    21.9261 |
| solution-aron-mark |     0.667585 |       0.272804 |    23.7971 |