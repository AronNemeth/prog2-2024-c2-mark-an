# 2024-10-23

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.37079  |       1.11024  |   0.109324 |
| solution-aron-mark |     0.570539 |       0.108822 |   0.173841 |
| solution-pl        |     5.75299  |       0.110427 |   0.193269 |
| solution-1-flask   |     0.567692 |       1.0091   |   0.258659 |
| solution-2         |     0.567587 |       0.767512 |   0.940815 |
| solution-1         |     7.96209  |       1e-06    |   0.99633  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.562907 |       0.109695 |   0.296818 |
| solution-aron-mark |     0.590894 |       0.113412 |   0.316158 |
| solution-flask     |     0.565085 |       1.0089   |   0.478753 |
| solution-1-flask   |     0.585994 |       1.00942  |   0.771116 |
| solution-2         |     0.562913 |       0.476104 |   2.82157  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.575869 |       0.117914 |   0.998946 |
| solution-pl        |     0.571717 |       0.116378 |   1.00284  |
| solution-flask     |     0.564831 |       1.00942  |   2.12021  |
| solution-1-flask   |     0.569963 |       1.00901  |   5.39637  |
| solution-2         |     0.560979 |       0.529651 |  37.5758   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.567361 |       0.146621 |    4.27837 |
| solution-aron-mark |     0.567713 |       0.150639 |    4.33432 |
| solution-flask     |     0.564798 |       1.00891  |    8.40246 |