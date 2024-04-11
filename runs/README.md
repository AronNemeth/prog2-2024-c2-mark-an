# 2024-04-11

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.658603 |       1.0088   |   0.064989 |
| solution-aron-mark |     0.657635 |       0.110464 |   0.164402 |
| solution-pl        |     5.77451  |       0.110758 |   0.166183 |
| solution-1-flask   |     1.41177  |       1.19885  |   0.270068 |
| solution-1         |     7.958    |       1e-06    |   0.638776 |
| solution-2         |     0.66539  |       0.417187 |   0.695456 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.664981 |       1.00867  |   0.172154 |
| solution-pl        |     0.658959 |       0.115145 |   0.254539 |
| solution-aron-mark |     0.661406 |       0.114323 |   0.25631  |
| solution-1-flask   |     0.66707  |       1.00919  |   0.79208  |
| solution-2         |     0.656195 |       0.430248 |   2.17485  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.658251 |       0.121484 |   0.813775 |
| solution-aron-mark |     0.658515 |       0.120569 |   0.839614 |
| solution-flask     |     0.662731 |       1.00892  |   0.92303  |
| solution-1-flask   |     0.674304 |       1.009    |   5.58441  |
| solution-2         |     0.655712 |       0.480819 | 177.129    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.661584 |       0.154972 |    3.27838 |
| solution-aron-mark |     0.662432 |       0.154706 |    3.32402 |
| solution-flask     |     0.658821 |       1.00907  |    5.1836  |