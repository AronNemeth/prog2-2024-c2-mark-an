# 2025-02-19

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.552576 |       1.00883  |   0.078252 |
| solution-aron-mark |     0.543087 |       0.14592  |   0.208865 |
| solution-pl        |     1.74996  |       0.1594   |   0.213868 |
| solution-1-flask   |     4.9752   |       1.08044  |   0.268706 |
| solution-1         |     7.32207  |       1e-06    |   0.632079 |
| solution-2         |     0.56776  |       0.557172 |   1.42797  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.565011 |       1.00902  |   0.294464 |
| solution-aron-mark |     0.57181  |       0.152302 |   0.312168 |
| solution-pl        |     0.562257 |       0.148811 |   0.319075 |
| solution-1-flask   |     0.573623 |       1.00912  |   0.816262 |
| solution-2         |     0.54283  |       0.544102 |   5.06796  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.56839  |       0.154376 |   0.916843 |
| solution-pl        |     0.558462 |       0.154842 |   0.921936 |
| solution-flask     |     0.569493 |       1.00921  |   1.24806  |
| solution-1-flask   |     0.537091 |       1.00949  |   5.85535  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.557761 |       0.181466 |    3.00842 |
| solution-pl        |     0.550639 |       0.178691 |    3.09659 |
| solution-flask     |     0.57782  |       1.00972  |    4.38602 |