# 2025-01-24

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.38784  |       1.08306  |   0.082541 |
| solution-pl        |     4.54204  |       0.147814 |   0.202768 |
| solution-aron-mark |     0.561563 |       0.140807 |   0.204365 |
| solution-1-flask   |     0.554077 |       1.00886  |   0.265093 |
| solution-1         |     7.43954  |       1e-06    |   0.604203 |
| solution-2         |     0.555339 |       0.589835 |   1.64669  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.542976 |       1.00898  |   0.295151 |
| solution-pl        |     0.544397 |       0.141364 |   0.304839 |
| solution-aron-mark |     0.54092  |       0.140593 |   0.310384 |
| solution-1-flask   |     0.547894 |       1.00888  |   0.819747 |
| solution-2         |     0.542996 |       0.534077 |   2.15364  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.552163 |       0.149797 |   0.898509 |
| solution-aron-mark |     0.548338 |       0.150643 |   0.907084 |
| solution-flask     |     0.559809 |       1.00905  |   1.24381  |
| solution-1-flask   |     0.553956 |       1.00942  |   5.72611  |
| solution-2         |     0.537464 |       0.558026 | 315.011    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.547989 |       0.179598 |    2.9215  |
| solution-pl        |     0.544585 |       0.178196 |    2.92752 |
| solution-flask     |     0.537035 |       1.00923  |    4.33876 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.546703 |       0.283065 |    17.9577 |
| solution-pl        |     0.53836  |       0.279775 |    18.218  |