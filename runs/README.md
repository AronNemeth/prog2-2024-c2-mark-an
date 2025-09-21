# 2025-09-21

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.507979 |       1.00838  |   0.100909 |
| solution-pl        |     6.43945  |       0.302664 |   0.24616  |
| solution-aron-mark |     0.503041 |       0.161115 |   0.24772  |
| solution-1-flask   |     1.41786  |       1.04065  |   0.275428 |
| solution-1         |     8.53517  |       1e-06    |   0.710906 |
| solution-2         |     0.513427 |       0.701072 |   1.19012  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.511643 |       0.160139 |   0.373374 |
| solution-pl        |     0.50797  |       0.159104 |   0.373716 |
| solution-flask     |     0.503091 |       1.00884  |   0.394247 |
| solution-1-flask   |     0.509375 |       1.00873  |   0.822633 |
| solution-2         |     0.509356 |       0.544345 |   2.42238  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.51548  |       0.168785 |    1.10547 |
| solution-aron-mark |     0.514174 |       0.170633 |    1.11121 |
| solution-flask     |     0.505149 |       1.00864  |    1.60362 |
| solution-1-flask   |     0.51537  |       1.00899  |    5.68876 |
| solution-2         |     0.520795 |       0.597018 |   29.0062  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.496083 |       0.205705 |    3.38643 |
| solution-pl        |     0.505714 |       0.199704 |    3.40293 |
| solution-flask     |     0.505161 |       1.00875  |    5.32303 |