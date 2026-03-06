# 2026-03-06

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.50234  |       1.07548  |   0.106151 |
| solution-aron-mark |     0.445348 |       0.148507 |   0.236879 |
| solution-pl        |     4.60143  |       0.145668 |   0.241095 |
| solution-1-flask   |     0.465078 |       1.00875  |   0.265486 |
| solution-1         |     7.53476  |       1e-06    |   0.869657 |
| solution-2         |     0.445584 |       0.724266 |   0.952341 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.456805 |       0.14843  |   0.370236 |
| solution-aron-mark |     0.444978 |       0.153563 |   0.370559 |
| solution-flask     |     0.452677 |       1.00874  |   0.394224 |
| solution-1-flask   |     0.454342 |       1.00864  |   0.801109 |
| solution-2         |     0.445747 |       0.512389 |   2.83682  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.465091 |       0.159572 |    1.1255  |
| solution-aron-mark |     0.446005 |       0.155091 |    1.13376 |
| solution-flask     |     0.45033  |       1.00895  |    1.64777 |
| solution-1-flask   |     0.446676 |       1.00901  |    5.53926 |
| solution-2         |     0.454981 |       0.615176 |  295.37    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.445186 |       0.179847 |    3.88654 |
| solution-pl        |     0.458637 |       0.182014 |    3.96566 |
| solution-flask     |     0.460455 |       1.00907  |    5.29171 |