# 2025-05-17

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.96118  |       1.00826  |   0.081312 |
| solution-aron-mark |     0.502058 |       0.122546 |   0.189475 |
| solution-pl        |     0.503666 |       0.120628 |   0.193148 |
| solution-1-flask   |     7.19245  |       1.07903  |   0.264875 |
| solution-1         |     7.55988  |       1e-06    |   0.689704 |
| solution-2         |     0.500389 |       0.658941 |   1.14859  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.501671 |       0.122995 |   0.289572 |
| solution-aron-mark |     0.496472 |       0.121729 |   0.291408 |
| solution-flask     |     0.505468 |       1.00827  |   0.2918   |
| solution-1-flask   |     0.509318 |       1.0085   |   0.777673 |
| solution-2         |     0.507362 |       0.522027 |   3.90679  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.498548 |       0.128559 |   0.879902 |
| solution-aron-mark |     0.501002 |       0.129082 |   0.902351 |
| solution-flask     |     0.502016 |       1.00849  |   1.23238  |
| solution-1-flask   |     0.506223 |       1.0084   |   5.37237  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.50322  |       0.158689 |    2.85476 |
| solution-aron-mark |     0.504054 |       0.16231  |    2.86308 |
| solution-flask     |     0.498132 |       1.00862  |    4.24734 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.511278 |       0.268729 |    16.6682 |
| solution-pl        |     0.50891  |       0.265263 |    16.7806 |