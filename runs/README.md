# 2024-11-15

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.55246  |       1.05714  |   0.107314 |
| solution-pl        |     5.69171  |       0.104913 |   0.1746   |
| solution-aron-mark |     0.548337 |       0.104044 |   0.195063 |
| solution-1-flask   |     0.558576 |       1.009    |   0.247756 |
| solution-1         |     7.46354  |       1e-06    |   0.722552 |
| solution-2         |     0.541793 |       0.581074 |   1.34562  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.552001 |       0.106267 |   0.30663  |
| solution-pl        |     0.549627 |       0.104515 |   0.331702 |
| solution-flask     |     0.55101  |       1.00889  |   0.480923 |
| solution-1-flask   |     0.558869 |       1.00892  |   0.767433 |
| solution-2         |     0.547481 |       0.461998 |   3.77001  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.550174 |       0.114315 |    1.00331 |
| solution-aron-mark |     0.550274 |       0.11216  |    1.01237 |
| solution-flask     |     0.542508 |       1.00862  |    2.14679 |
| solution-1-flask   |     0.56105  |       1.00902  |    5.38907 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.549264 |       0.145232 |    4.16019 |
| solution-aron-mark |     0.551075 |       0.142047 |    4.19691 |
| solution-flask     |     0.55054  |       1.0085   |    8.30922 |