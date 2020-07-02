## Profiling Python's `eval`

Average times comparing two functions:

    int('2') # convert string to int

vs.

    eval('2') # evaluate integer 2
        (pre-compiled vs. live)

Notes about testing setup:

>I started by looping through integers and using 10 ^ i as the number of loops, but the performance increased too quickly and some of the last loops were too slow

>I ended up using 5 to powers of 0 through 8 and achieved reasonably quick results with some obvious differences in performance. So, the best fit for this test, on this system, pairing an obvious trend with reasonable times are:

        i = [0 .. 8]
        n = 5 ^ i

Methods:

Times are recorded as ∆t with t(0) and t(1) setup immediately before and after the single statement being tested, respectively. They are measured in integer nanoseconds using the 'perfcounter' function from 'time.'

A few sample tests with other counters showed this counter to be the most consistent, but there were not any large discrepancies in any event. I am no expert in 'timing' or 'profiling' and I am making this up as I go, so ymmv ...

---

Data Set with precompiled eval statement, `EVAL_PRECOMPILED`, used in place of a live eval.

*lrucache: none   eval: precompiled*

| i   | n     | eval   avg | min  | set    avg | min  |
| --- | ----- | ---------- | ---- | ---------- | ---- |
| 0   | 1     | 4267       | 2100 | 3505       | 2631 |
| 1   | 5     | 900        | 377  | 1170       | 382  |
| 2   | 25    | 638        | 347  | 609        | 347  |
| 3   | 125   | 607        | 352  | 594        | 349  |
| 4   | 625   | 708        | 352  | 926        | 366  |
| 5   | 3125  | 801        | 322  | 1078       | 341  |
| 6   | 15625 | 770        | 322  | 695        | 334  |
| 7   | 78125 | 762        | 321  | 951        | 332  |

*lrucache: loops only   eval: precompiled*


| i   | n     | eval   avg | min  | set    avg | min  |
| --- | ----- | ---------- | ---- | ---------- | ---- |
| 0   | 1     | 5577       | 2724 | 4786       | 3449 |
| 1   | 5     | 1711       | 644  | 1492       | 655  |
| 2   | 25    | 1202       | 618  | 2968       | 544  |
| 3   | 125   | 1229       | 590  | 1399       | 556  |
| 4   | 625   | 882        | 351  | 858        | 335  |
| 5   | 3125  | 606        | 318  | 937        | 323  |
| 6   | 15625 | 1055       | 320  | 993        | 331  |
| 7   | 78125 | 1060       | 317  | 841        | 313  |

*lrucache: tests only   eval: precompiled*


| i   | n     | eval   avg | min  | set    avg | min  |
| --- | ----- | ---------- | ---- | ---------- | ---- |
| 0   | 1     | 5701       | 3787 | 5077       | 4257 |
| 1   | 5     | 608        | 175  | 540        | 184  |
| 2   | 25    | 444        | 178  | 429        | 174  |
| 3   | 125   | 437        | 175  | 513        | 179  |
| 4   | 625   | 409        | 174  | 410        | 176  |
| 5   | 3125  | 467        | 164  | 551        | 186  |
| 6   | 15625 | 543        | 164  | 720        | 169  |
| 7   | 78125 | 504        | 164  | 538        | 166  |

*lrucache: both   eval: precompiled*


| i   | n     | eval   avg | min  | set    avg | min  |
| --- | ----- | ---------- | ---- | ---------- | ---- |
| 0   | 1     | 3981       | 2303 | 3447       | 2513 |
| 1   | 5     | 607        | 170  | 514        | 174  |
| 2   | 25    | 422        | 173  | 428        | 179  |
| 3   | 125   | 400        | 175  | 399        | 175  |
| 4   | 625   | 406        | 173  | 404        | 166  |
| 5   | 3125  | 431        | 171  | 428        | 168  |
| 6   | 15625 | 479        | 163  | 669        | 165  |
| 7   | 78125 | 474        | 162  | 772        | 166  |

---

Data Set with live eval statement compiled on the fly.

*lrucache: none   eval: live*

| i   | n     | eval   avg | min   | set    avg | min  |
| --- | ----- | ---------- | ----- | ---------- | ---- |
| 0   | 1     | 20787      | 18892 | 3665       | 2534 |
| 1   | 5     | 8374       | 6334  | 814        | 339  |
| 2   | 25    | 6590       | 6125  | 631        | 354  |
| 3   | 125   | 6520       | 6104  | 604        | 342  |
| 4   | 625   | 7448       | 5870  | 996        | 354  |
| 5   | 3125  | 8635       | 5875  | 592        | 325  |
| 6   | 15625 | 8280       | 5710  | 648        | 315  |
| 7   | 78125 | 7231       | 5511  | 679        | 318  |

*lrucache: loops only   eval: live*

| i   | n     | eval   avg | min   | set    avg | min  |
| --- | ----- | ---------- | ----- | ---------- | ---- |
| 0   | 1     | 30893      | 28815 | 4198       | 2925 |
| 1   | 5     | 10491      | 7477  | 1527       | 664  |
| 2   | 25    | 14980      | 6836  | 1175       | 617  |
| 3   | 125   | 10749      | 6404  | 645        | 371  |
| 4   | 625   | 12659      | 6238  | 768        | 362  |
| 5   | 3125  | 8178       | 5731  | 664        | 338  |
| 6   | 15625 | 8204       | 5731  | 769        | 324  |
| 7   | 78125 | 8518       | 5410  | 649        | 314  |

*lrucache: tests only    eval: live*

| i   | n     | eval   avg | min   | set    avg | min  |
| --- | ----- | ---------- | ----- | ---------- | ---- |
| 0   | 1     | 22389      | 20386 | 3766       | 2724 |
| 1   | 5     | 612        | 164   | 537        | 167  |
| 2   | 25    | 429        | 166   | 429        | 165  |
| 3   | 125   | 402        | 167   | 404        | 177  |
| 4   | 625   | 408        | 174   | 521        | 170  |
| 5   | 3125  | 449        | 164   | 421        | 176  |
| 6   | 15625 | 591        | 164   | 527        | 170  |
| 7   | 78125 | 497        | 163   | 680        | 165  |

*lrucache: both   eval: live*

| i   | n     | eval   avg | min   | set    avg | min  |
| --- | ----- | ---------- | ----- | ---------- | ---- |
| 0   | 1     | 44258      | 41357 | 6733       | 4782 |
| 1   | 5     | 4265       | 286   | 1113       | 284  |
| 2   | 25    | 539        | 186   | 474        | 187  |
| 3   | 125   | 442        | 185   | 436        | 183  |
| 4   | 625   | 448        | 184   | 491        | 165  |
| 5   | 3125  | 527        | 170   | 442        | 172  |
| 6   | 15625 | 798        | 163   | 483        | 164  |
| 7   | 78125 | 538        | 162   | 589        | 165  |




