# 2025-10-12

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.18316  |       1.04645  |   0.103757 |
| solution-pl        |     0.520613 |       0.165508 |   0.24867  |
| solution-aron-mark |     0.494728 |       0.15994  |   0.254535 |
| solution-1-flask   |     0.508919 |       1.00836  |   0.278837 |
| solution-1         |     7.91401  |       1e-06    |   0.831006 |
| solution-2         |     4.75437  |       0.728753 |   0.83742  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.50217  |       0.168564 |   0.375245 |
| solution-aron-mark |     0.491856 |       0.159053 |   0.376495 |
| solution-flask     |     0.497792 |       1.00899  |   0.382584 |
| solution-1-flask   |     0.506074 |       1.00842  |   0.802835 |
| solution-2         |     0.490976 |       0.517401 |   2.97457  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.494809 |       0.168102 |    1.072   |
| solution-pl        |     0.494996 |       0.170424 |    1.07651 |
| solution-flask     |     0.501042 |       1.00883  |    1.59845 |
| solution-1-flask   |     0.502294 |       1.00861  |    5.69477 |
| solution-2         |     0.501006 |       0.582106 |   36.3796  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.495466 |       0.19705  |    3.35951 |
| solution-aron-mark |     0.496784 |       0.204488 |    3.39208 |
| solution-flask     |     0.503392 |       1.0085   |    5.23692 |