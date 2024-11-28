# 2024-11-28

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.28978  |       1.07677  |   0.104341 |
| solution-pl        |     5.74132  |       0.108926 |   0.176139 |
| solution-aron-mark |     0.548889 |       0.107104 |   0.1777   |
| solution-1-flask   |     0.557302 |       1.00917  |   0.25698  |
| solution-1         |     7.53948  |       1e-06    |   0.618694 |
| solution-2         |     0.54521  |       0.554664 |   1.03653  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.554002 |       0.108151 |   0.311197 |
| solution-pl        |     0.551703 |       0.109057 |   0.326243 |
| solution-flask     |     0.555611 |       1.00896  |   0.500113 |
| solution-1-flask   |     0.586503 |       1.01007  |   0.769603 |
| solution-2         |     0.554673 |       0.465386 |   2.56951  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.553807 |       0.115652 |    1.01187 |
| solution-pl        |     0.558601 |       0.116601 |    1.03241 |
| solution-flask     |     0.549344 |       1.00862  |    2.19591 |
| solution-1-flask   |     0.560205 |       1.0089   |    5.33554 |
| solution-2         |     0.563376 |       0.516856 |  163.737   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.550294 |       0.147068 |    4.28277 |
| solution-pl        |     0.554094 |       0.145006 |    4.35548 |
| solution-flask     |     0.548124 |       1.00891  |    8.67938 |