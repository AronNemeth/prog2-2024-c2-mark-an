# 2026-06-21

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.15383  |       1.03284  |   0.107507 |
| solution-aron-mark |     0.436472 |       0.151704 |   0.235272 |
| solution-pl        |     6.02676  |       0.164502 |   0.236734 |
| solution-1-flask   |     0.450929 |       1.00828  |   0.269738 |
| solution-1         |     7.42378  |       1e-06    |   0.661865 |
| solution-2         |     0.416866 |       0.637525 |   1.05579  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.436494 |       0.152221 |   0.367148 |
| solution-pl        |     0.431084 |       0.152809 |   0.371385 |
| solution-flask     |     0.428212 |       1.0085   |   0.396441 |
| solution-1-flask   |     0.433584 |       1.00843  |   0.800435 |
| solution-2         |     0.424272 |       0.516336 |   4.65512  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.435774 |       0.158486 |    1.0994  |
| solution-pl        |     0.436697 |       0.158378 |    1.10558 |
| solution-flask     |     0.437153 |       1.00842  |    1.67546 |
| solution-1-flask   |     0.443039 |       1.00862  |    5.6373  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.431831 |       0.182206 |    3.8836  |
| solution-aron-mark |     0.429682 |       0.183168 |    3.94166 |
| solution-flask     |     0.439732 |       1.00892  |    5.35128 |