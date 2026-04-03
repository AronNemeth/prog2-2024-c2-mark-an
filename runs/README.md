# 2026-04-03

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.48259  |       1.03899  |   0.108109 |
| solution-aron-mark |     0.436195 |       0.153575 |   0.242032 |
| solution-pl        |     4.88782  |       0.154691 |   0.250593 |
| solution-1-flask   |     0.442077 |       1.00825  |   0.271392 |
| solution-1         |     8.69367  |       1e-06    |   0.730386 |
| solution-2         |     0.427211 |       0.664665 |   0.954006 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.429467 |       0.151953 |   0.375342 |
| solution-pl        |     0.430088 |       0.150277 |   0.37735  |
| solution-flask     |     0.430008 |       1.00847  |   0.393814 |
| solution-1-flask   |     0.433929 |       1.00834  |   0.828472 |
| solution-2         |     0.428957 |       0.542797 |   3.79379  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.430668 |       0.156111 |    1.13414 |
| solution-pl        |     0.506856 |       0.171828 |    1.14427 |
| solution-flask     |     0.449942 |       1.00904  |    1.6728  |
| solution-1-flask   |     0.438429 |       1.00843  |    5.76196 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.438932 |       0.185563 |    4.10332 |
| solution-pl        |     0.43815  |       0.18441  |    4.11073 |
| solution-flask     |     0.439389 |       1.00901  |    5.36034 |