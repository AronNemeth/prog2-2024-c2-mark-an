# 2025-05-16

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.0596   |       1.07337  |   0.097282 |
| solution-pl        |     5.64295  |       0.122173 |   0.18937  |
| solution-aron-mark |     0.482651 |       0.122159 |   0.193204 |
| solution-1-flask   |     0.482908 |       1.00824  |   0.26285  |
| solution-1         |     7.45446  |       1e-06    |   0.652669 |
| solution-2         |     0.47849  |       0.598644 |   1.41318  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.477855 |       0.12302  |   0.29207  |
| solution-aron-mark |     0.474999 |       0.1236   |   0.294967 |
| solution-flask     |     0.475782 |       1.00817  |   0.295272 |
| solution-1-flask   |     0.494234 |       1.00838  |   0.790511 |
| solution-2         |     0.473119 |       0.515537 |   4.44202  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.477996 |       0.130749 |   0.885473 |
| solution-pl        |     0.477278 |       0.129378 |   0.90232  |
| solution-flask     |     0.481822 |       1.00838  |   1.23721  |
| solution-1-flask   |     0.489911 |       1.00837  |   5.43417  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.473709 |       0.159718 |    2.84019 |
| solution-pl        |     0.47789  |       0.163435 |    2.84962 |
| solution-flask     |     0.472095 |       1.00854  |    4.30315 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.478237 |       0.264295 |    16.3548 |
| solution-aron-mark |     0.480647 |       0.274159 |    16.3733 |