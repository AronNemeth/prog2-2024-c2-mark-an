# 2024-11-18

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.12292  |       1.05888  |   0.110402 |
| solution-aron-mark |     0.607433 |       0.108477 |   0.180341 |
| solution-pl        |     5.82597  |       0.110227 |   0.197407 |
| solution-1-flask   |     0.613828 |       1.00894  |   0.264243 |
| solution-1         |     7.62176  |       1e-06    |   0.59698  |
| solution-2         |     0.577289 |       0.553705 |   0.848056 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.600284 |       0.114338 |   0.313168 |
| solution-aron-mark |     0.573633 |       0.109825 |   0.314765 |
| solution-flask     |     0.584814 |       1.00917  |   0.492395 |
| solution-1-flask   |     0.586281 |       1.00923  |   0.774124 |
| solution-2         |     0.588043 |       0.501756 |   2.09776  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.608908 |       0.116637 |    1.00726 |
| solution-pl        |     0.587302 |       0.118789 |    1.00839 |
| solution-flask     |     0.576984 |       1.00921  |    2.16101 |
| solution-1-flask   |     0.580216 |       1.0092   |    5.36503 |
| solution-2         |     0.586105 |       0.541585 |  172.685   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.592695 |       0.151747 |    4.48304 |
| solution-aron-mark |     0.572513 |       0.15043  |    4.53395 |
| solution-flask     |     0.584208 |       1.00903  |    8.80065 |