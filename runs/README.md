# 2025-03-20

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.528797 |       1.00899  |   0.085782 |
| solution-aron-mark |     1.78699  |       0.121038 |   0.185551 |
| solution-pl        |     0.542719 |       0.123091 |   0.188846 |
| solution-1-flask   |     4.97614  |       1.08702  |   0.269792 |
| solution-1         |     7.46005  |       1e-06    |   0.614953 |
| solution-2         |     0.523522 |       0.578558 |   0.774675 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.535297 |       0.12697  |   0.29594  |
| solution-flask     |     0.525538 |       1.00873  |   0.297086 |
| solution-pl        |     0.531686 |       0.124979 |   0.302893 |
| solution-1-flask   |     0.533462 |       1.00904  |   0.804279 |
| solution-2         |     0.528755 |       0.526867 |   3.31833  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.529531 |       0.137462 |   0.901647 |
| solution-pl        |     0.539136 |       0.133241 |   0.923134 |
| solution-flask     |     0.533691 |       1.00902  |   1.29479  |
| solution-1-flask   |     0.584782 |       1.00887  |   5.67529  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.529239 |       0.160558 |    2.90399 |
| solution-aron-mark |     0.539657 |       0.16457  |    2.93868 |
| solution-flask     |     0.531282 |       1.0093   |    4.41691 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.527478 |       0.270674 |    17.8321 |
| solution-pl        |     0.517303 |       0.271078 |    18.6759 |