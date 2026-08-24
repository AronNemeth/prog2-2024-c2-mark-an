# 2026-08-24

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     4.51005  |       1.04279  |   0.124763 |
| solution-pl        |     0.450331 |       0.160459 |   0.241905 |
| solution-aron-mark |     4.92602  |       0.158144 |   0.246432 |
| solution-1-flask   |     0.458259 |       1.0086   |   0.275316 |
| solution-1         |     8.36657  |       1e-06    |   0.668857 |
| solution-2         |     0.451774 |       0.666155 |   0.83285  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.447926 |       0.160142 |   0.365241 |
| solution-pl        |     0.43642  |       0.155724 |   0.374307 |
| solution-flask     |     0.439013 |       1.00835  |   0.388433 |
| solution-1-flask   |     0.441211 |       1.00867  |   0.827063 |
| solution-2         |     0.438605 |       0.523861 |   3.23463  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.443506 |       0.164383 |    1.11747 |
| solution-aron-mark |     0.437375 |       0.163308 |    1.11965 |
| solution-flask     |     0.439594 |       1.00844  |    1.69565 |
| solution-1-flask   |     0.431217 |       1.00848  |    5.74342 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.445434 |       0.189206 |    3.54315 |
| solution-pl        |     0.427372 |       0.189699 |    3.57264 |
| solution-flask     |     0.430166 |       1.0086   |    5.39442 |