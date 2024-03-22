# 2024-03-22

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.50924  |       1.04386  |   0.066934 |
| solution-aron-mark |     0.659202 |       0.108367 |   0.161789 |
| solution-pl        |     0.668226 |       0.112139 |   0.16471  |
| solution-1-flask   |     0.677737 |       1.00854  |   0.264081 |
| solution-1         |     8.13418  |       1e-06    |   0.602751 |
| solution-2         |     4.67713  |       0.482234 |   0.897839 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.65775  |       1.00854  |   0.169155 |
| solution-aron-mark |     0.66018  |       0.11538  |   0.253508 |
| solution-pl        |     0.664515 |       0.115657 |   0.256518 |
| solution-1-flask   |     0.669907 |       1.00863  |   0.798524 |
| solution-2         |     0.659146 |       0.465224 |   2.23373  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.65749  |       0.123257 |   0.808856 |
| solution-pl        |     0.657442 |       0.120937 |   0.810682 |
| solution-flask     |     0.659629 |       1.00884  |   0.92504  |
| solution-1-flask   |     0.668851 |       1.00861  |   5.41082  |
| solution-2         |     0.656138 |       0.515882 |  40.6017   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.661934 |       0.158973 |    3.35367 |
| solution-pl        |     0.662006 |       0.16121  |    3.39359 |
| solution-flask     |     0.659263 |       1.00862  |    5.59555 |