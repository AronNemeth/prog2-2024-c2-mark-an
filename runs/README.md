# 2025-04-26

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.04232  |       1.06872  |   0.08208  |
| solution-pl        |     5.52616  |       0.120822 |   0.189566 |
| solution-aron-mark |     0.510596 |       0.120843 |   0.189945 |
| solution-1-flask   |     0.514235 |       1.00852  |   0.26396  |
| solution-1         |     7.33532  |       1e-06    |   0.589214 |
| solution-2         |     0.50613  |       0.587032 |   1.19497  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.50694  |       0.122212 |   0.293355 |
| solution-flask     |     0.506689 |       1.00888  |   0.297623 |
| solution-aron-mark |     0.507413 |       0.122109 |   0.298445 |
| solution-1-flask   |     0.51212  |       1.00883  |   0.78498  |
| solution-2         |     0.506781 |       0.502516 |   2.6485   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.511887 |       0.132301 |   0.910806 |
| solution-pl        |     0.531899 |       0.129794 |   0.934203 |
| solution-flask     |     0.511215 |       1.00896  |   1.25184  |
| solution-1-flask   |     0.519447 |       1.00857  |   5.43232  |
| solution-2         |     0.513563 |       0.561163 |  37.3844   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.50525  |       0.160297 |    2.83724 |
| solution-aron-mark |     0.511083 |       0.16345  |    2.90967 |
| solution-flask     |     0.509156 |       1.009    |    4.28029 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.509897 |       0.270728 |    16.0911 |
| solution-pl        |     0.526105 |       0.271667 |    16.301  |