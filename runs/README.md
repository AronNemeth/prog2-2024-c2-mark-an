# 2026-03-02

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.8156   |       1.03955  |   0.109167 |
| solution-pl        |     4.96487  |       0.14514  |   0.236165 |
| solution-aron-mark |     0.463226 |       0.147865 |   0.243835 |
| solution-1-flask   |     0.443896 |       1.08869  |   0.264865 |
| solution-1         |     7.93691  |       1e-06    |   0.607363 |
| solution-2         |     0.45715  |       0.574907 |   1.1873   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.452199 |       0.147808 |   0.369919 |
| solution-pl        |     0.442943 |       0.151786 |   0.374308 |
| solution-flask     |     0.456571 |       1.0088   |   0.393203 |
| solution-1-flask   |     0.450766 |       1.00896  |   0.797112 |
| solution-2         |     0.445309 |       0.540064 |   2.65968  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.453316 |       0.154551 |    1.13136 |
| solution-aron-mark |     0.447785 |       0.154149 |    1.14617 |
| solution-flask     |     0.45069  |       1.00877  |    1.64385 |
| solution-1-flask   |     0.457198 |       1.00906  |    5.67013 |
| solution-2         |     0.449554 |       0.576576 |   26.0227  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.441557 |       0.180765 |    3.9283  |
| solution-aron-mark |     0.439531 |       0.180715 |    3.96829 |
| solution-flask     |     0.447635 |       1.00908  |    5.2482  |