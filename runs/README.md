# 2024-05-08

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.666296 |       1.00862  |   0.072094 |
| solution-pl        |     5.8603   |       0.121102 |   0.172255 |
| solution-aron-mark |     0.692827 |       0.117875 |   0.174218 |
| solution-1-flask   |     1.41775  |       1.01231  |   0.254692 |
| solution-1         |     8.05395  |       1e-06    |   0.583602 |
| solution-2         |     0.663476 |       0.415091 |   1.66057  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.67003  |       1.00891  |   0.15912  |
| solution-aron-mark |     0.672296 |       0.123852 |   0.267731 |
| solution-pl        |     0.660062 |       0.124509 |   0.273613 |
| solution-1-flask   |     0.675128 |       1.00879  |   0.791717 |
| solution-2         |     0.661786 |       0.440209 |   2.87422  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.666026 |       1.00883  |   0.693124 |
| solution-aron-mark |     0.671901 |       0.131654 |   0.812804 |
| solution-pl        |     0.660345 |       0.13454  |   0.816418 |
| solution-1-flask   |     0.674222 |       1.00926  |   5.70364  |
| solution-2         |     0.678994 |       0.48823  |  31.5304   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.658482 |       1.009    |    2.5162  |
| solution-aron-mark |     0.661733 |       0.17106  |    2.60997 |
| solution-pl        |     0.655708 |       0.171196 |    2.62118 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.662693 |       0.293522 |    15.0151 |
| solution-flask     |     0.657832 |       1.00923  |    15.0983 |
| solution-aron-mark |     0.65257  |       0.296231 |    15.4141 |