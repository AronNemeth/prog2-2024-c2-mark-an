# 2026-06-03

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.66454  |       1.0684   |   0.116312 |
| solution-aron-mark |     0.434437 |       0.151506 |   0.243279 |
| solution-pl        |     0.434384 |       0.151531 |   0.245104 |
| solution-1-flask   |     0.438861 |       1.00809  |   0.268006 |
| solution-1         |     7.36036  |       1e-06    |   0.678168 |
| solution-2         |     4.32693  |       0.645217 |   0.994339 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.432698 |       0.153018 |   0.370461 |
| solution-aron-mark |     0.435599 |       0.151768 |   0.370993 |
| solution-flask     |     0.436217 |       1.00847  |   0.411008 |
| solution-1-flask   |     0.440823 |       1.00852  |   0.884402 |
| solution-2         |     0.433017 |       0.509749 |   4.5157   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.433178 |       0.158863 |    1.13197 |
| solution-aron-mark |     0.436727 |       0.156796 |    1.14135 |
| solution-flask     |     0.437632 |       1.00836  |    1.68248 |
| solution-1-flask   |     0.436906 |       1.00877  |    5.61751 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.429807 |       0.187613 |    4.05609 |
| solution-pl        |     0.43269  |       0.184653 |    4.09358 |
| solution-flask     |     0.43119  |       1.00849  |    5.47978 |