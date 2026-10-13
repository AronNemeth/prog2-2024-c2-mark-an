# 2026-10-13

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.27189  |       1.04607  |   0.087865 |
| solution-aron-mark |     5.8801   |       0.177557 |   0.226096 |
| solution-1-flask   |     0.42005  |       1.00731  |   0.231613 |
| solution-pl        |     0.399026 |       0.163719 |   0.231981 |
| solution-1         |     7.24497  |       1e-06    |   0.602961 |
| solution-2         |     0.400531 |       0.723073 |   1.44843  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.404196 |       1.00682  |   0.218133 |
| solution-pl        |     0.411533 |       0.158278 |   0.352376 |
| solution-aron-mark |     0.418848 |       0.1587   |   0.358497 |
| solution-1-flask   |     0.417437 |       1.00747  |   0.728661 |
| solution-2         |     0.403119 |       0.501932 |   5.38036  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.409642 |       1.00783  |   0.996032 |
| solution-aron-mark |     0.403339 |       0.171705 |   1.10404  |
| solution-pl        |     0.406066 |       0.169978 |   1.13418  |
| solution-1-flask   |     0.412532 |       1.00686  |   5.61139  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.424456 |       0.197696 |    4.55501 |
| solution-pl        |     0.406799 |       0.198253 |    4.58279 |
| solution-flask     |     0.408258 |       1.00763  |    5.09183 |