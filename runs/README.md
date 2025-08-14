# 2025-08-14

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.97376  |       1.11056  |   0.100025 |
| solution-aron-mark |     5.02535  |       0.151823 |   0.23764  |
| solution-pl        |     0.936733 |       0.153365 |   0.23774  |
| solution-1-flask   |     0.946121 |       1.00837  |   0.270206 |
| solution-1         |     8.6346   |       1e-06    |   1.02868  |
| solution-2         |     0.933632 |       0.738342 |   1.23736  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.921482 |       0.15587  |   0.362177 |
| solution-aron-mark |     0.938935 |       0.15277  |   0.363307 |
| solution-flask     |     0.938091 |       1.00826  |   0.375957 |
| solution-1-flask   |     0.483664 |       1.00833  |   0.818187 |
| solution-2         |     0.937814 |       0.507293 |   2.64334  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.47917  |       0.159912 |    1.06672 |
| solution-aron-mark |     0.482492 |       0.160125 |    1.07113 |
| solution-flask     |     0.488421 |       1.00843  |    1.54207 |
| solution-1-flask   |     0.494457 |       1.00864  |    5.58247 |
| solution-2         |     0.47945  |       0.564358 |  302.943   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.483412 |       0.195462 |    3.22826 |
| solution-pl        |     0.477276 |       0.194611 |    3.24961 |
| solution-flask     |     0.482004 |       1.00859  |    5.02524 |