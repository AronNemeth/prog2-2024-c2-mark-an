# 2026-01-02

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.65733  |       1.15362  |   0.105834 |
| solution-aron-mark |     0.496135 |       0.167389 |   0.252601 |
| solution-pl        |     0.505438 |       0.185132 |   0.253868 |
| solution-1-flask   |     0.500031 |       1.00864  |   0.275038 |
| solution-1         |     7.6578   |       1e-06    |   0.75199  |
| solution-2         |     4.57523  |       0.667457 |   1.0931   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.494638 |       0.170096 |   0.376328 |
| solution-pl        |     0.49837  |       0.17284  |   0.376815 |
| solution-flask     |     0.49972  |       1.00858  |   0.382933 |
| solution-1-flask   |     0.506798 |       1.00876  |   0.807251 |
| solution-2         |     0.495336 |       0.553947 |   3.63093  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.503604 |       0.175151 |    1.07228 |
| solution-pl        |     0.503954 |       0.179089 |    1.09978 |
| solution-flask     |     0.491633 |       1.00885  |    1.61574 |
| solution-1-flask   |     0.507623 |       1.00862  |    5.73056 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.498861 |       0.199026 |    3.78475 |
| solution-pl        |     0.495075 |       0.200489 |    3.80212 |
| solution-flask     |     0.505233 |       1.00888  |    5.36467 |