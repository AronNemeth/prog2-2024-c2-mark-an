# 2025-06-26

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.49427  |       1.14229  |   0.099827 |
| solution-aron-mark |     5.94745  |       0.21531  |   0.233308 |
| solution-pl        |     0.935421 |       0.147365 |   0.235652 |
| solution-1-flask   |     0.955516 |       1.00819  |   0.26457  |
| solution-1         |     7.72102  |       1e-06    |   0.969093 |
| solution-2         |     0.95048  |       0.793859 |   0.97974  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.692841 |       0.146805 |   0.35835  |
| solution-flask     |     0.489639 |       1.00838  |   0.37339  |
| solution-aron-mark |     0.950498 |       0.151131 |   0.390611 |
| solution-1-flask   |     0.498298 |       1.00819  |   0.804026 |
| solution-2         |     0.490344 |       0.496302 |  14.6391   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.491541 |       0.15702  |    1.06673 |
| solution-aron-mark |     0.491391 |       0.157057 |    1.07842 |
| solution-flask     |     0.491001 |       1.00849  |    1.58768 |
| solution-1-flask   |     0.501108 |       1.00814  |    5.67876 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.49482  |       0.189422 |    3.16962 |
| solution-aron-mark |     0.492476 |       0.19419  |    3.20864 |
| solution-flask     |     0.49048  |       1.00846  |    5.07212 |