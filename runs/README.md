# 2026-02-23

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.82042  |       1.05591  |   0.104407 |
| solution-pl        |     0.483585 |       0.15828  |   0.237149 |
| solution-aron-mark |     0.484124 |       0.156002 |   0.242158 |
| solution-1-flask   |     0.476326 |       1.00839  |   0.271829 |
| solution-1         |     7.95109  |       1e-06    |   0.948788 |
| solution-2         |     4.77115  |       0.765103 |   1.31457  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.494044 |       0.158921 |   0.368232 |
| solution-pl        |     0.479008 |       0.154791 |   0.373839 |
| solution-flask     |     0.485219 |       1.00879  |   0.395345 |
| solution-1-flask   |     0.496538 |       1.00859  |   0.818541 |
| solution-2         |     0.492291 |       0.564656 |   2.82588  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.475848 |       0.163522 |    1.08967 |
| solution-aron-mark |     0.472456 |       0.162216 |    1.09317 |
| solution-flask     |     0.467547 |       1.00908  |    1.61437 |
| solution-1-flask   |     0.470215 |       1.00893  |    5.8622  |
| solution-2         |     0.473818 |       0.626276 |   26.6145  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.469756 |       0.187971 |    4.01745 |
| solution-aron-mark |     0.480822 |       0.18671  |    4.03544 |
| solution-flask     |     0.468647 |       1.00872  |    5.37058 |