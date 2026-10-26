# 2026-10-26

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.28204  |       1.053    |   0.107093 |
| solution-pl        |     0.443722 |       0.174074 |   0.256274 |
| solution-aron-mark |     6.59456  |       0.19812  |   0.261037 |
| solution-1-flask   |     0.44137  |       1.00838  |   0.268672 |
| solution-1         |     8.34332  |       1e-06    |   0.838904 |
| solution-2         |     0.425622 |       0.801022 |   0.96979  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.428032 |       1.0086   |   0.236607 |
| solution-pl        |     0.432978 |       0.168184 |   0.396318 |
| solution-aron-mark |     0.455125 |       0.168027 |   0.398048 |
| solution-1-flask   |     0.432093 |       1.00839  |   0.812208 |
| solution-2         |     0.434053 |       0.523732 |   2.88315  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.439884 |       1.00857  |    1.0568  |
| solution-pl        |     0.432997 |       0.174022 |    1.19235 |
| solution-aron-mark |     0.441414 |       0.173578 |    1.19798 |
| solution-1-flask   |     0.447802 |       1.00842  |    5.53243 |
| solution-2         |     0.42749  |       0.58158  |  178.465   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.440635 |       0.212083 |    3.60714 |
| solution-pl        |     0.42716  |       0.203113 |    3.61512 |
| solution-flask     |     0.42695  |       1.00853  |    4.42248 |