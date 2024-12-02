# 2024-12-02

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.32469  |       1.04999  |   0.117451 |
| solution-aron-mark |     0.579186 |       0.109443 |   0.180477 |
| solution-pl        |     6.06031  |       0.109967 |   0.196596 |
| solution-1-flask   |     0.575107 |       1.00907  |   0.260356 |
| solution-1         |     7.96132  |       1e-06    |   0.589264 |
| solution-2         |     0.565584 |       0.543717 |   0.957916 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.568113 |       0.111068 |   0.303907 |
| solution-aron-mark |     0.565066 |       0.10998  |   0.323405 |
| solution-flask     |     0.57829  |       1.00893  |   0.507747 |
| solution-1-flask   |     0.580011 |       1.00912  |   0.776933 |
| solution-2         |     0.561633 |       0.491334 |   2.40362  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.600037 |       0.12264  |    1.04234 |
| solution-pl        |     0.579021 |       0.119166 |    1.04957 |
| solution-flask     |     0.582155 |       1.00917  |    2.23982 |
| solution-1-flask   |     0.57302  |       1.00942  |    5.33004 |
| solution-2         |     0.590635 |       0.544881 |  158.916   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.559075 |       0.148717 |    4.30706 |
| solution-pl        |     0.558061 |       0.148261 |    4.32969 |
| solution-flask     |     0.555857 |       1.00962  |    8.62033 |