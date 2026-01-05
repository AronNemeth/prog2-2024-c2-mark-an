# 2026-01-05

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.06564  |       1.06567  |   0.093317 |
| solution-pl        |     0.450033 |       0.159461 |   0.23174  |
| solution-aron-mark |     0.449172 |       0.157369 |   0.250274 |
| solution-1-flask   |     0.461636 |       1.00756  |   0.258896 |
| solution-1         |     8.19021  |       1e-06    |   0.664827 |
| solution-2         |     4.33383  |       0.664546 |   0.912527 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.452425 |       0.154252 |   0.338665 |
| solution-aron-mark |     0.449198 |       0.157879 |   0.345397 |
| solution-flask     |     0.445114 |       1.00687  |   0.422509 |
| solution-1-flask   |     0.486773 |       1.0071   |   0.738626 |
| solution-2         |     0.448345 |       0.516255 |   3.88196  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.444285 |       0.165061 |    1.04064 |
| solution-aron-mark |     0.464762 |       0.160879 |    1.04949 |
| solution-flask     |     0.442809 |       1.00673  |    1.82415 |
| solution-1-flask   |     0.454468 |       1.00663  |    5.5924  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.455049 |       0.196492 |    4.7992  |
| solution-aron-mark |     0.466076 |       0.201799 |    5.03088 |
| solution-flask     |     0.457174 |       1.00712  |    6.37979 |