# 2025-12-02

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.21777  |       1.06969  |   0.099639 |
| solution-pl        |     0.470066 |       0.158034 |   0.244586 |
| solution-aron-mark |     0.473767 |       0.156033 |   0.245551 |
| solution-1-flask   |     0.470858 |       1.00821  |   0.269132 |
| solution-1         |     7.96699  |       1e-06    |   0.697617 |
| solution-2         |     4.83672  |       0.636456 |   0.935697 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.469235 |       0.158418 |   0.368131 |
| solution-aron-mark |     0.472753 |       0.158889 |   0.369395 |
| solution-flask     |     0.469133 |       1.00855  |   0.372339 |
| solution-1-flask   |     0.476396 |       1.00834  |   0.783736 |
| solution-2         |     0.469204 |       0.511473 |   4.33358  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.469877 |       0.166862 |    1.0743  |
| solution-pl        |     0.467008 |       0.166475 |    1.08048 |
| solution-flask     |     0.478647 |       1.00867  |    1.57559 |
| solution-1-flask   |     0.473529 |       1.00856  |    5.47515 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.473819 |       0.195692 |    3.19464 |
| solution-pl        |     0.469259 |       0.195292 |    3.20351 |
| solution-flask     |     0.470929 |       1.00848  |    5.075   |