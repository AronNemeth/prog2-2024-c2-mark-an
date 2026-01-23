# 2026-01-23

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.16575  |       1.04327  |   0.102304 |
| solution-aron-mark |     0.481613 |       0.164965 |   0.250182 |
| solution-pl        |     0.487527 |       0.170086 |   0.253136 |
| solution-1-flask   |     0.483597 |       1.00857  |   0.273279 |
| solution-1         |     7.68865  |       2e-06    |   0.7274   |
| solution-2         |     4.5196   |       0.661471 |   0.761777 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.479037 |       0.168204 |   0.377643 |
| solution-flask     |     0.494172 |       1.00861  |   0.384136 |
| solution-aron-mark |     0.483524 |       0.169359 |   0.389219 |
| solution-1-flask   |     0.490915 |       1.00881  |   0.809011 |
| solution-2         |     0.487474 |       0.558403 |   5.51839  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.485232 |       0.171692 |    1.07894 |
| solution-aron-mark |     0.514913 |       0.182701 |    1.09161 |
| solution-flask     |     0.48591  |       1.00879  |    1.6152  |
| solution-1-flask   |     0.516242 |       1.00872  |    5.92143 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.472054 |       0.192778 |    3.52626 |
| solution-pl        |     0.47045  |       0.190494 |    3.63204 |
| solution-flask     |     0.475509 |       1.00862  |    5.15315 |