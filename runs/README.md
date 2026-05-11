# 2026-05-11

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.20225  |       1.05035  |   0.102731 |
| solution-aron-mark |     4.71625  |       0.147317 |   0.224402 |
| solution-pl        |     0.40933  |       0.147475 |   0.22768  |
| solution-1-flask   |     0.41776  |       1.00882  |   0.230964 |
| solution-1         |     7.93508  |       1e-06    |   0.677989 |
| solution-2         |     0.410702 |       0.633062 |   0.921204 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.412337 |       0.150418 |   0.344585 |
| solution-aron-mark |     0.413477 |       0.148073 |   0.346507 |
| solution-flask     |     0.415357 |       1.00882  |   0.381383 |
| solution-1-flask   |     0.421837 |       1.00905  |   0.716008 |
| solution-2         |     0.412407 |       0.519618 |   6.75711  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.414357 |       0.155748 |    1.01347 |
| solution-aron-mark |     0.413623 |       0.154658 |    1.02065 |
| solution-flask     |     0.416719 |       1.00913  |    1.60778 |
| solution-1-flask   |     0.418452 |       1.00896  |    5.51113 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.422732 |       0.181324 |    3.64543 |
| solution-pl        |     0.411296 |       0.180317 |    3.75343 |
| solution-flask     |     0.414582 |       1.00914  |    5.13406 |