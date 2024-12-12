# 2024-12-12

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.78062  |       1.00853  |   0.105002 |
| solution-aron-mark |     0.527478 |       0.105564 |   0.187634 |
| solution-pl        |     0.555127 |       0.107613 |   0.198815 |
| solution-1-flask   |     4.82243  |       1.08147  |   0.262019 |
| solution-1         |     7.35033  |       1e-06    |   0.807282 |
| solution-2         |     0.528272 |       0.741557 |   1.17245  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.525258 |       0.108258 |   0.314779 |
| solution-pl        |     0.527279 |       0.109907 |   0.315723 |
| solution-flask     |     0.529414 |       1.00872  |   0.513064 |
| solution-1-flask   |     0.534882 |       1.00863  |   0.821159 |
| solution-2         |     0.531326 |       0.46535  |   2.32552  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.582564 |       0.118415 |    1.07727 |
| solution-pl        |     0.538824 |       0.116242 |    1.07975 |
| solution-flask     |     0.532282 |       1.00896  |    2.24936 |
| solution-1-flask   |     0.535832 |       1.00876  |    5.92049 |
| solution-2         |     0.540418 |       0.539434 |  176.559   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.527311 |       0.145527 |    4.41853 |
| solution-aron-mark |     0.538075 |       0.146025 |    4.49226 |
| solution-flask     |     0.524447 |       1.00879  |    8.81417 |