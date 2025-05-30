# 2025-05-30

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.22432  |       1.00883  |   0.089268 |
| solution-aron-mark |     0.499547 |       0.145698 |   0.224627 |
| solution-pl        |     0.504935 |       0.150563 |   0.225176 |
| solution-1-flask   |     5.9094   |       1.06272  |   0.250719 |
| solution-1         |     8.08605  |       1e-06    |   0.651206 |
| solution-2         |     0.494807 |       0.595686 |   2.34778  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.502878 |       0.150121 |   0.349702 |
| solution-pl        |     0.504459 |       0.150255 |   0.372007 |
| solution-flask     |     0.497375 |       1.00819  |   0.398411 |
| solution-1-flask   |     0.504165 |       1.00806  |   0.792687 |
| solution-2         |     0.504249 |       0.509207 |   2.6285   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.504321 |       0.159156 |    1.04295 |
| solution-pl        |     0.505461 |       0.158545 |    1.05698 |
| solution-flask     |     0.502456 |       1.00855  |    1.55473 |
| solution-1-flask   |     0.5101   |       1.00838  |    5.42829 |
| solution-2         |     0.501522 |       0.561643 |   44.4674  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.499661 |       0.186418 |    3.18689 |
| solution-pl        |     0.500792 |       0.18937  |    3.19554 |
| solution-flask     |     0.503676 |       1.00843  |    5.00338 |