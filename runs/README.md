# 2026-09-02

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.05966  |       1.04996  |   0.104157 |
| solution-aron-mark |     0.36952  |       0.133398 |   0.19556  |
| solution-pl        |     3.25075  |       0.185489 |   0.199755 |
| solution-1-flask   |     0.374566 |       1.0069   |   0.221526 |
| solution-1         |     7.09174  |       1e-06    |   0.72604  |
| solution-2         |     4.09182  |       0.825495 |   0.952005 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.369778 |       0.144212 |   0.296765 |
| solution-aron-mark |     0.367801 |       0.135052 |   0.297883 |
| solution-flask     |     0.368078 |       1.00679  |   0.34887  |
| solution-1-flask   |     0.372173 |       1.00644  |   0.661465 |
| solution-2         |     0.382244 |       0.544832 |   4.05172  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.369039 |       0.142249 |    0.95639 |
| solution-pl        |     0.372234 |       0.144966 |    0.96638 |
| solution-flask     |     0.368056 |       1.00727  |    1.50815 |
| solution-1-flask   |     0.374323 |       1.00697  |    5.34629 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.372401 |       0.182805 |    3.76141 |
| solution-pl        |     0.370821 |       0.186959 |    3.76501 |
| solution-flask     |     0.372543 |       1.00708  |    4.97481 |