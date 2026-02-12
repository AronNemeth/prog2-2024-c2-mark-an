# 2026-02-12

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.87163  |       1.05796  |   0.10783  |
| solution-pl        |     4.79579  |       0.150628 |   0.244431 |
| solution-aron-mark |     0.462094 |       0.151849 |   0.251817 |
| solution-1-flask   |     0.489314 |       1.00884  |   0.271648 |
| solution-1         |     7.99562  |       1e-06    |   0.824894 |
| solution-2         |     0.475477 |       0.747504 |   1.04783  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.456557 |       0.155141 |   0.37519  |
| solution-flask     |     0.453811 |       1.00901  |   0.402324 |
| solution-pl        |     0.460066 |       0.151753 |   0.43342  |
| solution-1-flask   |     0.490072 |       1.00942  |   0.797504 |
| solution-2         |     0.462615 |       0.522968 |   2.96434  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.459332 |       0.156224 |    1.13529 |
| solution-aron-mark |     0.463862 |       0.156326 |    1.13578 |
| solution-flask     |     0.460708 |       1.00923  |    1.64416 |
| solution-1-flask   |     0.462654 |       1.00916  |    5.63516 |
| solution-2         |     0.455485 |       0.581903 |  306.211   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.451154 |        0.18305 |    3.91207 |
| solution-aron-mark |     0.448944 |        0.18232 |    3.98862 |
| solution-flask     |     0.45344  |        1.00888 |    5.2842  |