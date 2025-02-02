# 2025-02-02

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.40065  |       1.13283  |   0.082108 |
| solution-pl        |     4.51911  |       0.135494 |   0.200581 |
| solution-aron-mark |     0.531724 |       0.136413 |   0.204171 |
| solution-1-flask   |     0.53174  |       1.00894  |   0.265188 |
| solution-1         |     7.44986  |       1e-06    |   0.657582 |
| solution-2         |     0.527168 |       0.60684  |   0.895664 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.529934 |       1.0086   |   0.293986 |
| solution-pl        |     0.521976 |       0.138668 |   0.298284 |
| solution-aron-mark |     0.545023 |       0.138267 |   0.305269 |
| solution-1-flask   |     0.547919 |       1.00886  |   0.797031 |
| solution-2         |     0.525747 |       0.48451  |   2.70252  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.529027 |       0.14433  |   0.891867 |
| solution-pl        |     0.528478 |       0.146687 |   0.915727 |
| solution-flask     |     0.536406 |       1.00901  |   1.22454  |
| solution-1-flask   |     0.530432 |       1.00897  |   5.75645  |
| solution-2         |     0.524076 |       0.542033 |  42.4286   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.526059 |       0.174253 |    2.80635 |
| solution-aron-mark |     0.528983 |       0.171789 |    2.81008 |
| solution-flask     |     0.528051 |       1.00902  |    4.19786 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.525045 |       0.27354  |    16.3056 |
| solution-aron-mark |     0.522852 |       0.282031 |    16.3822 |