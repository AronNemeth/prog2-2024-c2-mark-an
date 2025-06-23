# 2025-06-23

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.499728 |       1.00828  |   0.101669 |
| solution-aron-mark |     5.60841  |       0.155723 |   0.235772 |
| solution-pl        |     0.487016 |       0.149072 |   0.239264 |
| solution-1-flask   |     1.07728  |       1.03574  |   0.265067 |
| solution-1         |     7.39057  |       1e-06    |   0.628141 |
| solution-2         |     0.502038 |       0.5464   |   1.1439   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.500704 |       0.150676 |   0.361229 |
| solution-aron-mark |     0.497396 |       0.151057 |   0.364047 |
| solution-flask     |     0.500819 |       1.00822  |   0.38611  |
| solution-1-flask   |     0.514375 |       1.00842  |   0.797974 |
| solution-2         |     0.509209 |       0.501737 |   2.48226  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.497555 |       0.157851 |    1.08304 |
| solution-aron-mark |     0.502119 |       0.157778 |    1.10755 |
| solution-flask     |     0.499835 |       1.00839  |    1.59382 |
| solution-1-flask   |     0.505035 |       1.00847  |    5.49143 |
| solution-2         |     0.498023 |       0.554241 |   48.9807  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.497253 |       0.187875 |    3.22382 |
| solution-aron-mark |     0.496031 |       0.191008 |    3.22493 |
| solution-flask     |     0.496782 |       1.00851  |    5.11593 |