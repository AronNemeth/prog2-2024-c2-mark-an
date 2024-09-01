# 2024-09-01

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.568896 |       1.00912  |   0.07336  |
| solution-aron-mark |     1.82683  |       0.106334 |   0.170491 |
| solution-pl        |     0.569825 |       0.104468 |   0.171183 |
| solution-1-flask   |     1.1115   |       1.0609   |   0.255511 |
| solution-1         |     7.65808  |       1e-06    |   0.728043 |
| solution-2         |     4.49152  |       0.64972  |   1.23919  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.574463 |       1.00915  |   0.226653 |
| solution-aron-mark |     0.570097 |       0.108392 |   0.299249 |
| solution-pl        |     0.56746  |       0.106845 |   0.327142 |
| solution-1-flask   |     0.576327 |       1.00922  |   0.781016 |
| solution-2         |     0.566179 |       0.501029 |   3.27921  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.561333 |       1.00944  |   0.890236 |
| solution-aron-mark |     0.569949 |       0.115489 |   0.993486 |
| solution-pl        |     0.579364 |       0.11686  |   0.995528 |
| solution-1-flask   |     0.58025  |       1.00938  |   5.54856  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.577158 |       1.00891  |    4.22191 |
| solution-pl        |     0.570658 |       0.143504 |    4.36357 |
| solution-aron-mark |     0.573862 |       0.147182 |    4.39982 |