# 2025-02-15

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.51914  |       1.00835  |   0.076872 |
| solution-pl        |     1.76321  |       0.176199 |   0.203809 |
| solution-aron-mark |     0.523063 |       0.138036 |   0.20466  |
| solution-1-flask   |     5.18036  |       1.10644  |   0.281771 |
| solution-1         |     7.51873  |       1e-06    |   0.671289 |
| solution-2         |     0.526772 |       0.5788   |   1.1942   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.528105 |       1.00946  |   0.29036  |
| solution-pl        |     0.52826  |       0.141264 |   0.303016 |
| solution-aron-mark |     0.521264 |       0.14057  |   0.305898 |
| solution-1-flask   |     0.530451 |       1.00888  |   0.812872 |
| solution-2         |     0.524624 |       0.496691 |   2.40114  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.524256 |       0.15394  |   0.90249  |
| solution-aron-mark |     0.525203 |       0.146408 |   0.913461 |
| solution-flask     |     0.524891 |       1.00859  |   1.23036  |
| solution-1-flask   |     0.531898 |       1.00874  |   5.66682  |
| solution-2         |     0.522952 |       0.549326 |  25.9312   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.527343 |       0.176593 |    2.79929 |
| solution-pl        |     0.521708 |       0.175922 |    2.8067  |
| solution-flask     |     0.522915 |       1.0084   |    4.12666 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.52433  |       0.275531 |    16.1094 |
| solution-aron-mark |     0.523762 |       0.275288 |    16.4927 |