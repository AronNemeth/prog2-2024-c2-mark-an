# 2025-06-12

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.539808 |       1.00842  |   0.104009 |
| solution-pl        |     0.572544 |       0.155558 |   0.24414  |
| solution-aron-mark |     6.86918  |       0.191939 |   0.245965 |
| solution-1-flask   |     1.488    |       1.0562   |   0.279541 |
| solution-1         |     8.6465   |       1e-06    |   0.711656 |
| solution-2         |     0.562432 |       0.683104 |   1.24479  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.522263 |       0.155097 |   0.366416 |
| solution-aron-mark |     0.532881 |       0.166089 |   0.373317 |
| solution-flask     |     0.528047 |       1.00876  |   0.382546 |
| solution-1-flask   |     0.544299 |       1.00893  |   0.803406 |
| solution-2         |     0.537696 |       0.565808 |   6.1988   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.533184 |        0.15964 |    1.0759  |
| solution-pl        |     0.527366 |        0.16578 |    1.0765  |
| solution-flask     |     0.562239 |        1.00899 |    1.62495 |
| solution-1-flask   |     0.554752 |        1.00883 |    5.8644  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.538227 |       0.198753 |    3.66234 |
| solution-aron-mark |     0.587336 |       0.213868 |    3.82318 |
| solution-flask     |     0.545592 |       1.00891  |    5.44206 |