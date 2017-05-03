## Admix
Admix is a simple tool to calculate ancestry composition (admixture proportions) from SNP raw data provided by different DNA testing vendors (such as 23andme and AncestryDNA).

### Usage
Support that you've already had your 23andme raw data downloaded and placed in the current directory with the name `my_raw_data.txt`. Then you can perform admixture calculation by specifying the calculation model (`K7b` in this example):

```
admix -f my_raw_data.txt -v 23andme -m K7b
```

You can also set multiple models for calculation:
```
admix -f my_raw_data.txt -v 23andme -m K7b K12b
```

If no models are set, the program will apply all the available models:
```
admix -f my_raw_data.txt -v 23andme
```
You can choose the raw data format by changing the `-v` or `--vendor` parameter. The value should be one of `23andme` and `ancestry`.

If you don't have your raw data yet, you can also test the program by using a demo 23andme data file provided by the program:
```
admix -m world9
```

Chinese users may turn on the `-z` flag so the population would be displayed in Chinese:
```
admix -z -m E11
```

For more help information, you could use:
```
admix -h
```

### Models
Admix supports many publicly available admixture models. All the calculator files are properties of their authors, and are not covered by the license of this program. Links are provided which contain more information for each model.

| model value | model name | source |
| ----- | --------- | ---- |
| `K7b` | Dodecad K7b | [Link](http://dodecad.blogspot.com/2012/01/k12b-and-k7b-calculators.html) |
| `K12b` | Dodecad K12b | [Link](http://dodecad.blogspot.com/2012/01/k12b-and-k7b-calculators.html) |
| `globe13` | Dodecad globe13 | [Link](http://dodecad.blogspot.com/2012/10/globe13-calculator.html) |
| `goble10` | Dodecad globe10 | [Link](http://dodecad.blogspot.com/2012/10/globe10-calculator.html) |
| `world9` | Dodecad world9 | [Link](http://dodecad.blogspot.com/2011/12/world9-calculator.html) |
| `Eurasia7` | Dodecad Eurasia7 | [Link](http://dodecad.blogspot.com/2011/10/eurasia7-calculator.html) |
| `Africa9` | Dodecad Africa9 | [Link](http://dodecad.blogspot.com/2011/09/africa9-calculator.html) |
| `weac2` | Dodecad weac (West Eurasian cline) 2 | [Link](http://dodecad.blogspot.com/2012/06/weac2-calculator.html) |
| `E11` | E11 | [Link](http://www.ranhaer.com/thread-32241-1-1.html) |
| `K36` | Eurogenes K36 | [Link](http://bga101.blogspot.com/2013/03/eurogenes-k36-at-gedmatch.html) |
| `EUtest13` | Eurogenes EUtest K13 | [Link](http://bga101.blogspot.com/2013/11/updated-eurogenes-k13-at-gedmatch.html) |
| `Jtest14` | Eurogenes Jtest K14 | [Link](http://bga101.blogspot.com/2012/09/eurogenes-ashkenazim-ancestry-test-files.html) |
| `HarappaWorld` | HarappaWorld | [Link](http://www.harappadna.org/2012/05/harappaworld-admixture/) |
| `TurkicK11` | Turkic K11 | [Link](http://www.anthrogenica.com/showthread.php?8817-Turkic-K11-Admixture-Calculator) |
| `KurdishK10` | Kurdish K10 | [Link](http://www.anthrogenica.com/showthread.php?8571-K10-Kurdish-Calculator-Version-1/page6) |
| `AncientNearEast13` | Ancient Near East K13 | [Link](http://www.anthrogenica.com/showthread.php?8193-ancient-DNA-in-the-Gedrosia-Near-East-Neolithic-K13) |
| `K7AMI` | Eurogenes K7 AMI | [Link](http://www.anthrogenica.com/showthread.php?4548-Upcoming-DIY-Eurogenes-K7-amp-K8-Calculator-amp-Oracles-for-tracking-E-Asian-amp-ASI) |
| `K8AMI` | Eurogenes K8 AMI | [Link](http://www.anthrogenica.com/showthread.php?4548-Upcoming-DIY-Eurogenes-K7-amp-K8-Calculator-amp-Oracles-for-tracking-E-Asian-amp-ASI) |
| MDLPK27 | MDLP K27 | [Link](http://www.anthrogenica.com/showthread.php?4557-Post-MDLP-K27-Results) |
| `puntDNAL` | puntDNAL K12 Ancient World | [Link](http://www.anthrogenica.com/showthread.php?8034-PuntDNAL-K12-Ancient-World-Results) |

### Implementation
Maximum likelihood estimation (MLE) algorithm is applied for ancestry composition calcuation, and the implementation is fairly straightforward.

Let *F<sub>nk</sub>* be the minor allele frequency of SNP marker *n* for popluation *k*, *l<sup>minor</sup><sub>n</sub>* and *l<sup>major</sup><sub>n</sub>* be the minor and major allele for marker *n* respectively, and *G<sub>ni</sub>* be the allele at marker *n* of the individual we're interested in (*i*=1,2). Our goal is to find the admixutre fraction *q<sub>k</sub>* of the individual, which maximize the log likelihood function

![](http://latex.codecogs.com/gif.latex?\\chi_{\\{l^{minor}_n\\}}(G_{ni})j_i\\log(F_{nk}q_k)+\\chi_{\\{l^{major}_n\\}}(G_{ni})j_i\\log((J_{nk}-F_{nk})q_k),) 

where *χ* is the indicator function, *J*/*j* are the all-ones matrix/vector. Note that the Einstein summation convention is implied here. With the constraints 0 ≤ *q<sub>k</sub>* ≤ 1 and Σ *q<sub>k</sub>* = 1, we can obtain the admixture proportions *q<sub>k</sub>* by applying optimization techniques.
