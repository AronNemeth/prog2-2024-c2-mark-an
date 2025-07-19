# 2025-07-19

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.3779   |       1.03438  |   0.100648 |
| solution-pl        |     0.500973 |       0.150768 |   0.235324 |
| solution-aron-mark |     4.3276   |       0.147226 |   0.236967 |
| solution-1-flask   |     0.501037 |       1.00813  |   0.268106 |
| solution-1         |     7.71729  |       1e-06    |   0.647623 |
| solution-2         |     0.497992 |       0.601625 |   1.13847  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.514071 |       0.151114 |   0.355106 |
| solution-pl        |     0.497992 |       0.149205 |   0.355814 |
| solution-flask     |     0.505333 |       1.00818  |   0.37852  |
| solution-1-flask   |     0.507614 |       1.00833  |   0.795236 |
| solution-2         |     0.503117 |       0.50548  |  11.9002   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.503829 |       0.159035 |    1.07876 |
| solution-aron-mark |     0.504148 |       0.158032 |    1.08479 |
| solution-flask     |     0.499687 |       1.00845  |    1.61419 |
| solution-1-flask   |     0.505343 |       1.00857  |    5.66835 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.500175 |       0.186946 |    3.2135  |
| solution-pl        |     0.497673 |       0.188456 |    3.23483 |
| solution-flask     |     0.511224 |       1.00836  |    5.1258  |