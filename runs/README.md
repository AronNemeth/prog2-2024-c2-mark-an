# 2026-01-21

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.65677  |       1.07174  |   0.101166 |
| solution-pl        |     0.476541 |       0.162174 |   0.243514 |
| solution-aron-mark |     0.474095 |       0.162616 |   0.254029 |
| solution-1-flask   |     0.476987 |       1.00825  |   0.271302 |
| solution-1         |     7.95808  |       1e-06    |   0.720276 |
| solution-2         |     4.54334  |       0.647667 |   0.958707 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.480287 |       0.165351 |   0.367806 |
| solution-pl        |     0.476386 |       0.163939 |   0.373419 |
| solution-flask     |     0.469361 |       1.00837  |   0.37527  |
| solution-1-flask   |     0.479737 |       1.00833  |   0.781188 |
| solution-2         |     0.47929  |       0.506288 |   5.18701  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.469853 |       0.169892 |    1.06951 |
| solution-pl        |     0.477912 |       0.169044 |    1.07634 |
| solution-flask     |     0.47448  |       1.00866  |    1.58155 |
| solution-1-flask   |     0.477856 |       1.0085   |    5.60538 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.473309 |       0.194435 |    3.51005 |
| solution-pl        |     0.467524 |       0.192927 |    3.51285 |
| solution-flask     |     0.483333 |       1.00877  |    5.14532 |