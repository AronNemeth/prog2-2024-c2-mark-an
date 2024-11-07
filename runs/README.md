# 2024-11-07

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.17165  |       1.06675  |   0.107351 |
| solution-aron-mark |     0.581067 |       0.110298 |   0.175194 |
| solution-pl        |     5.70577  |       0.110604 |   0.18837  |
| solution-1-flask   |     0.581586 |       1.00911  |   0.253407 |
| solution-1         |     7.73728  |       1e-06    |   0.597248 |
| solution-2         |     0.569685 |       0.547888 |   1.91263  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.570508 |       0.112708 |   0.333892 |
| solution-aron-mark |     0.633893 |       0.11563  |   0.343516 |
| solution-flask     |     0.583438 |       1.00918  |   0.48181  |
| solution-1-flask   |     0.593805 |       1.009    |   0.805924 |
| solution-2         |     0.574769 |       0.498029 |   5.41158  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.573575 |       0.120351 |    1.01181 |
| solution-aron-mark |     0.583294 |       0.119986 |    1.01375 |
| solution-flask     |     0.585652 |       1.00943  |    2.1498  |
| solution-1-flask   |     0.586559 |       1.0093   |    5.49935 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.579346 |       0.150406 |    4.6591  |
| solution-pl        |     0.582767 |       0.150914 |    4.69105 |
| solution-flask     |     0.574559 |       1.00933  |    9.06055 |