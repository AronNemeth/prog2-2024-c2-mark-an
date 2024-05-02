# 2024-05-02

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.684624 |       1.00915  |   0.075602 |
| solution-pl        |     5.81539  |       0.158319 |   0.175862 |
| solution-aron-mark |     0.677866 |       0.119058 |   0.179096 |
| solution-1-flask   |     1.44968  |       1.1594   |   0.293067 |
| solution-1         |     8.53645  |       1e-06    |   0.778708 |
| solution-2         |     0.671432 |       0.426772 |   1.28952  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.674104 |       1.00963  |   0.164267 |
| solution-aron-mark |     0.680381 |       0.126589 |   0.279966 |
| solution-pl        |     0.676937 |       0.128559 |   0.291759 |
| solution-1-flask   |     0.701612 |       1.00933  |   0.800285 |
| solution-2         |     0.68541  |       0.47001  |   2.86988  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.675153 |       1.00908  |   0.710803 |
| solution-aron-mark |     0.720917 |       0.134771 |   0.836697 |
| solution-pl        |     0.673939 |       0.136495 |   0.849912 |
| solution-1-flask   |     0.686593 |       1.00898  |   5.6593   |
| solution-2         |     0.681366 |       0.492787 |  42.5662   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.699767 |       1.00918  |    2.57999 |
| solution-aron-mark |     0.669016 |       0.172608 |    2.66299 |
| solution-pl        |     0.728883 |       0.179521 |    2.77395 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.675397 |       0.294404 |    17.5787 |
| solution-pl        |     0.672007 |       0.299533 |    18.299  |
| solution-flask     |     0.684016 |       1.00936  |    18.4815 |